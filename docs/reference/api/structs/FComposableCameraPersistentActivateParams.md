
# FComposableCameraPersistentActivateParams { #fcomposablecamerapersistentactivateparams }

```cpp
#include <ComposableCameraMixingCameraNode.h>
```

Parameters when activating a new persistent camera.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `bool` | [`bPreserveCameraPose`](#bpreservecamerapose-1)  |  |
| `FTransform` | [`InitialTransform`](#initialtransform-1)  |  |
| `bool` | [`bUseInitialTransformRotation`](#buseinitialtransformrotation-1)  |  |

---

#### bPreserveCameraPose { #bpreservecamerapose-1 }

```cpp
bool bPreserveCameraPose { true }
```

---

#### InitialTransform { #initialtransform-1 }

```cpp
FTransform InitialTransform
```

---

#### bUseInitialTransformRotation { #buseinitialtransformrotation-1 }

```cpp
bool bUseInitialTransformRotation { false }
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`FComposableCameraPersistentActivateParams`](#fcomposablecamerapersistentactivateparams-1)  | Defaulted constructor. |
|  | [`FComposableCameraPersistentActivateParams`](#fcomposablecamerapersistentactivateparams-2) `inline` |  |

---

#### FComposableCameraPersistentActivateParams { #fcomposablecamerapersistentactivateparams-1 }

```cpp
FComposableCameraPersistentActivateParams() = default
```

Defaulted constructor.

---

#### FComposableCameraPersistentActivateParams { #fcomposablecamerapersistentactivateparams-2 }

`inline`

```cpp
inline FComposableCameraPersistentActivateParams(const FTransform & InInitialTransform)
```
