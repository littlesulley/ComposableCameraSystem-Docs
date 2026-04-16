
# FComposableCameraNodePinDeclaration { #fcomposablecameranodepindeclaration }

```cpp
#include <ComposableCameraNodePinTypes.h>
```

Declaration of a single input or output pin on a camera node.

Nodes declare their pins by overriding GetPinDeclarations(). The editor reads these declarations to generate visual pins in the node graph, and the runtime uses them to allocate and resolve data in the RuntimeDataBlock.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FName` | [`PinName`](#pinname-4)  | Programmatic name of the pin (used in Get/SetPinValue calls and serialized connections). |
| `FText` | [`DisplayName`](#displayname-1)  | Display name shown in the editor graph. |
| `EComposableCameraPinDirection` | [`Direction`](#direction-1)  | Whether this is an input or output pin. |
| `EComposableCameraPinType` | [`PinType`](#pintype-3)  | Data type carried by this pin. |
| `TObjectPtr< UScriptStruct >` | [`StructType`](#structtype-3)  | For PinType == Struct: the specific USTRUCT type. Ignored for other pin types. |
| `TObjectPtr< UEnum >` | [`EnumType`](#enumtype-3)  | For PinType == Enum: the specific UEnum the pin represents. Ignored for other pin types. The data block always stores this pin's value as a normalized int64; this metadata is used at write time to narrow-cast into the actual backing property (uint8 / int32 / int64) and by the editor to render the enum's display names. |
| `bool` | [`bRequired`](#brequired-1)  | Whether this input is required. If true, the editor shows an error when the pin is neither wired nor exposed and has no default value. Ignored for output pins. |
| `bool` | [`bDefaultAsPin`](#bdefaultaspin)  | Class-level default for whether this pin is exposed as a wire on the graph node when a freshly-placed instance has no per-instance override. When false, new instances start out as Details-only (no graph wire, not exposable as a parameter); the user can still flip it on per-instance via the Details panel — same channel as toggling it off on a pin that defaulted to true. The per-instance toggle lives on [FComposableCameraPinOverride::bAsPin](FComposableCameraPinOverride.md#baspin) and, when present, supersedes this default. Defaults to true so existing pin declarations keep their current behavior with no asset migration. Ignored for output pins. |
| `FString` | [`DefaultValueString`](#defaultvaluestring)  | Default value for input pins when unwired and not exposed. Stored as serialized string. |
| `FText` | [`Tooltip`](#tooltip-2)  | Tooltip shown in the editor when hovering over this pin. |

---

#### PinName { #pinname-4 }

```cpp
FName PinName
```

Programmatic name of the pin (used in Get/SetPinValue calls and serialized connections).

---

#### DisplayName { #displayname-1 }

```cpp
FText DisplayName
```

Display name shown in the editor graph.

---

#### Direction { #direction-1 }

```cpp
EComposableCameraPinDirection Direction = 
```

Whether this is an input or output pin.

---

#### PinType { #pintype-3 }

```cpp
EComposableCameraPinType PinType = 
```

Data type carried by this pin.

---

#### StructType { #structtype-3 }

```cpp
TObjectPtr< UScriptStruct > StructType = nullptr
```

For PinType == Struct: the specific USTRUCT type. Ignored for other pin types.

---

#### EnumType { #enumtype-3 }

```cpp
TObjectPtr< UEnum > EnumType = nullptr
```

For PinType == Enum: the specific UEnum the pin represents. Ignored for other pin types. The data block always stores this pin's value as a normalized int64; this metadata is used at write time to narrow-cast into the actual backing property (uint8 / int32 / int64) and by the editor to render the enum's display names.

---

#### bRequired { #brequired-1 }

```cpp
bool bRequired = false
```

Whether this input is required. If true, the editor shows an error when the pin is neither wired nor exposed and has no default value. Ignored for output pins.

---

#### bDefaultAsPin { #bdefaultaspin }

```cpp
bool bDefaultAsPin = true
```

Class-level default for whether this pin is exposed as a wire on the graph node when a freshly-placed instance has no per-instance override. When false, new instances start out as Details-only (no graph wire, not exposable as a parameter); the user can still flip it on per-instance via the Details panel — same channel as toggling it off on a pin that defaulted to true. The per-instance toggle lives on [FComposableCameraPinOverride::bAsPin](FComposableCameraPinOverride.md#baspin) and, when present, supersedes this default. Defaults to true so existing pin declarations keep their current behavior with no asset migration. Ignored for output pins.

---

#### DefaultValueString { #defaultvaluestring }

```cpp
FString DefaultValueString
```

Default value for input pins when unwired and not exposed. Stored as serialized string.

---

#### Tooltip { #tooltip-2 }

```cpp
FText Tooltip
```

Tooltip shown in the editor when hovering over this pin.
