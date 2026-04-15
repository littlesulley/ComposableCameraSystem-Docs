
# FComposableCameraRayFeeler { #fcomposablecamerarayfeeler }

```cpp
#include <ComposableCameraDynamicDeocclusionTransition.h>
```

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `float` | [`Yaw`](#yaw)  |  |
| `float` | [`Pitch`](#pitch)  |  |
| `float` | [`Length`](#length)  |  |
| `float` | [`Radius`](#radius)  |  |
| `FVector` | [`Offset`](#offset)  |  |
| `UCurveFloat *` | [`StrengthCurve`](#strengthcurve)  |  |

---

#### Yaw { #yaw }

```cpp
float Yaw
```

---

#### Pitch { #pitch }

```cpp
float Pitch
```

---

#### Length { #length }

```cpp
float Length
```

---

#### Radius { #radius }

```cpp
float Radius
```

---

#### Offset { #offset }

```cpp
FVector Offset
```

---

#### StrengthCurve { #strengthcurve }

```cpp
UCurveFloat * StrengthCurve
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `FVector` | [`GetRayStartPosition`](#getraystartposition) `const` `inline` |  |
| `FVector` | [`GetRayEndPosition`](#getrayendposition) `const` `inline` |  |

---

#### GetRayStartPosition { #getraystartposition }

`const` `inline`

```cpp
inline FVector GetRayStartPosition(const FComposableCameraPose & Pose) const
```

---

#### GetRayEndPosition { #getrayendposition }

`const` `inline`

```cpp
inline FVector GetRayEndPosition(const FComposableCameraPose & Pose) const
```
