
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
| `TArray< uint8 >` | [`Storage`](#storage)  | Raw storage buffer. Allocated once during camera instantiation. |
| `TMap< FComposableCameraPinKey, int32 >` | [`OutputPinOffsets`](#outputpinoffsets)  | Lookup: (NodeIndex, PinName) for OUTPUT pins → byte offset in Storage. |
| `TMap< FName, int32 >` | [`ExposedParameterOffsets`](#exposedparameteroffsets)  | Lookup: ExposedParameterName → byte offset in Storage. |
| `TMap< FName, int32 >` | [`InternalVariableOffsets`](#internalvariableoffsets)  | Lookup: InternalVariableName → byte offset in Storage. |
| `TMap< FComposableCameraPinKey, int32 >` | [`InputPinSourceOffsets`](#inputpinsourceoffsets)  | Connection table: for each input pin, the offset of its source data. Key = (TargetNodeIndex, TargetPinName), Value = offset in Storage where the source output pin wrote its data. |
| `TMap< FComposableCameraPinKey, int32 >` | [`ExposedInputPinOffsets`](#exposedinputpinoffsets)  | Exposure table: for each exposed input pin, the offset of the parameter slot. Key = (TargetNodeIndex, TargetPinName), Value = offset of the exposed parameter in Storage. |
| `TMap< FComposableCameraPinKey, int32 >` | [`DefaultValueOffsets`](#defaultvalueoffsets)  | Per-instance default-value table: for each input pin that has an authored [FComposableCameraPinOverride::DefaultValueOverride](FComposableCameraPinOverride.md#defaultvalueoverride) (see [Nodes/ComposableCameraNodePinTypes.h](#composablecameranodepintypesh)), the offset of the slot holding the pre-parsed typed bytes. Key = (TargetNodeIndex, PinName), Value = offset in Storage. |
| `int32` | [`TotalSize`](#totalsize)  | Total allocated size. |

---

#### Storage { #storage }

```cpp
TArray< uint8 > Storage
```

Raw storage buffer. Allocated once during camera instantiation.

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
| `T` | [`ReadValue`](#readvalue) `const` `inline` | Read a typed value from the storage at the given byte offset. |
| `void` | [`WriteValue`](#writevalue) `inline` | Write a typed value to the storage at the given byte offset. |
| `T` | [`ReadOutputPin`](#readoutputpin) `const` `inline` | Read a value for a specific output pin. |
| `void` | [`WriteOutputPin`](#writeoutputpin) `inline` | Write a value for a specific output pin. |
| `bool` | [`TryResolveInputPin`](#tryresolveinputpin) `const` `inline` | Resolve an input pin's value. Checks in order: |
| `T` | [`ReadInternalVariable`](#readinternalvariable) `const` `inline` | Read an internal variable by name. |
| `void` | [`WriteInternalVariable`](#writeinternalvariable) `inline` | Write an internal variable by name. |
| `bool` | [`HasInternalVariable`](#hasinternalvariable) `const` `inline` | Check if a specific internal variable exists. |
| `void` | [`CopySlot`](#copyslot) `inline` | Copy raw bytes from one slot to another within the same storage. Used by the exec-chain SetVariable dispatch to transfer a source node's output pin value into an internal variable slot without knowing the concrete C++ type at compile time. |
| `bool` | [`IsValid`](#isvalid) `const` `inline` | Check if storage has been allocated. |
| `void` | [`ZeroInitialize`](#zeroinitialize) `inline` | Zero-initialize all storage. Called at allocation time. |

---

#### ReadValue { #readvalue }

`const` `inline`

```cpp
template<typename T> inline T ReadValue(int32 Offset) const
```

Read a typed value from the storage at the given byte offset.

---

#### WriteValue { #writevalue }

`inline`

```cpp
template<typename T> inline void WriteValue(int32 Offset, const T & Value)
```

Write a typed value to the storage at the given byte offset.

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
