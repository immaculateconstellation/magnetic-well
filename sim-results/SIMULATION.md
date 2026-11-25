# Magnetic well — simulation note

**Date:** 2026-11-10 (all numbers from the final saturated run, `results.json`)
**Code:** `code/magnetic_well_sim.py` — one file, runnable as
`python3 code/magnetic_well_sim.py` from the `code/` directory (~4 minutes;
writes `sim-results/results.json`, `sim-results/baseline_fields.npz` and the
three figures itself). Environment: numpy 1.26.4, scipy 1.11.4,
matplotlib 3.6.3, magpylib 5.2.1.
**Status:** private/local only. Nothing published, sent, bought, or contacted.

## What was modeled

A vertical 2D cross-section through Gregory's stack, bottom to top, through
two opposite star points so the flux crowding at the tips shows:

| layer | geometry in the model (mm) | material in the model |
|---|---|---|
| cast-iron yoke | x[−30, 30], y[0, 6] | μ_r = 200 (cast iron), B_sat = 1.5 T |
| neodymium magnet | x[−19, 19], y[6, 22] | N52 assumed, Br = 1.45 T, μ_r = 1.05 |
| dried clay | x[19, 30] both sides, y[6, 22] | μ_r = 1 (modeled as air — it is a dielectric) |
| aluminium cross | x[−25, 25], y[22, 25] | μ_r = 1 (transparent to a static field) |
| stainless star | x[−30, 30], y[25, 28], ends tapered to points | μ_r = 100, B_sat = 1.5 T |
| badge rim | x[25, 30] both sides, y[28, 31] | μ_r = 100, B_sat = 1.5 T |
| badge copper centre | x[−25, 25], y[28, 31] | χ = −1e-5 (diamagnetic) |

y = 0 is the bottom of the yoke. The magnet is modeled as 38 × 16 mm
(instead of the exact 38.1 × 15.9) so its edges land on the 0.5 mm grid
lines. The star's points are modeled as tapered bar ends in the vertical
plane (5-point: 36° tip, 4.6 mm taper; 8-point: 90° tip, 1.5 mm taper) —
a 2D stand-in for the true in-plane star geometry.

**Solver:** magnetic scalar potential φ on a cell-centred grid
(dx = dy = 0.5 mm; x ∈ [−80, 80], y ∈ [−30, 110]; 320 × 280 cells),
H = −∇φ, B = μH + Br·ŷ inside the magnet, harmonic mean of μ on cell
faces, sparse solve (scipy `spsolve`). Boundary: Dirichlet φ set to the
2D line-dipole potential of the magnet's dipole moment. Saturation is a
simple fixed-point cap: cells over their B_sat get μ_r reduced to
B_sat/(μ0·H), up to 4 passes.

## Assumptions (stated plainly)

- Magnet is **N52, Br = 1.45 T** — assumed; Gregory did not state a grade.
- Cast iron μ_r ≈ 200, low-carbon steel μ_r ≈ 1000, permalloy μ_r ≈ 10000 —
  estimates, not measured values.
- The star is a **magnetic stainless grade** (μ_r = 100). An austenitic
  (non-magnetic) stainless star would not concentrate flux at all — this
  run is the magnetic-grade case.
- The clay is treated as air (μ_r = 1); the aluminium cross as μ_r = 1,
  which is correct for a **static** field. The cross's real jobs — eddy
  currents against changing fields, heat spreading, mechanical spacing —
  are not in this model.
- The rim force uses a demagnetisation-corrected susceptibility
  (χ_eff ≈ 1 for a flat plate normal to the field), not the naive χ = 99.
  The naive value is shown in `results.json` to make the correction visible.
- Badge weight ≈ 0.39 N (rim ~20 g + copper star ~20 g, as assumed).
- All force figures are **order-of-magnitude estimates** from field
  gradients, not measurements.

## Headline numbers — baseline (cast-iron yoke, sharp 5-point star)

