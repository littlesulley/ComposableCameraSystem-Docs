
# FShotAim { #fshotaim }

```cpp
#include <ComposableCameraShot.h>
```

Aim layer — decides camera ROTATION (Position is already determined by the Placement layer). See spec §4.4.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FComposableCameraAnchorSpec` | [`AimAnchor`](#aimanchor)  | Where in the world the camera LOOKS AT. Independent of Placement's anchor — when they differ, you get OTS / two-shot framing for free. Resolved from the Shot's Targets list (or a fixed world point). |
| `EShotAimMode` | [`Mode`](#mode)  | Selects how Rotation is computed. Currently a single mode (LookAtAnchor); kept as an enum for symmetry with PlacementMode and future expansion (e.g. ManualEuler). |
| `FVector2D` | [`ScreenPosition`](#screenposition)  | Where the resolved aim anchor should land on screen, normalized to [-0.5, 0.5]². With `AimZones.bEnabled == false` (V1 default) this is a hard rotation constraint — the closed-form solver satisfies it exactly via `SolveCameraRotationForScreenTarget` every frame. With `AimZones.bEnabled == true` this becomes the *target* position the anchor is damped toward (and the center of the zone rectangles). |
| `FShotScreenZones` | [`AimZones`](#aimzones)  | Cinemachine-style screen-space framing zones for `Aim.ScreenPosition`. Only meaningful for `AimMode == LookAtAnchor` (NoOp ignores ScreenPosition entirely). When enabled the closed-form rotation solver runs against the zone-derived effective screen target instead of the raw authored `ScreenPosition` — see `[FShotScreenZones](FShotScreenZones.md#fshotscreenzones)` for the algorithm. |

---

#### AimAnchor { #aimanchor }

```cpp
FComposableCameraAnchorSpec AimAnchor
```

Where in the world the camera LOOKS AT. Independent of Placement's anchor — when they differ, you get OTS / two-shot framing for free. Resolved from the Shot's Targets list (or a fixed world point).

---

#### Mode { #mode }

```cpp
EShotAimMode Mode = 
```

Selects how Rotation is computed. Currently a single mode (LookAtAnchor); kept as an enum for symmetry with PlacementMode and future expansion (e.g. ManualEuler).

---

#### ScreenPosition { #screenposition }

```cpp
FVector2D ScreenPosition = FVector2D::ZeroVector
```

Where the resolved aim anchor should land on screen, normalized to [-0.5, 0.5]². With `AimZones.bEnabled == false` (V1 default) this is a hard rotation constraint — the closed-form solver satisfies it exactly via `SolveCameraRotationForScreenTarget` every frame. With `AimZones.bEnabled == true` this becomes the *target* position the anchor is damped toward (and the center of the zone rectangles).

---

#### AimZones { #aimzones }

```cpp
FShotScreenZones AimZones
```

Cinemachine-style screen-space framing zones for `Aim.ScreenPosition`. Only meaningful for `AimMode == LookAtAnchor` (NoOp ignores ScreenPosition entirely). When enabled the closed-form rotation solver runs against the zone-derived effective screen target instead of the raw authored `ScreenPosition` — see `[FShotScreenZones](FShotScreenZones.md#fshotscreenzones)` for the algorithm.
