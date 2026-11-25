#!/usr/bin/env python3
"""
Magnetic well simulation — Gregory's stacked build, 2D magnetostatic
finite-difference solve (magnetic scalar potential).

Stack, bottom to top (all dimensions mm, y = 0 at the bottom of the yoke):
  yoke    cast-iron plate,   x [-30, 30],  y [0, 6]        mu_r = 200
  magnet  NdFeB square,     x [-19, 19],  y [6, 22]       Br = 1.45 T (N52),
                                                             mu_r = 1.05
  clay    packed around it, x [19, 30] both sides, y [6, 22]
                                                             mu_r = 1 (air-equivalent)
  cross   aluminium bar,    x [-25, 25],  y [22, 25]      mu_r = 1
  star    steel star,       x [-30, 30],  y [25, 28]      mu_r = 100
            ends tapered to a point in the vertical plane (2D stand-in
            for the in-plane star points; see LIMITS in SIMULATION.md)
  badge   steel rim + copper star, y [28, 31]
            rim:  25 <= |x| <= 30, mu_r = 100
            copper: |x| <= 25,     mu_r = 1, chi = -1e-5

ASSUMPTIONS (stated plainly; see SIMULATION.md for the full list):
  * 2D vertical cross-section through two opposite star points. A 2D slice
    cannot show the true in-plane star-point geometry; the tapered bar ends
    are a stand-in for sharp tips, so tip-concentration ratios are
    indicative, not exact.
  * Static solve only. The aluminium cross is transparent to a static field
    (mu_r = 1); no eddy currents are modelled.
  * Linear permeability with a simple saturation cap (B capped at 1.5 T
    for cast iron / star / rim steel, 2.0 T for low-carbon steel,
    0.8 T for permalloy).  Without the cap the linear model lets iron
    next to a 1.45 T magnet reach tens of tesla, which is unphysical.
    No B-H curve, no hysteresis, no temperature effects.
  * Magnet is 38 x 16 mm in the model (19.0 / 16.0) instead of the exact
    38.1 x 15.9 mm, so region edges land on grid lines.
  * Badge rim force uses a demagnetisation-corrected susceptibility
    (chi_eff ~ 1 for a flat plate normal to the field); the naive chi = 99
    value is reported alongside it so the correction is visible.
  * All force numbers are order-of-magnitude estimates from the solved
    field gradients, not measurements.

Method: magnetic scalar potential phi, H = -grad(phi),
  B = mu*H (+ Br*y-hat inside the magnet),
  div(B) = 0  ->  div(mu grad(phi)) = div(Br*y-hat).
The magnet's remanence enters as magnetic surface charge (-Br on the top
face, +Br on the bottom face, from div(B_r)). Cell-centred finite
differences, harmonic mean of mu on cell faces, Dirichlet phi = 0 on the
outer boundary.
Solved with scipy.sparse.linalg.spsolve.

Run:  python3 magnetic_well_sim.py
Writes figures and results.json into ../sim-results/ .
"""
import json
import os
import sys
import time

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

MU0 = 4.0 * np.pi * 1e-7          # H/m
BR = 1.45                          # T, N52 remanence (assumed)
KT = 1.380649e-23 * 293.0          # J, thermal energy at 20 C

# ---------------------------------------------------------------- grid
DX = 0.5                           # mm
DY = 0.5                           # mm
X0, X1 = -80.0, 80.0               # mm
Y0, Y1 = -30.0, 110.0              # mm
NX = int(round((X1 - X0) / DX))    # cells in x
NY = int(round((Y1 - Y0) / DY))    # cells in y
XC = X0 + (np.arange(NX) + 0.5) * DX   # cell-centre x
YC = Y0 + (np.arange(NY) + 0.5) * DY   # cell-centre y

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "..", "sim-results")
os.makedirs(OUT, exist_ok=True)

