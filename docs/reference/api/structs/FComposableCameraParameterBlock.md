
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
| `TMap< FName, TObjectPtr< AActor > >` | [`ActorValues`](#actorvalues)  | GC-visible owners for object-valued entries mirrored in Values. |
| `TMap< FName, TObjectPtr< UObject > >` | [`ObjectValues`](#objectvalues)  | GC-visible owners for object-valued entries mirrored in Values. |
| `TMap< FName, FScriptDelegate >` | [`DelegateValues`](#delegatevalues)  | Parallel storage for single-cast delegate bindings. Delegates are not POD and cannot be stored in the byte-array-based [FComposableCameraParameterValue](FComposableCameraParameterValue.md#fcomposablecameraparametervalue). They are applied at activation time via ApplyDelegateBindings (on the type asset), which writes them into the target node's FDelegateProperty UPROPERTY via reflection. |
| `TMap< FName, FInstancedStruct >` | [`StructValues`](#structvalues)  | Parallel storage for non-POD struct values (USTRUCTs containing FString / FText / TArray / object refs / delegates &ndash; anything `IsBytewiseSafeStruct` rejects). The byte-array `Values` map cannot transport these because raw memcpy aliases heap-owned storage and makes the GC blind to embedded references; FInstancedStruct owns its memory, runs proper constructors / destructors, and surfaces UObject references via AddStructReferencedObjects. POD struct values (FVector / FRotator / FTransform / etc.) still go through the byte-array `Values` map &ndash; they're memcpy-safe and the existing offset tables in RuntimeDataBlock are tighter. |

---

#### Values { #values }

```cpp
TMap< FName, FComposableCameraParameterValue > Values
```

Type-erased parameter storage, keyed by parameter name. POD-only — delegates are stored in DelegateValues instead.

---

#### ActorValues { #actorvalues }

```cpp
TMap< FName, TObjectPtr< AActor > > ActorValues
```

GC-visible owners for object-valued entries mirrored in Values.

---

#### ObjectValues { #objectvalues }

```cpp
TMap< FName, TObjectPtr< UObject > > ObjectValues
```

GC-visible owners for object-valued entries mirrored in Values.

---

#### DelegateValues { #delegatevalues }

```cpp
TMap< FName, FScriptDelegate > DelegateValues
```

Parallel storage for single-cast delegate bindings. Delegates are not POD and cannot be stored in the byte-array-based [FComposableCameraParameterValue](FComposableCameraParameterValue.md#fcomposablecameraparametervalue). They are applied at activation time via ApplyDelegateBindings (on the type asset), which writes them into the target node's FDelegateProperty UPROPERTY via reflection.

---

#### StructValues { #structvalues }

```cpp
TMap< FName, FInstancedStruct > StructValues
```

Parallel storage for non-POD struct values (USTRUCTs containing FString / FText / TArray / object refs / delegates &ndash; anything `IsBytewiseSafeStruct` rejects). The byte-array `Values` map cannot transport these because raw memcpy aliases heap-owned storage and makes the GC blind to embedded references; FInstancedStruct owns its memory, runs proper constructors / destructors, and surfaces UObject references via AddStructReferencedObjects. POD struct values (FVector / FRotator / FTransform / etc.) still go through the byte-array `Values` map &ndash; they're memcpy-safe and the existing offset tables in RuntimeDataBlock are tighter.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`Reserve`](#reserve) `inline` |  |
| `void` | [`RemoveValue`](#removevalue) `inline` | Drop any value stored under Name across every storage class (Values / ActorValues / ObjectValues / StructValues / DelegateValues). After this call, `HasValue(Name)` returns false and downstream reads fall through to the type asset's authored default. |
| `void` | [`StoreValue`](#storevalue) `inline` |  |
| `void` | [`SetStruct`](#setstruct) `inline` | Set a non-POD struct parameter. The struct is copied into a fresh FInstancedStruct via InitializeAs(StructType, Memory), which runs the proper per-property copy (FString operator=, TArray copy, UObject ptr etc.) and owns the result for the lifetime of this map entry. The parallel `Values` / `ActorValues` / `ObjectValues` / `DelegateValues` entries under the same Name are cleared so a subsequent Get-by-name cannot read a stale POD-shaped entry for what is now a struct value. |
| `void` | [`AddReferencedObjects`](#addreferencedobjects-4)  |  |
| `void` | [`AddStructReferencedObjects`](#addstructreferencedobjects) `const` `inline` | Engine reflection hook — called automatically by `AddPropertyReferencesWithStructARO` (and any UPROPERTY-driven GC walk that reaches this struct) once the matching `TStructOpsTypeTraits` opt-in is declared below. Without this hook, embedding the struct as a UPROPERTY (`[UComposableCameraPatchInstance::CachedParameters](../uobjects-other/UComposableCameraPatchInstance.md#cachedparameters)`, `[UComposableCameraLevelSequenceComponent](../uobjects-other/UComposableCameraLevelSequenceComponent.md#ucomposablecameralevelsequencecomponent)` overlay surfaces, ...) only walked the struct's reflected fields — `ActorValues` / `ObjectValues` / `StructValues` are `UPROPERTY` so reflection sees them, but `DelegateValues` is non-`UPROPERTY` and the `FScriptDelegate`'s bound target's strong-mark step (see `AddReferencedObjects` body) was therefore unreachable from any reflection-driven owner. Same hole for the `StructValues`-side `UScriptStruct` mark: reflection walks members, not type identity. Routing through `AddReferencedObjects` closes both gaps. |
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
| `bool` | [`HasValue`](#hasvalue) `const` `inline` | Check if a parameter exists by name (POD / actor / object / struct / delegate). |
| `bool` | [`Get`](#get-1) `const` `inline` | Try to get a typed value. Returns false if not found or type mismatch. |
| `int32` | [`CopyRawTo`](#copyrawto) `const` `inline` | Copy a parameter's raw bytes into a destination buffer, with strict PinType + exact-size validation. |

---

#### Reserve { #reserve }

`inline`

```cpp
inline void Reserve(int32 Num)
```

---

#### RemoveValue { #removevalue }

`inline`

```cpp
inline void RemoveValue(FName Name)
```

Drop any value stored under Name across every storage class (Values / ActorValues / ObjectValues / StructValues / DelegateValues). After this call, `HasValue(Name)` returns false and downstream reads fall through to the type asset's authored default.

Used by failure paths in `SetStruct` so a refused setter call does not silently leave a previous-shape stale value live under the same name — the contract is "failed setter = no value here", not "old value
preserved". Public so callers that want to explicitly clear a slot (e.g. a designer-driven "reset to default" affordance) have a single entry point that handles all five maps.

---

#### StoreValue { #storevalue }

`inline`

```cpp
inline void StoreValue(FName Name, FComposableCameraParameterValue && Entry)
```

---

#### SetStruct { #setstruct }

`inline`

```cpp
inline void SetStruct(FName Name, const UScriptStruct * Struct, const void * Memory)
```

Set a non-POD struct parameter. The struct is copied into a fresh FInstancedStruct via InitializeAs(StructType, Memory), which runs the proper per-property copy (FString operator=, TArray copy, UObject ptr etc.) and owns the result for the lifetime of this map entry. The parallel `Values` / `ActorValues` / `ObjectValues` / `DelegateValues` entries under the same Name are cleared so a subsequent Get-by-name cannot read a stale POD-shaped entry for what is now a struct value.

---

#### AddReferencedObjects { #addreferencedobjects-4 }

```cpp
void AddReferencedObjects(FReferenceCollector & Collector)
```

---

#### AddStructReferencedObjects { #addstructreferencedobjects }

`const` `inline`

```cpp
inline void AddStructReferencedObjects(FReferenceCollector & Collector) const
```

Engine reflection hook — called automatically by `AddPropertyReferencesWithStructARO` (and any UPROPERTY-driven GC walk that reaches this struct) once the matching `TStructOpsTypeTraits` opt-in is declared below. Without this hook, embedding the struct as a UPROPERTY (`[UComposableCameraPatchInstance::CachedParameters](../uobjects-other/UComposableCameraPatchInstance.md#cachedparameters)`, `[UComposableCameraLevelSequenceComponent](../uobjects-other/UComposableCameraLevelSequenceComponent.md#ucomposablecameralevelsequencecomponent)` overlay surfaces, ...) only walked the struct's reflected fields — `ActorValues` / `ObjectValues` / `StructValues` are `UPROPERTY` so reflection sees them, but `DelegateValues` is non-`UPROPERTY` and the `FScriptDelegate`'s bound target's strong-mark step (see `AddReferencedObjects` body) was therefore unreachable from any reflection-driven owner. Same hole for the `StructValues`-side `UScriptStruct` mark: reflection walks members, not type identity. Routing through `AddReferencedObjects` closes both gaps.

Const because the trait expects `const`; the implementation `const_cast`s through to the non-const `AddReferencedObjects` since `FReferenceCollector::AddReferencedObject` needs a mutable `TObjectPtr<>&` reference.

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

Check if a parameter exists by name (POD / actor / object / struct / delegate).

---

#### Get { #get-1 }

`const` `inline`

```cpp
template<typename T> inline bool Get(FName Name, T & OutValue) const
```

Try to get a typed value. Returns false if not found or type mismatch.

---

#### CopyRawTo { #copyrawto }

`const` `inline`

```cpp
inline int32 CopyRawTo(FName Name, uint8 * Dest, int32 DestSize, EComposableCameraPinType ExpectedPinType) const
```

Copy a parameter's raw bytes into a destination buffer, with strict PinType + exact-size validation.

Returns the number of bytes copied (== DestSize on success), or 0 on any of: parameter not found, PinType mismatch, Data.Num() != DestSize.

Strict validation rationale: the prior signature accepted any source size `<= DestSize` and silently memcpy'd. A stale row entry that stored a Float (4 B Data) under a name now bound to an Actor target slot (8 B Dest) landed 4 bytes of float data in the lower half of the slot and left the upper 4 bytes whatever was already there; the immediately following `RefreshReferenceSlot` reinterpreted the result as `AActor*` and registered a fake pointer with the GC mirror — next sweep crashed. Equality-on-size plus a PinType match forces a clean miss for any shape-wrong entry, and the caller's existing zero-init of the destination keeps the slot empty rather than half-populated.

PinType match is sufficient for most types because PinType pins down storage size for primitives / vectors / Actor / Object / Name. For Struct and Enum the additional shape (StructType / EnumType) is metadata the caller carries; layout-phase validation in `BuildRuntimeDataLayout` handles those, so this hot-path check only needs PinType + size to catch the cross-shape case the reviewer reported.

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
