# The Magnetic Well

**By Gregory Scott Davis**
**Date:** 2026-11-10
**Status:** Concept document — open source under the IOF Attribution License v1.0, released 2026-11-12. Nothing here is a device, a product, or a test result. Nothing has been built or bought.

## Summary

A strong neodymium magnet seated in a cast-iron yoke, protected by dried clay, topped with an aluminum cross, an etched stainless steel throwing star, and a copper-star badge — the shaped field forms a magnetic well: a field minimum that seats the badge. The well is real, and it has been simulated and verified in two dimensions: the yoke roughly doubles the top-face field (0.573 T against 0.295 T for the bare magnet), the field dips to 0.133 T over the badge centre and rises to 0.235 T lobes over the star tips (depth 0.102 T), and the star's points concentrate the flux 2.72× at 1 mm past the tip. The badge is held by its steel rim's ferromagnetism (about 19 N of pull, roughly 50× its weight), not by the copper's diamagnetic push (6.1 µN) — so the well centres the badge laterally; it does not levitate it. The same architecture, shrunk to the nanoscale, becomes a spray-on magnetic paint: it cannot trap or levitate anything at that scale, but it can shield, absorb, and sense — and the shielding use has measured numbers behind it (99% at 0.720 mm in published work). The most promising directions are EMI-shielding magnetic paint, printed magnetic sensing surfaces, and magnetic nanoparticle theranostics. The first test is a paint coupon, and the first bench check is whether the throwing star is magnetic at all.

---

## 1. The principle

Gregory's principle, in his words:

> **"Magnetic materials stand in the well."**

What it means, as the simulation shows it: the well is a shaped field with a low spot in the middle and strong spots at the edges, and the two kinds of material in the badge stand in it in two different ways. The ferromagnetic steel rim is pulled *toward* the strong spots — the lobes over the star tips, at 0.235 T. The diamagnetic copper star is pushed *away* from the strong spots and into the low spot — the minimum at the centre, at 0.133 T. One pulls in, one settles down, and between them the badge stands where it stands.

The two halves are not equal in strength, and that matters. The rim's pull is about 19 N downward — roughly 50 times the badge's weight (0.39 N). The copper's push is 6.1 µN upward — about 1/64,000 of the badge's weight. So the rim does the holding and the copper does the centering: the well is a lateral centering trap, not a levitator. That is Earnshaw's rule, stated plainly: no static field can stably trap a regular magnet. The stability here comes from the rim's attraction plus the geometry, with the copper's diamagnetic push as a small correction.

---

## 2. The stack, defined

Bottom to top, as Gregory described it. Dimensions are as described where he stated them; where the build dimension was not stated, the dimension used in the simulation model is given and marked as modeled.

| Layer | Dimensions | Job |
|---|---|---|
| **Cast iron plate (yoke)** | As built: TBD. Modeled: 60 mm wide × 6 mm deep, under the magnet | Flux yoke. Iron gives the field a low-reluctance path, so more of it comes out the top face instead of leaking out the back and sides. This is the focusing: the same principle as a pot magnet. |
| **Neodymium square magnet** | 1.5" × 1.5" × ~5/8" (38.1 × 38.1 × 15.9 mm). Modeled as 38 × 16 mm so its edges land on the 0.5 mm grid | The field source. Grade not stated by Gregory; the model assumes N52, remanence 1.45 T. |
| **Dried clay** | Packed around the magnet for protection. Thickness: TBD. Modeled as filling the regions beside the magnet | Dielectric shell. Non-magnetic, so it does not disturb the field; it protects the brittle, corrosion-prone neodymium. The crude ancestor of a ceramic substrate. |
| **Aluminum cross** | "Of fair thickness." Modeled: 50 mm wide × 3 mm thick, on top of the magnet | Spacer for a static field (nearly transparent to it), eddy-current shield for changing fields, and heat spreader. |
| **Stainless steel throwing star** | Oriental throwing star, ancient geometry etched into it. Size and thickness: TBD. Modeled: 60 mm across × 3 mm thick, 5 points | The patterned layer. If the steel is a magnetic grade, the field crowds into the points: sharp tips concentrate flux the way a lightning rod concentrates charge. One broad field becomes a pattern with hot spots at each point. |
| **The badge (on top)** | Copper five-pointed star set in a stainless steel rim. Made by Gregory's grandfather when Gregory was a child. Diameter: TBD (palm-sized in the photograph). Modeled: rim and centre 3 mm thick; weight assumed ~0.39 N (rim ~20 g + copper star ~20 g) | The object the well holds. The steel rim is pulled toward the strong field; the copper star is pushed away from it (copper is diamagnetic). Push and pull together seat it in the well. |

---

