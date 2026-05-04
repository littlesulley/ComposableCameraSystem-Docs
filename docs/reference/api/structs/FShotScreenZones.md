
# FShotScreenZones { #fshotscreenzones }

```cpp
#include <ComposableCameraShot.h>
```

Cinemachine-style screen-space framing zones for an anchor's screen position constraint. The zone is a pair of nested rectangles **centered on `ScreenPosition`** (NOT on the anchor's projected position) — the anchor "floats" inside the zone, its projection drifts relative to ScreenPosition while the camera holds, and the solver pulls it back when it strays.

When `bEnabled == false` the solver runs the V1 hard-constraint path (anchor lands exactly at `ScreenPosition` every frame). When `bEnabled == true` the solver:

1. projects the anchor through `LastOutputPose` to read its current screen position;

1. computes the per-axis residual outside the dead-zone padding — anchor inside the dead rect [SP - DeadLeft, SP + DeadRight] × [SP - DeadBottom, SP + DeadTop] → zero residual → camera holds;

1. one-pole (`FMath::FInterpTo`) damps the residual per axis using `HorizontalSpeed` / `VerticalSpeed`;

1. clamps the post-damping offset to the soft-zone padding rectangle (hard limit — anchor never leaves soft zone, no damping on the clamp);

1. feeds the resulting effective screen target into the V1 closed- form / Picard solver.

One struct, two attachment sites — `[FShotAim::AimZones](FShotAim.md#aimzones)` (always applies when AimMode == LookAtAnchor) and `[FShotPlacement::PlacementZones](FShotPlacement.md#placementzones)` (only consumed in `AnchorAtScreen` placement; ignored by `AnchorOrbit` because that mode does not author a `Placement.ScreenPosition`).

**Asymmetric paddings** allow zones that aren't centered on ScreenPosition — useful for lead-room framing where the dead zone trails the subject on one axis. Designer drags one edge → only the matching padding mutates (Cinemachine-style single-side resize).

Damping speeds are `FMath::FInterpTo`-style — higher = snappier; `0` = no damping (snap to zone boundary instantly). Match the convention used by `[UComposableCameraIIRInterpolator::Speed](../interpolators/UComposableCameraIIRInterpolator.md#speed-1)`.

Per-side soft padding must be `>=` matching dead padding (Soft is the outer rect; Dead is the inner). The drag handler enforces this by pushing the partner side; the solver also defensively clamps.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `bool` | [`bEnabled`](#benabled)  | Master switch. `false` = V1 hard-constraint path (every frame the anchor is solved to land exactly at `ScreenPosition` — closed-form for `LookAtAnchor`, Picard for `AnchorAtScreen + LookAtAnchor`). `true` = pose-state-aware Cinemachine-style damped framing described above. Default `false` for V1 backward compatibility. |
| `FShotScreenZonePadding` | [`DeadZone`](#deadzone)  | Inner rectangle (per-side padding from ScreenPosition). Anchor inside this rect = camera does not adjust. Default 0.1 each side = 20% × 20% rect when zones are symmetric. |
| `FShotScreenZonePadding` | [`SoftZone`](#softzone)  | Outer rectangle (per-side padding from ScreenPosition). Anchor is hard-clamped to never leave this rect. Each side must be `>=` matching dead-zone padding (drag handler enforces; solver also defensively clamps). |
| `float` | [`HorizontalSpeed`](#horizontalspeed)  | Horizontal damping speed (`FMath::FInterpTo` Speed semantics) — higher = snappier, `0` = instant snap to zone boundary. |
| `float` | [`VerticalSpeed`](#verticalspeed)  | Vertical damping speed (`FMath::FInterpTo` Speed semantics) — higher = snappier, `0` = instant snap to zone boundary. |

---

#### bEnabled { #benabled }

```cpp
bool bEnabled = false
```

Master switch. `false` = V1 hard-constraint path (every frame the anchor is solved to land exactly at `ScreenPosition` — closed-form for `LookAtAnchor`, Picard for `AnchorAtScreen + LookAtAnchor`). `true` = pose-state-aware Cinemachine-style damped framing described above. Default `false` for V1 backward compatibility.

---

#### DeadZone { #deadzone }

```cpp
FShotScreenZonePadding DeadZone
```

Inner rectangle (per-side padding from ScreenPosition). Anchor inside this rect = camera does not adjust. Default 0.1 each side = 20% × 20% rect when zones are symmetric.

---

#### SoftZone { #softzone }

```cpp
FShotScreenZonePadding SoftZone
```

Outer rectangle (per-side padding from ScreenPosition). Anchor is hard-clamped to never leave this rect. Each side must be `>=` matching dead-zone padding (drag handler enforces; solver also defensively clamps).

---

#### HorizontalSpeed { #horizontalspeed }

```cpp
float HorizontalSpeed = 5.f
```

Horizontal damping speed (`FMath::FInterpTo` Speed semantics) — higher = snappier, `0` = instant snap to zone boundary.

---

#### VerticalSpeed { #verticalspeed }

```cpp
float VerticalSpeed = 5.f
```

Vertical damping speed (`FMath::FInterpTo` Speed semantics) — higher = snappier, `0` = instant snap to zone boundary.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`FShotScreenZones`](#fshotscreenzones-1) `inline` |  |

---

#### FShotScreenZones { #fshotscreenzones-1 }

`inline`

```cpp
inline FShotScreenZones()
```
