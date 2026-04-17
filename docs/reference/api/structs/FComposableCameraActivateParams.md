
# FComposableCameraActivateParams { #fcomposablecameraactivateparams }

```cpp
#include <ComposableCameraCameraBase.h>
```

Parameters when activating a new camera.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `bool` | [`bPreserveCameraPose`](#bpreservecamerapose)  |  |
| `FTransform` | [`InitialTransform`](#initialtransform)  |  |
| `bool` | [`bUseInitialTransformRotation`](#buseinitialtransformrotation)  |  |
| `bool` | [`bFreezeSourceCamera`](#bfreezesourcecamera)  |  |
| `bool` | [`bIsTransient`](#bistransient-1)  |  |
| `float` | [`LifeTime`](#lifetime-1)  |  |

---

#### bPreserveCameraPose { #bpreservecamerapose }

```cpp
bool bPreserveCameraPose { true }
```

---

#### InitialTransform { #initialtransform }

```cpp
FTransform InitialTransform
```

---

#### bUseInitialTransformRotation { #buseinitialtransformrotation }

```cpp
bool bUseInitialTransformRotation { false }
```

---

#### bFreezeSourceCamera { #bfreezesourcecamera }

```cpp
bool bFreezeSourceCamera { false }
```

---

#### bIsTransient { #bistransient-1 }

```cpp
bool bIsTransient = false
```

---

#### LifeTime { #lifetime-1 }

```cpp
float LifeTime = 0.f
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`FComposableCameraActivateParams`](#fcomposablecameraactivateparams-1)  | Defaulted constructor. |
|  | [`FComposableCameraActivateParams`](#fcomposablecameraactivateparams-2) `inline` |  |
|  | [`FComposableCameraActivateParams`](#fcomposablecameraactivateparams-3) `inline` |  |

---

#### FComposableCameraActivateParams { #fcomposablecameraactivateparams-1 }

```cpp
FComposableCameraActivateParams() = default
```

Defaulted constructor.

---

#### FComposableCameraActivateParams { #fcomposablecameraactivateparams-2 }

`inline`

```cpp
inline FComposableCameraActivateParams(const FTransform & InInitialTransform)
```

---

#### FComposableCameraActivateParams { #fcomposablecameraactivateparams-3 }

`inline`

```cpp
inline FComposableCameraActivateParams(bool bInPreserveCameraPose, const FTransform & InInitialTransform, bool bInUseInitialTransformRotation, bool bInIsTransient, float InLifeTime)
```