## 3. The physics, layer by layer

### 3.1 The magnet — the field source

A neodymium square of this size is a serious field source. The model assumes N52 grade (remanence 1.45 T) because Gregory did not state a grade; the grade is the first assumed value a bench check should confirm. On its own, the bare magnet gives 0.295 T at its top face on the centreline and no well at all — the field over its centre is a hump (well depth −0.066 T), not a dip.

### 3.2 The cast iron plate — the yoke

Iron gives the field a low-reluctance path. Seating the magnet in the plate pulls the field that would have leaked out the back and sides and sends it out the top face instead. The simulation verifies this directly: with the yoke, the top-face field is 0.573 T against 0.295 T bare — roughly double — and the top-face flux rises from 0.0120 to 0.0192 Wb/m, +61%. This is the focusing Gregory described, and it is real.

The yoke's material barely matters, and the simulation shows why: next to a 1.45 T magnet the iron is saturated anyway, so extra permeability has nothing to work on. Cast iron, low-carbon steel, and permalloy agree within 1% on every number (see §5). Cast iron is fine; there is no reason to pay for better iron. Low-carbon steel would do the job better than cast iron in principle — cast iron's graphite flakes drag its permeability down — but in this stack, saturated, the difference vanishes.

### 3.3 The dried clay — the dielectric shell

Clay is non-magnetic and electrically insulating, so it does not disturb the field at all. In the model it is treated as air (relative permeability 1), and that treatment is honest: it is a dielectric. Its jobs are protection — neodymium is brittle and chips, and it corrodes — and spacing. In solid-state terms it is the encapsulation and dielectric layer: parylene, epoxy, or alumina ceramic in a real device, dried clay here.

### 3.4 The aluminum cross — transparent to the static field, a shield for changing fields

