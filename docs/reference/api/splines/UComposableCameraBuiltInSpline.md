
# UComposableCameraBuiltInSpline { #ucomposablecamerabuiltinspline }

```cpp
#include <ComposableCameraBuiltInSpline.h>
```

> **Inherits:** `UObject`, [`IComposableCameraSplineInterface`](../interfaces/IComposableCameraSplineInterface.md#icomposablecamerasplineinterface)

Unreal's built-in splines.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TObjectPtr< USplineComponent >` | [`SplineComponent`](#splinecomponent)  |  |

---

#### SplineComponent { #splinecomponent }

```cpp
TObjectPtr< USplineComponent > SplineComponent
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `FVector` | [`GetPointOnSplineClosestToWorldSpacePosition`](#getpointonsplineclosesttoworldspaceposition-3) `virtual` |  |
| `FVector` | [`GetWorldSpacePositionByDistanceOnSpline`](#getworldspacepositionbydistanceonspline-3) `virtual` |  |
| `FRotator` | [`GetWorldSpaceRotationByDistanceOnSpline`](#getworldspacerotationbydistanceonspline-3) `virtual` |  |
| `float` | [`GetSplineLength`](#getsplinelength-3) `virtual` |  |

---

#### GetPointOnSplineClosestToWorldSpacePosition { #getpointonsplineclosesttoworldspaceposition-3 }

`virtual`

```cpp
virtual FVector GetPointOnSplineClosestToWorldSpacePosition(const FVector & WorldPosition)
```

---

#### GetWorldSpacePositionByDistanceOnSpline { #getworldspacepositionbydistanceonspline-3 }

`virtual`

```cpp
virtual FVector GetWorldSpacePositionByDistanceOnSpline(float DistanceOnSpline)
```

---

#### GetWorldSpaceRotationByDistanceOnSpline { #getworldspacerotationbydistanceonspline-3 }

`virtual`

```cpp
virtual FRotator GetWorldSpaceRotationByDistanceOnSpline(float DistanceOnSpline)
```

---

#### GetSplineLength { #getsplinelength-3 }

`virtual`

```cpp
virtual float GetSplineLength()
```