# ---------------------------------------------------------------- geometry
# Region extents (mm).  All edges are multiples of DX/DY by construction.
GEOM = {
    "yoke":    dict(x=(-30.0, 30.0), y=(0.0, 6.0)),
    "magnet":  dict(x=(-19.0, 19.0), y=(6.0, 22.0)),
    "clay":    dict(x=(19.0, 30.0),  y=(6.0, 22.0)),   # both sides
    "cross":   dict(x=(-25.0, 25.0), y=(22.0, 25.0)),
    "star":    dict(x=(-30.0, 30.0), y=(25.0, 28.0)),
    "rim":     dict(x=(25.0, 30.0),  y=(28.0, 31.0)),   # both sides
    "copper":  dict(x=(-25.0, 25.0), y=(28.0, 31.0)),
}
# Star tip taper: half-thickness goes from 1.5 mm at x = 30-L to 0 at x = 30.
#   5-point star: tip angle 36 deg -> L = 1.5 / tan(18 deg) = 4.6 mm
#   8-point star: tip angle 90 deg -> L = 1.5 / tan(45 deg) = 1.5 mm
#   blunted 5-point: same 36 deg taper but cut flat at 2 mm wide (half 1.0).
STAR_TAPER = {"5pt": 4.6, "8pt": 1.5, "5pt-blunt": 4.6}
STAR_BLUNT_HALF = {"5pt": 0.0, "8pt": 0.0, "5pt-blunt": 1.0}

# Volumes used for the force estimates (m^3, order of magnitude).
#   copper star: ~800 mm^2 area x 3 mm thick  -> 2.4e-6 m^3
#   steel rim:   pi*(30^2-25^2) mm^2 x 3 mm   -> 2.6e-6 m^3
V_COPPER = 2.4e-6
V_RIM = 2.6e-6
CHI_COPPER = -1.0e-5
CHI_GRAPHITE = -4.0e-4


def build_mu(config):
    """Return (mu_r map, region-label map, Bsat map) for a config dict.

    Bsat is the saturation flux density (T) for high-mu regions; inf
    where no cap applies.  A linear mu with no cap lets the iron next to
    a 1.45 T magnet reach absurd flux densities (tens of tesla) -- real
    iron saturates around 0.8-2 T, so the cap is what makes the model
    physical.  Cast iron 1.5 T, low-carbon steel 2.0 T, permalloy 0.8 T,
    star/rim steel 1.5 T.
    """
    xx, yy = np.meshgrid(XC, YC)
    ax = np.abs(xx)
    mu = np.ones((NY, NX))
    lab = np.full((NY, NX), "", dtype=object)
    bsat = np.full((NY, NX), np.inf)
    yoke_bsat = {200: 1.5, 1000: 2.0, 10000: 0.8}[config["yoke_mu"]]

    def box(key, value, label, cap=np.inf):
        g = GEOM[key]
        m = (xx >= g["x"][0]) & (xx <= g["x"][1]) & \
            (yy >= g["y"][0]) & (yy <= g["y"][1])
        # clay / rim boxes are one-sided in the table; mirror them.
        if key in ("clay", "rim"):
            m = m | ((xx >= -g["x"][1]) & (xx <= -g["x"][0]) &
                     (yy >= g["y"][0]) & (yy <= g["y"][1]))
        mu[m] = value
        lab[m] = label
        bsat[m] = cap
        return m

    # --- yoke (flat plate; the cup walls are added AFTER the clay below,
    #     because the clay region overlaps the wall region and would
    #     otherwise overwrite the walls back to mu = 1)
    if config["yoke_shape"] in ("flat", "cup"):
        box("yoke", config["yoke_mu"], "yoke", cap=yoke_bsat)
    elif config["yoke_shape"] == "none":
        pass
    else:
        raise ValueError(config["yoke_shape"])

    # --- magnet (only if present)
    if config["magnet"]:
        box("magnet", 1.05, "magnet")

    # --- clay (air-equivalent; labelled for the figure)
    box("clay", 1.0, "clay")

    # --- cup-yoke side walls (applied after the clay so they survive)
    if config["yoke_shape"] == "cup":
        wall = (yy >= 0.0) & (yy <= 22.0) & (ax >= 19.0) & (ax <= 25.0)
        mu[wall] = config["yoke_mu"]
        lab[wall] = "yoke"
        bsat[wall] = yoke_bsat

    # --- aluminium cross (or air in its place)
    if config["spacer"] == "cross":
        box("cross", 1.0, "cross")
    elif config["spacer"] == "none":
        pass  # air gap, same stack heights
    elif config["spacer"] == "thick":
        g = GEOM["cross"]
        m = (xx >= g["x"][0]) & (xx <= g["x"][1]) & \
            (yy >= 22.0) & (yy <= 28.0)
        mu[m] = 1.0
        lab[m] = "cross"
    else:
        raise ValueError(config["spacer"])

    # --- star (tapered ends; shifted up for the thick spacer)
    #     star=None means no star region at all (control run).
    yshift = 3.0 if config["spacer"] == "thick" else 0.0
    if config.get("star") is not None:
        g = GEOM["star"]
        ylo, yhi = g["y"][0] + yshift, g["y"][1] + yshift
        ymid = 0.5 * (ylo + yhi)
        L = STAR_TAPER[config["star"]]
        blunt = STAR_BLUNT_HALF[config["star"]]
        core = (ax <= 30.0 - L) & (yy >= ylo) & (yy <= yhi)
        taper = (ax > 30.0 - L) & (ax <= 30.0)
        half = blunt + (1.5 - blunt) * (30.0 - ax) / L
        taper = taper & (np.abs(yy - ymid) <= half)
        star = core | taper
        mu[star] = config["star_mu"]
        lab[star] = "star"
        bsat[star] = 1.5

    # --- badge (rim + copper centre; shifted up for the thick spacer)
    if config["badge"]:
        g = GEOM["rim"]
        m = (yy >= g["y"][0] + yshift) & (yy <= g["y"][1] + yshift) & \
            (ax >= g["x"][0]) & (ax <= g["x"][1])
        mu[m] = config["rim_mu"]
        lab[m] = "rim"
        bsat[m] = 1.5
        g = GEOM["copper"]
        m = (xx >= g["x"][0]) & (xx <= g["x"][1]) & \
            (yy >= g["y"][0] + yshift) & (yy <= g["y"][1] + yshift)
        mu[m] = 1.0
        lab[m] = "copper"

    return mu, lab, bsat


