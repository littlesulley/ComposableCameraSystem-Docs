
# FComposableCameraShot { #fcomposablecamerashot }

```cpp
#include <ComposableCameraShot.h>
```

Top-level Shot data — the layered composition snapshot for one shot. Three orthogonal solver layers (Placement / Aim / Lens) each take a sub-struct + a per-layer anchor spec, plus an independent Focus layer and a single Roll value composed onto the final rotation.

Targets are pure world-space objects (Actor + Bone + Offset + Bounds); they carry NO screen-space data. Screen-space composition lives on Placement (`ScreenPosition`) and Aim (`ScreenPosition`) — each tied to its own anchor.

See Docs/ShotBasedKeyframing.md §3 for the full data model and §4 for the solver pipeline.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TArray< FComposableCameraShotTarget >` | [`Targets`](#targets)  | All actors tracked by this Shot, in authoring order. Index stability matters — Placement / Aim / Focus anchor specs reference indices into this array. Reordering must update those indices in lockstep. |
| `FShotPlacement` | [`Placement`](#placement)  | Placement layer — decides Position. |
| `FShotAim` | [`Aim`](#aim)  | Aim layer — decides Rotation (Position is already set by Placement). |
| `float` | [`Roll`](#roll)  | Camera roll about its forward (look) axis, in degrees. Composed onto the output rotation as the final operation; the solver pre-rotates Aim.ScreenPosition by -Roll before solving so the screen constraint holds at any Roll. 0 = level. See spec §4.8. |
| `FShotLens` | [`Lens`](#lens)  | Lens layer — decides FOV + Aperture. |
| `FShotFocus` | [`Focus`](#focus)  | Focus layer — decides focus distance. Independent of pose / FOV. |

---

#### Targets { #targets }

```cpp
TArray< FComposableCameraShotTarget > Targets
```

All actors tracked by this Shot, in authoring order. Index stability matters — Placement / Aim / Focus anchor specs reference indices into this array. Reordering must update those indices in lockstep.

Category is `"Shot"` (NOT a sub-category like `"Shot|Targets"`) so the array renders at the top of the Details panel, above the Placement / Aim / Lens / Focus sub-structs. Designer authoring flow is "pick the actors first, then frame them" — Targets at the top reflects that.

---

#### Placement { #placement }

```cpp
FShotPlacement Placement
```

Placement layer — decides Position.

---

#### Aim { #aim }

```cpp
FShotAim Aim
```

Aim layer — decides Rotation (Position is already set by Placement).

---

#### Roll { #roll }

```cpp
float Roll = 0.f
```

Camera roll about its forward (look) axis, in degrees. Composed onto the output rotation as the final operation; the solver pre-rotates Aim.ScreenPosition by -Roll before solving so the screen constraint holds at any Roll. 0 = level. See spec §4.8.

Range `[-180, 180]`° — kept narrow on purpose:

1. The Alt+RMB-drag Roll gesture (§23.13) accumulates via `FMath::UnwindDegrees`, which already maps every accumulated value into `[-180, 180]`. Numeric input through the Details panel slider is clamped to the same range, so the field's edit surfaces and authoring gesture agree on the canonical representation.

1. Values outside `[-180, 180]` are mathematically equivalent (mod 360) — extending to e.g. `[-540, 540]` would let the designer author redundant values (540° == 180° visually) and open up confusing transition behavior (a linear blend from Shot A Roll=170 to Shot B Roll=540 takes the long way around).

1. FRotator's wrap math handles in-engine values outside the range correctly — the clamp is purely a UX / authoring- canonical-form constraint, not a runtime correctness one.

If a future use case (e.g. multi-revolution roll for a transition effect) demands wider range, prefer a dedicated transition node over widening this clamp — the canonical shot Roll should stay unique-per-pose.

---

#### Lens { #lens }

```cpp
FShotLens Lens
```

Lens layer — decides FOV + Aperture.

---

#### Focus { #focus }

```cpp
FShotFocus Focus
```

Focus layer — decides focus distance. Independent of pose / FOV.
