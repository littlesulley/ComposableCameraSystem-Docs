
# FComposableCameraParameterBlock { #fcomposablecameraparameterblock }

```cpp
#include <ComposableCameraParameterBlock.h>
```

Container for parameter values passed by callers when activating a camera from a type asset.

The K2Node fills this automatically from its dynamic pins. C++ callers fill it manually. DataTable callers fill it by parsing row data.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TMap< FName, FComposableCameraParameterValue >` | [`Values`](#values)  | Type-erased parameter storage, keyed by parameter name. |

---

#### Values { #values }

```cpp
TMap< FName, FComposableCameraParameterValue > Values
```

Type-erased parameter storage, keyed by parameter name.

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
| `bool` | [`HasValue`](#hasvalue) `const` `inline` | Check if a parameter exists by name. |
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

#### HasValue { #hasvalue }

`const` `inline`

```cpp
inline bool HasValue(FName Name) const
```

Check if a parameter exists by name.

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
static bool ApplyStringValue(FComposableCameraParameterBlock & OutBlock, FName ParameterName, EComposableCameraPinType PinType, UScriptStruct * StructType, const FString & ValueString, FString * OutError)
```

Parse a serialized string into a typed entry and store it under ParameterName.

This is the single string→typed-value entry point shared by the DataTable activation path and the DataTable row property-type customization. The two sides must round-trip through the same parser so that anything you can type in the editor is accepted identically at runtime.

Supported types: Bool, Int32, Float, Double — LexFromString Vector2D/3D/4, Rotator, Transform — ImportText on the matching core struct Struct — ImportText on the provided StructType Object — resolved via FSoftObjectPath and sync-loaded

Unsupported (returns false, writes OutError): Actor — actors are world-scoped and cannot be resolved from a DataTable asset. Use Object with a soft path to a CDO/archetype instead if you need a class reference.

**Parameters**
* `OutBlock` Parameter block to write into. 

* `ParameterName` Key the entry is stored under in OutBlock.Values. 

* `PinType` Target pin type — dispatches the parse branch. 

* `StructType` Only read when PinType == Struct; ignored otherwise. 

* `ValueString` The serialized value. Empty input is treated as a parse failure so callers can decide whether to fall back to the node pin's authored default. 

* `OutError` Optional human-readable error written on failure. 

**Returns**
true on success, false otherwise. On failure the OutBlock is left untouched for this key.
