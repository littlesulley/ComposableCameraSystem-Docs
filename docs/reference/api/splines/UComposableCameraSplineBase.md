
# UComposableCameraSplineBase { #ucomposablecamerasplinebase }

```cpp
#include <ComposableCameraBasicSpline.h>
```

> **Inherits:** `UObject`, [`IComposableCameraSplineInterface`](../interfaces/IComposableCameraSplineInterface.md#icomposablecamerasplineinterface)

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `FVector` | [`GetPointOnSplineClosestToWorldSpacePosition`](#getpointonsplineclosesttoworldspaceposition-1) `virtual` |  |
| `FVector` | [`GetWorldSpacePositionByDistanceOnSpline`](#getworldspacepositionbydistanceonspline-1) `virtual` |  |
| `FRotator` | [`GetWorldSpaceRotationByDistanceOnSpline`](#getworldspacerotationbydistanceonspline-1) `virtual` |  |
| `float` | [`GetSplineLength`](#getsplinelength-1) `virtual` |  |

---

#### GetPointOnSplineClosestToWorldSpacePosition { #getpointonsplineclosesttoworldspaceposition-1 }

`virtual`

```cpp
virtual FVector GetPointOnSplineClosestToWorldSpacePosition(const FVector & WorldPosition)
```

---

#### GetWorldSpacePositionByDistanceOnSpline { #getworldspacepositionbydistanceonspline-1 }

`virtual`

```cpp
virtual FVector GetWorldSpacePositionByDistanceOnSpline(float DistanceOnSpline)
```

---

#### GetWorldSpaceRotationByDistanceOnSpline { #getworldspacerotationbydistanceonspline-1 }

`virtual`

```cpp
virtual FRotator GetWorldSpaceRotationByDistanceOnSpline(float DistanceOnSpline)
```

---

#### GetSplineLength { #getsplinelength-1 }

`virtual`

```cpp
virtual float GetSplineLength()
```
