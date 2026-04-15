
# UComposableCameraFixedPoseNode { #ucomposablecamerafixedposenode }

```cpp
#include <ComposableCameraFixedPoseNode.h>
```

> **Inherits:** [`UComposableCameraCameraNodeBase`](../uobjects-other/UComposableCameraCameraNodeBase.md#ucomposablecameracameranodebase)

Node for keeping a fixed pose camera, i.e., keeping its position, rotation and FOV. <br/>
This node simply uses the current camera's CameraPose as the output pose. So it's not rigorously "fixed".

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`OnTickNode_Implementation`](#onticknode_implementation-2) `virtual` |  |
| `void` | [`GetPinDeclarations_Implementation`](#getpindeclarations_implementation-2) `virtual` `const` |  |

---

#### OnTickNode_Implementation { #onticknode_implementation-2 }

`virtual`

```cpp
virtual void OnTickNode_Implementation(float DeltaTime, const FComposableCameraPose & CurrentCameraPose, FComposableCameraPose & OutCameraPose)
```

---

#### GetPinDeclarations_Implementation { #getpindeclarations_implementation-2 }

`virtual` `const`

```cpp
virtual void GetPinDeclarations_Implementation(TArray< FComposableCameraNodePinDeclaration > & OutPins) const
```
