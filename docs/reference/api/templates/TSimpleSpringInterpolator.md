
# TSimpleSpringInterpolator { #tsimplespringinterpolator }

```cpp
#include <ComposableCameraSimpleSpringInterpolator.h>
```

> **Inherits:** [`TCameraInterpolator< TValueTypeWrapper< ValueType > >`](TCameraInterpolator.md#tcamerainterpolatortvaluetypewrappervaluetype)

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`TSimpleSpringInterpolator`](#tsimplespringinterpolator-1) `inline` |  |
|  | [`TSimpleSpringInterpolator`](#tsimplespringinterpolator-2) `inline` |  |
| `ValueType` | [`Run`](#run-1) `virtual` `inline` |  |

---

#### TSimpleSpringInterpolator { #tsimplespringinterpolator-1 }

`inline`

```cpp
inline TSimpleSpringInterpolator(const UComposableCameraSimpleSpringInterpolator * Interpolator)
```

---

#### TSimpleSpringInterpolator { #tsimplespringinterpolator-2 }

`inline`

```cpp
inline TSimpleSpringInterpolator(const float DampTime)
```

---

#### Run { #run-1 }

`virtual` `inline`

```cpp
virtual inline ValueType Run(const float DeltaTime)
```

### Protected Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`OnReset`](#onreset-1) `virtual` `inline` |  |

---

#### OnReset { #onreset-1 }

`virtual` `inline`

```cpp
virtual inline void OnReset(ConstValueType OldCurrentValue, ConstValueType OldTargetValue, ConstValueType NewCurrentValue, ConstValueType NewTargetValue)
```

### Public Types

| Name | Description |
|------|-------------|
| [`ConstValueType`](#constvaluetype-1)  |  |
| [`WrappedValueType`](#wrappedvaluetype-1)  |  |

---

#### ConstValueType { #constvaluetype-1 }

```cpp
typename TCameraInterpolator< TValueTypeWrapper< ValueType > >::ConstValueType ConstValueType()
```

---

#### WrappedValueType { #wrappedvaluetype-1 }

```cpp
typename TCameraInterpolator< TValueTypeWrapper< ValueType > >::WrappedValueType WrappedValueType()
```

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `const UComposableCameraSimpleSpringInterpolator *` | [`SimpleSpringInterpolator`](#simplespringinterpolator)  |  |
| `float` | [`DampTime`](#damptime)  |  |

---

#### SimpleSpringInterpolator { #simplespringinterpolator }

```cpp
const UComposableCameraSimpleSpringInterpolator * SimpleSpringInterpolator
```

---

#### DampTime { #damptime }

```cpp
float DampTime = 1.f
```
