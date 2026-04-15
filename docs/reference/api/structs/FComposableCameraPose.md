
# FComposableCameraPose { #fcomposablecamerapose }

```cpp
#include <ComposableCameraCameraBase.h>
```

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FVector` | [`Position`](#position)  |  |
| `FRotator` | [`Rotation`](#rotation)  |  |
| `double` | [`FieldOfView`](#fieldofview)  |  |

---

#### Position { #position }

```cpp
FVector Position { 0, 0, 0 }
```

---

#### Rotation { #rotation }

```cpp
FRotator Rotation { 0, 0, 0 }
```

---

#### FieldOfView { #fieldofview }

```cpp
double FieldOfView { 75.f }
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`BlendBy`](#blendby) `inline` |  |

---

#### BlendBy { #blendby }

`inline`

```cpp
inline void BlendBy(const FComposableCameraPose & Other, float OtherWeight)
```
