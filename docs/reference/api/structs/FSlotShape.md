
# FSlotShape { #fslotshape }

```cpp
#include <ComposableCameraRuntimeDataBlock.h>
```

Per-slot shape metadata: pin type + size in bytes. Populated at layout time by `AllocateSlot` for every byte-storage slot AND every struct-slot synthetic offset, then consulted by `ReadValue<T>` and `WriteValue<T>` to refuse cross-shape access before the memcpy fires.

The earlier ref-slot directionality guard (eleventh-pass P0) only caught one axis of the cross-shape problem — UObject-pointer T vs ref-slot membership. It did not catch cross-shape access where neither side involves a ref slot, e.g.

`WriteValue<FVector>(FloatPinOffset, V)` // 12 B into 4 B `WriteValue<FTransform>(BoolPinOffset, T)` // 64 B into 1 B `WriteValue<double>(IntVarOffset, D)` // 8 B into 4 B

Each of these passes the `Offset + sizeof(T) <= Storage.Num()` bounds check (the slot is not the LAST slot in Storage), runs the oversized memcpy, and clobbers adjacent slots' bytes. If any clobbered adjacent slot is an Object/Actor reference slot, a later read of that slot reads polluted bytes as a UObject pointer and the IsA virtual call dereferences garbage memory. Strict shape match (`PinType == ExpectedFor<T>` AND `Size == sizeof(T)`) blocks every cross-shape direction at the first templated access.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `EComposableCameraPinType` | [`PinType`](#pintype-3)  |  |
| `int32` | [`Size`](#size)  |  |
| `TObjectPtr< UScriptStruct >` | [`StructType`](#structtype-3)  | Only meaningful when `PinType == Struct`. The exact `UScriptStruct` the slot was allocated for. Templated `ReadValue<T>` / `WriteValue<T>` must verify `T::StaticStruct() == StructType` before letting `CopyScriptStruct` touch the slot — the struct- slot offset table can deliver a wrong-shape T if it ever desyncs (stale type asset, hand-edited connection, asset saved before validation existed), and `CopyScriptStruct` walks T's property layout against whatever bytes the slot actually holds, which is heap corruption / GC pollution territory under non-POD struct fields (FString operator=, UObject ref overwrites, embedded TArray copy). The previous-pass `check()` guards before this field were debug-only safety nets that stripped in Shipping; this metadata promotes the same check to a real return-on-mismatch in every build. |

---

#### PinType { #pintype-3 }

```cpp
EComposableCameraPinType PinType = 
```

---

#### Size { #size }

```cpp
int32 Size = 0
```

---

#### StructType { #structtype-3 }

```cpp
TObjectPtr< UScriptStruct > StructType = nullptr
```

Only meaningful when `PinType == Struct`. The exact `UScriptStruct` the slot was allocated for. Templated `ReadValue<T>` / `WriteValue<T>` must verify `T::StaticStruct() == StructType` before letting `CopyScriptStruct` touch the slot — the struct- slot offset table can deliver a wrong-shape T if it ever desyncs (stale type asset, hand-edited connection, asset saved before validation existed), and `CopyScriptStruct` walks T's property layout against whatever bytes the slot actually holds, which is heap corruption / GC pollution territory under non-POD struct fields (FString operator=, UObject ref overwrites, embedded TArray copy). The previous-pass `check()` guards before this field were debug-only safety nets that stripped in Shipping; this metadata promotes the same check to a real return-on-mismatch in every build.

## FSlotShape { #fslotshape }

```cpp
#include <ComposableCameraRuntimeDataBlock.h>
```

Per-slot shape metadata: pin type + size in bytes. Populated at layout time by `AllocateSlot` for every byte-storage slot AND every struct-slot synthetic offset, then consulted by `ReadValue<T>` and `WriteValue<T>` to refuse cross-shape access before the memcpy fires.

The earlier ref-slot directionality guard (eleventh-pass P0) only caught one axis of the cross-shape problem — UObject-pointer T vs ref-slot membership. It did not catch cross-shape access where neither side involves a ref slot, e.g.

`WriteValue<FVector>(FloatPinOffset, V)` // 12 B into 4 B `WriteValue<FTransform>(BoolPinOffset, T)` // 64 B into 1 B `WriteValue<double>(IntVarOffset, D)` // 8 B into 4 B

Each of these passes the `Offset + sizeof(T) <= Storage.Num()` bounds check (the slot is not the LAST slot in Storage), runs the oversized memcpy, and clobbers adjacent slots' bytes. If any clobbered adjacent slot is an Object/Actor reference slot, a later read of that slot reads polluted bytes as a UObject pointer and the IsA virtual call dereferences garbage memory. Strict shape match (`PinType == ExpectedFor<T>` AND `Size == sizeof(T)`) blocks every cross-shape direction at the first templated access.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `EComposableCameraPinType` | [`PinType`](#pintype-3)  |  |
| `int32` | [`Size`](#size)  |  |
| `TObjectPtr< UScriptStruct >` | [`StructType`](#structtype-3)  | Only meaningful when `PinType == Struct`. The exact `UScriptStruct` the slot was allocated for. Templated `ReadValue<T>` / `WriteValue<T>` must verify `T::StaticStruct() == StructType` before letting `CopyScriptStruct` touch the slot — the struct- slot offset table can deliver a wrong-shape T if it ever desyncs (stale type asset, hand-edited connection, asset saved before validation existed), and `CopyScriptStruct` walks T's property layout against whatever bytes the slot actually holds, which is heap corruption / GC pollution territory under non-POD struct fields (FString operator=, UObject ref overwrites, embedded TArray copy). The previous-pass `check()` guards before this field were debug-only safety nets that stripped in Shipping; this metadata promotes the same check to a real return-on-mismatch in every build. |

---

#### PinType { #pintype-3 }

```cpp
EComposableCameraPinType PinType = 
```

---

#### Size { #size }

```cpp
int32 Size = 0
```

---

#### StructType { #structtype-3 }

```cpp
TObjectPtr< UScriptStruct > StructType = nullptr
```

Only meaningful when `PinType == Struct`. The exact `UScriptStruct` the slot was allocated for. Templated `ReadValue<T>` / `WriteValue<T>` must verify `T::StaticStruct() == StructType` before letting `CopyScriptStruct` touch the slot — the struct- slot offset table can deliver a wrong-shape T if it ever desyncs (stale type asset, hand-edited connection, asset saved before validation existed), and `CopyScriptStruct` walks T's property layout against whatever bytes the slot actually holds, which is heap corruption / GC pollution territory under non-POD struct fields (FString operator=, UObject ref overwrites, embedded TArray copy). The previous-pass `check()` guards before this field were debug-only safety nets that stripped in Shipping; this metadata promotes the same check to a real return-on-mismatch in every build.