def magnet_rows():
    """Cell rows of the magnet top / bottom faces (for the source charge)."""
    g = GEOM["magnet"]
    top = np.where(np.isclose(YC, g["y"][1] - DY / 2))[0][0]
    bot = np.where(np.isclose(YC, g["y"][0] + DY / 2))[0][0]
    cols = np.where((XC >= g["x"][0]) & (XC <= g["x"][1]))[0]
    return top, bot, cols


def solve(mu, bsat=None):
    """Solve div(mu grad(phi)) = div(Br y-hat) for phi (cell centres).

    bsat: array of saturation flux densities (T) per cell, inf where no
    cap applies.  Cells whose |B| exceeds their Bsat get mu_r reduced so
    B caps at Bsat; iterated a few times (simple saturation model).
    Without this, linear iron next to a 1.45 T magnet reaches tens of
    tesla, which is unphysical (iron saturates at 0.8-2 T).
    Returns (phi, mu_used, n_cap_first, n_cap_final, Bmap)."""
    mu = mu.copy()
    top, bot, cols = magnet_rows()
    bc = _dipole_bc()
    n_cap_first = 0
    n_capped = 0
    for it in range(4):
        phi, b = _solve_once(mu, top, bot, cols, bc=bc)
        bx, by = fields(phi, mu)
        bmag = np.hypot(bx, by)
        if bsat is None:
            return phi, mu, 0, 0, bmag
        over = np.isfinite(bsat) & (bmag > bsat)
        n_capped = int(over.sum())
        if it == 0:
            n_cap_first = n_capped
        if n_capped == 0:
            return phi, mu, n_cap_first, 0, bmag
        # H in those cells, then mu_r that would cap B at Bsat.
        h = bmag / (MU0 * mu)
        mu_new = mu.copy()
        mu_new[over] = bsat[over] / (MU0 * h[over])
        mu = mu_new
    return phi, mu, n_cap_first, n_capped, bmag


def _dipole_bc():
    """Dipole-potential Dirichlet values on the outer boundary ring.

    This is a 2D model (an infinitely extruded cross-section), so the far
    field is a LINE dipole: phi = (m' / 2*pi) * (y - yc) / r^2 with m'
    the dipole moment per unit depth, m' = (Br/mu0) * (magnet width x
    magnet height).  A 3D dipole BC (phi ~ 1/r^2) is WRONG here -- it
    forces phi far too small at the boundary and inflates the field near
    the top of the box.  A plain phi = 0 boundary does the same thing
    worse.  The 2D dipole value is the correct far-field form.
    (For the yoke runs the yoke adds induced moment, so the BC slightly
    underestimates their far field -- stated in SIMULATION.md; all
    comparisons use the same BC.)"""
    mp = (BR / MU0) * (38e-3 * 16e-3)        # A m, moment per unit depth
    yc = 14e-3                                 # magnet centre, m
    xx, yy = np.meshgrid(XC * 1e-3, YC * 1e-3)
    r2 = xx ** 2 + (yy - yc) ** 2
    return (mp / (2 * np.pi)) * (yy - yc) / r2


