
# FComposableCameraInternalVariable { #fcomposablecamerainternalvariable }

```cpp
#include <ComposableCameraTypeAsset.h>
```

Describes a camera-level variable (internal or caller-exposed).

This is the struct used for BOTH InternalVariables and ExposedVariables on [UComposableCameraTypeAsset](../data-assets/UComposableCameraTypeAsset.md#ucomposablecameratypeasset) — the two arrays share the same field layout and the runtime also stores both in a single FName→offset map. The distinction lives purely at the authoring surface: which array an entry lives in.

* InternalVariables: node-only slots. InitialValueString is applied at camera instantiation; callers have no way to override it.

* ExposedVariables: same node-level read/write semantics, but the caller's [FComposableCameraParameterBlock](FComposableCameraParameterBlock.md#fcomposablecameraparameterblock) may override the initial value at activation time (by keying on VariableName, same channel used for ExposedParameters). After activation, there is no external read/write API for them — they behave exactly like internal variables from that point on.

All fields apply to both usages; none are ignored in either case.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FGuid` | [`VariableGuid`](#variableguid-1)  | Stable identifier for this variable, independent of VariableName. |
| `FName` | [`VariableName`](#variablename-1)  | Name of this variable. |
| `EComposableCameraPinType` | [`VariableType`](#variabletype)  |  |
| `TObjectPtr< UScriptStruct >` | [`StructType`](#structtype-2)  |  |
| `TObjectPtr< UEnum >` | [`EnumType`](#enumtype-2)  | For VariableType == Enum: the specific UEnum this variable represents. Stored internally as a normalized int64 (matching Enum pin behavior). |
| `FString` | [`InitialValueString`](#initialvaluestring)  | Initial value at camera instantiation (serialized string). |
| `bool` | [`bResetEveryFrame`](#breseteveryframe)  | If true, the variable resets to InitialValue at the start of every frame (before node execution). If false, the variable persists across frames. |
| `FText` | [`Tooltip`](#tooltip-1)  |  |

---

#### VariableGuid { #variableguid-1 }

```cpp
FGuid VariableGuid
```

Stable identifier for this variable, independent of VariableName.

VariableName is the user-facing key used at runtime to look up values in the ParameterBlock / RuntimeDataBlock, but the editor needs a separate identity that survives renames so existing Get/Set variable graph nodes can follow a variable across a rename in the Details panel. The editor's UComposableCameraVariableGraphNode tracks its variable by this GUID, and the toolkit populates a missing GUID lazily on load (see UComposableCameraTypeAsset::PostLoad).

This field is never read by the runtime — it exists purely for editor identity tracking and serialization round-trip.

---

#### VariableName { #variablename-1 }

```cpp
FName VariableName
```

Name of this variable.

Serves both as the runtime lookup key (ParameterBlock / RuntimeDataBlock) and as the display label in the graph editor context menu and on Get/Set variable nodes. There is no separate DisplayName — the FName IS the display name. Renames are tracked via VariableGuid so existing Get/Set graph nodes follow the variable through edits in the Details panel.

---

#### VariableType { #variabletype }

```cpp
EComposableCameraPinType VariableType = 
```

---

#### StructType { #structtype-2 }

```cpp
TObjectPtr< UScriptStruct > StructType = nullptr
```

---

#### EnumType { #enumtype-2 }

```cpp
TObjectPtr< UEnum > EnumType = nullptr
```

For VariableType == Enum: the specific UEnum this variable represents. Stored internally as a normalized int64 (matching Enum pin behavior).

---

#### InitialValueString { #initialvaluestring }

```cpp
FString InitialValueString
```

Initial value at camera instantiation (serialized string).

---

#### bResetEveryFrame { #breseteveryframe }

```cpp
bool bResetEveryFrame = false
```

If true, the variable resets to InitialValue at the start of every frame (before node execution). If false, the variable persists across frames.

---

#### Tooltip { #tooltip-1 }

```cpp
FText Tooltip
```
