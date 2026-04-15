
# FComposableCameraVariablePinConnection { #fcomposablecameravariablepinconnection }

```cpp
#include <ComposableCameraNodePinTypes.h>
```

Describes a wire between an internal-variable graph node (Get or Set) and a camera/compute node pin.

For a Get variable node: CameraNodeIndex/CameraPinName identify a node's input pin that reads the variable's current value.

For a Set variable node: CameraNodeIndex/CameraPinName identify a node's output pin whose value is written into the variable when the source node executes.

The "Camera" prefix on CameraNodeIndex / CameraPinName is a legacy naming artifact from before variable nodes could live on the compute chain. The index space depends on the owning [FComposableCameraVariableNodeRecord](FComposableCameraVariableNodeRecord.md#fcomposablecameravariablenoderecord)'s bIsComputeChain flag:

* bIsComputeChain == false: CameraNodeIndex indexes NodeTemplates.

* bIsComputeChain == true: CameraNodeIndex indexes ComputeNodeTemplates.

The field names are preserved for serialization compatibility.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `int32` | [`CameraNodeIndex`](#cameranodeindex-1)  | Index of the node endpoint. Indexes NodeTemplates for camera-chain records, ComputeNodeTemplates for compute-chain records. The "Camera" prefix is preserved for serialization compatibility. |
| `FName` | [`CameraPinName`](#camerapinname)  | Name of the pin on the node (input pin for Get, output pin for Set). |

---

#### CameraNodeIndex { #cameranodeindex-1 }

```cpp
int32 CameraNodeIndex = INDEX_NONE
```

Index of the node endpoint. Indexes NodeTemplates for camera-chain records, ComputeNodeTemplates for compute-chain records. The "Camera" prefix is preserved for serialization compatibility.

---

#### CameraPinName { #camerapinname }

```cpp
FName CameraPinName
```

Name of the pin on the node (input pin for Get, output pin for Set).