def _solve_once(mu, top, bot, cols, bc=None):
    """One linear solve with fixed mu.  Returns (phi, rhs)."""
    mu_si = mu * MU0
    # Face permeabilities (harmonic mean of neighbouring cells).
    # mu_e[j, i] is the face between cell (j, i) and (j, i+1).
    mu_e = np.zeros((NY, NX - 1))
    mu_e[:] = 2.0 * mu_si[:, :-1] * mu_si[:, 1:] / (mu_si[:, :-1] + mu_si[:, 1:])
    mu_n = np.zeros((NY - 1, NX))
    mu_n[:] = 2.0 * mu_si[:-1, :] * mu_si[1:, :] / (mu_si[:-1, :] + mu_si[1:, :])

    n = NY * NX

    def idx(j, i):
        return j * NX + i

    # Assemble the 5-point stencil in COO form.
    rows, cols_i, vals = [], [], []
    rhs = np.zeros(n)
    # Source: magnetic surface charge.  B_r = Br*y-hat inside the magnet,
    # so div(B_r) = -Br on the TOP face (B_r drops to zero going up) and
    # +Br on the BOTTOM face.  (The sign is easy to get backwards: the
    # charge that matters for phi is div(B_r), not M.n-hat.)
    for i in cols:
        w = 0.5 if i in (cols[0], cols[-1]) else 1.0
        rhs[idx(top, i)] -= w * BR / (DY * 1e-3)
        rhs[idx(bot, i)] += w * BR / (DY * 1e-3)

    diag = np.zeros((NY, NX))
    for j in range(NY):
        for i in range(NX):
            if j in (0, NY - 1) or i in (0, NX - 1):
                # Dirichlet phi = dipole value on the outer ring.
                rows.append(idx(j, i)); cols_i.append(idx(j, i)); vals.append(1.0)
                rhs[idx(j, i)] = bc[j, i] if bc is not None else 0.0
                continue
            ce = mu_e[j, i] / (DX * 1e-3) ** 2
            cw = mu_e[j, i - 1] / (DX * 1e-3) ** 2
            cn = mu_n[j, i] / (DY * 1e-3) ** 2
            cs = mu_n[j - 1, i] / (DY * 1e-3) ** 2
            diag[j, i] = -(ce + cw + cn + cs)
            rows.append(idx(j, i)); cols_i.append(idx(j, i)); vals.append(diag[j, i])
            rows.append(idx(j, i)); cols_i.append(idx(j, i + 1)); vals.append(ce)
            rows.append(idx(j, i)); cols_i.append(idx(j, i - 1)); vals.append(cw)
            rows.append(idx(j, i)); cols_i.append(idx(j + 1, i)); vals.append(cn)
            rows.append(idx(j, i)); cols_i.append(idx(j - 1, i)); vals.append(cs)
    a = sp.coo_matrix((vals, (rows, cols_i)), shape=(n, n)).tocsc()
    phi = spla.spsolve(a, rhs)
    return phi.reshape(NY, NX), rhs


def fields(phi, mu):
    """H and B (Tesla) at cell centres from phi.  B includes Br in magnet."""
    dphi_dy, dphi_dx = np.gradient(phi, DY * 1e-3, DX * 1e-3)
    hx = -dphi_dx
    hy = -dphi_dy
    bx = MU0 * mu * hx
    by = MU0 * mu * hy
    g = GEOM["magnet"]
    m = (np.abs(np.meshgrid(XC, YC)[0]) <= g["x"][1]) & \
        (np.meshgrid(XC, YC)[1] >= g["y"][0]) & \
        (np.meshgrid(XC, YC)[1] <= g["y"][1])
    by[m] += BR
    return bx, by


def at(bmap, x, y):
    """Nearest-cell sample of a map at (x, y) in mm."""
    i = int(np.clip(round((x - X0) / DX - 0.5), 0, NX - 1))
    j = int(np.clip(round((y - Y0) / DY - 0.5), 0, NY - 1))
    return bmap[j, i]


