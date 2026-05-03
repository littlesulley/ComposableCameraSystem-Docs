
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
| `FVector2D` | [`ScreenPosition`](#screenposition)  | Where the resolved aim anchor should land on screen, normalized to [-0.5, 0.5]². **This is the hard rotation constraint** — the closed-form solver always satisfies it exactly via `SolveCameraRotationForScreenTarget`. |

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

Where the resolved aim anchor should land on screen, normalized to [-0.5, 0.5]². **This is the hard rotation constraint** — the closed-form solver always satisfies it exactly via `SolveCameraRotationForScreenTarget`.
