
# ComposableCameraPolynomial { #composablecamerapolynomial }

```cpp
#include <ComposableCameraInertializedTransition.h>
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`ComposableCameraPolynomial`](#composablecamerapolynomial-1) `inline` |  |
| `ElementType` | [`Evaluate`](#evaluate-1) `inline` |  |

---

#### ComposableCameraPolynomial { #composablecamerapolynomial-1 }

`inline`

```cpp
template<class... CoefficientTypes> inline ComposableCameraPolynomial(CoefficientTypes &&... coefficients)
```

---

#### Evaluate { #evaluate-1 }

`inline`

```cpp
inline ElementType Evaluate(float TimeStamp)
```

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TStaticArray< ElementType, Order+1 >` | [`Coefficients`](#coefficients)  |  |

---

#### Coefficients { #coefficients }

```cpp
TStaticArray< ElementType, Order+1 > Coefficients
```