def grad_b2(bx, by, x, y):
    """Gradient of B^2 (T^2/m) at (x, y) by central differences."""
    h = DX * 1e-3
    b2 = bx ** 2 + by ** 2
    i = int(np.clip(round((x - X0) / DX - 0.5), 1, NX - 2))
    j = int(np.clip(round((y - Y0) / DY - 0.5), 1, NY - 2))
    gx = (b2[j, i + 1] - b2[j, i - 1]) / (2 * h)
    gy = (b2[j + 1, i] - b2[j - 1, i]) / (2 * h)
    return gx, gy


def analyse(name, config, phi, mu, bmag, bx, by, t_solve, twin=None):
    """Extract the comparison numbers for one configuration.

    twin: (bx_t, by_t, bmag_t) from the same configuration with the badge
    removed.  The well depth and the forces are taken from the TWIN field:
    the force on a body must be computed from the field it does NOT itself
    produce, and the steel rim concentrates flux inside itself, so the
    field sampled inside the rim in the full run is the rim's own field,
    not the external field -- using it gives absurd forces (hundreds of
    newtons for a 20 g rim).  The copper centre does not perturb the
    field (mu ~ 1), so its values are the same in either run.
    The star-tip concentration ratio is taken from the full run (as built).
    """
    yshift = 3.0 if config["spacer"] == "thick" else 0.0
    y_star_top = 28.0 + yshift
    y_badge = 29.5 + yshift
    r = {"name": name, "config": {k: v for k, v in config.items()},
         "solve_s": round(t_solve, 1)}
    bx_t, by_t, bmag_t = twin if twin is not None else (bx, by, bmag)

    # --- field on the centreline, magnet top face up to the domain top
    ys = np.arange(22.0, 110.0, 0.5)
    prof = [at(bmag, 0.0, y) for y in ys]
    r["centerline_B_at_magnet_top_T"] = round(float(prof[0]), 4)
    r["centerline_B_at_star_top_T"] = round(float(at(bmag, 0.0, y_star_top + 0.5)), 4)
    r["centerline_B_at_badge_T"] = round(float(at(bmag, 0.0, y_badge)), 4)
    # total flux out of the magnet top face (per unit depth, Wb/m) --
    # the yoke-boost check: the yoke should raise the total flux, not
    # just the centreline value.
    xs_top = np.arange(-19.0, 19.01, 0.5)
    r["top_face_flux_Wb_per_m"] = round(
        float(sum(at(by, x, 22.5) for x in xs_top) * 0.5e-3), 5)
    # far-field decay check (distance measured from the magnet centre, y=14)
    far = {int(y): float(at(bmag, 0.0, y)) for y in (60.0, 80.0, 100.0)}
    r["far_field_B_T"] = {str(k): round(v, 6) for k, v in far.items()}
    # fitted decay exponent between 60 and 100 mm on the axis.
    # NOTE: this is a 2D model, so the far field is a LINE dipole and the
    # expected exponent is ~2, not 3.  A genuine field null on the axis
    # (the cup yoke's wall poles can oppose the main field there) makes
    # a single exponent meaningless -- a null is a LOCAL minimum strictly
    # inside the range, not the smallest value at the range's end (the
    # field decays monotonically, so the end value is always smallest).
    ys_f = np.arange(40.0, 110.0, 0.5)
    prof_f = np.array([at(bmag, 0.0, y) for y in ys_f])
    null_y = None
    for k in range(1, len(prof_f) - 1):
        if prof_f[k] < prof_f[k - 1] and prof_f[k] < prof_f[k + 1] \
                and prof_f[k] < 0.5 * prof_f[0]:
            null_y = float(ys_f[k])
            break
    if null_y is not None:
        r["far_field_decay_exponent"] = None
        r["axis_field_null_y_mm"] = round(null_y, 1)
    else:
        r["axis_field_null_y_mm"] = None
        d1, d2 = 60.0 - 14.0, 100.0 - 14.0
        r["far_field_decay_exponent"] = round(
            float(np.log(far[60] / far[100]) / np.log(d2 / d1)), 2)

    # --- well profile: B(x) at badge height, from the TWIN (external) field
    r["well_B_centre_T"] = round(float(at(bmag_t, 0.0, y_badge)), 4)
    r["well_B_rim_T"] = round(float(at(bmag_t, 27.5, y_badge)), 4)
    r["well_depth_dB_T"] = round(r["well_B_rim_T"] - r["well_B_centre_T"], 4)
    b2c = r["well_B_centre_T"] ** 2
    b2r = r["well_B_rim_T"] ** 2
    r["well_depth_dB2_T2"] = round(b2r - b2c, 4)
    # field inside the steel rim in the full run (diagnostic only -- this
    # is the rim's own flux concentration, NOT the well)
    r["field_inside_rim_T"] = round(float(at(bmag, 27.5, y_badge)), 4) \
        if config["badge"] else None
    # energy well depth for the diamagnetic centre (J), from the twin field
    for tag, chi in (("copper", CHI_COPPER), ("graphite", CHI_GRAPHITE)):
        du = abs(chi) * V_COPPER * (b2r - b2c) / (2 * MU0)
        r[f"well_energy_depth_{tag}_J"] = float(f"{du:.3e}")
        r[f"well_energy_depth_{tag}_vs_kT"] = float(f"{du / KT:.3e}")

    # --- star-point flux concentration (full run, as built)
    #     sampled at 0.5, 1 and 2 mm beyond the tip: a sharp tip wins
    #     right at the point, a fatter tip carries more flux a little
    #     farther out, so the distance matters.
    if config["star"] is not None:
        b_ctr = float(at(bmag, 0.0, y_badge))
        r["star_centre_B_T"] = round(b_ctr, 4)
        for d in (0.5, 1.0, 2.0):
            b_tip = float(at(bmag, 30.0 + d, 26.5 + yshift))
            r[f"star_tip_B_{d}mm_T"] = round(b_tip, 4)
            r[f"star_tip_ratio_{d}mm"] = round(b_tip / b_ctr, 2) if b_ctr > 0 else None
        r["star_tip_B_T"] = r["star_tip_B_1.0mm_T"]
        r["star_tip_concentration_ratio"] = r["star_tip_ratio_1.0mm"]
    else:
        r["star_tip_B_T"] = None
        r["star_centre_B_T"] = None
        r["star_tip_concentration_ratio"] = None

    # --- forces on the badge, from the TWIN (external) field.
    #     Order-of-magnitude estimates: F = chi_eff * V / (2 mu0) * grad(B^2).
    #     Rim: chi_eff is demagnetisation-corrected (~1 for a flat plate
    #     normal to the field); the naive chi = 99 value is shown too.
    #     Sign: negative vertical = pulled DOWN toward the star/magnet.
    #     The rim gradient is sampled at the rim centroid height (badge
    #     height), NOT 1 mm below it: 1 mm below, the difference interval
    #     crosses the star's top face, where B jumps, and the gradient
    #     comes out orders of magnitude too large.
    gx, gy = grad_b2(bx_t, by_t, 27.5, y_badge)
    chi_eff_rim = (config["rim_mu"] - 1) / (1 + 1.0 * (config["rim_mu"] - 1))
    f_rim_z = chi_eff_rim * V_RIM / (2 * MU0) * gy
    f_rim_z_naive = (config["rim_mu"] - 1) * V_RIM / (2 * MU0) * gy
    gx_c, gy_c = grad_b2(bx_t, by_t, 0.0, y_badge)
    f_cu_z = CHI_COPPER * V_COPPER / (2 * MU0) * gy_c
    f_gr_z = CHI_GRAPHITE * V_COPPER / (2 * MU0) * gy_c
    r["force_rim_vertical_N"] = float(f"{f_rim_z:.3e}")
    r["force_rim_vertical_naive_chi99_N"] = float(f"{f_rim_z_naive:.3e}")
    r["force_copper_vertical_N"] = float(f"{f_cu_z:.3e}")
    r["force_graphite_vertical_N"] = float(f"{f_gr_z:.3e}")
    # lateral force on the diamagnetic centre at 10 and 15 mm off centre.
    # (At 5 mm the field is almost flat, so the value there is noise.)
    # Negative = restoring, pushed back toward the centre.
    for off in (10.0, 15.0):
        gxo, _ = grad_b2(bx_t, by_t, off, y_badge)
        r[f"force_copper_lateral_{int(off)}mm_N"] = float(
            f"{CHI_COPPER * V_COPPER / (2 * MU0) * gxo:.3e}")
        r[f"force_graphite_lateral_{int(off)}mm_N"] = float(
            f"{CHI_GRAPHITE * V_COPPER / (2 * MU0) * gxo:.3e}")
    # badge weight for scale: rim ~20 g steel + copper star ~20 g
    r["badge_weight_N"] = 0.39
    return r


