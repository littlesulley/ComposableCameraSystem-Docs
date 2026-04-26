
# UComposableCameraCameraOffsetNode { #ucomposablecameracameraoffsetnode }

```cpp
#include <ComposableCameraCameraOffsetNode.h>
```

> **Inherits:** [`UComposableCameraCameraNodeBase`](../uobjects-other/UComposableCameraCameraNodeBase.md#ucomposablecameracameranodebase)

Applies a positional offset to the camera in camera-local space.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FVector` | [`PivotPosition`](#pivotposition-2)  |  |
| `FVector` | [`CameraOffset`](#cameraoffset)  |  |

---

#### PivotPosition { #pivotposition-2 }

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
|  | [`UComposableCameraCameraOffsetNode`](#ucomposablecameracameraoffsetnode-1) `inline` |  |
| `void` | [`OnTickNode_Implementation`](#onticknode_implementation-12) `virtual` |  |
| `void` | [`GetPinDeclarations_Implementation`](#getpindeclarations_implementation-11) `virtual` `const` |  |

---

#### UComposableCameraCameraOffsetNode { #ucomposablecameracameraoffsetnode-1 }

`inline`

```cpp
inline UComposableCameraCameraOffsetNode()
```

---

#### OnTickNode_Implementation { #onticknode_implementation-12 }

`virtual`

```cpp
virtual void OnTickNode_Implementation(float DeltaTime, const FComposableCameraPose & CurrentCameraPose, FComposableCameraPose & OutCameraPose)
```

---

#### GetPinDeclarations_Implementation { #getpindeclarations_implementation-11 }

`virtual` `const`

```cpp
virtual void GetPinDeclarations_Implementation(TArray< FComposableCameraNodePinDeclaration > & OutPins) const
```
