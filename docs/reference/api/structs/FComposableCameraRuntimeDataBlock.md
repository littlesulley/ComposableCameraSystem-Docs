
# FComposableCameraRuntimeDataBlock { #fcomposablecameraruntimedatablock }

```cpp
#include <ComposableCameraRuntimeDataBlock.h>
```

Flat, contiguous memory block that holds all pin output values, exposed parameter values, internal variable values, and per-instance input pin default values for a single camera instance at runtime.

The layout is computed once from the camera type asset's pin declarations, connections, exposed parameters, internal variables, and per-instance pin overrides. All access is offset-based for performance.

Memory layout: [Output pin slots][Exposed parameter slots][Per-instance default slots][Internal variable slots]

Each slot is aligned to the type's natural alignment. The per-instance default slots mirror the authoring-layer [FComposableCameraPinOverride::DefaultValueOverride](FComposableCameraPinOverride.md#defaultvalueoverride) values (see [Nodes/ComposableCameraNodePinTypes.h](#composablecameranodepintypesh)) pre-parsed into typed bytes so the per-frame resolution path in TryResolveInputPin is a pure pointer lookup — no string parsing on the hot path.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TArray< uint8 >` | [`Storage`](#storage)  | Raw storage buffer. Allocated once during camera instantiation. POD pin values live here at real byte offsets; non-POD struct values live in StructSlots below at synthetic offsets >= StructSlotsOffsetBase. |
| `TArray< FInstancedStruct >` | [`StructSlots`](#structslots)  | Typed storage for non-POD struct slots (ExposedParameter / ExposedVariable / InternalVariable / OutputPin / DefaultValue per-instance override of a USTRUCT containing FString / FText / TArray / TMap / TSet / object refs / delegates &ndash; anything `IsBytewiseSafeStruct` rejects). |
| `TMap< FComposableCameraPinKey, int32 >` | [`OutputPinOffsets`](#outputpinoffsets)  | Lookup: (NodeIndex, PinName) for OUTPUT pins → byte offset in Storage. |
| `TMap< FName, int32 >` | [`ExposedParameterOffsets`](#exposedparameteroffsets)  | Lookup: ExposedParameterName → byte offset in Storage. |
| `TMap< FName, int32 >` | [`InternalVariableOffsets`](#internalvariableoffsets)  | Lookup: InternalVariableName → byte offset in Storage. |
| `TMap< int32, TObjectPtr< AActor > >` | [`ActorReferenceSlots`](#actorreferenceslots)  | Object-reference slots mirrored from raw storage for explicit GC collection. |
| `TMap< int32, TObjectPtr< UObject > >` | [`ObjectReferenceSlots`](#objectreferenceslots)  | Object-reference slots mirrored from raw storage for explicit GC collection. |
| `TMap< FComposableCameraPinKey, int32 >` | [`InputPinSourceOffsets`](#inputpinsourceoffsets)  | Connection table: for each input pin, the offset of its source data. Key = (TargetNodeIndex, TargetPinName), Value = offset in Storage where the source output pin wrote its data. |
| `TMap< FComposableCameraPinKey, int32 >` | [`ExposedInputPinOffsets`](#exposedinputpinoffsets)  | Exposure table: for each exposed input pin, the offset of the parameter slot. Key = (TargetNodeIndex, TargetPinName), Value = offset of the exposed parameter in Storage. |
| `TMap< FComposableCameraPinKey, int32 >` | [`DefaultValueOffsets`](#defaultvalueoffsets)  | Per-instance default-value table: for each input pin that has an authored [FComposableCameraPinOverride::DefaultValueOverride](FComposableCameraPinOverride.md#defaultvalueoverride) (see [Nodes/ComposableCameraNodePinTypes.h](#composablecameranodepintypesh)), the offset of the slot holding the pre-parsed typed bytes. Key = (TargetNodeIndex, PinName), Value = offset in Storage. |
| `int32` | [`TotalSize`](#totalsize)  | Total allocated size. |

---

#### Storage { #storage }

```cpp
TArray< uint8 > Storage
```

Raw storage buffer. Allocated once during camera instantiation. POD pin values live here at real byte offsets; non-POD struct values live in StructSlots below at synthetic offsets >= StructSlotsOffsetBase.

---

#### StructSlots { #structslots }

```cpp
TArray< FInstancedStruct > StructSlots
```

Typed storage for non-POD struct slots (ExposedParameter / ExposedVariable / InternalVariable / OutputPin / DefaultValue per-instance override of a USTRUCT containing FString / FText / TArray / TMap / TSet / object refs / delegates &ndash; anything `IsBytewiseSafeStruct` rejects).

Each entry is owned (proper ctor / dtor) and GC-walked via AddPropertyReferencesWithStructARO in AddReferencedObjects. The various offset tables below (OutputPinOffsets, ExposedParameterOffsets, etc.) store synthetic offsets >= StructSlotsOffsetBase for non-POD struct entries; the dispatch in ReadValue / WriteValue / TryResolveInputPin detects this and routes to StructSlots[Offset - StructSlotsOffsetBase] instead of memcpying out of Storage.

Activation-time: BuildRuntimeDataLayout pre-allocates one slot per non-POD struct entry via InitializeAs(StructType). Per-frame copy-in (ApplyParameterBlock, WriteOutputPin, CopySlot) reuses the slot's existing memory via CopyScriptStruct &ndash; bounded one-time alloc when embedded FString members grow, no alloc when they fit existing capacity.

---

#### OutputPinOffsets { #outputpinoffsets }

```cpp
TMap< FComposableCameraPinKey, int32 > OutputPinOffsets
```

Lookup: (NodeIndex, PinName) for OUTPUT pins → byte offset in Storage.

---

#### ExposedParameterOffsets { #exposedparameteroffsets }

```cpp
TMap< FName, int32 > ExposedParameterOffsets
```

Lookup: ExposedParameterName → byte offset in Storage.

---

#### InternalVariableOffsets { #internalvariableoffsets }

```cpp
TMap< FName, int32 > InternalVariableOffsets
```

Lookup: InternalVariableName → byte offset in Storage.

---

#### ActorReferenceSlots { #actorreferenceslots }

```cpp
TMap< int32, TObjectPtr< AActor > > ActorReferenceSlots
```

Object-reference slots mirrored from raw storage for explicit GC collection.

---

#### ObjectReferenceSlots { #objectreferenceslots }

```cpp
TMap< int32, TObjectPtr< UObject > > ObjectReferenceSlots
```

Object-reference slots mirrored from raw storage for explicit GC collection.

---

#### InputPinSourceOffsets { #inputpinsourceoffsets }

```cpp
TMap< FComposableCameraPinKey, int32 > InputPinSourceOffsets
```

Connection table: for each input pin, the offset of its source data. Key = (TargetNodeIndex, TargetPinName), Value = offset in Storage where the source output pin wrote its data.

---

#### ExposedInputPinOffsets { #exposedinputpinoffsets }

```cpp
TMap< FComposableCameraPinKey, int32 > ExposedInputPinOffsets
```

Exposure table: for each exposed input pin, the offset of the parameter slot. Key = (TargetNodeIndex, TargetPinName), Value = offset of the exposed parameter in Storage.

---

#### DefaultValueOffsets { #defaultvalueoffsets }

```cpp
TMap< FComposableCameraPinKey, int32 > DefaultValueOffsets
```

Per-instance default-value table: for each input pin that has an authored [FComposableCameraPinOverride::DefaultValueOverride](FComposableCameraPinOverride.md#defaultvalueoverride) (see [Nodes/ComposableCameraNodePinTypes.h](#composablecameranodepintypesh)), the offset of the slot holding the pre-parsed typed bytes. Key = (TargetNodeIndex, PinName), Value = offset in Storage.

This is ranked below InputPinSourceOffsets (wired) and ExposedInputPinOffsets (exposed-as-parameter) by TryResolveInputPin. It exists so that per-frame default resolution is a pointer-lookup / memcpy instead of a string-parse, honoring the "no hot-path allocations" rule.

Pins without an authored override are simply absent from this map; their default is resolved by the node's own class-level fallback (e.g. a UPROPERTY on the node template) when TryResolveInputPin returns false.

---

#### TotalSize { #totalsize }

```cpp
int32 TotalSize = 0
```

Total allocated size.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `bool` | [`IsStructSlotOffset`](#isstructslotoffset) `const` `inline` | True if Offset addresses a non-POD struct slot in StructSlots. |
| `int32` | [`GetStructSlotIndex`](#getstructslotindex) `const` `inline` | Convert a synthetic offset to its StructSlots index. |
| `int32` | [`RegisterStructSlot`](#registerstructslot) `inline` | Reserve a fresh struct slot pre-initialized for StructType, returning the synthetic offset that should be stored in the relevant offset table (ExposedParameterOffsets / OutputPinOffsets / etc.). Called once per non-POD struct entry by BuildRuntimeDataLayout. |
| `T` | [`ReadValue`](#readvalue) `const` `inline` | Read a typed value from the storage at the given byte offset. POD path: memcpy out of Storage. Non-POD struct path (T is a USTRUCT and Offset >= StructSlotsOffsetBase): CopyScriptStruct out of the typed slot in StructSlots. |
| `void` | [`WriteValue`](#writevalue) `inline` | Write a typed value to the storage at the given byte offset. POD path: memcpy into Storage. Non-POD struct path: CopyScriptStruct into the existing struct slot's owned memory &ndash; no allocation unless an embedded FString grows beyond its existing capacity (see TechDoc.md §7.2 alloc characteristic). |
| `T` | [`ReadOutputPin`](#readoutputpin) `const` `inline` | Read a value for a specific output pin. |
| `void` | [`WriteOutputPin`](#writeoutputpin) `inline` | Write a value for a specific output pin. |
| `bool` | [`TryResolveInputPin`](#tryresolveinputpin) `const` `inline` | Resolve an input pin's value. Checks in order: |
| `bool` | [`ResolveInputPinOffset`](#resolveinputpinoffset) `const` `inline` | Resolve an input pin to its source slot offset using the same three-tier priority as TryResolveInputPin (wired -> exposed -> per-instance default), but without copying the value out &ndash; useful for non-templated paths (auto-resolve Struct case, struct subobject pin dispatch) that need to decide between byte storage and FInstancedStruct slot at runtime. Returns true and writes OutOffset when a slot is found. |
| `T` | [`ReadInternalVariable`](#readinternalvariable) `const` `inline` | Read an internal variable by name. |
| `void` | [`WriteInternalVariable`](#writeinternalvariable) `inline` | Write an internal variable by name. |
| `bool` | [`HasInternalVariable`](#hasinternalvariable) `const` `inline` | Check if a specific internal variable exists. |
| `void` | [`CopySlot`](#copyslot) `inline` | Copy raw bytes from one slot to another within the same storage. Used by the exec-chain SetVariable dispatch to transfer a source node's output pin value into an internal variable slot without knowing the concrete C++ type at compile time. |
| `const FInstancedStruct &` | [`GetStructSlotChecked`](#getstructslotchecked) `const` `inline` | Direct access to the FInstancedStruct backing a non-POD struct slot. Used by auto-resolve / subobject-pin code paths whose dispatch happens on a runtime EComposableCameraPinType value (not a compile-time T) &ndash; the templated ReadValue<T> path is preferred when T is known. Asserts the offset is in fact a struct slot. |
| `FInstancedStruct &` | [`GetStructSlotMutableChecked`](#getstructslotmutablechecked) `inline` |  |
| `void` | [`RegisterReferenceSlot`](#registerreferenceslot)  |  |
| `void` | [`RefreshReferenceSlot`](#refreshreferenceslot)  |  |
| `void` | [`RefreshAllReferenceSlots`](#refreshallreferenceslots)  |  |
| `void` | [`AddReferencedObjects`](#addreferencedobjects-4)  |  |
| `bool` | [`IsValid`](#isvalid) `const` `inline` | Check if storage has been allocated. |
| `void` | [`ZeroInitialize`](#zeroinitialize) `inline` | Zero-initialize all storage. Called at allocation time. |

---

#### IsStructSlotOffset { #isstructslotoffset }

`const` `inline`

```cpp
inline bool IsStructSlotOffset(int32 Offset) const
```

True if Offset addresses a non-POD struct slot in StructSlots.

---

#### GetStructSlotIndex { #getstructslotindex }

`const` `inline`

```cpp
inline int32 GetStructSlotIndex(int32 Offset) const
```

Convert a synthetic offset to its StructSlots index.

---

#### RegisterStructSlot { #registerstructslot }

`inline`

```cpp
inline int32 RegisterStructSlot(const UScriptStruct * StructType)
```

Reserve a fresh struct slot pre-initialized for StructType, returning the synthetic offset that should be stored in the relevant offset table (ExposedParameterOffsets / OutputPinOffsets / etc.). Called once per non-POD struct entry by BuildRuntimeDataLayout.

---

#### ReadValue { #readvalue }

`const` `inline`

```cpp
template<typename T> inline T ReadValue(int32 Offset) const
```

Read a typed value from the storage at the given byte offset. POD path: memcpy out of Storage. Non-POD struct path (T is a USTRUCT and Offset >= StructSlotsOffsetBase): CopyScriptStruct out of the typed slot in StructSlots.

---

#### WriteValue { #writevalue }

`inline`

```cpp
template<typename T> inline void WriteValue(int32 Offset, const T & Value)
```

Write a typed value to the storage at the given byte offset. POD path: memcpy into Storage. Non-POD struct path: CopyScriptStruct into the existing struct slot's owned memory &ndash; no allocation unless an embedded FString grows beyond its existing capacity (see TechDoc.md §7.2 alloc characteristic).

---

#### ReadOutputPin { #readoutputpin }

`const` `inline`

```cpp
template<typename T> inline T ReadOutputPin(int32 NodeIndex, FName PinName) const
```

Read a value for a specific output pin.

---

#### WriteOutputPin { #writeoutputpin }

`inline`

```cpp
template<typename T> inline void WriteOutputPin(int32 NodeIndex, FName PinName, const T & Value)
```

Write a value for a specific output pin.

---

#### TryResolveInputPin { #tryresolveinputpin }

`const` `inline`

```cpp
template<typename T> inline bool TryResolveInputPin(int32 NodeIndex, FName PinName, T & OutValue) const
```

Resolve an input pin's value. Checks in order:

1. Wired connection (InputPinSourceOffsets)

1. Exposed parameter (ExposedInputPinOffsets)

1. Per-instance default override (DefaultValueOffsets) — authoring-layer [FComposableCameraPinOverride::DefaultValueOverride](FComposableCameraPinOverride.md#defaultvalueoverride), pre-parsed by BuildRuntimeDataLayout.

1. Returns false if none of the above are found. Callers with a class-level fallback (e.g. a UPROPERTY on the node template) should read it in the false branch; see [UComposableCameraFieldOfViewNode::OnTickNode](../uobjects-other/UComposableCameraCameraNodeBase.md#onticknode) for the canonical pattern.

---

#### ResolveInputPinOffset { #resolveinputpinoffset }

`const` `inline`

```cpp
inline bool ResolveInputPinOffset(int32 NodeIndex, FName PinName, int32 & OutOffset) const
```

Resolve an input pin to its source slot offset using the same three-tier priority as TryResolveInputPin (wired -> exposed -> per-instance default), but without copying the value out &ndash; useful for non-templated paths (auto-resolve Struct case, struct subobject pin dispatch) that need to decide between byte storage and FInstancedStruct slot at runtime. Returns true and writes OutOffset when a slot is found.

---

#### ReadInternalVariable { #readinternalvariable }

`const` `inline`

```cpp
template<typename T> inline T ReadInternalVariable(FName VariableName) const
```

Read an internal variable by name.

---

#### WriteInternalVariable { #writeinternalvariable }

`inline`

```cpp
template<typename T> inline void WriteInternalVariable(FName VariableName, const T & Value)
```

Write an internal variable by name.

---

#### HasInternalVariable { #hasinternalvariable }

`const` `inline`

```cpp
inline bool HasInternalVariable(FName VariableName) const
```

Check if a specific internal variable exists.

---

#### CopySlot { #copyslot }

`inline`

```cpp
inline void CopySlot(int32 SourceOffset, int32 TargetOffset, int32 NumBytes)
```

Copy raw bytes from one slot to another within the same storage. Used by the exec-chain SetVariable dispatch to transfer a source node's output pin value into an internal variable slot without knowing the concrete C++ type at compile time.

Three cases: both POD (memcpy), both non-POD struct (CopyScriptStruct through the slot's owned memory, the struct types must match), or mismatched &ndash; the layout builder must never emit a connection between pins of different storage classes, so a mismatch is a bug.

---

#### GetStructSlotChecked { #getstructslotchecked }

`const` `inline`

```cpp
inline const FInstancedStruct & GetStructSlotChecked(int32 Offset) const
```

Direct access to the FInstancedStruct backing a non-POD struct slot. Used by auto-resolve / subobject-pin code paths whose dispatch happens on a runtime EComposableCameraPinType value (not a compile-time T) &ndash; the templated ReadValue<T> path is preferred when T is known. Asserts the offset is in fact a struct slot.

---

#### GetStructSlotMutableChecked { #getstructslotmutablechecked }

`inline`

```cpp
inline FInstancedStruct & GetStructSlotMutableChecked(int32 Offset)
```

---

#### RegisterReferenceSlot { #registerreferenceslot }

```cpp
void RegisterReferenceSlot(EComposableCameraPinType PinType, int32 Offset)
```

---

#### RefreshReferenceSlot { #refreshreferenceslot }

```cpp
void RefreshReferenceSlot(int32 Offset)
```

---

#### RefreshAllReferenceSlots { #refreshallreferenceslots }

```cpp
void RefreshAllReferenceSlots()
```

---

#### AddReferencedObjects { #addreferencedobjects-4 }

```cpp
void AddReferencedObjects(FReferenceCollector & Collector)
```

---

#### IsValid { #isvalid }

`const` `inline`

```cpp
inline bool IsValid() const
```

Check if storage has been allocated.

---

#### ZeroInitialize { #zeroinitialize }

`inline`

```cpp
inline void ZeroInitialize()
```

Zero-initialize all storage. Called at allocation time.

### Public Static Attributes

| Return | Name | Description |
|--------|------|-------------|
| `constexpr int32` | [`StructSlotsOffsetBase`](#structslotsoffsetbase) `static` | Synthetic offsets >= this value index into StructSlots; offsets < this value are real byte offsets into Storage. INT32_MAX/2 is well outside any plausible Storage size and leaves the same headroom for synthetic range, so collisions are impossible without TotalSize crossing 1 GiB. |

---

#### StructSlotsOffsetBase { #structslotsoffsetbase }

`static`

```cpp
constexpr int32 StructSlotsOffsetBase = TNumericLimits<int32>::Max() / 2
```

Synthetic offsets >= this value index into StructSlots; offsets < this value are real byte offsets into Storage. INT32_MAX/2 is well outside any plausible Storage size and leaves the same headroom for synthetic range, so collisions are impossible without TotalSize crossing 1 GiB.