BASE = dict(yoke_shape="flat", yoke_mu=200, magnet=True, spacer="cross",
            star="5pt", star_mu=100, badge=True, rim_mu=100)

CONFIGS = [
    ("baseline_castiron_5pt", dict(BASE)),
    ("control_magnet_only", dict(BASE, yoke_shape="none", star=None,
                                  badge=False, spacer="none")),
    ("yoke_steel_mu1000", dict(BASE, yoke_mu=1000)),
    ("yoke_permalloy_mu10000_sat", dict(BASE, yoke_mu=10000)),
    ("yoke_cup_castiron", dict(BASE, yoke_shape="cup")),
    ("star_8pt", dict(BASE, star="8pt")),
    ("star_5pt_blunt", dict(BASE, star="5pt-blunt")),
    ("center_graphite", dict(BASE)),          # same field; forces differ
    ("spacer_none", dict(BASE, spacer="none")),
    ("spacer_thick_6mm", dict(BASE, spacer="thick")),
    ("no_badge", dict(BASE, badge=False)),
]


def run_all():
    results = {}
    t0 = time.time()
    for name, cfg in CONFIGS:
        t1 = time.time()
        mu, lab, bsat = build_mu(cfg)
        phi, mu_used, n_cap_first, n_cap, bmag = solve(mu, bsat=bsat)
        bx, by = fields(phi, mu_used)
        # No-badge twin: same geometry, badge removed.  The well depth
        # and the forces are taken from the twin (external) field.
        if cfg["badge"]:
            cfg_t = dict(cfg, badge=False)
            mu_t, _, bsat_t = build_mu(cfg_t)
            phi_t, mu_tu, _, _, bmag_t = solve(mu_t, bsat=bsat_t)
            bx_t, by_t = fields(phi_t, mu_tu)
            twin = (bx_t, by_t, bmag_t)
        else:
            twin = (bx, by, bmag)
        r = analyse(name, cfg, phi, mu_used, bmag, bx, by,
                    time.time() - t1, twin=twin)
        r["cells_over_saturation_first"] = n_cap_first
        r["cells_over_saturation_final"] = n_cap
        results[name] = r
        print(f"{name:28s} B_top={r['centerline_B_at_magnet_top_T']:.3f} T  "
              f"flux={r['top_face_flux_Wb_per_m']:.4f}  "
              f"well_dB={r['well_depth_dB_T']:.3f} T  "
              f"tip_ratio={r['star_tip_concentration_ratio']}  "
              f"({time.time() - t1:.0f} s)", flush=True)
        # keep the baseline fields for the figures
        if name == "baseline_castiron_5pt":
            np.savez(os.path.join(OUT, "baseline_fields.npz"),
                     bx=bx, by=by, bmag=bmag, mu=mu_used, lab=lab)
            globals()["_base"] = (bx, by, bmag, mu_used, lab)
            globals()["_base_twin"] = twin
        if name == "control_magnet_only":
            globals()["_ctrl"] = (bx, by, bmag)
        if name == "yoke_cup_castiron":
            globals()["_cup"] = (bx, by, bmag)
        if name == "no_badge":
            globals()["_nobadge"] = (bx, by, bmag)
    with open(os.path.join(OUT, "results.json"), "w") as f:
        json.dump(results, f, indent=2)
    print(f"total {time.time() - t0:.0f} s")
    return results


