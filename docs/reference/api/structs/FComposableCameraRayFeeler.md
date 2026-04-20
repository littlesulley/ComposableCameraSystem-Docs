
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
| `TObjectPtr< UCurveFloat >` | [`StrengthCurve`](#strengthcurve)  |  |

---

#### Yaw { #yaw }

```cpp
float Yaw { 0.f }
```

---

#### Pitch { #pitch }

```cpp
float Pitch { 0.f }
```

---

#### Length { #length }

```cpp
float Length { 100.f }
```

---

#### Radius { #radius }

```cpp
float Radius { 0.f }
```

---

#### Offset { #offset }

```cpp
FVector Offset { FVector::ZeroVector }
```

---

#### StrengthCurve { #strengthcurve }

```cpp
TObjectPtr< UCurveFloat > StrengthCurve { nullptr }
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
