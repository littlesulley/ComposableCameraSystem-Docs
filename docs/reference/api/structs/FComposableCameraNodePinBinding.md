
# FComposableCameraNodePinBinding { #fcomposablecameranodepinbinding }

```cpp
#include <ComposableCameraCameraNodeBase.h>
```

Cached description of a single pin ↔ UPROPERTY binding on a camera node class.

Produced once per concrete UClass by UComposableCameraCameraNodeBase::GetOrBuildPinBindings() and reused by every instance of that class to resolve declared input pins without per-frame reflection. Bindings are indexed by raw byte offset into the node UObject, not by FProperty*, so the hot path is a straight pointer + switch.

Only top-level pins matched to a top-level UPROPERTY on the node are recorded here. Subobject property pins (compound "Subobject.Field" names) are still handled by ApplySubobjectPinValues and are NOT included.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FName` | [`PinName`](#pinname-3)  | Pin name as declared in GetPinDeclarations and matched against a UPROPERTY FName. |
| `EComposableCameraPinType` | [`PinType`](#pintype)  | Pin type for typed dispatch at resolve time. |
| `UScriptStruct *` | [`StructType`](#structtype)  | For PinType == Struct: the specific USTRUCT type. Ignored otherwise. |
| `TWeakObjectPtr< UEnum >` | [`EnumType`](#enumtype)  | For PinType == Enum: the specific UEnum the pin represents. Ignored otherwise. The data block stores the value as a normalized int64; we use the backing FProperty (by offset) to narrow-cast into the actual storage width (uint8 / int32 / int64) at write time. Held as a weak ref so we don't keep the enum alive via a non-UPROPERTY cache. |
| `const FProperty *` | [`BackingProperty`](#backingproperty)  | For PinType == Enum: the backing FProperty, captured when the binding table is built. Used to narrow-cast the int64 value from the data block into the property's actual underlying width. nullptr for non-Enum pins. |
| `int32` | [`FieldOffset`](#fieldoffset)  | Byte offset of the backing UPROPERTY into the node UObject (via FProperty::GetOffset_ForInternal). |

---

#### PinName { #pinname-3 }

```cpp
FName PinName
```

Pin name as declared in GetPinDeclarations and matched against a UPROPERTY FName.

---

#### PinType { #pintype }

```cpp
EComposableCameraPinType PinType = 
```

Pin type for typed dispatch at resolve time.

---

#### StructType { #structtype }

```cpp
UScriptStruct * StructType = nullptr
```

For PinType == Struct: the specific USTRUCT type. Ignored otherwise.

---

#### EnumType { #enumtype }

```cpp
TWeakObjectPtr< UEnum > EnumType
```

For PinType == Enum: the specific UEnum the pin represents. Ignored otherwise. The data block stores the value as a normalized int64; we use the backing FProperty (by offset) to narrow-cast into the actual storage width (uint8 / int32 / int64) at write time. Held as a weak ref so we don't keep the enum alive via a non-UPROPERTY cache.

---

#### BackingProperty { #backingproperty }

```cpp
const FProperty * BackingProperty = nullptr
```

For PinType == Enum: the backing FProperty, captured when the binding table is built. Used to narrow-cast the int64 value from the data block into the property's actual underlying width. nullptr for non-Enum pins.

---

#### FieldOffset { #fieldoffset }

```cpp
int32 FieldOffset = 0
```

Byte offset of the backing UPROPERTY into the node UObject (via FProperty::GetOffset_ForInternal).
