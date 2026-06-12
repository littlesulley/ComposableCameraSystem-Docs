
# UComposableCameraSimpleSpringInterpolator { #ucomposablecamerasimplespringinterpolator }

```cpp
#include <ComposableCameraSimpleSpringInterpolator.h>
```

> **Inherits:** [`UComposableCameraInterpolatorBase`](UComposableCameraInterpolatorBase.md#ucomposablecamerainterpolatorbase)

Simple exact spring interpolator.

`Run()` returns the new absolute interpolated value. Scalar damping computes the
progress from current toward target and adds it back to the current value; vector
specializations return the per-component absolute values directly. This matters
for nodes that reset interpolators from their last smoothed output every frame.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `float` | [`DampTime`](#damptime-1)  |  |

---

#### DampTime { #damptime-1 }

```cpp
float DampTime { 1.f }
```

Time constant for the exponential damping response. Larger values make the
spring softer and slower to reach the target.

### Private Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`COMPOSABLECAMERASYSTEM_DECLARE_CAMERA_INTERPOLATOR`](#composablecamerasystem_declare_camera_interpolator-1)  |  |

---

#### COMPOSABLECAMERASYSTEM_DECLARE_CAMERA_INTERPOLATOR { #composablecamerasystem_declare_camera_interpolator-1 }

```cpp
COMPOSABLECAMERASYSTEM_DECLARE_CAMERA_INTERPOLATOR()
```
