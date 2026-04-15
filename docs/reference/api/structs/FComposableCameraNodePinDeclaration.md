
# FComposableCameraNodePinDeclaration { #fcomposablecameranodepindeclaration }

```cpp
#include <ComposableCameraNodePinTypes.h>
```

Declaration of a single input or output pin on a camera node.

Nodes declare their pins by overriding GetPinDeclarations(). The editor reads these declarations to generate visual pins in the node graph, and the runtime uses them to allocate and resolve data in the RuntimeDataBlock.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FName` | [`PinName`](#pinname-3)  | Programmatic name of the pin (used in Get/SetPinValue calls and serialized connections). |
| `FText` | [`DisplayName`](#displayname-1)  | Display name shown in the editor graph. |
| `EComposableCameraPinDirection` | [`Direction`](#direction-1)  | Whether this is an input or output pin. |
| `EComposableCameraPinType` | [`PinType`](#pintype-2)  | Data type carried by this pin. |
| `UScriptStruct *` | [`StructType`](#structtype-2)  | For PinType == Struct: the specific USTRUCT type. Ignored for other pin types. |
| `bool` | [`bRequired`](#brequired-1)  | Whether this input is required. If true, the editor shows an error when the pin is neither wired nor exposed and has no default value. Ignored for output pins. |
| `FString` | [`DefaultValueString`](#defaultvaluestring)  | Default value for input pins when unwired and not exposed. Stored as serialized string. |
| `FText` | [`Tooltip`](#tooltip-2)  | Tooltip shown in the editor when hovering over this pin. |

---

#### PinName { #pinname-3 }

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

#### PinType { #pintype-2 }

```cpp
EComposableCameraPinType PinType = 
```

Data type carried by this pin.

---

#### StructType { #structtype-2 }

```cpp
UScriptStruct * StructType = nullptr
```

For PinType == Struct: the specific USTRUCT type. Ignored for other pin types.

---

#### bRequired { #brequired-1 }

```cpp
bool bRequired = false
```

Whether this input is required. If true, the editor shows an error when the pin is neither wired nor exposed and has no default value. Ignored for output pins.

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
