
# UComposableCameraNURBSpline { #ucomposablecameranurbspline }

```cpp
#include <ComposableCameraNURBSpline.h>
```

> **Inherits:** `UObject`, [`IComposableCameraSplineInterface`](../interfaces/IComposableCameraSplineInterface.md#icomposablecamerasplineinterface)

Non-uniform rational B-Splines.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `FVector` | [`GetPointOnSplineClosestToWorldSpacePosition`](#getpointonsplineclosesttoworldspaceposition) `virtual` |  |
| `FVector` | [`GetWorldSpacePositionByDistanceOnSpline`](#getworldspacepositionbydistanceonspline) `virtual` |  |
| `FRotator` | [`GetWorldSpaceRotationByDistanceOnSpline`](#getworldspacerotationbydistanceonspline) `virtual` |  |
| `float` | [`GetSplineLength`](#getsplinelength) `virtual` |  |

---

#### GetPointOnSplineClosestToWorldSpacePosition { #getpointonsplineclosesttoworldspaceposition }

`virtual`

```cpp
virtual FVector GetPointOnSplineClosestToWorldSpacePosition(const FVector & WorldPosition)
```

---

#### GetWorldSpacePositionByDistanceOnSpline { #getworldspacepositionbydistanceonspline }

`virtual`

```cpp
virtual FVector GetWorldSpacePositionByDistanceOnSpline(float DistanceOnSpline)
```

---

#### GetWorldSpaceRotationByDistanceOnSpline { #getworldspacerotationbydistanceonspline }

`virtual`

```cpp
virtual FRotator GetWorldSpaceRotationByDistanceOnSpline(float DistanceOnSpline)
```

---

#### GetSplineLength { #getsplinelength }

`virtual`

```cpp
virtual float GetSplineLength()
```
