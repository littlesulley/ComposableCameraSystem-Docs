
# FComposableCameraParameterBlock { #fcomposablecameraparameterblock }

```cpp
#include <ComposableCameraParameterBlock.h>
```

Container for parameter values passed by callers when activating a camera from a type asset.

The K2Node fills this automatically from its dynamic pins. C++ callers fill it manually. DataTable callers fill it by parsing row data.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TMap< FName, FComposableCameraParameterValue >` | [`Values`](#values)  | Type-erased parameter storage, keyed by parameter name. POD-only — delegates are stored in DelegateValues instead. |
| `TMap< FName, FScriptDelegate >` | [`DelegateValues`](#delegatevalues)  | Parallel storage for single-cast delegate bindings. Delegates are not POD and cannot be stored in the byte-array-based [FComposableCameraParameterValue](FComposableCameraParameterValue.md#fcomposablecameraparametervalue). They are applied at activation time via ApplyDelegateBindings (on the type asset), which writes them into the target node's FDelegateProperty UPROPERTY via reflection. |

---

#### Values { #values }

```cpp
TMap< FName, FComposableCameraParameterValue > Values
```

Type-erased parameter storage, keyed by parameter name. POD-only — delegates are stored in DelegateValues instead.

---

#### DelegateValues { #delegatevalues }

```cpp
TMap< FName, FScriptDelegate > DelegateValues
```

Parallel storage for single-cast delegate bindings. Delegates are not POD and cannot be stored in the byte-array-based [FComposableCameraParameterValue](FComposableCameraParameterValue.md#fcomposablecameraparametervalue). They are applied at activation time via ApplyDelegateBindings (on the type asset), which writes them into the target node's FDelegateProperty UPROPERTY via reflection.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`SetBool`](#setbool) `inline` | Set a bool parameter. |
| `void` | [`SetInt32`](#setint32) `inline` | Set an int32 parameter. |
| `void` | [`SetFloat`](#setfloat) `inline` | Set a float parameter. |
| `void` | [`SetDouble`](#setdouble) `inline` | Set a double parameter. |
| `void` | [`SetVector`](#setvector) `inline` | Set a Vector parameter. |
| `void` | [`SetRotator`](#setrotator) `inline` | Set a Rotator parameter. |
| `void` | [`SetTransform`](#settransform) `inline` | Set a Transform parameter. |
| `void` | [`SetActor`](#setactor) `inline` | Set an Actor pointer parameter. |
| `void` | [`SetObject`](#setobject) `inline` | Set a UObject pointer parameter. |
| `void` | [`SetName`](#setname) `inline` | Set an FName parameter. FName is POD (NAME_INDEX + NAME_NUMBER, 8 bytes) and is memcpy-safe in the type-erased data storage. |
| `void` | [`SetEnum`](#setenum) `inline` | Set an enum parameter. Enums are always normalized to int64 in the data storage, regardless of the backing property's actual underlying width. The narrow-cast into the final storage happens at resolve time, where the owning FProperty is known (see WriteEnumInt64ToProperty). |
| `void` | [`SetDelegate`](#setdelegate) `inline` | Set a single-cast delegate binding. The delegate is stored in a parallel map (not the POD byte array) and applied at activation time via ApplyDelegateBindings on the type asset. |
| `bool` | [`HasValue`](#hasvalue) `const` `inline` | Check if a parameter exists by name (either POD or delegate). |
| `bool` | [`Get`](#get) `const` `inline` | Try to get a typed value. Returns false if not found or type mismatch. |
| `int32` | [`CopyRawTo`](#copyrawto) `const` `inline` | Copy a parameter's raw bytes into a destination buffer. Returns the number of bytes copied, or 0 if not found. |

---

#### SetBool { #setbool }

`inline`

```cpp
inline void SetBool(FName Name, bool Value)
```

Set a bool parameter.

---

#### SetInt32 { #setint32 }

`inline`

```cpp
inline void SetInt32(FName Name, int32 Value)
```

Set an int32 parameter.

---

#### SetFloat { #setfloat }

`inline`

```cpp
inline void SetFloat(FName Name, float Value)
```

Set a float parameter.

---

#### SetDouble { #setdouble }

`inline`

```cpp
inline void SetDouble(FName Name, double Value)
```

Set a double parameter.

---

#### SetVector { #setvector }

`inline`

```cpp
inline void SetVector(FName Name, const FVector & Value)
```

Set a Vector parameter.

---

#### SetRotator { #setrotator }

`inline`

```cpp
inline void SetRotator(FName Name, const FRotator & Value)
```

Set a Rotator parameter.

---

#### SetTransform { #settransform }

`inline`

```cpp
inline void SetTransform(FName Name, const FTransform & Value)
```

Set a Transform parameter.

---

#### SetActor { #setactor }

`inline`

```cpp
inline void SetActor(FName Name, AActor * Value)
```

Set an Actor pointer parameter.

---

#### SetObject { #setobject }

`inline`

```cpp
inline void SetObject(FName Name, UObject * Value)
```

Set a UObject pointer parameter.

---

#### SetName { #setname }

`inline`

```cpp
inline void SetName(FName Name, FName Value)
```

Set an FName parameter. FName is POD (NAME_INDEX + NAME_NUMBER, 8 bytes) and is memcpy-safe in the type-erased data storage.

---

#### SetEnum { #setenum }

`inline`

```cpp
inline void SetEnum(FName Name, int64 Value)
```

Set an enum parameter. Enums are always normalized to int64 in the data storage, regardless of the backing property's actual underlying width. The narrow-cast into the final storage happens at resolve time, where the owning FProperty is known (see WriteEnumInt64ToProperty).

---

#### SetDelegate { #setdelegate }

`inline`

```cpp
inline void SetDelegate(FName Name, const FScriptDelegate & Value)
```

Set a single-cast delegate binding. The delegate is stored in a parallel map (not the POD byte array) and applied at activation time via ApplyDelegateBindings on the type asset.

---

#### HasValue { #hasvalue }

`const` `inline`

```cpp
inline bool HasValue(FName Name) const
```

Check if a parameter exists by name (either POD or delegate).

---

#### Get { #get }

`const` `inline`

```cpp
template<typename T> inline bool Get(FName Name, T & OutValue) const
```

Try to get a typed value. Returns false if not found or type mismatch.

---

#### CopyRawTo { #copyrawto }

`const` `inline`

```cpp
inline int32 CopyRawTo(FName Name, uint8 * Dest, int32 DestSize) const
```

Copy a parameter's raw bytes into a destination buffer. Returns the number of bytes copied, or 0 if not found.

### Public Static Methods

| Return | Name | Description |
|--------|------|-------------|
| `bool` | [`ApplyStringValue`](#applystringvalue) `static` | Parse a serialized string into a typed entry and store it under ParameterName. |

---

#### ApplyStringValue { #applystringvalue }

`static`

```cpp
static bool ApplyStringValue(FComposableCameraParameterBlock & OutBlock, FName ParameterName, EComposableCameraPinType PinType, UScriptStruct * StructType, UEnum * EnumType, const FString & ValueString, FString * OutError)
```

Parse a serialized string into a typed entry and store it under ParameterName.

This is the single string→typed-value entry point shared by the DataTable activation path and the DataTable row property-type customization. The two sides must round-trip through the same parser so that anything you can type in the editor is accepted identically at runtime.

Supported types: Bool, Int32, Float, Double — LexFromString Vector2D/3D/4, Rotator, Transform — ImportText on the matching core struct Struct — ImportText on the provided StructType Object — resolved via FSoftObjectPath and sync-loaded Name — FName::FromString (no Unicode canonicalization) Enum — UEnum::GetValueByNameString, stored as int64

Unsupported (returns false, writes OutError): Actor — actors are world-scoped and cannot be resolved from a DataTable asset. Use Object with a soft path to a CDO/archetype instead if you need a class reference.

**Parameters**

* `OutBlock` Parameter block to write into. 

* `ParameterName` Key the entry is stored under in OutBlock.Values. 

* `PinType` Target pin type — dispatches the parse branch. 

* `StructType` Only read when PinType == Struct; ignored otherwise. 

* `EnumType` Only read when PinType == Enum; ignored otherwise. Used to parse the display / authored name back to an int64 value (UEnum::GetValueByNameString). 

* `ValueString` The serialized value. Empty input is treated as a parse failure so callers can decide whether to fall back to the node pin's authored default. 

* `OutError` Optional human-readable error written on failure. 

**Returns**

true on success, false otherwise. On failure the OutBlock is left untouched for this key.
