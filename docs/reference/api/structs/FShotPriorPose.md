
# FShotPriorPose { #fshotpriorpose }

```cpp
#include <ComposableCameraShotSolver.h>
```

Optional prior camera pose handed to `SolveShot` so the zone path has a base to project anchors through. Lightweight (Pos + Rot, FOV reuses `Context.PreviousFrameFOV`) — the Solver header stays free of `[FComposableCameraPose](FComposableCameraPose.md#fcomposablecamerapose)` (which lives one module-folder away in `[Cameras/ComposableCameraCameraBase.h](#composablecameracamerabaseh)`).

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FVector` | [`Position`](#position-4)  |  |
| `FRotator` | [`Rotation`](#rotation-4)  |  |
| `float` | [`LastDistance`](#lastdistance)  | Last frame's effective `Distance` (after V2.2 damping + 1cm clamp). `< 0` ⇒ no prior, solver skips Distance damping and uses the authored value. Set by the caller from `[FShotSolveResult::EffectiveDistance](FShotSolveResult.md#effectivedistance)` after a successful solve. |
| `float` | [`LastFOV`](#lastfov)  | Last frame's effective FOV (degrees, post-damping + post-clamp). `< 0` ⇒ no prior, solver skips FOV damping and uses the freshly-solved value. Caller sets this from `[FShotSolveResult::FieldOfView](FShotSolveResult.md#fieldofview-2)` after a successful solve. |
| `float` | [`LastRoll`](#lastroll)  | Last frame's effective Roll (degrees, post-damping). Sentinel is `FLT_MAX` — Roll legitimately spans the entire `[-180, 180]` range incl. 0, so a numeric-zero default would be ambiguous. Caller sets this from `FShotSolveResult::CameraRotation.Roll` after a successful solve. |

---

#### Position { #position-4 }

```cpp
FVector Position = FVector::ZeroVector
```

---

#### Rotation { #rotation-4 }

```cpp
FRotator Rotation = FRotator::ZeroRotator
```

---

#### LastDistance { #lastdistance }

```cpp
float LastDistance = -1.f
```

Last frame's effective `Distance` (after V2.2 damping + 1cm clamp). `< 0` ⇒ no prior, solver skips Distance damping and uses the authored value. Set by the caller from `[FShotSolveResult::EffectiveDistance](FShotSolveResult.md#effectivedistance)` after a successful solve.

---

#### LastFOV { #lastfov }

```cpp
float LastFOV = -1.f
```

Last frame's effective FOV (degrees, post-damping + post-clamp). `< 0` ⇒ no prior, solver skips FOV damping and uses the freshly-solved value. Caller sets this from `[FShotSolveResult::FieldOfView](FShotSolveResult.md#fieldofview-2)` after a successful solve.

---

#### LastRoll { #lastroll }

```cpp
float LastRoll = TNumericLimits<float>::Max()
```

Last frame's effective Roll (degrees, post-damping). Sentinel is `FLT_MAX` — Roll legitimately spans the entire `[-180, 180]` range incl. 0, so a numeric-zero default would be ambiguous. Caller sets this from `FShotSolveResult::CameraRotation.Roll` after a successful solve.
