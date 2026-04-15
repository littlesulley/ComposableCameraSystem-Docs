
# FComposableCameraExecEntry { #fcomposablecameraexecentry }

```cpp
#include <ComposableCameraNodePinTypes.h>
```

A single entry in the full execution chain serialized by the editor.

The editor walks the exec-pin chain in the visual graph (starting from the Start sentinel's ExecOut) and records each step here. Camera-node steps resolve to a camera node index; Set-variable steps capture the variable GUID and the source pin that feeds the Set node's Value input.

The runtime consumes the full chain to interleave camera node execution with scratch-variable writes. The older TypeAsset::ExecutionOrder array is kept as a camera-node-only projection of this chain for quick runtime iteration and backwards compatibility with code paths that don't care about Set operations.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `EComposableCameraExecEntryType` | [`EntryType`](#entrytype)  | Which kind of step this entry represents. |
| `int32` | [`CameraNodeIndex`](#cameranodeindex)  | Node index in the chain-local template array. Used when EntryType == CameraNode (the node to execute), or as the source node of a SetVariable entry (the node whose output pin feeds the Set node's Value input). |
| `FGuid` | [`VariableGuid`](#variableguid)  | Stable identity of the internal variable being written. Used when EntryType == SetVariable. |
| `FName` | [`VariableName`](#variablename)  | Cached runtime name of the internal variable, matching [FComposableCameraInternalVariable::VariableName](FComposableCameraInternalVariable.md#variablename-1). The editor populates this during SyncToTypeAsset by resolving VariableGuid against the type asset's variable arrays. The runtime uses this to index into [FComposableCameraRuntimeDataBlock::InternalVariableOffsets](FComposableCameraRuntimeDataBlock.md#internalvariableoffsets) without a GUID→Name lookup. Used when EntryType == SetVariable. |
| `FName` | [`SourcePinName`](#sourcepinname)  | Name of the output pin on CameraNodeIndex's node that supplies the value being written into the variable. Used when EntryType == SetVariable. |
| `int32` | [`VariableSlotSize`](#variableslotsize)  | Byte size of the variable's data slot. Pre-computed from the variable's EComposableCameraPinType at sync time so the runtime can do a raw memcpy from the source output pin offset to the variable offset without a type-dispatch. Used when EntryType == SetVariable. |

---

#### EntryType { #entrytype }

```cpp
EComposableCameraExecEntryType EntryType = 
```

Which kind of step this entry represents.

---

#### CameraNodeIndex { #cameranodeindex }

```cpp
int32 CameraNodeIndex = INDEX_NONE
```

Node index in the chain-local template array. Used when EntryType == CameraNode (the node to execute), or as the source node of a SetVariable entry (the node whose output pin feeds the Set node's Value input).

For entries in FullExecChain: indexes NodeTemplates. For entries in ComputeFullExecChain: indexes ComputeNodeTemplates.

The "Camera" prefix is preserved for serialization compatibility.

---

#### VariableGuid { #variableguid }

```cpp
FGuid VariableGuid
```

Stable identity of the internal variable being written. Used when EntryType == SetVariable.

---

#### VariableName { #variablename }

```cpp
FName VariableName
```

Cached runtime name of the internal variable, matching [FComposableCameraInternalVariable::VariableName](FComposableCameraInternalVariable.md#variablename-1). The editor populates this during SyncToTypeAsset by resolving VariableGuid against the type asset's variable arrays. The runtime uses this to index into [FComposableCameraRuntimeDataBlock::InternalVariableOffsets](FComposableCameraRuntimeDataBlock.md#internalvariableoffsets) without a GUID→Name lookup. Used when EntryType == SetVariable.

---

#### SourcePinName { #sourcepinname }

```cpp
FName SourcePinName
```

Name of the output pin on CameraNodeIndex's node that supplies the value being written into the variable. Used when EntryType == SetVariable.

---

#### VariableSlotSize { #variableslotsize }

```cpp
int32 VariableSlotSize = 0
```

Byte size of the variable's data slot. Pre-computed from the variable's EComposableCameraPinType at sync time so the runtime can do a raw memcpy from the source output pin offset to the variable offset without a type-dispatch. Used when EntryType == SetVariable.
