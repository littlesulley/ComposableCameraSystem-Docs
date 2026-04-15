
# TSpringDamperInterpolator { #tspringdamperinterpolator }

```cpp
#include <ComposableCameraSpringDamperInterpolator.h>
```

> **Inherits:** [`TCameraInterpolator< TValueTypeWrapper< ValueType > >`](TCameraInterpolator.md#tcamerainterpolatortvaluetypewrappervaluetype)

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`TSpringDamperInterpolator`](#tspringdamperinterpolator-1) `inline` |  |
|  | [`TSpringDamperInterpolator`](#tspringdamperinterpolator-2) `inline` |  |
| `ValueType` | [`Run`](#run-2) `virtual` `inline` |  |

---

#### TSpringDamperInterpolator { #tspringdamperinterpolator-1 }

`inline`

```cpp
inline TSpringDamperInterpolator(const UComposableCameraSpringDamperInterpolator * Interpolator)
```

---

#### TSpringDamperInterpolator { #tspringdamperinterpolator-2 }

`inline`

```cpp
inline TSpringDamperInterpolator(const float InFrequency, const float InDampRatio)
```

---

#### Run { #run-2 }

`virtual` `inline`

```cpp
virtual inline ValueType Run(const float DeltaTime)
```

### Protected Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`OnReset`](#onreset-2) `virtual` `inline` |  |

---

#### OnReset { #onreset-2 }

`virtual` `inline`

```cpp
virtual inline void OnReset(ConstValueType OldCurrentValue, ConstValueType OldTargetValue, ConstValueType NewCurrentValue, ConstValueType NewTargetValue)
```

### Public Types

| Name | Description |
|------|-------------|
| [`ConstValueType`](#constvaluetype-2)  |  |
| [`WrappedValueType`](#wrappedvaluetype-2)  |  |
| [`IntermediateValueType`](#intermediatevaluetype)  |  |
| [`WrappedIntermediateValueType`](#wrappedintermediatevaluetype)  |  |

---

#### ConstValueType { #constvaluetype-2 }

```cpp
typename TCameraInterpolator< TValueTypeWrapper< ValueType > >::ConstValueType ConstValueType()
```

---

#### WrappedValueType { #wrappedvaluetype-2 }

```cpp
typename TCameraInterpolator< TValueTypeWrapper< ValueType > >::WrappedValueType WrappedValueType()
```

---

#### IntermediateValueType { #intermediatevaluetype }

```cpp
typename TSpringDamperInterpolatorTraits< ValueType >::IntermediateValueType IntermediateValueType()
```

---

#### WrappedIntermediateValueType { #wrappedintermediatevaluetype }

```cpp
TValueTypeWrapper< IntermediateValueType > WrappedIntermediateValueType()
```

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `const UComposableCameraSpringDamperInterpolator *` | [`SpringDamperInterpolator`](#springdamperinterpolator)  |  |
| `float` | [`Frequency`](#frequency)  |  |
| `float` | [`DampRatio`](#dampratio)  |  |
| `WrappedIntermediateValueType` | [`Velocity`](#velocity)  |  |

---

#### SpringDamperInterpolator { #springdamperinterpolator }

```cpp
const UComposableCameraSpringDamperInterpolator * SpringDamperInterpolator
```

---

#### Frequency { #frequency }

```cpp
float Frequency
```

---

#### DampRatio { #dampratio }

```cpp
float DampRatio
```

---

#### Velocity { #velocity }

```cpp
WrappedIntermediateValueType Velocity {}
```