def main():
    results = run_all()
    # ---- figures (need matplotlib; import lazily so a headless failure
    # does not lose the numbers, which are already in results.json)
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.patches import Rectangle, Polygon

    bx, by, bmag, mu, lab = globals()["_base"]

    # --- figure 1: field map, baseline, log scale, stack outline
    fig, ax = plt.subplots(figsize=(9, 7))
    xx, yy = np.meshgrid(
        X0 + (np.arange(NX) + 0.5) * DX, Y0 + (np.arange(NY) + 0.5) * DY)
    im = ax.pcolormesh(xx, yy, np.log10(np.maximum(bmag, 1e-6)),
                       shading="auto", cmap="inferno", vmin=-3, vmax=0.3)
    fig.colorbar(im, ax=ax, label="log10 |B|  (T)")
    # stack outline (white edges)
    for (x0, x1, y0, y1) in [(-30, 30, 0, 6), (-19, 19, 6, 22),
                             (-25, 25, 22, 25), (-25, 25, 28, 31)]:
        ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, fill=False,
                               edgecolor="white", linewidth=1.2))
    # star outline (tapered bar)
    ax.add_patch(Polygon([(-30, 26.5), (-25.4, 25), (25.4, 25), (30, 26.5),
                          (25.4, 28), (-25.4, 28)], closed=True, fill=False,
                         edgecolor="white", linewidth=1.2))
    # rim
    for (x0, x1) in [(-30, -25), (25, 30)]:
        ax.add_patch(Rectangle((x0, 28), x1 - x0, 3, fill=False,
                               edgecolor="white", linewidth=1.2))
    ax.plot([0], [29.5], "wo", markersize=5)
    ax.annotate("well (B min)", (0, 29.5), (8, 32), color="white",
                fontsize=9, arrowprops=dict(arrowstyle="->", color="white"))
    ax.plot([31], [26.5], "wx", markersize=7, markeredgewidth=1.5)
    ax.annotate("star tip", (31, 26.5), (36, 22), color="white", fontsize=9,
                arrowprops=dict(arrowstyle="->", color="white"))
    ax.set_xlim(-70, 70)
    ax.set_ylim(-20, 70)
    ax.set_xlabel("x  (mm)")
    ax.set_ylabel("y  (mm)")
    ax.set_title("Magnetic well — |B| map, baseline (cast-iron yoke, 5-pt star)\n"
                 "white outlines: yoke / magnet / cross / star / badge")
    ax.set_aspect("equal")
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "field_map.png"), dpi=150)
    plt.close(fig)

    # --- figure 2: centreline B(y), baseline vs control vs cup
    fig, ax = plt.subplots(figsize=(8, 5))
    ys = np.arange(22.0, 110.0, 0.5)
    for label, fields_ in (("baseline (cast-iron yoke)", globals()["_base"][:3]),
                           ("control (magnet only)", globals()["_ctrl"]),
                           ("cup yoke (cast iron)", globals()["_cup"])):
        prof = [at(fields_[2], 0.0, y) for y in ys]
        ax.semilogy(ys, prof, label=label)
    ax.axvspan(25, 28, color="grey", alpha=0.25)
    ax.axvspan(28, 31, color="grey", alpha=0.15)
    ax.text(26.5, 0.9, "star", ha="center", fontsize=9)
    ax.text(29.5, 0.9, "badge", ha="center", fontsize=9)
    ax.set_xlabel("height above magnet top face  y  (mm)")
    ax.set_ylabel("|B| on the centreline  (T, log scale)")
    ax.set_title("Centreline field above the stack")
    ax.legend()
    ax.grid(True, which="both", alpha=0.3)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "centerline_profile.png"), dpi=150)
    plt.close(fig)

    # --- figure 3: well profile B(x) at badge height
    #     twin (external field, no badge) shows the well itself;
    #     full baseline shows the rim's own flux concentration on top;
    #     control shows there is no well without the star.
    fig, ax = plt.subplots(figsize=(8, 5))
    xs = np.arange(-40.0, 40.01, 0.5)
    for label, fields_ in (
            ("baseline, external field (badge removed)",
             globals()["_base_twin"]),
            ("baseline, with badge (rim concentrates flux)",
             globals()["_base"][:3]),
            ("control (magnet only, no star)", globals()["_ctrl"])):
        prof = [at(fields_[2], x, 29.5) for x in xs]
        ax.plot(xs, prof, label=label)
    ax.axvspan(-30, -25, color="grey", alpha=0.2)
    ax.axvspan(25, 30, color="grey", alpha=0.2)
    ax.text(-27.5, 0.02, "rim", ha="center", fontsize=9)
    ax.text(27.5, 0.02, "rim", ha="center", fontsize=9)
    ax.text(0, 0.02, "copper centre", ha="center", fontsize=9)
    ax.set_xlabel("x  (mm)")
    ax.set_ylabel("|B| at badge height (y = 29.5 mm)  (T)")
    ax.set_title("The well: field across the badge — lobes over the star "
                 "tips, dip over the centre")
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "well_profile.png"), dpi=150)
    plt.close(fig)
    print("figures written")


if __name__ == "__main__":
    main()