| quantity | value |
|---|---|
| Field at magnet top face (centreline) | **0.573 T** (control, bare magnet: 0.295 T — the yoke **doubles** it) |
| Top-face flux (per unit depth) | **0.0192 Wb/m** (control: 0.0120 — the yoke adds **+61%**) |
| Well minimum (badge centre, y = 29.5 mm) | **B = 0.133 T** at the centre, lobes **0.235 T** over the star tips |
| Well depth (lobe − centre) | **0.102 T** (control: **−0.066 T** — the bare magnet has *no* well, it has a hump) |
| Star-tip concentration ratio (tip B / centre B, 1 mm past the tip) | **2.72** (3.16 at 0.5 mm, 2.40 at 2 mm) |
| Rim pull (vertical, downward) | **≈ −19 N** — about **50× the badge's weight** (0.39 N) |
| Copper centre push (vertical, upward) | **+6.1 µN** — about **1/64,000 of the badge's weight** |
| Graphite centre push (vertical, upward) | **+0.25 mN** — 40× copper, still **~1,600× too small to lift the badge** |
| Lateral restoring force on the copper centre (10 mm off-centre) | **−9 µN** (toward centre); graphite **−0.37 mN** |
| Well energy depth | copper **3.6e-07 J** (≈ 9e13 kT — thermal noise is irrelevant); graphite **1.4e-05 J** |
| Far-field decay exponent (60–100 mm) | **1.63** (2D line-dipole expectation ≈ 2; control gives 2.01) |

