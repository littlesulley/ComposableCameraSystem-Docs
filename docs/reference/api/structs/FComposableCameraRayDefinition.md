
# FComposableCameraRayDefinition { #fcomposablecameraraydefinition }

```cpp
#include <ComposableCameraCylindricalTransition.h>
```

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FVector` | [`Origin`](#origin)  |  |
| `FVector` | [`Direction`](#direction)  |  |
| `float` | [`MinimumDistance`](#minimumdistance)  |  |
| `float` | [`Distance`](#distance-1)  |  |
| `bool` | [`bInfiniteDistance`](#binfinitedistance)  |  |

---

#### Origin { #origin }

```cpp
FVector Origin
```

---

#### Direction { #direction }

```cpp
FVector Direction
```

---

#### MinimumDistance { #minimumdistance }

```cpp
float MinimumDistance
```

---

#### Distance { #distance-1 }

```cpp
float Distance
```

---

#### bInfiniteDistance { #binfinitedistance }

```cpp
bool bInfiniteDistance
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`FComposableCameraRayDefinition`](#fcomposablecameraraydefinition-1) `inline` |  |
|  | [`FComposableCameraRayDefinition`](#fcomposablecameraraydefinition-2) `inline` |  |
| `FComposableCameraNearestPointsOnRaysResult` | [`FindNearestPointsByOtherRay`](#findnearestpointsbyotherray) `inline` |  |

---

#### FComposableCameraRayDefinition { #fcomposablecameraraydefinition-1 }

`inline`

```cpp
inline FComposableCameraRayDefinition(FVector InOrigin, FVector InDirection)
```

---

#### FComposableCameraRayDefinition { #fcomposablecameraraydefinition-2 }

`inline`

```cpp
inline FComposableCameraRayDefinition(FVector InOrigin, FVector InDirection, float InMinimumDistance)
```

---

#### FindNearestPointsByOtherRay { #findnearestpointsbyotherray }

`inline`

```cpp
inline FComposableCameraNearestPointsOnRaysResult FindNearestPointsByOtherRay(const FComposableCameraRayDefinition & OtherRay)
```
