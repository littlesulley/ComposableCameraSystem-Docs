
# TValueTypeWrapper { #tvaluetypewrapper }

```cpp
#include <ComposableCameraInterpolatorBase.h>
```

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `ValueType` | [`Value`](#value)  |  |

---

#### Value { #value }

```cpp
ValueType Value {}
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`TValueTypeWrapper`](#tvaluetypewrapper-1) `inline` |  |
|  | [`TValueTypeWrapper`](#tvaluetypewrapper-2) `inline` |  |
| `TValueTypeWrapper &` | [`operator-=`](#operator) `inline` |  |
| `TValueTypeWrapper &` | [`operator+=`](#operator-1) `inline` |  |
| `TValueTypeWrapper &` | [`operator*=`](#operator-2) `inline` |  |
| `TValueTypeWrapper &` | [`operator-`](#operator-3) `inline` |  |
| `TValueTypeWrapper` | [`operator*`](#operator-4) `const` `inline` |  |
| `TValueTypeWrapper` | [`operator/`](#operator-5) `const` `inline` |  |

---

#### TValueTypeWrapper { #tvaluetypewrapper-1 }

`inline`

```cpp
inline TValueTypeWrapper()
```

---

#### TValueTypeWrapper { #tvaluetypewrapper-2 }

`inline`

```cpp
inline TValueTypeWrapper(const ValueType & Value)
```

---

#### operator-= { #operator }

`inline`

```cpp
inline TValueTypeWrapper & operator-=(const TValueTypeWrapper & RHS)
```

---

#### operator+= { #operator-1 }

`inline`

```cpp
inline TValueTypeWrapper & operator+=(const TValueTypeWrapper & RHS)
```

---

#### operator*= { #operator-2 }

`inline`

```cpp
inline TValueTypeWrapper & operator*=(double Multiplier)
```

---

#### operator- { #operator-3 }

`inline`

```cpp
inline TValueTypeWrapper & operator-()
```

---

#### operator* { #operator-4 }

`const` `inline`

```cpp
inline TValueTypeWrapper operator*(double Multiplier) const
```

---

#### operator/ { #operator-5 }

`const` `inline`

```cpp
inline TValueTypeWrapper operator/(double Multiplier) const
```



## TValueTypeWrapper< FQuat > { #tvaluetypewrapperfquat }

```cpp
#include <ComposableCameraInterpolatorBase.h>
```

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FQuat` | [`Value`](#value-1)  |  |

---

#### Value { #value-1 }

```cpp
FQuat Value {}
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`TValueTypeWrapper`](#tvaluetypewrapper-3) `inline` |  |
|  | [`TValueTypeWrapper`](#tvaluetypewrapper-4) `inline` |  |
| `TValueTypeWrapper &` | [`operator-=`](#operator-9) `inline` |  |
| `TValueTypeWrapper &` | [`operator+=`](#operator-10) `inline` |  |
| `TValueTypeWrapper &` | [`operator*=`](#operator-11) `inline` |  |
| `TValueTypeWrapper` | [`operator*`](#operator-12) `const` `inline` |  |

---

#### TValueTypeWrapper { #tvaluetypewrapper-3 }

`inline`

```cpp
inline TValueTypeWrapper()
```

---

#### TValueTypeWrapper { #tvaluetypewrapper-4 }

`inline`

```cpp
inline TValueTypeWrapper(const FQuat & Value)
```

---

#### operator-= { #operator-9 }

`inline`

```cpp
inline TValueTypeWrapper & operator-=(const TValueTypeWrapper & RHS)
```

---

#### operator+= { #operator-10 }

`inline`

```cpp
inline TValueTypeWrapper & operator+=(const TValueTypeWrapper & RHS)
```

---

#### operator*= { #operator-11 }

`inline`

```cpp
inline TValueTypeWrapper & operator*=(double Multiplier)
```

---

#### operator* { #operator-12 }

`const` `inline`

```cpp
inline TValueTypeWrapper operator*(double Multiplier) const
```



## TValueTypeWrapper< FRotator > { #tvaluetypewrapperfrotator }

```cpp
#include <ComposableCameraInterpolatorBase.h>
```

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FRotator` | [`Value`](#value-2)  |  |

---

#### Value { #value-2 }

```cpp
FRotator Value {}
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`TValueTypeWrapper`](#tvaluetypewrapper-5) `inline` |  |
|  | [`TValueTypeWrapper`](#tvaluetypewrapper-6) `inline` |  |
| `TValueTypeWrapper &` | [`operator-=`](#operator-13) `inline` |  |
| `TValueTypeWrapper &` | [`operator+=`](#operator-14) `inline` |  |
| `TValueTypeWrapper &` | [`operator*=`](#operator-15) `inline` |  |
| `TValueTypeWrapper` | [`operator*`](#operator-16) `const` `inline` |  |

---

#### TValueTypeWrapper { #tvaluetypewrapper-5 }

`inline`

```cpp
inline TValueTypeWrapper()
```

---

#### TValueTypeWrapper { #tvaluetypewrapper-6 }

`inline`

```cpp
inline TValueTypeWrapper(const FRotator & Value)
```

---

#### operator-= { #operator-13 }

`inline`

```cpp
inline TValueTypeWrapper & operator-=(const TValueTypeWrapper & RHS)
```

---

#### operator+= { #operator-14 }

`inline`

```cpp
inline TValueTypeWrapper & operator+=(const TValueTypeWrapper & RHS)
```

---

#### operator*= { #operator-15 }

`inline`

```cpp
inline TValueTypeWrapper & operator*=(double Multiplier)
```

---

#### operator* { #operator-16 }

`const` `inline`

```cpp
inline TValueTypeWrapper operator*(double Multiplier) const
```
