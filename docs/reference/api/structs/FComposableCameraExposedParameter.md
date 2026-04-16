
# FComposableCameraExposedParameter { #fcomposablecameraexposedparameter }

```cpp
#include <ComposableCameraTypeAsset.h>
```

Describes a parameter exposed to callers from a camera type asset. Created when a designer right-clicks a node input pin and selects "Expose as Camera Parameter".

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FName` | [`ParameterName`](#parametername)  | Unique name of the parameter (used in K2Node pins, DataTable columns, and ParameterBlock keys). |
| `FText` | [`DisplayName`](#displayname)  | Display name shown in the editor and K2Node. |
| `EComposableCameraPinType` | [`PinType`](#pintype-2)  | The data type of this parameter (mirrors the source node pin's type). |
| `TObjectPtr< UScriptStruct >` | [`StructType`](#structtype-1)  | For Struct types: the specific USTRUCT. |
| `TObjectPtr< UEnum >` | [`EnumType`](#enumtype-1)  | For Enum types: the specific UEnum. Mirrors the source node pin's EnumType. |
| `int32` | [`TargetNodeIndex`](#targetnodeindex-1)  | Which node this parameter feeds into (index in NodeTemplates). |
| `FName` | [`TargetPinName`](#targetpinname-1)  | Which input pin on the target node this parameter feeds into. |
| `bool` | [`bRequired`](#brequired)  | Whether the caller is required to provide this parameter. |
| `FText` | [`Tooltip`](#tooltip)  | Tooltip shown in the K2Node and editor. |

---

#### ParameterName { #parametername }

```cpp
FName ParameterName
```

Unique name of the parameter (used in K2Node pins, DataTable columns, and ParameterBlock keys).

Read-only on purpose: this name is the lookup key for every consumer (K2 node UserOverrideNames, DataTable row Values map, ParameterBlock activation keys, the row editor's orphan detection, the K2 node's per-pin SetParameterBlockValue emission). Editing it from the Details panel would silently break all of those without any rename plumbing. To rename an exposed parameter, unexpose it from the graph and re-expose the underlying pin under a new name (or rename the underlying C++ pin declaration in code).

---

#### DisplayName { #displayname }

```cpp
FText DisplayName
```

Display name shown in the editor and K2Node.

---

#### PinType { #pintype-2 }

```cpp
EComposableCameraPinType PinType = 
```

The data type of this parameter (mirrors the source node pin's type).

---

#### StructType { #structtype-1 }

```cpp
TObjectPtr< UScriptStruct > StructType = nullptr
```

For Struct types: the specific USTRUCT.

---

#### EnumType { #enumtype-1 }

```cpp
TObjectPtr< UEnum > EnumType = nullptr
```

For Enum types: the specific UEnum. Mirrors the source node pin's EnumType.

---

#### TargetNodeIndex { #targetnodeindex-1 }

```cpp
int32 TargetNodeIndex = INDEX_NONE
```

Which node this parameter feeds into (index in NodeTemplates).

---

#### TargetPinName { #targetpinname-1 }

```cpp
FName TargetPinName
```

Which input pin on the target node this parameter feeds into.

---

#### bRequired { #brequired }

```cpp
bool bRequired = false
```

Whether the caller is required to provide this parameter.

---

#### Tooltip { #tooltip }

```cpp
FText Tooltip
```

Tooltip shown in the K2Node and editor.
