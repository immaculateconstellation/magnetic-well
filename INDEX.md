# Magnetic Well — package index (2026-11-10)

Open source under the IOF Attribution License v1.0, released 2026-11-12. Nothing here is a device, a product, or a test result. Nothing has been built or bought. The package was sent to three named recipients 2026-11-10 (Justin Asendorf, Bishop Tyler Carey, Raymond Turley).

## Contents

- `LICENSE.md` — the IOF Attribution License v1.0: free for anyone to use, copy, modify, and build upon, with attribution.
- `README.md` — folder guide.
- `STATUS.md` — what is done, what is verified, what is still open.
- **magnetic-well-concept.md** — the canonical concept document ("The Magnetic Well," by Gregory Scott Davis, 2026-11-10): his principle stated prominently ("Magnetic materials stand in the well"), the stack defined layer by layer, the physics, the verified sim numbers, the 11-configuration variation table and recommendation, the nanoscale/paint summary, all uses, honest limits, and the first test (bench check first: is the star magnetic? then the paint coupon test).
- **magnetic-well-nanoscale-assessment.md** — the nanoscale extension: current nanomaterials per layer, the spray-on magnetic paint, every use assessed with benefits and honest limits, the three most promising directions, and a first coupon test.
- **magnetic-well-paint-coupon-test-plan.md** — the first physical test of the spray-on magnetic paint: 300×300 mm panels, formulations A/B/C plus optional D, five measurements with proposed pass/fail criteria, materials ≈ $670, and §8 with the assessed macro build requirements.
- `code/magnetic_well_sim.py` — 2D magnetostatic solver for the macro stack. Run: `python3 code/magnetic_well_sim.py` (~4 min; writes `sim-results/` outputs itself).
- `sim-results/SIMULATION.md` — simulation write-up: model, assumptions, headline numbers, variation comparison table, verification checks, limits, recommendation.
- `sim-results/results.json` — all numbers for 11 configurations plus no-badge twins.
- `sim-results/field_map.png` — B-field map over the stack.
- `sim-results/centerline_profile.png` — B along the vertical centerline.
- `sim-results/well_profile.png` — the well profile across the badge.
- `sim-results/baseline_fields.npz` — baseline B, permeability, and region maps.

## The stack

Neodymium magnet (1.5" × 1.5" × 5/8") → cast iron yoke → dried clay → aluminum cross → etched stainless steel throwing star → grandfather's badge (copper star, steel rim) on top. The shaped field forms a magnetic well — a field minimum that seats the badge.
