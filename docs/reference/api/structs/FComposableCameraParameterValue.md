
# FComposableCameraParameterValue { #fcomposablecameraparametervalue }

```cpp
#include <ComposableCameraParameterBlock.h>
```

A single parameter value in a ParameterBlock. Type-erased storage using a byte array.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `EComposableCameraPinType` | [`PinType`](#pintype-1)  | The pin type of this value. |
| `TArray< uint8 >` | [`Data`](#data)  | Raw bytes holding the value. Size depends on PinType. |

---

#### PinType { #pintype-1 }

```cpp
EComposableCameraPinType PinType = 
```

The pin type of this value.

---

#### Data { #data }

```cpp
TArray< uint8 > Data
```

Raw bytes holding the value. Size depends on PinType.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`Set`](#set) `inline` | Set a typed value. |
| `bool` | [`Get`](#get-2) `const` `inline` | Get a typed value. Returns false on: |

---

#### Set { #set }

`inline`

```cpp
template<typename T> inline void Set(EComposableCameraPinType InPinType, const T & Value)
```

Set a typed value.

---

#### Get { #get-2 }

`const` `inline`

```cpp
template<typename T> inline bool Get(T & OutValue) const
```

Get a typed value. Returns false on:

* byte-size mismatch (`Data.Num() != sizeof(T)`),

* PinType mismatch (e.g. `Get<float>` on an Int32 entry — same size, wrong meaning),

* unsupported T (no PinType maps to this template parameter),

* for UObject pointers, when the stored pointer fails `IsA<T>()`.

Strict validation rationale: the prior signature only checked `Data.Num()`, so any same-size cross-type read silently succeeded — `Get<float>` would read an `int32` entry's bit pattern as a float, `Get<UCurveFloat*>` would return any `UObject*` cast to `UCurveFloat*` regardless of actual class. The runtime path is already guarded by `CopyRawTo`'s PinType + size check; this validates the public C++ template entry point so manual callers cannot type-pun through it either.