**The honest bottom line on the well:** the well is real — the external
field really dips by 0.102 T over the badge centre and rises to lobes over
the star tips, and the bare magnet has no such dip. But the badge is **not**
held by the diamagnetic push. Even graphite's push (0.25 mN) is ~1,600×
too small to lift the 0.39 N badge, and the copper well energy (3.6e-07 J)
is ~1,000× smaller than the energy to lift the badge 1 mm (3.9e-04 J).
What holds the badge down is the **steel rim's ferromagnetism** (~19 N of
pull, ~50× its weight). The well is a **lateral centering trap** — it
nudges the diamagnetic centre toward the middle — not a levitator.
(Earnshaw's rule agrees: no static field stably traps a regular magnet;
the stability here comes from the rim's attraction plus the geometry.)

## Comparison table — all variations

Same grid, same solver, so the numbers are comparable. Well depth, tip
ratio, and forces are all taken from each config's **no-badge twin**
(external) field, so the badge's own flux concentration does not
contaminate them.

| config | B_top (T) | flux (Wb/m) | well depth (T) | tip ratio @1 mm | rim pull (N) | Cu push (µN) | graphite push (mN) |
|---|---|---|---|---|---|---|---|
| **baseline — cast iron, 5 pt** | 0.573 | 0.0192 | **+0.102** | 2.72 | −18.9 | +6.1 | +0.25 |
| control — magnet only | 0.295 | 0.0120 | −0.066 | — | −2.74 | +46 | +1.84 |
| yoke — low-carbon steel (μ=1000) | 0.578 | 0.0194 | +0.102 | 2.71 | −19.1 | +6.3 | +0.25 |
| yoke — permalloy (μ=10000, capped) | 0.573 | 0.0192 | +0.102 | 2.71 | −18.8 | +6.2 | +0.25 |
| yoke — cup (wraps magnet sides) | **0.688** | 0.0196 | **−0.053** | 1.60 | −0.19 | +9.2 | +0.37 |
| star — 8 points | 0.575 | 0.0194 | +0.033 | 3.12 | −1.27 | +6.1 | +0.25 |
| star — 5 pt, blunted tips | 0.575 | 0.0194 | +0.043 | 3.19 | −7.57 | +6.1 | +0.25 |
| centre — pyrolytic graphite | 0.573 | 0.0192 | +0.102 | 2.72 | −18.9 | — | +0.25 |
| spacer — no cross | 0.573 | 0.0192 | +0.102 | 2.72 | −18.9 | +6.1 | +0.25 |
| spacer — thick cross (6 mm) | 0.521 | 0.0177 | +0.121 | 3.22 | −17.7 | +3.6 | +0.14 |
| no badge (external field check) | 0.570 | 0.0191 | +0.102 | 2.48 | −18.9 | +6.1 | +0.25 |

What each variation shows:

1. **Yoke material — no difference worth naming.** Cast iron, low-carbon
   steel, and permalloy agree within 1% on every number. The reason is
   saturation: next to a 1.45 T magnet the iron is saturated anyway, so
   the extra permeability has nothing to work on. Permalloy is the worst
   buy of all — it saturates hardest (1,716 cells over its 0.8 T cap on
   the first pass) for zero gain. Cast iron is fine; there is no reason
   to pay for better iron.
2. **Yoke shape — the cup is a trade.** It gives the strongest top-face
   field (+20%: 0.688 T vs 0.573 T) and the most flux (+2%), but it
   **destroys the well** (depth −0.053 T — the centre becomes a field
   maximum, not a minimum), collapses the tip ratio (1.60 vs 2.72), and
   collapses the rim pull (−0.19 N vs −18.9 N). It also confines the
   field hard: the far field decays with exponent 6.82 and B at 100 mm is
   0.00033 T (vs 0.018 T for the flat plate). Use the cup if the goal is
   "most field out the top and least stray field"; do not use it if the
   well is the point.
3. **Star points — sharp 5-point wins the well; fat tips win the tip
   reading.** The 8-point and blunted stars read *higher* right at the
   tips (tip ratio 3.12 / 3.19 vs 2.72; tip B at 1 mm 0.395 / 0.404 T
   vs 0.346 T) but make a *shallower* well (0.033 / 0.043 T vs 0.102 T).
   The sharp tip concentrates the field into a tighter lobe that projects
   up to badge height; the fat tip spreads its field broadly — higher
   at the tip itself, weaker where the badge sits. The rim pull follows
   the same pattern (sharp 5-pt: −18.9 N; blunt: −7.6 N; 8-pt: −1.3 N),
   because it depends on the vertical gradient at the rim, which is
   steepest for the sharp tip.
4. **Centre material — graphite is 40× stronger, and it still does not
   levitate.** Switching the copper centre for pyrolytic graphite
   (χ = −4e-4) multiplies the upward push by 40 (0.25 mN vs 6.1 µN) and
   the well energy depth by 40 (1.4e-05 J vs 3.6e-07 J), with the field
   itself unchanged (identical numbers — the centre material does not
   affect the field at these susceptibilities). But 0.25 mN is still
   ~1,600× short of the badge's 0.39 N weight. Graphite buys a stiffer
   trap, not a levitator.
5. **Spacer — the cross is invisible to the static field, as expected.**
   Removing it changes nothing (identical numbers to the last digit).
   The thick (6 mm) cross costs ~9% of the top field and ~8% of the
   flux for a slightly deeper well (0.121 T vs 0.102 T) — not worth it
   unless the extra spacing is needed mechanically. Keep the cross for
   its real jobs (spacing, heat, eddy-current shielding of changing
   fields), not for the static field.
6. **Magnet shape — square vs cylinder (magpylib analytic, not the 2D
   solver).** The 2D solver cannot distinguish them (identical
   cross-sections), so this was done with magpylib on bare magnets of
   the same footprint. Cylinder / cuboid B ratio: 1.067 at the face
   (y = 22.5 mm), **1.009 at badge height (y = 29.5 mm)**, 0.924 at
   y = 40 mm, 0.844 at y = 60 mm. At the badge, the two shapes are
   within 1%. The cylinder is a little stronger close in and weaker
   farther away (it has 21.5% less volume — π/4 — so its far field is
   ~16% weaker). **The square is fine; the cylinder is no better for
   the well.**

## Recommendation

**Best combination found: cast-iron flat yoke + sharp 5-point star +
pyrolytic graphite centre (if a stiffer trap is wanted) + the standard
3 mm aluminium cross + the square magnet — i.e. the build as described,
with graphite swapped in for the copper centre if the diamagnetic trap
itself matters.**

- What it improves: the yoke roughly doubles the top-face field vs the
  bare magnet (0.573 T vs 0.295 T, flux +61%); the sharp 5-point star
  gives the deepest well of any star tried (0.102 T, ~3× the 8-point's
  0.033 T); graphite gives 40× copper's diamagnetic push and well
  energy; the flat yoke keeps the rim pull strong (−19 N).
- What it does **not** fix: nothing in this stack levitates the badge.
  The diamagnetic push stays ~1,600× too small even with graphite; the
  badge is held by the steel rim's ferromagnetism, and the well is a
  lateral centering trap, not a levitator. No yoke material, star shape,
  or centre material changes that — it is the size of χ, not the
  geometry. A real levitating version would need a diamagnet with a far
  larger χ·V product (or a much lighter centre piece), which is a
  different build, not a variation of this one.
- What to avoid: the cup yoke if the well matters (it kills the well and
  the rim pull); permalloy (saturates, no gain, costs more); the thick
  cross (costs field for a marginal well gain); blunting the tips if the
  well depth is the goal.

## Verification checks that passed

- **Sign of the source.** The first build had the remanence sign flipped
  (field pointing the wrong way). Caught by comparing with magpylib;
  fixed (top face −Br, bottom face +Br, from div(B_r)). The field above
  the magnet now points up, as it must.
- **Boundary condition.** The first build used a 3D dipole potential
  (∝ 1/r²) on a 2D problem and inflated the field near the top
  several-fold; a plain φ = 0 boundary was worse still. Replaced with
  the 2D line-dipole potential (∝ 1/r).
- **Gauss's law.** Net flux around a box enclosing the magnet ≈
  −1e-4 T·m, ~1% of the ~0.015 T·m face flux. (The residual is the
  boundary condition, not a source error.)
- **Finite-difference vs analytic 2D bar magnet** (charged-strip
  formula): ratio 0.89–0.94 near the magnet — the solver reads ~10% low,
  systematically, from central-difference smoothing across the face
  plus μ_r = 1.05. Acceptable for an order-of-magnitude model.
- **Finite-difference vs magpylib 3D cuboid:** ratio 0.69–0.76 near the
  face. That gap is the genuine 2D-vs-3D geometry difference (the 3D
  patch gives a higher near-face field than the 2D infinite strip), not
  a solver error. The far field decays as 1/r² (2D line dipole): fitted
  exponent 2.01 for the control, as expected.
- **Yoke boost.** Top-face field 1.94×, flux 1.61× vs the no-yoke
  control. The yoke does what a yoke should.
- **Spacer transparency.** No-cross = baseline to the last digit — the
  aluminium cross is invisible to the static field, as predicted.
- **Centre-material neutrality.** Copper vs graphite give identical
  field numbers; only the forces differ (by 40×). As expected for
  χ ~ 1e-5–1e-4.
- **Saturation matters.** Without the cap, the iron next to the magnet
  reached **77 T** in the yoke and **29 T** in the star — unphysical.
  With the cap, the iron stays at 1.5–2.3 T (yoke max 2.28 T, 95th
  percentile 1.98 T; star max 2.23 T). The cap cut the well depth from
  0.152 T to 0.102 T and the tip ratio from 4.4 to 2.72 — the saturated
  numbers are the honest ones, and the earlier uncapped numbers are
  superseded.
- **Rim force cross-check.** The gradient method gives −18.91 N; the
  independent Maxwell-stress estimate B²·A/(2μ0) with B = 0.235 T at
  the rim and A = 8.6e-4 m² gives **18.9 N**. Two methods agree.
  (The naive χ = 99 value, −1,891 N, is 100× too large — that is why
  the demagnetisation correction is essential. The first attempt also
  sampled the gradient across the star's top face and gave hundreds of
  newtons; sampling at the rim centroid fixed it.)
- **Well definition.** The first attempt measured the field *inside* the
  steel rim (~1.0 T) and called it the well. That is the rim's own flux
  concentration, not the well. The well is now measured on the external
  (no-badge twin) field: 0.102 T.
- **Cup-yoke bug.** The first cup run gave numbers identical to the
  flat plate — the cup walls were being overwritten by the clay region.
  Caught by the identical-numbers check; fixed (walls applied after
  the clay).
- **Determinism.** Two full runs of the final code reproduce the
  headline numbers identically.

## Honest limits — what this model cannot show

- **2D, not 3D.** The model is an infinite extrusion. The true 3D field
  is ~25% stronger near the magnet (magpylib cross-check) and decays as
  1/r³, not 1/r². Tip ratios are indicative, not exact.
- **Static only.** No eddy currents (so the aluminium cross's real
  shielding job is unmodeled), no thermal effects, no time dependence,
  no vibration.
- **Simple saturation.** The cap is a fixed-point iteration (4 passes),
  not a B-H curve; ~1,300 cells remain modestly above their cap after
  the last pass (yoke max 2.28 T vs cap 1.5 T). No hysteresis. The
  numbers are order-of-magnitude, not exact.
- **Star-tip geometry is a 2D stand-in.** The true in-plane star points
  are 3D; the taper-in-the-vertical-plane model captures flux crowding
  qualitatively.
- **Square vs cylinder** is answered only analytically (magpylib); the
  2D solver cannot distinguish them.
- **Forces are estimates** from single-point field gradients. The rim
  force is cross-checked against Maxwell stress; the diamagnetic forces
  are at the µN–mN level and the lateral force sign beyond ~10 mm
  offset is at the grid's noise level — do not read more into it than
  "the lateral push is tiny and restoring near the centre."
- **Material values are assumptions**, not measurements: N52 grade,
  cast-iron μ_r = 200, magnetic stainless μ_r = 100. If the real star
  is austenitic (non-magnetic), the tip concentration and the well
  disappear with it.

## Files

- `code/magnetic_well_sim.py` — the solver (single runnable file).
- `sim-results/results.json` — all numbers for all 11 configurations
  plus the no-badge twins.
- `sim-results/baseline_fields.npz` — baseline B, μ, and region maps
  (load with `np.load(..., allow_pickle=True)`).
- `sim-results/field_map.png` — |B| map, baseline, stack outline drawn.
- `sim-results/centerline_profile.png` — B along the vertical centreline.
- `sim-results/well_profile.png` — B across the badge at badge height:
  external field (well), with badge (rim concentration), control.
