
# UComposableCameraCubicHermiteSpline { #ucomposablecameracubichermitespline }

```cpp
#include <ComposableCameraCubicHermiteSpline.h>
```

> **Inherits:** `UObject`, [`IComposableCameraSplineInterface`](../interfaces/IComposableCameraSplineInterface.md#icomposablecamerasplineinterface)

Cubic Hermite spline.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `FVector` | [`GetPointOnSplineClosestToWorldSpacePosition`](#getpointonsplineclosesttoworldspaceposition-5) `virtual` |  |
| `FVector` | [`GetWorldSpacePositionByDistanceOnSpline`](#getworldspacepositionbydistanceonspline-5) `virtual` |  |
| `FRotator` | [`GetWorldSpaceRotationByDistanceOnSpline`](#getworldspacerotationbydistanceonspline-5) `virtual` |  |
| `float` | [`GetSplineLength`](#getsplinelength-5) `virtual` |  |

---

#### GetPointOnSplineClosestToWorldSpacePosition { #getpointonsplineclosesttoworldspaceposition-5 }

`virtual`

```cpp
virtual FVector GetPointOnSplineClosestToWorldSpacePosition(const FVector & WorldPosition)
```

---

#### GetWorldSpacePositionByDistanceOnSpline { #getworldspacepositionbydistanceonspline-5 }

`virtual`

```cpp
virtual FVector GetWorldSpacePositionByDistanceOnSpline(float DistanceOnSpline)
```

---

#### GetWorldSpaceRotationByDistanceOnSpline { #getworldspacerotationbydistanceonspline-5 }

`virtual`

```cpp
virtual FRotator GetWorldSpaceRotationByDistanceOnSpline(float DistanceOnSpline)
```

---

#### GetSplineLength { #getsplinelength-5 }

`virtual`

```cpp
virtual float GetSplineLength()
```
