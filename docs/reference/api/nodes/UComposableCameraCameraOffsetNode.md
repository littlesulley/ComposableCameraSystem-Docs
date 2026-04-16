
# UComposableCameraCameraOffsetNode { #ucomposablecameracameraoffsetnode }

```cpp
#include <ComposableCameraCameraOffsetNode.h>
```

> **Inherits:** [`UComposableCameraCameraNodeBase`](../uobjects-other/UComposableCameraCameraNodeBase.md#ucomposablecameracameranodebase)

Applies a positional offset to the camera in camera-local space.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FVector` | [`PivotPosition`](#pivotposition-1)  |  |
| `FVector` | [`CameraOffset`](#cameraoffset)  |  |

---

#### PivotPosition { #pivotposition-1 }

```cpp
FVector PivotPosition { FVector::ZeroVector }
```

---

#### CameraOffset { #cameraoffset }

```cpp
FVector CameraOffset
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`OnTickNode_Implementation`](#onticknode_implementation-8) `virtual` |  |
| `void` | [`GetPinDeclarations_Implementation`](#getpindeclarations_implementation-8) `virtual` `const` |  |

---

#### OnTickNode_Implementation { #onticknode_implementation-8 }

`virtual`

```cpp
virtual void OnTickNode_Implementation(float DeltaTime, const FComposableCameraPose & CurrentCameraPose, FComposableCameraPose & OutCameraPose)
```

---

#### GetPinDeclarations_Implementation { #getpindeclarations_implementation-8 }

`virtual` `const`

```cpp
virtual void GetPinDeclarations_Implementation(TArray< FComposableCameraNodePinDeclaration > & OutPins) const
```
