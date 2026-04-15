
# TIIRInterpolator { #tiirinterpolator }

```cpp
#include <ComposableCameraIIRInterpolator.h>
```

> **Inherits:** [`TCameraInterpolator< TValueTypeWrapper< ValueType > >`](TCameraInterpolator.md#tcamerainterpolatortvaluetypewrappervaluetype)

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`TIIRInterpolator`](#tiirinterpolator-1) `inline` |  |
|  | [`TIIRInterpolator`](#tiirinterpolator-2) `inline` |  |
| `ValueType` | [`Run`](#run) `virtual` `inline` |  |

---

#### TIIRInterpolator { #tiirinterpolator-1 }

`inline`

```cpp
inline TIIRInterpolator(const UComposableCameraIIRInterpolator * Interpolator)
```

---

#### TIIRInterpolator { #tiirinterpolator-2 }

`inline`

```cpp
inline TIIRInterpolator(const float InSpeed, const bool InUseFixedStep)
```

---

#### Run { #run }

`virtual` `inline`

```cpp
virtual inline ValueType Run(const float DeltaTime)
```

### Protected Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`OnReset`](#onreset) `virtual` `inline` |  |
| `ValueType` | [`RunSubstep`](#runsubstep) `inline` |  |

---

#### OnReset { #onreset }

`virtual` `inline`

```cpp
virtual inline void OnReset(ConstValueType OldCurrentValue, ConstValueType OldTargetValue, ConstValueType NewCurrentValue, ConstValueType NewTargetValue)
```

---

#### RunSubstep { #runsubstep }

`inline`

```cpp
inline ValueType RunSubstep(ValueType SubstepTargetValue, float DeltaTime)
```

### Public Types

| Name | Description |
|------|-------------|
| [`ConstValueType`](#constvaluetype)  |  |
| [`WrappedValueType`](#wrappedvaluetype)  |  |

---

#### ConstValueType { #constvaluetype }

```cpp
typename TCameraInterpolator< TValueTypeWrapper< ValueType > >::ConstValueType ConstValueType()
```

---

#### WrappedValueType { #wrappedvaluetype }

```cpp
typename TCameraInterpolator< TValueTypeWrapper< ValueType > >::WrappedValueType WrappedValueType()
```

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `const UComposableCameraIIRInterpolator *` | [`IIRInterpolator`](#iirinterpolator)  |  |
| `float` | [`Speed`](#speed)  |  |
| `bool` | [`bUseFixedStep`](#busefixedstep)  |  |
| `WrappedValueType` | [`LastTargetValue`](#lasttargetvalue)  |  |
| `float` | [`LastUpdateLeftoverTime`](#lastupdateleftovertime)  |  |

---

#### IIRInterpolator { #iirinterpolator }

```cpp
const UComposableCameraIIRInterpolator * IIRInterpolator
```

---

#### Speed { #speed }

```cpp
float Speed = 1.f
```

---

#### bUseFixedStep { #busefixedstep }

```cpp
bool bUseFixedStep = false
```

---

#### LastTargetValue { #lasttargetvalue }

```cpp
WrappedValueType LastTargetValue {}
```

---

#### LastUpdateLeftoverTime { #lastupdateleftovertime }

```cpp
float LastUpdateLeftoverTime = 0.f
```
