
# IComposableCameraSplineInterface { #icomposablecamerasplineinterface }

```cpp
#include <ComposableCameraSplineInterface.h>
```

> **Subclassed by:** [`UComposableCameraBezierSpline`](../splines/UComposableCameraBezierSpline.md#ucomposablecamerabezierspline), [`UComposableCameraBuiltInSpline`](../splines/UComposableCameraBuiltInSpline.md#ucomposablecamerabuiltinspline), [`UComposableCameraCubicHermiteSpline`](../splines/UComposableCameraCubicHermiteSpline.md#ucomposablecameracubichermitespline), [`UComposableCameraNURBSpline`](../splines/UComposableCameraNURBSpline.md#ucomposablecameranurbspline), [`UComposableCameraSplineBase`](../splines/UComposableCameraSplineBase.md#ucomposablecamerasplinebase)

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `FVector` | [`GetPointOnSplineClosestToWorldSpacePosition`](#getpointonsplineclosesttoworldspaceposition-4)  |  |
| `FVector` | [`GetWorldSpacePositionByDistanceOnSpline`](#getworldspacepositionbydistanceonspline-4)  |  |
| `FRotator` | [`GetWorldSpaceRotationByDistanceOnSpline`](#getworldspacerotationbydistanceonspline-4)  |  |
| `float` | [`GetSplineLength`](#getsplinelength-4)  |  |

---

#### GetPointOnSplineClosestToWorldSpacePosition { #getpointonsplineclosesttoworldspaceposition-4 }

```cpp
FVector GetPointOnSplineClosestToWorldSpacePosition(const FVector & WorldPosition)
```

---

#### GetWorldSpacePositionByDistanceOnSpline { #getworldspacepositionbydistanceonspline-4 }

```cpp
FVector GetWorldSpacePositionByDistanceOnSpline(float DistanceOnSpline)
```

---

#### GetWorldSpaceRotationByDistanceOnSpline { #getworldspacerotationbydistanceonspline-4 }

```cpp
FRotator GetWorldSpaceRotationByDistanceOnSpline(float DistanceOnSpline)
```

---

#### GetSplineLength { #getsplinelength-4 }

```cpp
float GetSplineLength()
```
