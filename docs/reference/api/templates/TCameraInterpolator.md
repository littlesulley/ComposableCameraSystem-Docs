
# TCameraInterpolator { #tcamerainterpolator }

## TCameraInterpolator< TValueTypeWrapper< ValueType > > { #tcamerainterpolatortvaluetypewrappervaluetype }

```cpp
#include <ComposableCameraInterpolatorBase.h>
```

> **Subclassed by:** [`TIIRInterpolator< ValueType >`](TIIRInterpolator.md#tiirinterpolator), [`TSimpleSpringInterpolator< ValueType >`](TSimpleSpringInterpolator.md#tsimplespringinterpolator), [`TSpringDamperInterpolator< ValueType >`](TSpringDamperInterpolator.md#tspringdamperinterpolator)

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`TCameraInterpolator`](#tcamerainterpolator-1) `inline` |  |
| `ValueType` | [`GetCurrentValue`](#getcurrentvalue) `const` `inline` |  |
| `ValueType` | [`GetTargetValue`](#gettargetvalue) `const` `inline` |  |
| `bool` | [`IsFinished`](#isfinished-2) `const` `inline` |  |
| `void` | [`Reset`](#reset) `inline` |  |
| `ValueType` | [`Run`](#run-3)  |  |

---

#### TCameraInterpolator { #tcamerainterpolator-1 }

`inline`

```cpp
inline TCameraInterpolator(const UComposableCameraInterpolatorBase * Interpolator)
```

---

#### GetCurrentValue { #getcurrentvalue }

`const` `inline`

```cpp
inline ValueType GetCurrentValue() const
```

---

#### GetTargetValue { #gettargetvalue }

`const` `inline`

```cpp
inline ValueType GetTargetValue() const
```

---

#### IsFinished { #isfinished-2 }

`const` `inline`

```cpp
inline bool IsFinished() const
```

---

#### Reset { #reset }

`inline`

```cpp
inline void Reset(ConstValueType NewCurrentValue, ConstValueType NewTargetValue)
```

---

#### Run { #run-3 }

```cpp
ValueType Run(const float DeltaTime)
```

### Protected Attributes

| Return | Name | Description |
|--------|------|-------------|
| `const UComposableCameraInterpolatorBase *` | [`Interpolator`](#interpolator-5)  |  |
| `WrappedValueType` | [`CurrentValue`](#currentvalue)  |  |
| `WrappedValueType` | [`TargetValue`](#targetvalue)  |  |
| `bool` | [`bFinished`](#bfinished-1)  |  |

---

#### Interpolator { #interpolator-5 }

```cpp
const UComposableCameraInterpolatorBase * Interpolator
```

---

#### CurrentValue { #currentvalue }

```cpp
WrappedValueType CurrentValue
```

---

#### TargetValue { #targetvalue }

```cpp
WrappedValueType TargetValue
```

---

#### bFinished { #bfinished-1 }

```cpp
bool bFinished
```

### Protected Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`OnReset`](#onreset-3)  |  |

---

#### OnReset { #onreset-3 }

```cpp
void OnReset(ConstValueType OldCurrentValue, ConstValueType OldTargetValue, ConstValueType NewCurrentValue, ConstValueType NewTargetValue)
```

### Public Types

| Name | Description |
|------|-------------|
| [`ConstValueType`](#constvaluetype-3)  |  |
| [`WrappedValueType`](#wrappedvaluetype-3)  |  |

---

#### ConstValueType { #constvaluetype-3 }

```cpp
const ValueType ConstValueType()
```

---

#### WrappedValueType { #wrappedvaluetype-3 }

```cpp
TValueTypeWrapper< ValueType > WrappedValueType()
```
