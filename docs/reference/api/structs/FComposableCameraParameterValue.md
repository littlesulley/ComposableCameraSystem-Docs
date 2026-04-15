
# FComposableCameraParameterValue { #fcomposablecameraparametervalue }

```cpp
#include <ComposableCameraParameterBlock.h>
```

A single parameter value in a ParameterBlock. Type-erased storage using a byte array.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `EComposableCameraPinType` | [`PinType`](#pintype)  | The pin type of this value. |
| `TArray< uint8 >` | [`Data`](#data)  | Raw bytes holding the value. Size depends on PinType. |

---

#### PinType { #pintype }

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
| `bool` | [`Get`](#get-1) `const` `inline` | Get a typed value. Returns false if types mismatch or data is empty. |

---

#### Set { #set }

`inline`

```cpp
template<typename T> inline void Set(EComposableCameraPinType InPinType, const T & Value)
```

Set a typed value.

---

#### Get { #get-1 }

`const` `inline`

```cpp
template<typename T> inline bool Get(T & OutValue) const
```

Get a typed value. Returns false if types mismatch or data is empty.
