
# UComposableCameraIIRInterpolator { #ucomposablecameraiirinterpolator }

```cpp
#include <ComposableCameraIIRInterpolator.h>
```

> **Inherits:** [`UComposableCameraInterpolatorBase`](UComposableCameraInterpolatorBase.md#ucomposablecamerainterpolatorbase)

IIR interpolator.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `float` | [`Speed`](#speed-1)  |  |
| `bool` | [`bUseFixedStep`](#busefixedstep-1)  | Substep the interpolation at 120 Hz and linearly advance the target across the frame. |

---

#### Speed { #speed-1 }

```cpp
float Speed = 1.f
```

---

#### bUseFixedStep { #busefixedstep-1 }

```cpp
bool bUseFixedStep = true
```

When true, `TIIRInterpolator` substeps the frame at 120 Hz and linearly advances from the previous target value to the current target value across those substeps. This keeps fixed-step smoothing stable while still following a moving target instead of repeatedly chasing only the final target for the whole frame.
