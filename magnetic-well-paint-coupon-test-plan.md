# Paint Coupon Test Plan — Magnetic-Well Spray-On Paint

> **Date:** 2026-11-10. **Package:** `magnetic-well-2026-11-10/`,
> `magnetic-well-paint-coupon-test-plan.md`. **Private/local only** — nothing in
> this plan has been published, sent, or shared anywhere, and nothing has been
> bought.
>
> **What this plan is:** the first physical test of the spray-on magnetic paint
> from the magnetic-well assessment
> (`magnetic-well-nanoscale-assessment.md` §2 and §5.1) and the concept
> document (`magnetic-well-concept.md` §6, §9.2): three formulations of the
> five-coat paint on 300 × 300 mm panels, measured for shielding, sheet
> resistance, permeability, adhesion, and the field pattern of the printed
> star. It is the test that would show whether the paint shields, absorbs,
> and senses as claimed — and whether the printed star pattern adds anything
> at coating scale.
>
> **What it is not:** a trapping or levitation test (the paint cannot trap or
> levitate — see §7), a wall test, or a device test. See §7 for the honest
> limits.
>
> **Cost and price rule:** every price below is labeled **verified** (found on
> a named supplier's listing in November 2026) or **estimate / unverified**
> (no price found; a range given as a budgeting figure, never a quote).
> Prices are in USD and exclude shipping and tax.
>
> **The macro bench check is done.** The concept document's first bench
> check (§9.1) — whether the throwing star is magnetic — was answered by
> Gregory on 2026-11-10: **the star is magnetic.** The tip concentration
> and the well stand as simulated, and the austenitic warning no longer
> applies to this star. Nothing in this plan depends on re-checking it.

## 0. Decisions before anything is built

Four decisions gate the plan. Each must be made before materials are ordered,
because each changes what gets built.

| # | Decision | Plan's assumption | What changes if it goes the other way |
|---|---|---|---|
| D1 | **Ferrite grade and particle size.** The assessment requires blocked/ferrimagnetic particles (30–100 nm) — below ~20 nm the particles are superparamagnetic and hold no field of their own. | **Fe₃O₄, 50–100 nm, 99% purity, blocked/ferrimagnetic.** Primary source: Ossila 50–100 nm, 250 g jar ($285, verified). | A smaller size (e.g. 20–50 nm) sits near the superparamagnetic limit and the paint's remanence falls; the M5 pattern would weaken or vanish. A larger size (>100 nm) settles faster, clumps harder, and roughens the paint. Any size change must be recorded with the results, and the particle size stated on every panel's build log. |
| D2 | **Binder.** The assessment specifies a water-based acrylic. | **Water-based acrylic binder** (1 L, ~$30, estimate). Same binder for every coat, so the coats bond to each other and the comparison is not confounded by binder chemistry. | An epoxy binder changes cure time (longer), adhesion (usually stronger), and the working window. If epoxy is chosen, the cure schedule in §5 changes and the adhesion result (M4) is a result for epoxy, not for acrylic. |
| D3 | **Star pattern size.** The printed star must be large enough to scan with a Hall probe and to show a point-vs-centre difference. | **Five-point star, 200 mm span, on the 300 × 300 mm panel** (50 mm margin each side), sharp points, stencil-cut. | A smaller star (e.g. 100 mm) puts the points too close together for the Hall probe to resolve the pattern; a larger star (e.g. 280 mm) leaves no margin and the points run off the panel edge. The star size must be recorded with the M5 results. |
| D4 | **Whether to add formulation D (skin, no pattern).** With only A/B/C, the B-vs-A comparison attributes the pattern and the skin *jointly* — it cannot separate them. | **Core set is A/B/C (2 panels each). D is recommended as an optional add-on (2 panels): ferrite + GNP skin, no star pattern.** | Without D, if B beats A on shielding (M1) or sheet resistance (M2), the plan can only say "pattern + skin together" did it. With D, B vs D isolates the pattern and D vs A isolates the skin. D costs two more panels and ~$30 of material — cheap insurance for attribution. |

---

## 1. The panels, defined

### 1.1 Panel size — 300 × 300 mm (12" × 12")

Chosen because every part of the test fits it, and because it is the same size
as the alloy coupon — so the TEM cell, the fixtures, and the bench set carry
over:

- **12" × 12" is how the aluminum is sold.** OnlineMetals sells 2024-T3 sheet
  cut to 12" × 12" ($21.98, verified — same sheet as the alloy plan).
- **It fits the TEM cell.** The TekBox TBTC3 open TEM cell (1038 × 501 ×
  305 mm, 150 mm septum) takes a 300 × 300 mm panel. The smaller TBTC1 does
  not.
- **It is big enough to scan.** The 200 mm star (D3) leaves a 50 mm margin,
  and the Hall probe grid (M5) fits with room to spare.
- **It is big enough to cut.** The cross-hatch test (M4) needs a flat area
  away from the edges; the four-point probe (M2) needs five points with
  clearance.

### 1.2 The five-coat stack (from the assessment §2.1)

Every panel gets the same five coats in the same order, except where a
formulation omits a coat (see §1.3). Dry-film thicknesses are nominal targets;
measure the actual thickness on each panel with a wet-film comb during
application and record it.

| Coat | Macro analogue | Contents (this plan) | Dry thickness | Job |
|---|---|---|---|---|
| **Primer** | Dried clay | Ceramic-filled dielectric primer (alumina/silica filler in water-based acrylic) | ~50 µm | Insulates, protects, gives the magnetic layer something to grip |
| **Magnetic layer** | Cast iron yoke + throwing star | Fe₃O₄, 50–100 nm, **40% by volume** in water-based acrylic (see D1) | ~200 µm | Provides permeability, shapes the field, absorbs the magnetic part of EM waves |
| **Pattern layer** | Etched star geometry | Same magnetic ink, applied through a Mylar stencil in a five-point star, 200 mm span (see D3) | ~50 µm | Creates hot spots and field minima — the well, printed |
| **Conductive skin** | Aluminum cross + copper star | Graphene nanoplatelets (GNP), ~10% by volume, in water-based acrylic | ~50 µm | Reflects the electric part of EM waves; diamagnetic platelets add a weak repulsive term |
| **Topcoat** | (protection) | Clear polyurethane | ~30 µm | Seals against moisture and corrosion, locks the pattern in |

Total dry-film thickness: A and C ≈ 280 µm; B ≈ 380 µm. The C control's
middle coat is plain acrylic at the same 200 µm thickness as the magnetic
layer, so the shielding comparison is not confounded by thickness. **Note:**
the published 99% shielding reference (ChemistrySelect 2024) was measured at
0.720 mm total thickness — about twice this stack. The 20 dB pass in M1 is a
proposed threshold for *this* stack, not a claim that this stack will match
that paper.

### 1.3 Formulations — what gets built

| ID | Formulation | Coats | Qty | Purpose |
|---|---|---|---|---|
| **A** | Ferrite-only paint | Primer + magnetic layer + topcoat (no pattern, no skin) | 2 | The ferrite baseline. Shielding (M1), permeability (M3), and adhesion (M4) for the magnetic layer alone. |
| **B** | Full well paint | Primer + magnetic layer + star pattern + GNP skin + topcoat | 2 | The test article. All measurements M1–M5. |
| **C** | Plain control | Primer + plain acrylic (same 200 µm) + topcoat (no ferrite, no GNP) | 2 | The baseline. What the substrate and binder do on their own — every measurement is read against C. |
| **D** *(optional, recommended — see D4)* | Ferrite + skin, no pattern | Primer + magnetic layer + GNP skin + topcoat | 2 | Separates the skin from the pattern: B vs D isolates the pattern; D vs A isolates the skin. |

6 panels in the core set (8 with D). Two repeats per formulation give two
independent values for each headline number — enough to see whether a result
repeats, not enough for statistics. **Report both values; do not compute a
mean with a spread from n = 2 and call it a measurement of variance.** Every
panel gets a unique ID (A1, A2, B1, B2, C1, C2, D1, D2) marked on its back,
and a build log: material batch, mix ratios, application date, cure time,
and measured dry-film thickness at four points.

### 1.4 Paint quantities — calculated, not guessed

Panel area is 0.09 m². Dry volumes below are per panel, from the §1.2
thicknesses; wet volumes assume ~50% solids by volume.

| Material | Per panel | Panels using it | Total needed | Buy |
|---|---|---|---|---|
| Fe₃O₄, 50–100 nm (density 5.17 g/cm³) | Magnetic layer: 7.2 mL ferrite = **37 g**; pattern layer (B only): 3.7 g | A×2, B×2 (magnetic layer); B×2 (pattern) | **~156 g** | **250 g jar** (Ossila, $285 verified) — covers the set with margin |
| GNP (density ~2.2 g/cm³) | Skin: 0.45 mL = **~1 g** | B×2 (D×2 if built) | **~2 g** (4 g with D) | **100 g jar** (~$50 budgeted, estimate) — far more than needed; the rest is stock for the next set |
| Water-based acrylic binder | Magnetic layer ~12 g solids; skin ~4 g; plain coat (C) ~20 g | All 6–8 panels | **~150 g solids** (~300 mL wet) | **1 L** (~$30, estimate) |
| Ceramic-filled primer | 4.5 mL dry per panel | All panels | **~27 mL dry** | **1 qt** (~$25, estimate) |
| Clear polyurethane topcoat | 2.7 mL dry per panel | All panels | **~16 mL dry** | **1 qt** (~$20, estimate) |
| Dispersant (Triton X-100 or BYK equivalent) | ~1% of the magnetic mix by weight | Magnetic + pattern mixes | **~5 g** | **Small bottle** (~$25, estimate) |

**Mixing rule (read before mixing):** mix wet, never handle dry nanopowder
outside a ventilated enclosure (see §6). Disperse the ferrite into the binder
with the dispersant, then an ultrasonic bath (10–15 min) to break up clumps
— clumping is the failure mode that wrecks the pattern and the surface
finish (assessment §4.4). Record the mix ratio by weight *and* by volume for
every batch. Do not cure any coat under a field for the core set — the
field-cure idea (assessment §2.2) is a follow-on variant, not part of this
test, because it would confound the pattern comparison.

---

## 2. Materials — what to get, and what it costs

All prices are **estimates for budgeting, never quotes**. "Verified" means
found on a named supplier listing in November 2026; "unverified" means no
price was found and the figure is a budgeting range.

| # | Material | Spec for this plan | Source | Qty | Unit cost | Line cost |
|---|---|---|---|---|---|---|
| 1 | Fe₃O₄ nanopowder | 50–100 nm, 99% purity, blocked/ferrimagnetic | Ossila, product M2439A3 (50–100 nm): 100 g $143, 250 g $285, 500 g $450 | 250 g jar | $285 (verified) | ~$285 |
| 2 | Graphene nanoplatelets | Industrial grade, powder | Marketplace/bulk listings: TECHINSTRO 1 kg $327.49 (verified listing); Accio range $50–$500/kg; KBelement $100–$150/kg — **quote required** for the exact grade | 100 g | ~$50 (estimate — inside the verified $10–$35/100 g bulk range, budgeted high) | ~$50 |
| 3 | Water-based acrylic binder | 1 L, general-purpose acrylic medium | General art/industrial supplier | 1 L | ~$30 (estimate — unverified) | ~$30 |
| 4 | Aluminum panels | 2024-T3 sheet, 0.063" (1.6 mm), 12" × 12" | OnlineMetals, part #8059 (same sheet as the alloy plan) | 6 sheets (8 with D) | $21.98 (verified) | ~$132 (~$176 with D) |
| 5 | Ceramic-filled primer | 1 qt, alumina/silica-filled | General paint supplier | 1 qt | ~$25 (estimate — unverified) | ~$25 |
| 6 | Clear polyurethane topcoat | 1 qt | General paint supplier | 1 qt | ~$20 (estimate — unverified) | ~$20 |
| 7 | Mylar stencil sheets | 0.25 mm Mylar, A3 sheets, for the 200 mm star stencil | General craft/industrial supplier | 1 pack | ~$15 (estimate — unverified) | ~$15 |
| 8 | Dispersant | Triton X-100 or BYK equivalent, small bottle | General lab supplier | 1 bottle | ~$25 (estimate — unverified) | ~$25 |
| 9 | Consumables | Mixing cups, stirrers, brushes/rollers, wet-film comb gauge, tape, labels, coil wire for M3 | General lab/industrial supplier | 1 lot | ~$50 (estimate — unverified) | ~$50 |
| 10 | PPE | P100 respirator + filters, nitrile gloves (box), safety glasses | General safety supplier | 1 lot | ~$40 (estimate — unverified) | ~$40 |

**Materials total, one coupon set: ≈ $670** (range ≈ $600–$750; 8 panels with D:
≈ $720). The two verified lines — the ferrite ($285) and the panels ($132) —
are most of it.

**Cheaper ferrite route (noted, not recommended as the primary):** 1 kg bulk
Fe₃O₄ at ~$100–$150/kg from marketplace suppliers (Guangzhou Hongwu 80–100 nm
99.8%, $100–$150/kg, verified listing; TECHINSTRO 1 kg, $150.88, verified
listing) would bring the materials total to ~$540. The Ossila jar is the
primary because its particle size (50–100 nm) and purity (99%) are stated on
the listing and it is a Western lab supplier with a datasheet. **Do not buy
research-grade dispersions** (e.g. Sigma-Aldrich 10 mL Fe₃O₄ at €604, verified
in the assessment) — they would multiply the cost several times over and are
not the route for a paint test. **Do not buy industrial pigment-grade Fe₃O₄**
($0.50–$1.50/kg, verified listings) — it is micron-scale, not nano, and its
particle size is not controlled for this test.

**What is NOT in this total:** instruments (§3) — those are separate lines
below.

### Ferrite price — what the research actually found (the two unverified prices, now checked)

The assessment left two prices unverified; both are now grounded in real
listings (November 2026):

- **Bulk Fe₃O₄ nanopowder, 50–100 nm:** Ossila (ossila.com) lists Fe₃O₄
  powder 50–100 nm, 99% purity, at 100 g $143, 250 g $285, 500 g $450 —
  i.e. **$900/kg at 500 g**. Marketplace bulk (1 kg) runs **$100–$350/kg**
  depending on grade and supplier (Guangzhou Hongwu 80–100 nm 99.8%:
  $100–$150/kg; TECHINSTRO 1 kg: $150.88; Shanghai Epoch: $300/kg).
  Industrial pigment-grade magnetite is $0.50–$1.50/kg but is micron-scale
  and uncontrolled — not the same material. **Budgeting figure for this
  plan: $285 for the 250 g Ossila jar** (the size this test actually needs).
- **Graphene nanoplatelets, bulk:** marketplace listings run **$50–$500/kg**
  for industrial grade (TECHINSTRO 1 kg, 99.98%, $327.49; KBelement
  $100–$150/kg; Accio mid-tier range $300–$400/kg). The assessment's
  earlier estimate of ~$100–$150 per 100 g was a small-quantity
  marketplace figure and is **superseded** by these bulk listings — at bulk
  prices 100 g costs roughly $10–$35. This test needs only ~2 g, so the
  GNP line is budgeted at $50 (deliberately high) and is not a cost driver.

---

## 3. Gear — what it takes to measure

Same bench set as the alloy plan (four-point probe, TEM cell, spectrum
analyzer) plus the three instruments this test adds: a gaussmeter, an LCR
meter, and an adhesion kit. Each line is marked **bench-accessible** (a
hobbyist bench or a small lab can own it) or **lab-only** (needs a facility).

| # | Instrument | What it does here | Source / model | Access | Cost |
|---|---|---|---|---|---|
| 1 | Four-point probe | Sheet resistance (M2) | Ossila Four-Point Probe (verified in the alloy plan; range 10 mΩ/sq – 1 MΩ/sq) | Bench | $2,550 (verified) |
| 2 | TEM cell | Shielding effectiveness (M1) | TekBox TBTC3 open TEM cell (verified in the alloy plan; 10 MHz–1 GHz) | Bench | $1,619 (verified) |
| 3 | Spectrum analyzer | Shielding effectiveness (M1) | Siglent SSA3021X (verified in the alloy plan; 9 kHz–2.1 GHz) | Bench | ~$1,400 (verified) |
| 4 | Signal generator | Drives the TEM cell (M1) | Siglent SDG2042X (verified in the alloy plan) or the SSA3021X tracking generator | Bench | — (same bench set; not re-budgeted) |
| 5 | Gaussmeter / Hall probe | Field pattern (M5) | **AlphaLab GM2 Gaussmeter** (verified: $902 on alphalabinc.com; DC/AC, 0–3,000 G range, HS probe resolution 0.01 G = 1 µT) | Bench | $902 (verified) |
| 6 | LCR meter | Permeability (M3), via coil inductance | **DER DE-5000 LCR meter** (verified: ~$187 on Amazon via umtsmarttool; Ubuy $231) + a hand-wound flat coil (50 turns, 50 mm diameter, ~$10 of wire) | Bench | ~$200 (verified) |
| 7 | Adhesion test kit | Cross-hatch tape test (M4) | **Gardco PosiTest CH Cross Hatch Adhesion Kit** (verified: $340 on gardco.com, 2 mm / 6 teeth, ISO 2409 and ASTM D3359; Elcometer 1542 full kit $619 is the alternative) | Bench | $340 (verified) |
| 8 | Ultrasonic bath | Disperses the ferrite into the binder before spraying (§1.4) | General lab/industrial supplier | Bench | ~$80 (estimate — unverified) |
| 9 | Precision scale | Mix ratios by weight | Same scale as the alloy plan | Bench | ~$25 (verified) |
| 10 | Film thickness gauge (optional) | Dry-film thickness check | Wet-film comb gauge is in the consumables (§2 #9); a dry-film gauge (Elcometer-type, ~$200–$500) is optional — the comb plus the recorded wet thickness is enough for a coupon test | Bench | $0 (comb) / ~$200–$500 optional |
| 11 | VSM (optional) | Permeability (M3), intrinsic | **Lab-only** — a vibrating sample magnetometer would measure the material's intrinsic μr and saturation directly | Lab | — (not budgeted; use only if a lab is available) |
| 12 | Anechoic chamber / GHz test rig (optional) | Shielding effectiveness above 1 GHz | **Lab-only** — the TEM cell + analyzer covers 10 MHz–1 GHz; the published 99% figure is in 3.5–12.5 GHz, which this bench cannot reach | Lab | — (not budgeted; out of scope) |

**Instrument total if buying everything new: ≈ $7,790.** Split honestly:
- **Shared bench set (already costed in the alloy plan): ≈ $5,594** — probe
  $2,550 + TEM cell $1,619 + analyzer ~$1,400 + scale ~$25. If it is already
  on the bench for the alloy work, it costs nothing again.
- **New instruments this test adds: ≈ $1,520** — GM2 $902 + LCR ~$200 +
  adhesion kit $340 + ultrasonic bath ~$80.
- **Materials: ≈ $670** (§2).
- **Program total, buying everything: ≈ $7,800.** **Materials-only, if the
  instruments are borrowed or lab-provided: ≈ $670.**

---

## 4. Measurements and pass/fail criteria

Five measurements. Every measurement is made on all six panels (eight with
D), in the same order, with the same procedure, and the results are read
against the controls. **Thresholds are proposed, not properties** — they are
carried over from the assessment and the alloy plan, and they are the
hypotheses the test is designed to check, not facts about the paint.

| # | Measurement | What it settles | Procedure | Repeats / controls | Criterion |
|---|---|---|---|---|---|
| **M1** | **Shielding effectiveness (SE)** in the TEM cell | Does the paint block RF? Is the ferrite layer the blocker, or the skin, or the pattern? | TEM cell + spectrum analyzer + signal generator, per the alloy plan's method. Panel clamped in the cell aperture; sweep **10 MHz–1 GHz**; record SE in dB at 100 MHz, 500 MHz, and 1 GHz. Record the temperature and the panel's dry-film thickness with each reading. | 2 panels per formulation; 3 readings per panel (re-clamp between readings). Controls: C (no ferrite, no GNP) is the baseline; A (ferrite only) vs C isolates the ferrite; B vs A isolates pattern + skin together; B vs D and D vs A (if D is built) isolate the pattern and the skin separately. | **Pass:** B ≥ **20 dB** SE and ≥ **10 dB above C** at all three frequencies. **Fail:** B < 10 dB, or B within 3 dB of C (the paint adds nothing). **Inconclusive:** between 10 and 20 dB, or one panel passes and the other fails — re-clamp and re-run before calling it. **Note:** 20 dB = 99% attenuation, the published figure for a 0.720 mm ferrite + CNT coating in 3.5–12.5 GHz. This stack is thinner (~0.28–0.38 mm) and this sweep is a different band (10 MHz–1 GHz) — the 20 dB bar is proposed, not borrowed from that paper. |
| **M2** | **Sheet resistance** | Does the GNP skin conduct? Is the skin's resistance low enough to matter for shielding? | Four-point probe, 5 points per panel (centre + four corners, 20 mm from the edges). Record Rs in Ω/sq. | 2 panels per formulation; 5 points each. Controls: A (no skin) and C (no skin, no ferrite) — both should read high. B vs A isolates the skin's conductivity. | **Pass (skin):** B **< 100 Ω/sq**. **Fail:** B **> 10 kΩ/sq** (the skin is not a conductor — check the GNP loading and the dispersion). **Inconclusive:** 100 Ω/sq–10 kΩ/sq — the skin is marginal; re-check the loading and re-measure after a second cure day. **Note:** a conductive skin is not required for the ferrite to shield (magnetic absorption works without it); M2 failing does not by itself fail the paint — it fails the skin. |
| **M3** | **Permeability** | Does the paint actually have the magnetic property the well depends on? | Hand-wound flat coil (50 turns, 50 mm diameter) on the panel; DE-5000 LCR meter reads inductance with the panel present vs in air. Report the inductance ratio and the **inferred effective μr** (see the note below). If a VSM is available, measure the intrinsic μr and saturation on a cut sample instead and report both. | 2 panels per formulation; 3 readings per panel. Controls: C should read μr ≈ 1 (no ferrite); A and B should read the same (the pattern and skin do not change the bulk μr). | **Pass:** A and B **μr ≥ 5** and C μr ≈ 1 (±0.2). **Fail:** A and B μr < 2 (the ferrite is not contributing — check the loading and whether the particles are superparamagnetic). **Inconclusive:** 2–5 — the ferrite is contributing weakly; check the particle size (D1) and the dispersion. **Note:** the coil method gives an **effective** permeability for the coil's geometry, not the material's intrinsic μr — the number is comparative (A/B vs C), not absolute. The assessment's value (μr ≈ 60–80 for a high-quality magnetite layer, from the literature) is a reference point, not a pass bar. |
| **M4** | **Adhesion** — cross-hatch tape test, ASTM D3359 Method B | Does the paint stay on? A coating that peels is not a coating. | Cross-hatch cutter, 2 mm spacing, 6 cuts each direction, on a flat area away from the edges; apply the tape, pull, rate the removal **0B–5B** (5B = no removal, 4B = <5% removal). Use the Gardco PosiTest CH kit (§3 #7). | 2 panels per formulation; 2 test areas per panel. Controls: all formulations should be compared — if A peels and C does not, the ferrite loading is the cause. | **Pass:** **≥ 4B** on every panel. **Fail:** ≤ 2B on any panel (the coating is not fit for use — reduce the loading or change the binder). **Inconclusive:** 3B — marginal; re-test after a second cure day (adhesion improves as the binder fully cures). **Note:** ASTM D3359's spacing guidance is written for coatings up to 125 µm; this stack is ~280–380 µm. The 2 mm spacing is the closest applicable spacing and the rating is comparative across A/B/C — which is the point. Record the actual dry-film thickness with the rating. |
| **M5** | **Hall-probe field pattern** — does the printed star shape the field? | Does the star pattern do anything at coating scale? This is the measurement that tests the "well, printed" idea directly. | **Magnetize every panel first, identically:** stroke the panel with a neodymium magnet (or place it on a strong magnet for 30 s) so the ferrite holds a remanent field. Then scan the **AlphaLab GM2** Hall probe on a grid (10 mm spacing) over the panel at a fixed height (1 mm above the surface, held by a spacer jig), and record the field at the star points and at the star centre. | 2 panels per formulation; full grid scan per panel. Controls: A (no pattern) scanned the same way — if A shows the same point-vs-centre difference, the pattern adds nothing. C (no ferrite) — should read near zero everywhere; if it does not, the magnetization procedure or the probe is the problem, not the paint. B vs A is the pattern's contribution. | **Pass:** B's field at the star points is **≥ 1.5× the field at the star centre**, the difference **exceeds the probe noise and the variation across A**, and the pattern is visible on the grid map. **Fail:** B's point/centre ratio < 1.2, or A shows the same ratio (the pattern adds nothing — the field is uniform). **Inconclusive:** ratio 1.2–1.5 — repeat the magnetization and re-scan; if it persists, the pattern is marginal at this loading. **Note:** the pattern's field is the **remanent** field of the ferrite — it depends on the magnetization procedure, so the procedure must be identical for every panel and recorded. A phone magnetometer can screen the pattern for free, but the GM2 is the instrument of record. |

### Attribution — what each comparison settles

| Comparison | What it isolates | Read it as |
|---|---|---|
| A vs C | The ferrite layer's contribution (shielding M1, permeability M3) | "The ferrite does X" |
| B vs A | The pattern + skin together (shielding M1, sheet resistance M2, field pattern M5) | "Pattern + skin together do X" |
| B vs D *(if D is built)* | The star pattern alone (M1, M5) | "The pattern does X" |
| D vs A *(if D is built)* | The GNP skin alone (M1, M2) | "The skin does X" |
| B vs C | The full paint vs nothing | "The paint as a whole does X" |

Without D, B vs A is the only pattern measurement — and it is confounded
with the skin. That is why D is recommended (D4).

---

## 5. Sequence and effort

### Order of work

| Step | What | When | Notes / decision before it |
|---|---|---|---|
| 0 | **Decisions D1–D4** (§0) | Before anything is ordered | D1 (ferrite grade) and D2 (binder) fix the materials list. D4 (formulation D) fixes the panel count. |
| 1 | **Order materials** (§2) | Day 1 | Ferrite lead time: Ossila ships from the UK — allow **1–2 weeks**. Nothing else has a long lead time. |
| 2 | **Mix the paints** (§1.4) | After delivery, ~2 h | Wet mixing only (§6). Record batch, lot, and mix ratios by weight and volume. One batch per formulation — do not mix A and B from the same batch. |
| 3 | **Apply the coats** (§1.2) | ~1 day, spread over 2 days | Primer → dry **4–6 h** to touch → magnetic layer → dry 4–6 h → (B: pattern layer through the stencil → dry 4–6 h) → (B: skin → dry 4–6 h) → topcoat. Apply with a spray gun or a roller; a spray gun gives the evenest 200 µm layer. Record the wet-film thickness with the comb at four points per coat. |
| 4 | **Cure** | **24 h after the last coat (48 h in humidity)** before any measurement | Do not measure before the cure is done — the conductivity and the magnetism settle during the cure (assessment §2.2). Record the cure time and the humidity. |
| 5 | **M2 sheet resistance + M4 adhesion** | Day 3, ~1 h | First — because they are fast and because if the skin is not conductive or the coats peel, the rest of the results are already explained. Adhesion is destructive in the test area, so do M4 last on each panel's test patch, after M2. |
| 6 | **M3 permeability** | Day 3, ~1 h | Bench, LCR + coil. Non-destructive. |
| 7 | **M1 shielding** | Day 3–4, ~2 h | TEM cell + analyzer. Clamp each panel three times (re-clamp between readings). Record the dry-film thickness with each reading. |
| 8 | **M5 field pattern** | Day 4, ~2 h | Magnetize each panel identically, then scan. Last — because the magnetization step must be the same for every panel and it is the most procedure-sensitive measurement. |
| 9 | **Write up** | Day 4–5, ~2 h | One page per measurement (procedure, both panel values, the control comparison, pass/fail/inconclusive per the §4 table), plus the build log. File it with this plan. |

**Total effort: 2–3 working days hands-on, spread over ~2 weeks elapsed**
(delivery and cure dominate). **Total cost: ≈ $670 materials-only** if the
instruments are borrowed or lab-provided; **≈ $7,800** if every instrument is
bought new (§3).

### What must be decided before each step

- Before step 1 (ordering): D1, D2, D4.
- Before step 2 (mixing): the exact mix ratios (ferrite 40 vol%, GNP 10 vol%)
  and the dispersant dose.
- Before step 3 (application): spray gun vs roller, and the stencil for the
  B panels (D3 — 200 mm star, cut and checked against a printed template).
- Before step 8 (M5): the magnetization procedure (stroke vs soak, duration,
  magnet used) — it must be identical for every panel, so it must be written
  down before the first panel is magnetized.

---

## 6. Safety

**No fire, no sealed-container, no energetic-material work — none is added
here, and none is needed for this test.** The hazards are dust, sensitizers,
and electricity.

| Hazard | Rule |
|---|---|
| **Nanoparticle dust (Fe₃O₄, GNP)** — the main hazard. Dry nanopowder is an inhalation risk; graphene platelets and ferrite nanoparticles are not to be breathed. | **P100 respirator** (not a paper dust mask) whenever dry powder is handled or whenever spraying. **Nitrile gloves** and **safety glasses** at all times. Work in a ventilated area (fume hood or a fan to the outside). **Mix wet** — add the powder to the binder, never the binder to a dry pile of powder, and never handle dry powder in the open air. Clean up with a damp cloth, never a dry brush or compressed air. |
| **Epoxy / binder sensitizers** | If an epoxy binder is chosen instead of acrylic (D2), treat it as a skin sensitizer: gloves at all times, no bare skin contact, and do not reuse contaminated gloves. Water-based acrylic is the safer choice and is the plan's assumption. |
| **Electrical safety** | The TEM cell drive is limited to **25 W** (TBTC3 rating) — do not exceed it. The spectrum analyzer input is **milliwatts** — do not connect a transmitter directly. The LCR meter and the gaussmeter are battery/low-voltage instruments. No mains work is needed. |
| **Spraying** | Spray in a ventilated area or outdoors; the respirator rule applies. Keep the spray away from the eyes and the skin. |
| **Disposal** | Leftover paint and wash water go in a sealed container and out with the household hazardous waste, not down a drain. Dry ferrite powder left over goes back in its sealed jar. |
| **General** | Work on a stable bench, keep the panels flat while curing, and keep the strong magnet used for M5 away from the gaussmeter probe when it is not in use (it can saturate the probe). |

---

## 7. Honest limits — what a paint coupon test can and cannot prove

- **It tests shielding, absorption, and sensing at coating scale — not
  trapping or levitation.** The paint's field is ~1,000× weaker than the
  macro magnet's (assessment §4.1). No coupon result, however good, shows
  that the paint can trap or levitate anything. The macro well's centering
  is a separate claim, tested by the macro build (§8), not by this plan.
- **A coupon result is not a wall or a device result.** A 300 × 300 mm panel
  in a TEM cell is not a wall, a room, or a vehicle. Edges, seams, real-world
  angles of incidence, and the substrate behind the paint all change the
  result. A pass here means "worth scaling up to a wall coupon," not "works
  on a wall."
- **The TEM sweep (10 MHz–1 GHz) does not cover the published band.** The
  99% figure (ChemistrySelect 2024) is in 3.5–12.5 GHz. This bench cannot
  reach that band. A pass at 1 GHz does not imply a pass at 10 GHz, and a
  fail at 1 GHz does not rule out a pass at 10 GHz.
- **n = 2 per formulation is not statistics.** Two panels show whether a
  result repeats; they do not show a distribution. Report both values. Do
  not compute a mean and a standard deviation from two points.
- **The pattern's field (M5) is remanent and procedure-dependent.** The
  star's field depends on how the panel was magnetized. A different
  magnetization procedure gives a different pattern. The M5 result is
  "with this magnetization procedure, the pattern does X" — nothing more.
- **Permeability from a coil (M3) is an effective value.** The coil method
  gives the permeability the coil sees, for the coil's geometry. It is not
  the material's intrinsic μr. A VSM would give the intrinsic value; the
  coil gives the comparative one. Both are useful; neither is the other.
- **Adhesion (M4) is comparative.** The 2 mm spacing is the closest
  applicable spacing for a stack this thick (see the M4 note in §4). The
  rating is meaningful as a comparison across A/B/C and against the 4B bar —
  not as an absolute materials property.
- **Nothing here is a device.** A shielding paint is a coating. A sensing
  surface is a coating with a readout. Neither is a device until it is
  built into one and tested as one.

---

## 8. Assessed requirements for the macro build — derived from the simulation

**This section is assessed requirements, not Gregory's measurements and not
verified hardware values.** Gregory asked that the build dimensions not be
left as "needs Gregory" — so each requirement below is assessed here, derived
from the simulation numbers (`sim-results/results.json` and
`sim-results/SIMULATION.md`) and the physics. Every requirement states the
reasoning and what changes if it is not met. The numbers in this section come
from a **2D static magnetostatic model** (an infinite extrusion, not the true
3D stack) with assumed material values (N52, Br = 1.45 T; cast iron μr = 200,
B_sat = 1.5 T; magnetic stainless μr = 100) — so the derivations below are
order-of-magnitude, not exact, and a hardware measurement could move them.
The modeled geometry is: magnet 38 × 16 mm (the 1.5" × ~5/8" square, modeled
as 38 × 16 so its edges land on the 0.5 mm grid); yoke 60 × 6 mm; star
60 mm across, 3 mm thick, sharp 5-point (36° tip, 4.6 mm taper); cross 3 mm;
badge rim at x = ±25–30 mm, copper centre x = ±25 mm; badge weight ≈ 0.39 N
(assumed).

### 8.1 Yoke plate — size and thickness

**Requirement: footprint 55–70 mm square (nominal 60 mm, as modeled);
thickness 4–8 mm (nominal 6 mm, as modeled). Cast iron is fine; there is no
reason to pay for a better iron.**

*Derivation.* The yoke's job is to carry the return flux and double the
top-face field — and it does: the simulated top-face field is **0.573 T with
the yoke vs 0.295 T bare** (1.94×), and the top-face flux is **0.0192 Wb/m
vs 0.0120 Wb/m** (+61%). The total flux leaving the magnet face in 3D is
roughly B × area = 0.573 T × (38.1 mm)² ≈ **8.3×10⁻⁴ Wb**. That flux must
flow back through the plate, and the narrowest section of the return path is
the annulus at the magnet edge (perimeter 4 × 38.1 mm = 152 mm). To keep the
flux density there at or below the iron's saturation (B_sat ≈ 1.5 T), the
plate needs t ≥ Φ / (B_sat × perimeter) = 8.3×10⁻⁴ / (1.5 × 0.152) ≈
**3.6 mm**. The modeled 6 mm satisfies that at the edge — but the region
directly under the magnet still saturates (the model shows a yoke maximum of
2.28 T against the 1.5 T cap, with ~1,290 cells over the cap on the final
pass), because the flux concentrates as it turns 90° under the magnet. That
is why the yoke material does not matter: cast iron, low-carbon steel
(μr = 1000), and permalloy (μr = 10000) agree within 1% on every number in
the variation table — the iron next to a 1.45 T magnet is saturated anyway,
so the extra permeability has nothing to work on, and permalloy is the worst
buy of all (it saturates hardest, 1,716 cells over its 0.8 T cap on the
first pass, for zero gain).

*Footprint.* The plate must extend beyond the magnet by enough to collect the
return flux: the modeled 60 mm plate gives **11 mm of overhang per side**.
The requirement is an overhang of **≥ ~8–10 mm per side** (footprint ≥ ~55 mm
for the 38 mm magnet). Beyond ~15 mm of overhang the extra iron carries
little flux — the far-field decay shows the field has already spread into
the air by 60–100 mm — so a plate much larger than ~70 mm is wasted iron.

*What changes if the requirement is not met.* Thinner than ~3 mm, the plate
saturates through and the yoke boost falls toward the bare-magnet value
(0.295 T top field, no well — the control has a well depth of −0.066 T, a
hump, not a dip). A footprint no bigger than the magnet chokes the return
path at the plate edge and costs field the same way. Thicker than ~8 mm or
wider than ~70 mm, nothing is gained — the extra iron sits where the flux
has already leaked to air. A cup yoke (wrapping the magnet sides) gives the
strongest top field (+20%, 0.688 T) but **destroys the well** (depth −0.053 T)
and collapses the rim pull (−0.19 N vs −18.9 N) — use it only if the well
does not matter.

### 8.2 Clay — thickness

**Requirement: lateral packing 3–11 mm thick (nominal 11 mm, as modeled —
the gap between the magnet edge and the yoke edge); it must cover the magnet
edges and corners with ≥ ~3–5 mm of clay, and it must seal against moisture.
It must NOT sit between the magnet top face and the cross.**

*Derivation.* The clay is magnetically neutral (μr = 1, modeled as air), so
its thickness costs nothing magnetically — its job is protection, not
field-shaping. The magnet is neodymium: brittle, and its edges and corners
are the chipping points. The modeled clay fills the region beside the magnet
(x = 19–30 mm both sides, y = 6–22 mm), i.e. 11 mm of packing on each side.
The requirement is the minimum that protects: **≥ ~3–5 mm over the edges and
corners**, enough to absorb a knock and to seal the magnet against moisture
(neodymium corrodes). The modeled 11 mm is more than enough; the only cost
of a thicker clay layer is that it forces a bigger yoke footprint, which adds
mass without magnetic benefit.

*The trade-off that matters is vertical, not lateral.* The clay must not be
allowed between the magnet top face and the cross, because any non-magnetic
gap there costs field fast. The simulation shows the field falling from
**0.573 T at the magnet top face to 0.127 T at badge height, 7.5 mm above the
face** — roughly a factor of 4.5 over 7.5 mm — so each extra millimetre of
gap between the magnet and the star costs on the order of 10–20% of the
field at the star. The cross thickness is the same trade: the modeled 3 mm
cross is invisible to the static field (removing it changes nothing to the
last digit), but the 6 mm cross costs ~9% of the top field (0.521 T vs
0.573 T) for a slightly deeper well (0.121 T vs 0.102 T) — not worth it
unless the extra spacing is needed mechanically. **Keep the cross at
≤ ~3–4 mm and keep the clay out of the vertical stack.**

*What changes if the requirement is not met.* Clay thinner than ~2 mm over
the edges will not protect them — a knock chips the magnet, and moisture
reaches the neodymium. Clay in the vertical stack (or a cross thicker than
~4 mm) costs field at the star and at the badge for no benefit.

### 8.3 Throwing star — size and thickness

**Requirement: span 55–65 mm (nominal 60 mm, as modeled); thickness
2.5–4 mm (nominal 3 mm, as modeled); sharp points, tip angle ≤ ~40°,
taper ≥ ~4 mm. Magnetic stainless grade (confirmed — the star is magnetic).**

*Derivation.* The star's points must project **~10 mm beyond each magnet
edge into the fringing field** (modeled tips at x = ±30 mm vs magnet edge at
±19 mm). That is where the tip concentration happens: the simulated tip
ratio is **2.72 at 1 mm past the tip** (3.16 at 0.5 mm, 2.40 at 2 mm), and
the well lobes (**0.235 T**) sit over the tips, against a centre of
**0.133 T** — the well depth is **0.102 T**. The star carries a substantial
fraction of the face flux out to the tips: the model shows the star near
saturation (maximum 2.23 T against the 1.5 T cap). Its cross-section at the
point base (roughly 10 mm wide × 3 mm thick = 30 mm²) carrying flux at
1–2 T gives ~3–6×10⁻⁵ Wb per point — five points, ~1.5–3×10⁻⁴ Wb, a
substantial fraction of the total face flux (8.3×10⁻⁴ Wb). That sets the
thickness: below ~2 mm the star saturates through at the point bases and
the tip ratio falls; above ~4–5 mm there is no gain, because the flux is
limited by the magnet, not by the star. The tip shape is set by the
variation table: the sharp 5-point star gives the deepest well (**0.102 T**,
~3× the 8-point's 0.033 T and ~2.4× the blunted 5-point's 0.043 T), while
the 8-point and blunted stars read *higher* right at the tips (tip ratio
3.12 / 3.19 vs 2.72) but make a *shallower* well — the fat tip spreads its
field broadly, higher at the tip itself, weaker where the badge sits. The
rim pull follows the same pattern (sharp 5-point −18.9 N; blunted −7.6 N;
8-point −1.3 N), because it depends on the vertical gradient at the rim,
which is steepest for the sharp tip.

*What changes if the requirement is not met.* A star no wider than the
magnet puts its points over the uniform face field, and the tip
concentration collapses — the well depth falls toward the no-star case.
A star thinner than ~2 mm saturates at the point bases and the tip ratio
falls. Blunt or 8-point tips read higher at the tip but give a shallower
well and a much weaker rim pull. A non-magnetic (austenitic) star would
concentrate nothing at all — **this does not apply to this star, which
Gregory confirmed is magnetic**.

### 8.4 Badge — diameter

**Requirement: diameter 55–65 mm (nominal 60 mm, as modeled); the steel rim
centred on the star-tip radius (25–30 mm, tolerance ±5 mm); the copper centre
≤ ~50 mm diameter.**

*Derivation.* The rim must sit over the lobes (**0.235 T** at the star tips)
to get the pull — the simulated rim pull is **≈ −19 N, about 50× the
badge's weight (0.39 N)**. The pull scales as B² (Maxwell stress,
B²·A / 2μ0 — cross-checked in the simulation note: 18.9 N by the gradient
method, 18.9 N by Maxwell stress). If the badge were smaller than ~40 mm
diameter, the rim would sit in the well minimum (**0.133 T**) instead of
over the lobes, and the pull would fall by ~(0.133 / 0.235)² ≈ 1/3, to
~6 N — still 15× the weight, so it would hold, but the well as felt by the
badge would be shallower and the centering weaker. If the badge were larger
than ~75 mm, the rim would sit beyond the tips where the field is falling
(B at 100 mm from the origin is 0.018 T in the far field) and the pull would
drop sharply. The modeled 60 mm badge puts the rim (x = 25–30 mm) directly
over the tips (x = ±30 mm) — that is the requirement.

*The centre and the stable basin.* The diamagnetic centre is restored toward
the middle only within about **±10 mm** of centre: the simulated lateral
force on the copper centre is **−9 µN (toward centre) at 10 mm offset** and
**+8 µN (outward) at 15 mm offset** — beyond ~12 mm the push reverses. So
the badge can wander ~10 mm off-centre and still be pushed back, and the
copper centre should be **≤ ~50 mm diameter** (as modeled) so the net
lateral force stays restoring. A much wider centre would push the net force
outward and the centering would fail. (For graphite, the lateral force is
40× copper's — −0.37 mN at 10 mm — a stiffer trap, same basin.)

*What changes if the requirement is not met.* A badge much smaller than
~40 mm or much larger than ~75 mm loses the rim pull and the well depth as
felt by the badge. A copper centre much wider than ~50 mm loses the
centering. None of this changes the levitation picture: the diamagnetic push
is ~1,600× too small to lift the badge even with graphite (0.25 mN vs
0.39 N) — the badge is held by the steel rim's ferromagnetism, and the well
is a lateral centering trap, not a levitator.

### 8.5 Magnet grade

**Requirement: N52 (Br = 1.45 T) to reproduce the simulated numbers exactly;
functional minimum N35 (Br ≈ 1.17 T). Nothing above N52 gains anything
worth naming.**

*Derivation.* The yoke is saturated at N52, so the field scales roughly
linearly with the magnet's remanence Br (the saturated iron cannot add
anything) and the rim pull scales as B². Scaling the simulated numbers:

| Grade | Br (T) | Top-face field (T) | Well depth (T) | Rim pull (N) | Pull / badge weight |
|---|---|---|---|---|---|
| **N52 (as modeled)** | 1.45 | 0.573 | 0.102 | ~19 | ~50× |
| N48 | 1.38 | ~0.55 | ~0.097 | ~17 | ~44× |
| N42 | 1.30 | ~0.51 | ~0.091 | ~15 | ~39× |
| **N35 (functional minimum)** | 1.17 | ~0.46 | ~0.082 | ~12 | ~31× |
| Ferrite (for comparison) | ~0.40 | ~0.16 | ~0.03 | ~1.4 | ~3.6× |

The table is a scaling of the simulated N52 numbers (field ∝ Br, pull ∝
Br²), not a new simulation — it is assessed, not measured. The point it
makes: **N52 is not required for the function.** At N35 the well is still
0.082 T deep and the rim pull is still ~31× the badge weight — the well and
the hold survive with a ~20% shallower well. The grade matters for
reproducing the simulated numbers exactly, and for the margin — not for
whether the well exists. Above N52 there is nothing to gain: N55 (Br ≈
1.48 T) would add ~2% to the field, and the yoke is already saturated. A
ferrite magnet (Br ~0.4 T) would still hold the badge (3.6× the weight) but
the well would be shallow (~0.03 T) and the tip concentration lower — it is
not the requirement.

*What changes if the requirement is not met.* Below N35 the well depth and
the rim pull fall together (both ∝ Br and Br²). The well does not vanish
abruptly — it degrades smoothly — but below ~N30 the margin over the badge
weight and the well depth both become thin enough that the centering would
be hard to feel by hand. If the magnet on hand is not N52, record its actual
grade and scale the expected numbers from the table above before judging
any hardware measurement against the simulation.

### 8.6 Summary — assessed requirements table

| Part | Requirement | Nominal (as modeled) | If not met |
|---|---|---|---|
| Yoke plate | Footprint 55–70 mm square; thickness 4–8 mm; cast iron | 60 × 6 mm | <3 mm or footprint = magnet size: yoke saturates through, boost falls toward bare magnet, well disappears. >8 mm / >70 mm: wasted iron, no gain. Cup yoke: kills the well. |
| Clay | Lateral packing 3–11 mm; ≥ ~3–5 mm over edges/corners; seals against moisture; none in the vertical stack | 11 mm lateral | <2 mm over edges: chips and corrosion. In the vertical stack: costs ~10–20% of the field per mm. |
| Throwing star | Span 55–65 mm; thickness 2.5–4 mm; sharp points (tip ≤ ~40°, taper ≥ ~4 mm); magnetic stainless | 60 mm span, 3 mm, sharp 5-point | No wider than the magnet: tip concentration collapses. <2 mm: saturates at the point bases. Blunt/8-point: shallower well, weaker rim pull. |
| Badge | Diameter 55–65 mm; rim on the tip radius (25–30 mm, ±5 mm); copper centre ≤ ~50 mm | 60 mm diameter | <40 mm or >75 mm: rim pull and well depth fall. Centre >50 mm: centering fails. |
| Magnet | N52 to reproduce the simulated numbers; N35 minimum for the function | N52, Br 1.45 T | Below N35: well and pull degrade smoothly (∝ Br, Br²). Ferrite: holds, but the well is shallow. Above N52: ~2% gain, not worth it. |
| Cross (for reference) | ≤ ~3–4 mm thick; aluminium (transparent to the static field) | 3 mm | 6 mm: costs ~9% of the top field for a slightly deeper well. Removing it changes nothing statically. |

**All of §8 is assessed requirements derived from a 2D static simulation
with assumed material values. It is not a measurement of the hardware, and
it is not Gregory's measurements. A hardware check (Hall-probe scan of the
real stack, §4 M5-style) would be the next step that turns these
requirements into verified values.**

---

## Appendix A — Sources

All prices and listings checked November 2026. "Verified" in the body means
found on the listing named here.

- **Fe₃O₄ nanopowder, 50–100 nm:** Ossila (ossila.com), product M2439A3 —
  100 g $143, 250 g $285, 500 g $450. Also: Ossila 20–50 nm (M2442A3) 100 g
  $125, 250 g $250, 500 g $400.
- **Fe₃O₄ nanopowder, bulk 1 kg:** Guangzhou Hongwu (Alibaba) 80–100 nm
  99.8%, $100–$150/kg; TECHINSTRO 1 kg, $150.88; Shanghai Epoch 1 kg,
  $300/kg; KBelement 1 kg, $100–$150/kg.
- **Graphene nanoplatelets, bulk:** TECHINSTRO 1 kg, 99.98%, $327.49;
  KBelement $100–$150/kg; Accio mid-tier range $300–$400/kg; Accio general
  range $50–$500/kg.
- **Aluminum sheet:** OnlineMetals, 2024-T3 0.063" × 12" × 12", part #8059,
  $21.98 (same sheet as the alloy plan).
- **Gaussmeter:** AlphaLab GM2 Gaussmeter, $902 (alphalabinc.com; DC/AC,
  0–3,000 G, HS probe 0.01 G resolution).
- **LCR meter:** DER DE-5000, ~$187 (Amazon via umtsmarttool); Ubuy $231.
- **Adhesion kit:** Gardco PosiTest CH Cross Hatch Adhesion Kit, $340
  (gardco.com, 2 mm / 6 teeth, ISO 2409 and ASTM D3359); Gardco X-Cut
  Adhesion Gauge Basic Kit $120; Elcometer 1542 full kit $619.
- **Bench set (from the alloy plan):** Ossila Four-Point Probe $2,550;
  TekBox TBTC3 $1,619; Siglent SSA3021X ~$1,400.
- **Shielding reference:** ChemistrySelect 2024, "Synthesis and
  Characterization of a Flexible Electromagnetic-Shielding Composite Fabric
  Based on Fe₃O₄/CNTs" — 99% shielding effectiveness at 0.720 mm in
  3.5–12.5 GHz (assessment §2.1, §5.1).
- **Simulation numbers:** `sim-results/results.json` and
  `sim-results/SIMULATION.md` (baseline and all 11 variations, two runs
  identical).
- **Alloy coupon plan (pattern followed):**
  `~/workspace/your_files/alloy-plane-satellite-package-2026-11-10/revised/coupon-test-plan.md`.

## Appendix B — What could not be verified

- **Binder, primer, topcoat, stencil, dispersant, consumables, PPE, and the
  ultrasonic bath** — no specific product and price was checked for these
  lines; each is an estimate ($15–$80) marked as such in §2. They are
  commodity items and the estimates are budgeting figures, not quotes.
- **GNP exact grade** — the bulk listings give a price range ($50–$500/kg),
  not a single grade with a datasheet for the 100 g quantity this test needs.
  The line is budgeted at $50, deliberately above the bulk range's low end.
- **Ferrite bulk listings** (Alibaba/TECHINSTRO) — the listings exist and the
  prices are as quoted, but the particle size and purity on a marketplace
  listing are the supplier's claim, not a datasheet. The Ossila jar is the
  primary source for that reason.
- **The 20 dB / 100 Ω/sq / μr ≥ 5 / 4B / 1.5× thresholds** — proposed, not
  verified properties. They are the hypotheses this test is designed to
  check.
- **All of §8** — assessed requirements derived from a 2D static simulation
  with assumed material values, not hardware measurements.

---

*End of plan. Private/local only. Nothing in this plan has been published,
sent, or shared anywhere, and nothing has been bought.*
