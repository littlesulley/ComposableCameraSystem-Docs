
# UComposableCameraBezierSpline { #ucomposablecamerabezierspline }

```cpp
#include <ComposableCameraBezierSpline.h>
```

> **Inherits:** `UObject`, [`IComposableCameraSplineInterface`](../interfaces/IComposableCameraSplineInterface.md#icomposablecamerasplineinterface)

Custom bezier curves.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `FVector` | [`GetPointOnSplineClosestToWorldSpacePosition`](#getpointonsplineclosesttoworldspaceposition-2) `virtual` |  |
| `FVector` | [`GetWorldSpacePositionByDistanceOnSpline`](#getworldspacepositionbydistanceonspline-2) `virtual` |  |
| `FRotator` | [`GetWorldSpaceRotationByDistanceOnSpline`](#getworldspacerotationbydistanceonspline-2) `virtual` |  |
| `float` | [`GetSplineLength`](#getsplinelength-2) `virtual` |  |

---

#### GetPointOnSplineClosestToWorldSpacePosition { #getpointonsplineclosesttoworldspaceposition-2 }

`virtual`

```cpp
virtual FVector GetPointOnSplineClosestToWorldSpacePosition(const FVector & WorldPosition)
```

---

#### GetWorldSpacePositionByDistanceOnSpline { #getworldspacepositionbydistanceonspline-2 }

`virtual`

```cpp
virtual FVector GetWorldSpacePositionByDistanceOnSpline(float DistanceOnSpline)
```

---

#### GetWorldSpaceRotationByDistanceOnSpline { #getworldspacerotationbydistanceonspline-2 }

`virtual`

```cpp
virtual FRotator GetWorldSpaceRotationByDistanceOnSpline(float DistanceOnSpline)
```

---

#### GetSplineLength { #getsplinelength-2 }

`virtual`

```cpp
virtual float GetSplineLength()
```
