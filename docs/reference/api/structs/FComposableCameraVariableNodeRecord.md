
# FComposableCameraVariableNodeRecord { #fcomposablecameravariablenoderecord }

```cpp
#include <ComposableCameraNodePinTypes.h>
```

Editor-only record describing a single internal-variable graph node instance.

Multiple Get/Set nodes can exist for the same underlying variable. Each is tracked here by its own FGuid so the editor can round-trip the graph layout and the wires connecting it to camera nodes.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FGuid` | [`NodeGuid`](#nodeguid) | Matches UEdGraphNode::NodeGuid of the variable graph node. |
| `FGuid` | [`VariableGuid`](#variableguid-2) | Stable identity of the internal variable this node points at, matching [FComposableCameraInternalVariable::VariableGuid](FComposableCameraInternalVariable.md#variableguid-1) on the owning type asset. Survives variable renames so Get/Set nodes follow the variable across edits. May be invalid on records saved before the GUID migration; in that case RebuildFromTypeAsset falls back to VariableName. |
| `FName` | [`VariableName`](#variablename-2) | Legacy / display fallback name of the internal variable. Authoritative identity is VariableGuid; this is kept as a debug aid and legacy fallback. |
| `bool` | [`bIsSetter`](#bissetter) | True for Set nodes, false for Get nodes. |
| `bool` | [`bIsComputeChain`](#biscomputechain) | Legacy node-level chain classification. For Set-variable nodes this still identifies which exec chain owns the node. For Get-variable nodes, each connection's bIsComputeChain is authoritative because a pure getter can feed camera and compute consumers independently. |
| `FVector2D` | [`Position`](#position-3) | Serialized position on the graph canvas. |
| `TArray< FComposableCameraVariablePinConnection >` | [`Connections`](#connections) | Node endpoints this variable node is wired to. The index space of each connection's CameraNodeIndex depends on the connection's own bIsComputeChain flag. |

---

#### NodeGuid { #nodeguid }

```cpp
FGuid NodeGuid
```

Matches UEdGraphNode::NodeGuid of the variable graph node.

---

#### VariableGuid { #variableguid-2 }

```cpp
FGuid VariableGuid
```

Stable identity of the internal variable this node points at, matching [FComposableCameraInternalVariable::VariableGuid](FComposableCameraInternalVariable.md#variableguid-1) on the owning type asset. Survives variable renames so Get/Set nodes follow the variable across edits. May be invalid on records saved before the GUID migration; in that case RebuildFromTypeAsset falls back to VariableName.

---

#### VariableName { #variablename-2 }

```cpp
FName VariableName
```

Legacy / display fallback name of the internal variable. Authoritative identity is VariableGuid; this is kept as a debug aid and legacy fallback.

---

#### bIsSetter { #bissetter }

```cpp
bool bIsSetter = false
```

True for Set nodes, false for Get nodes.

---

#### bIsComputeChain { #biscomputechain }

```cpp
bool bIsComputeChain = false
```

Legacy node-level chain classification. For Set-variable nodes this still identifies which exec chain owns the node. For Get-variable nodes, each connection's bIsComputeChain is authoritative because a pure getter can feed camera and compute consumers independently.

Defaults to false for migration safety: records saved before this field existed deserialize as camera-chain, matching v1 behavior.

---

#### Position { #position-3 }

```cpp
FVector2D Position = FVector2D::ZeroVector
```

Serialized position on the graph canvas.

---

#### Connections { #connections }

```cpp
TArray< FComposableCameraVariablePinConnection > Connections
```

Node endpoints this variable node is wired to. The index space of each connection's CameraNodeIndex depends on the connection's own bIsComputeChain flag.
