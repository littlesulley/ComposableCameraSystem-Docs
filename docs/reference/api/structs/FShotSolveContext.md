
# FShotSolveContext { #fshotsolvecontext }

```cpp
#include <ComposableCameraShotSolver.h>
```

Per-frame inputs the solver needs from the runtime — viewport state + the previous frame's FOV (used as the projection FOV when the Shot is in SolvedFromBoundsFit mode).

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `float` | [`ViewportAspectRatio`](#viewportaspectratio)  | Viewport aspect ratio (width / height). |
| `float` | [`PreviousFrameFOV`](#previousframefov)  | Previous frame's FOV in degrees. Used as projection FOV in the bounds-fit pass; Manual mode uses ManualFOV instead. |

---

#### ViewportAspectRatio { #viewportaspectratio }

```cpp
float ViewportAspectRatio = 16.f / 9.f
```

Viewport aspect ratio (width / height).

---

#### PreviousFrameFOV { #previousframefov }

```cpp
float PreviousFrameFOV = 79.f
```

Previous frame's FOV in degrees. Used as projection FOV in the bounds-fit pass; Manual mode uses ManualFOV instead.