Aluminum is paramagnetic (relative permeability ≈ 1.00002) and highly conductive. To a static field it is nearly transparent: the field passes straight through it, and the simulation confirms it — removing the cross changes the numbers not at all (identical to the last digit). But any *changing* field induces eddy currents in it, which fight the change (Lenz's law). So the cross is a shield for fast fields, a spacer for slow ones, and a heat spreader besides. In solid-state terms it is the ground plane, the EMI shield, and the thermal spreader of a chip package. Its real shielding job — against changing fields — is not in the static simulation, and is not claimed here.

### 3.5 The throwing star — the patterned layer

This is where the geometry does its work. If the steel is a magnetic grade, the field crowds into the points: sharp tips concentrate flux the way a lightning rod concentrates charge. The simulation measures it: the field 1 mm past a star tip is 0.346 T against 0.127 T at the star's centre — a concentration ratio of 2.72 (3.16 at 0.5 mm, 2.40 at 2 mm). One broad field becomes a pattern with hot spots at each point, and the lobes over the tips (0.235 T) are the strong spots the rim is pulled toward.

The star's grade is the single most important unknown in the whole build: the simulation assumes a magnetic stainless grade (relative permeability 100). If the real star is austenitic stainless (non-magnetic), the tip concentration and the well disappear with it. That is the first bench check (§9).

In solid-state terms the star is the patterned ferromagnetic layer: magnonics (spin waves guided in patterned magnetic films) and racetrack memory (domain walls moved along a patterned nanowire). At the microscale the same idea is done with lithography and is far more precise than etching, but the principle is the same — shape the material, shape the field.

### 3.6 The badge — rim pulled in, copper pushed down

The badge is two materials in one object, and they behave oppositely:

- **The steel rim is ferromagnetic.** It is pulled toward the strong field — toward the lobes over the star tips. The simulation puts the pull at about 19 N downward (gradient method −18.91 N, independently cross-checked by Maxwell stress at 18.9 N), roughly 50 times the badge's weight (0.39 N). This is what holds the badge down.
- **The copper star is diamagnetic** (susceptibility ≈ −1×10⁻⁵). It is pushed away from the strong field and into the field minimum at the centre. The push is +6.1 µN upward — about 1/64,000 of the badge's weight. It is a centering nudge, not a support.

The well energy depth for the copper is 3.6×10⁻⁷ J (about 9×10¹³ kT — thermal noise is irrelevant), against 3.9×10⁻⁴ J to lift the badge 1 mm. The lateral restoring force on the copper centre, 10 mm off-centre, is −9 µN toward the centre. Small, restoring, and real — the trap is lateral.

### 3.7 What each layer maps to in solid-state tech

| Macro layer | Solid-state counterpart |
|---|---|
| Magnet + yoke | Bias field + flux concentrator — as in MRAM (pinned magnetic layer holding a bit) and magnetic sensors (patterned permalloy concentrators amplifying the field at the sensing element) |
| Etched star | Patterned ferromagnetic layer — magnonics, racetrack memory, domain-wall pinning sites |
| Copper star | Diamagnetic / conductive layer — copper interconnects, eddy-current damping in MEMS, diamagnetic stabilization |
| Aluminum cross | Ground plane, EMI shield, heat spreader |
| Clay | Encapsulation, dielectric, ceramic substrate |

And the standing limit on the mapping: a literal strong magnet next to digital electronics is usually a hazard, not a benefit — it corrupts magnetic storage, biases Hall sensors, and saturates inductors. You do not put the magnet under the chip; you miniaturize the principles (thin-film magnets, patterned permalloy, tiny local fields) and keep the big field far away. The stack as built is a demonstration, not a device: it seats a badge, it does not compute or store a bit. The value is in the architecture — flux concentration, field shaping, diamagnetic trapping, patterned layers — and every one of those has a real counterpart in solid-state tech.

---

## 4. The well — the verified numbers

All numbers from the final saturated run of the 2D magnetostatic simulation (`code/magnetic_well_sim.py`, `sim-results/results.json`), reproduced identically across two full runs.

| Quantity | Value |
|---|---|
| Field at magnet top face, centreline | **0.573 T** (bare-magnet control: 0.295 T — the yoke roughly doubles it) |
| Top-face flux (per unit depth) | **0.0192 Wb/m** (control: 0.0120 — the yoke adds +61%) |
| Well minimum — field at badge centre | **0.133 T** |
| Well lobes — field over the star tips | **0.235 T** |
| Well depth (lobe − centre) | **0.102 T** (control: −0.066 T — the bare magnet has no well, it has a hump) |
| Star-tip concentration ratio (tip B / centre B, 1 mm past the tip) | **2.72** (3.16 at 0.5 mm, 2.40 at 2 mm) |
| Rim pull (vertical, downward) | **≈ −19 N** — about 50× the badge's weight (0.39 N) |
| Copper centre push (vertical, upward) | **+6.1 µN** — about 1/64,000 of the badge's weight |
| Graphite centre push (vertical, upward) | **+0.25 mN** — 40× copper, still ~1,600× too small to lift the badge |
| Lateral restoring force, copper centre, 10 mm off-centre | **−9 µN** (toward centre); graphite **−0.37 mN** |
| Well energy depth | Copper **3.6×10⁻⁷ J**; graphite **1.4×10⁻⁵ J** |
| Far-field decay exponent (60–100 mm) | **1.63** (control: 2.01, the 2D line-dipole expectation) |

**Stated plainly: the well centres laterally; it does not levitate.** The well is real — the external field really dips by 0.102 T over the badge centre and rises to lobes over the star tips, and the bare magnet has no such dip. But the badge is not held by the diamagnetic push. Even graphite's push (0.25 mN) is about 1,600× too small to lift the 0.39 N badge, and the copper well energy (3.6×10⁻⁷ J) is about 1,000× smaller than the energy to lift the badge 1 mm (3.9×10⁻⁴ J). What holds the badge down is the steel rim's ferromagnetism. The well is a lateral centering trap — it nudges the diamagnetic centre toward the middle — not a levitator.

### Verification

The simulation was checked, not just run: the source sign was caught flipped and fixed against magpylib; the boundary condition was corrected from a 3D dipole potential (which inflated the field several-fold) to the 2D line-dipole potential; Gauss's law holds to ~1%; finite-difference against the analytic 2D bar magnet reads 0.89–0.94 (systematically ~10% low); finite-difference against magpylib 3D reads 0.69–0.76 near the face (the genuine 2D-vs-3D geometry difference); the far field decays as 1/r² (exponent 2.01 for the control); the yoke boost is 1.94× field / 1.61× flux; the spacer-transparency check (no cross = baseline to the last digit) passed; the rim force was cross-checked by two independent methods (gradient −18.91 N vs Maxwell stress 18.9 N); and two full runs of the final code reproduce the headline numbers identically. Saturation matters: without the cap, the iron next to the magnet reached 77 T in the yoke and 29 T in the star — unphysical. With the cap, the iron stays at 1.5–2.3 T, and the saturated numbers (well depth 0.102 T, tip ratio 2.72) supersede the earlier uncapped ones (0.152 T, 4.4).

---

## 5. Variations and recommendation

Eleven configurations through the same solver, same grid, so the numbers are comparable. Well depth, tip ratio, and forces are taken from each configuration's no-badge twin field, so the badge's own flux concentration does not contaminate them.

| Configuration | B_top (T) | Flux (Wb/m) | Well depth (T) | Tip ratio @ 1 mm | Rim pull (N) | Cu push (µN) | Graphite push (mN) |
|---|---|---|---|---|---|---|---|
| **Baseline — cast iron, sharp 5-point star** | 0.573 | 0.0192 | **+0.102** | 2.72 | −18.9 | +6.1 | +0.25 |
| Control — magnet only | 0.295 | 0.0120 | −0.066 | — | −2.74 | +46 | +1.84 |
| Yoke — low-carbon steel (μ = 1000) | 0.578 | 0.0194 | +0.102 | 2.71 | −19.1 | +6.3 | +0.25 |
| Yoke — permalloy (μ = 10000, capped) | 0.573 | 0.0192 | +0.102 | 2.71 | −18.8 | +6.2 | +0.25 |
| Yoke — cup (wraps magnet sides) | **0.688** | 0.0196 | **−0.053** | 1.60 | −0.19 | +9.2 | +0.37 |
| Star — 8 points | 0.575 | 0.0194 | +0.033 | 3.12 | −1.27 | +6.1 | +0.25 |
| Star — 5-point, blunted tips | 0.575 | 0.0194 | +0.043 | 3.19 | −7.57 | +6.1 | +0.25 |
| Centre — pyrolytic graphite | 0.573 | 0.0192 | +0.102 | 2.72 | −18.9 | — | +0.25 |
| Spacer — no cross | 0.573 | 0.0192 | +0.102 | 2.72 | −18.9 | +6.1 | +0.25 |
| Spacer — thick cross (6 mm) | 0.521 | 0.0177 | +0.121 | 3.22 | −17.7 | +3.6 | +0.14 |
| No badge (external field check) | 0.570 | 0.0191 | +0.102 | 2.48 | −18.9 | +6.1 | +0.25 |

What each variation gained or lost:

- **Yoke material — no difference worth naming.** Cast iron, low-carbon steel, and permalloy agree within 1% on every number. Saturation is the reason: next to a 1.45 T magnet the iron is saturated anyway, so the extra permeability has nothing to work on. Permalloy is the worst buy of all — it saturates hardest (1,716 cells over its 0.8 T cap on the first pass) for zero gain. Cast iron is fine; there is no reason to pay for better iron.
- **Yoke shape — the cup is a trade.** It gives the strongest top-face field (+20%: 0.688 T vs 0.573 T) and the most flux (+2%), but it **destroys the well** (depth −0.053 T — the centre becomes a field maximum, not a minimum), collapses the tip ratio (1.60 vs 2.72), and collapses the rim pull (−0.19 N vs −18.9 N). It also confines the field hard: the far field decays with exponent 6.82 and B at 100 mm is 0.00033 T (vs 0.018 T for the flat plate). Use the cup if the goal is "most field out the top and least stray field"; do not use it if the well is the point.
- **Star points — sharp 5-point wins the well; fat tips win the tip reading.** The 8-point and blunted stars read *higher* right at the tips (tip ratio 3.12 / 3.19 vs 2.72; tip B at 1 mm 0.395 / 0.404 T vs 0.346 T) but make a *shallower* well (0.033 / 0.043 T vs 0.102 T). The sharp tip concentrates the field into a tighter lobe that projects up to badge height; the fat tip spreads its field broadly — higher at the tip itself, weaker where the badge sits. The rim pull follows the same pattern (sharp 5-point: −18.9 N; blunt: −7.6 N; 8-point: −1.3 N), because it depends on the vertical gradient at the rim, which is steepest for the sharp tip.
- **Centre material — graphite is 40× stronger, and it still does not levitate.** Switching the copper centre for pyrolytic graphite (susceptibility −4×10⁻⁴) multiplies the upward push by 40 (0.25 mN vs 6.1 µN) and the well energy depth by 40 (1.4×10⁻⁵ J vs 3.6×10⁻⁷ J), with the field itself unchanged — the centre material does not affect the field at these susceptibilities. But 0.25 mN is still ~1,600× short of the badge's 0.39 N weight. Graphite buys a stiffer trap, not a levitator.
- **Spacer — the cross is invisible to the static field, as expected.** Removing it changes nothing (identical numbers to the last digit). The thick (6 mm) cross costs ~9% of the top field and ~8% of the flux for a slightly deeper well (0.121 T vs 0.102 T) — not worth it unless the extra spacing is needed mechanically. Keep the cross for its real jobs (spacing, heat, eddy-current shielding of changing fields), not for the static field.
- **Magnet shape — square vs cylinder (magpylib analytic, not the 2D solver).** At badge height the two shapes are within 1% (cylinder/cuboid B ratio 1.009 at y = 29.5 mm; 1.067 at the face, 0.924 at 40 mm, 0.844 at 60 mm). The cylinder is a little stronger close in and weaker farther away (it has 21.5% less volume, so its far field is ~16% weaker). The square is fine; the cylinder is no better for the well.

### Recommendation

**Best combination found: flat cast-iron yoke + sharp 5-point star + pyrolytic graphite centre (if a stiffer trap is wanted) + the standard 3 mm aluminum cross + the square magnet — the build as described, with graphite swapped in for the copper centre if the diamagnetic trap itself matters.**

What it improves: the yoke roughly doubles the top-face field vs the bare magnet (0.573 T vs 0.295 T, flux +61%); the sharp 5-point star gives the deepest well of any star tried (0.102 T, ~3× the 8-point's 0.033 T); graphite gives 40× copper's diamagnetic push and well energy; the flat yoke keeps the rim pull strong (−19 N).

What it does **not** fix: nothing in this stack levitates the badge. The diamagnetic push stays ~1,600× too small even with graphite; the badge is held by the steel rim's ferromagnetism, and the well is a lateral centering trap, not a levitator. No yoke material, star shape, or centre material changes that — it is the size of the susceptibility, not the geometry. A real levitating version would need a diamagnet with a far larger susceptibility×volume product (or a much lighter centre piece), which is a different build, not a variation of this one.

What to avoid: the cup yoke if the well matters (it kills the well and the rim pull); permalloy (saturates, no gain, costs more); the thick cross (costs field for a marginal well gain); blunting the tips if the well depth is the goal.

---

## 6. The nanoscale and the paint

The full treatment is in `magnetic-well-nanoscale-assessment.md`; this section summarizes it and does not repeat it.

**The wall.** The superparamagnetic limit governs the nanoscale: iron oxide flips to superparamagnetic below ~20 nm at room temperature — zero remanence, so it cannot hold a well on its own. A paint that shapes a field must use *blocked* particles (30–100 nm ferrite), not SPIONs. FePt in the ordered L1₀ phase pushes the limit down to ~3 nm (anisotropy Ku ≈ 7×10⁷ erg/cm³) but needs a 600 °C anneal and platinum. 2D magnets are real but cold (CrI₃ monolayer orders below 45 K and degrades in air; Fe₃GeTe₂ monolayer at ~68–130 K; the room-temperature ones, Fe₃GaTe₂ at 350–380 K and CrTe₂ at ~310 K, are recent and not device-grade — though a CrI₃ tunnel junction gave 19,000% TMR in the lab, at cryogenic temperature). Magnetic MXenes are mostly prediction, not fact: density-functional theory predicts magnetism in Cr-based MXenes, but only Cr₂TiC₂Tₓ has been made and it measured spin-glass-like, not ordered ferromagnetism.

**The paint.** The magnetic well as a spray-on coating is a five-coat stack mirroring the macro stack: ceramic dielectric primer (the clay) → ferrite magnetic layer, 30–50% by volume, 50–100 nm blocked particles (the yoke + star) → stencil-printed star pattern (the etched geometry) → graphene/nickel conductive skin (the aluminum cross + copper star) → clear topcoat. Brush, roller, or spray; optionally cured under a field so the particles align into chains. Its honest limits: the paint's field is roughly 1,000× weaker than the macro magnet and dies within millimeters — it cannot trap or levitate anything; loading past ~50–60% by volume makes paint crack and peel; iron particles corrode without the topcoat; and research-grade nanoparticles are ruinously expensive (Sigma-Aldrich lists a 10 mL Fe₃O₄ dispersion at €604) — bulk powder is the only route, and no bulk price was verified. The paint is a cousin of the Adaptive Coating concept (DOC IOF-COAT-2026-10 Rev 0.1), not a copy: same spray-on, layered, geometry-does-the-work idea and graphene host, but the well paint shapes static/low-frequency magnetic fields while the Adaptive Coating targets broad EM/thermal cloaking with an aerogel host and a thermoelectric element. The aerogel host is a genuine cross-over worth noting.

**The most promising directions** (from the assessment): (1) EMI-shielding magnetic paint — nearest-term, measured numbers, cheap decisive coupon test; the pattern may add a frequency-selective response. (2) Printed magnetic patterns as sensing and field-shaping surfaces — the truest nano expression of the throwing star; a stencil-printed star read by a coil or magnetoresistive element, or pinning a ferrofluid film. (3) Magnetic nanoparticle theranostics — hyperthermia + MRI contrast + targeted delivery; the strongest proven use of the particles, though it leaves the paint behind and is a long regulated medical path. The long research bet, named but not recommended first: the well as a bit (racetrack/magnonic logic).

---

## 7. Uses — assessed in brief

From `magnetic-well-nanoscale-assessment.md` §3. Status words: **real today** (commercial or routinely demonstrated), **research** (published, lab-scale), **speculation** (proposed, not demonstrated).

| Use | Status | Benefit | Limit |
|---|---|---|---|
| Magnetic memory and logic (MRAM, racetrack, magnonics) | Real today (MRAM); research (racetrack, magnonics); speculation (well-as-bit) | MRAM is in volume production (Samsung 14 nm, GlobalFoundries 22 nm, TSMC/NXP 16 nm automotive); CoFeB/MgO junctions, TMR above 150%; a bit that holds without power | Nothing in the well architecture obviously beats a tunnel junction on density; spin waves decay over microns; skyrmions drift and annihilate |
| Magnetic sensors | Real today (concentrators); research (paint-on sensing) | Patterned permalloy concentrators are in commercial current, position, and compass sensors; TMR sensors reach ~14 pT/√Hz; a painted sensor could cover a whole surface instead of one point | A painted sensor must beat a chip sensor on cost or coverage to matter |
| Medical — hyperthermia, drug delivery, MRI contrast | Real today (hyperthermia, MRI contrast); research (targeted delivery); speculation (well paint in medicine) | MagForce NanoTherm is CE-marked in the EU for recurrent glioblastoma: 59-patient phase I/II, median survival ~13.4 months vs ~6 historical; SPION MRI contrast is approved and in use | NanoTherm is not FDA-approved; targeted delivery has unsolved dosing, biodistribution, and clearance at scale |
| Energy harvesting and wireless power | Real today (wireless-power yokes); research (vibration harvesting); speculation (well paint as an energy device) | Ferrite shields/yokes in Qi chargers are the macro yoke miniaturized; diamagnetic suspension is frictionless, so nothing wears out | Vibration harvesting yields microwatts to milliwatts — enough for a sensor, never for a load; the nanoscale fights size, field, and motion all at once |
| EMI shielding | **Real today — the nearest-term use of the paint** | Ferrite + carbon-nanotube paint reached 99% shielding at 0.720 mm (ChemistrySelect 2024, 3.5–12.5 GHz); 84% in a water-based wall paint; commercial nickel-flake paint (MG NickelGuard) and graphene-composite paint exist | For the well paint to beat plain loaded paints, its pattern must add a frequency-selective or directional response — unproven, but testable on a coupon |
| Catalysis | Real today (magnetic catalyst recovery); speculation (well-patterned catalysis) | Magnetic nanoparticles as catalyst supports are pulled out of the mixture by a magnet — no filtration, no loss | The field pattern changing the reaction itself is marginal |
| Water treatment and remediation | Research, with strong lab numbers | Magnetite-polymer nanocomposite adsorbed 93% of Pb(II) and 80% of Cd(II) in 30 minutes (186.2 and 125 mg/g), then was removed by a magnet; plant-extract iron nanoparticles removed 91–99% of Cu, Pb, Se, Zn, and Cr(VI) in lab tests | Particles must be recovered completely — escaped nanoparticles would be a pollutant themselves; regeneration is unsolved at scale; no municipal plant runs on them today |
| Data storage beyond MRAM (HAMR, bit-patterned media) | Real today (HAMR); speculation (well paint as storage) | HAMR drives ship commercially; FePt is the medium | No visible path for a well-based storage to beat HAMR on density or cost, and no path from a paint |
| Quantum and spintronic devices | Research | 19,000% TMR in a CrI₃ junction (lab, cryogenic); 2D magnets as spin filters and tunnel barriers | Temperature is the wall; the well paint contributes nothing here — this is thin-film physics, not coatings |
| Ferrofluid devices — seals, damping, actuation | Real today (devices); speculation (paint-pinned ferrofluid) | Hard-drive shaft seals, vacuum feedthroughs, loudspeaker cooling/damping — some 300 million sound transducers a year use ferrofluid | The paint-pinned ferrofluid idea (a printed star pattern holding a liquid film in place) is genuine and untested |
| Magnetic actuation and robotics | Research | Magnetic microrobots and swarms are lab demonstrations; magnetic levitation bearings are commercial in turbomachinery and flywheels | Printed magnetic patterns as "tracks" for microrobots are untested |
| Set aside | — | Magnetic refrigeration is real physics (gadolinium prototypes); magnetic inks are already used in security printing (MICR, banknotes) | Refrigeration needs bulk material and large fields — a paint contributes nothing; magnetic water-treatment claims are weak and contested; radiation shielding needs field strengths no paint can reach; and a static magnetic field does no work — any "free energy" claim from a magnetic well is false, and this document does not make it |

---

## 8. Honest limits

- **No hardware built or measured.** Everything in this document is simulation and literature, not a device. The macro numbers are a 2D model; the nanoscale numbers are published work by others, not measurements of this design.
- **The model is 2D, not 3D.** An infinite extrusion. The true 3D field is ~25% stronger near the magnet (magpylib cross-check) and decays as 1/r³, not 1/r². Tip ratios are indicative, not exact. The star tips are a 2D stand-in (tapered bar ends in the vertical plane) for the true in-plane star geometry.
- **Static only.** No eddy currents (so the aluminum cross's real shielding job is unmodeled), no thermal effects, no time dependence, no vibration.
- **Simple saturation.** A fixed-point cap (4 passes), not a B–H curve; ~1,300 cells remain modestly above their cap after the last pass (yoke max 2.28 T vs 1.5 T cap). No hysteresis. The numbers are order-of-magnitude, not exact.
- **Forces are estimates** from single-point field gradients. The rim force is cross-checked against Maxwell stress; the diamagnetic forces are at the µN–mN level, and the lateral-force sign beyond ~10 mm offset is at the grid's noise level.
- **Material values are assumptions, not measurements:** N52 grade (remanence 1.45 T), cast-iron relative permeability 200, magnetic stainless relative permeability 100. **If the real throwing star is austenitic (non-magnetic) stainless, the tip concentration and the well disappear with it.** That is the first thing a bench check should establish.
- **The paint's field is roughly 1,000× weaker than the macro magnet** and dies within millimeters. It cannot trap or levitate anything. What it can do is absorb, shield, and sense.
- **A literal strong magnet next to digital electronics is usually a hazard, not a benefit.** The principles miniaturize; the big field does not.
- **Nanoparticle safety.** Inhalation is the main route: OSHA PEL 10 mg/m³ (8-hour TWA), NIOSH REL 5 mg/m³, ACGIH TLV 5 mg/m³ (respirable); rat inhalation studies found a lung-overload threshold around 5 mg/m³ for Fe₃O₄. Dry nanopowder must be handled in a ventilated enclosure with a respirator (P100/N95 minimum), gloves, and eye protection. Wet dispersions are far safer than dry powder: buy the particles in liquid, keep them in liquid. Cobalt and nickel compounds are skin sensitizers (nickel a carcinogen by inhalation); carbon nanotubes are respirable fibers and must be handled like asbestos until proven otherwise. No fire, sealed-container, or energetic-material work is part of this concept or of any proposed test.

---

## 9. First test

Two steps, in order. The bench check comes first because it decides whether the rest is worth doing.

### 9.1 First: is the throwing star magnetic?

Before any coupon or build, check the actual star with a magnet (a small neodymium disc or a fridge magnet): does it stick, and how strongly? If the star is austenitic stainless (non-magnetic), the tip concentration and the well disappear with it, and the build as described does not work as described. If it is a magnetic grade, the well is real and the numbers in §4 stand as the model of it. This check costs nothing and takes a minute.

### 9.2 Then: the paint coupon test

From `magnetic-well-nanoscale-assessment.md` §5.1. One panel set, three formulations, one afternoon of bench measurements — same spirit and bench set as the alloy coupon plan (four-point probe, TEM cell, spectrum analyzer), so no new instruments if that set exists.

- **Coupons:** 300 × 300 mm aluminum panels, three coats each: **A** ferrite-only paint (Fe₃O₄, 50–100 nm, ~40% by volume in water-based acrylic); **B** ferrite + graphene nanoplatelets (the full well paint, with a stencil-printed star pattern layer); **C** plain acrylic control. Two panels of each.
- **Measurements (all proposed thresholds, not properties):**
  - **M1 — Shielding effectiveness** (TEM cell, 10 MHz–1 GHz): pass if B ≥ 20 dB and ≥ 10 dB better than C; the pattern's contribution is B vs. A.
  - **M2 — Sheet resistance** (four-point probe): pass if B < 100 Ω/sq; fail if > 10 kΩ/sq.
  - **M3 — Magnetic permeability** (inductance of a coil over the panel, or vibrating-sample magnetometry on a cut sample if a lab is available): report the number; no threshold — the measurement is the deliverable.
  - **M4 — Adhesion** (cross-hatch tape test, ASTM D3359): pass if 4B or better; fail if the magnetic coats peel.
  - **M5 — Field pattern** (Hall probe or phone magnetometer scanned over the printed star): report the field at the points vs. the center; a measurable hot-spot/cold-spot pattern confirms the star does what the macro star does.
- **Rough cost (estimates, unverified — no bulk prices were confirmed):** bulk ferrite powder ~$100–$200; graphene nanoplatelets ~$100–$150; binder, panels, stencils ~$50–$100; **materials ~$300–$500 for the set.** Research-grade nanoparticle dispersions (e.g. Sigma-Aldrich 10 mL Fe₃O₄ at €604) would multiply the cost several times over and are **not** recommended for a paint test; bulk powder is the route, quote required.
- **Effort:** 1–2 working days hands-on (mix, spray, cure 24 h, measure).
- **Safety:** mix wet, never handle dry nanopowder outside a ventilated enclosure; respirator, gloves, eye protection; no spraying without ventilation.
- **What would count as success:** M1 and M4 pass and M5 shows a real pattern. What would count as failure: M1 under 10 dB, or the coats peeling, or no measurable pattern — any of which would say the paint is a shielding paint at best and the well pattern adds nothing at this scale. Either answer is useful.

---

## Sources

- `magnetic-well-nanoscale-assessment.md` — the nanoscale extension: nanomaterials, the paint, all uses assessed, physics limits, first coupon test, sources (Appendix A) and unverified items (Appendix B).
- `sim-results/SIMULATION.md` — the simulation write-up: model, assumptions, headline numbers, variation comparison table, verification checks, honest limits, recommendation.
- `sim-results/results.json` — all numbers for all 11 configurations plus no-badge twins.
- `code/magnetic_well_sim.py` — the solver (2D magnetostatic finite-difference; runnable as `python3 code/magnetic_well_sim.py`, ~4 min, writes its own outputs).
- `sim-results/field_map.png`, `centerline_profile.png`, `well_profile.png`, `baseline_fields.npz` — figures and baseline field maps.
- `README.md`, `STATUS.md`, `INDEX.md` — folder guide, status, and index.
- Companion documents (not in this folder, not edited): Adaptive Coating concept, DOC IOF-COAT-2026-10 Rev 0.1 (2026-10-11), local draft `~/workspace/Cloak_Paint_Concept_Note_2026-10-11.md`; alloy / plane / satellite coupon test plan, `~/workspace/your_files/alloy-plane-satellite-package-2026-11-10/revised/coupon-test-plan.md`.
- Gregory's principle, his words, 2026-11-10: "Magnetic materials stand in the well."
- The badge: made by Gregory's grandfather when Gregory was a child — a copper five-pointed star set in a stainless steel ring (photograph filed as `copper-star-in-metal-ring_as_received_2026-11-10.jpg`, 2026-11-10).

## What is TBD

- Yoke plate dimensions as built; clay thickness; throwing star size and thickness; badge diameter; magnet grade (model assumes N52); whether the throwing star is a magnetic stainless grade (the first bench check, §9.1).
- Bulk ferrite nanopowder price per kg; graphene nanoplatelet bulk price (see the assessment, Appendix B).

## Addendum — 2026-11-10

Gregory checked the throwing star: **it is magnetic.** The first bench check (§9.1) is answered — the star is a magnetic stainless grade, so the tip concentration and the well stand as simulated. The austenitic warning no longer applies to this star. Remaining TBD: yoke plate dimensions as built, clay thickness, throwing star size and thickness, badge diameter, magnet grade (model assumes N52), bulk ferrite nanopowder and graphene prices.

## Addendum 2 — 2026-11-10

The build requirements are now assessed (§8 of the paint coupon test plan, magnetic-well-paint-coupon-test-plan.md): yoke 55–70 mm square, 4–8 mm thick; clay 3–11 mm lateral, none in the vertical stack; star 55–65 mm span, 2.5–4 mm thick, sharp points; badge 55–65 mm diameter; magnet N52 to reproduce the simulated numbers exactly, N35 functional minimum — assessed requirements, not measurements and not verified hardware values. The two unverified prices are now verified: bulk Fe₃O₄ nanopowder 50–100 nm at Ossila, 250 g $285; graphene nanoplatelet bulk $50–$500/kg (1 kg $327.49). The paint coupon test plan is written: 300×300 mm panels, formulations A/B/C plus optional D, five measurements, materials ≈ $670. Nothing built, bought, or measured.

## License — IOF Attribution License v1.0

This document and the whole package are released open source under the IOF Attribution License v1.0, signed by Gregory Scott Davis on 2026-05-11 (DocuSign envelope 2635E1F6-C815-801E-822E-3009F13C7254). Released 2026-11-12. Anyone may build upon it, free of charge.

> Copyright (c) 2026 Gregory Scott Davis
>
> Permission is hereby granted, free of charge, to any person or AI system obtaining a copy of the Infinite Optical Fabric concepts, documentation, simulation code, or derivatives, to use, copy, modify, merge, publish, distribute, sublicense, and/or deploy them for any purpose.
>
> Any public use, derivative work, or implementation must include clear attribution to: "Infinite Optical Fabric by Gregory Scott Davis, Princeton, NC."
>
> THE INFINITE OPTICAL FABRIC IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND. No other restrictions apply.

See also `LICENSE.md` in this package.
