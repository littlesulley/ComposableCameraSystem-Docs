
# TSpringDamperInterpolatorTraits { #tspringdamperinterpolatortraits }

```cpp
#include <ComposableCameraSpringDamperInterpolator.h>
```

### Public Static Methods

| Return | Name | Description |
|--------|------|-------------|
| `TValueTypeWrapper< ValueType > &` | [`ConvertTo`](#convertto) `static` `inline` |  |
| `TValueTypeWrapper< ValueType > &` | [`ConvertFrom`](#convertfrom) `static` `inline` |  |

---

#### ConvertTo { #convertto }

`static` `inline`

```cpp
static inline TValueTypeWrapper< ValueType > & ConvertTo(TValueTypeWrapper< ValueType > & WrappedValue)
```

---

#### ConvertFrom { #convertfrom }

`static` `inline`

```cpp
static inline TValueTypeWrapper< ValueType > & ConvertFrom(TValueTypeWrapper< ValueType > & WrappedValue)
```

### Public Types

| Name | Description |
|------|-------------|
| [`IntermediateValueType`](#intermediatevaluetype-1)  |  |

---

#### IntermediateValueType { #intermediatevaluetype-1 }

```cpp
ValueType IntermediateValueType()
```



## TSpringDamperInterpolatorTraits< FQuat > { #tspringdamperinterpolatortraitsfquat }

```cpp
#include <ComposableCameraSpringDamperInterpolator.h>
```

### Public Static Methods

| Return | Name | Description |
|--------|------|-------------|
| `TValueTypeWrapper< FVector >` | [`ConvertTo`](#convertto-1) `static` `inline` |  |
| `TValueTypeWrapper< FQuat >` | [`ConvertFrom`](#convertfrom-1) `static` `inline` |  |

---

#### ConvertTo { #convertto-1 }

`static` `inline`

```cpp
static inline TValueTypeWrapper< FVector > ConvertTo(TValueTypeWrapper< FQuat > & WrappedValue)
```

---

#### ConvertFrom { #convertfrom-1 }

`static` `inline`

```cpp
static inline TValueTypeWrapper< FQuat > ConvertFrom(TValueTypeWrapper< FVector > & WrappedValue)
```

### Public Types

| Name | Description |
|------|-------------|
| [`IntermediateValueType`](#intermediatevaluetype-2)  |  |

---

#### IntermediateValueType { #intermediatevaluetype-2 }

```cpp
FVector IntermediateValueType()
```



## TSpringDamperInterpolatorTraits< FRotator > { #tspringdamperinterpolatortraitsfrotator }

```cpp
#include <ComposableCameraSpringDamperInterpolator.h>
```

### Public Static Methods

| Return | Name | Description |
|--------|------|-------------|
| `TValueTypeWrapper< FVector >` | [`ConvertTo`](#convertto-2) `static` `inline` |  |
| `TValueTypeWrapper< FRotator >` | [`ConvertFrom`](#convertfrom-2) `static` `inline` |  |

---

#### ConvertTo { #convertto-2 }

`static` `inline`

```cpp
static inline TValueTypeWrapper< FVector > ConvertTo(TValueTypeWrapper< FRotator > & WrappedValue)
```

---

#### ConvertFrom { #convertfrom-2 }

`static` `inline`

```cpp
static inline TValueTypeWrapper< FRotator > ConvertFrom(TValueTypeWrapper< FVector > & WrappedValue)
```

### Public Types

| Name | Description |
|------|-------------|
| [`IntermediateValueType`](#intermediatevaluetype-3)  |  |

---

#### IntermediateValueType { #intermediatevaluetype-3 }

```cpp
FVector IntermediateValueType()
```
