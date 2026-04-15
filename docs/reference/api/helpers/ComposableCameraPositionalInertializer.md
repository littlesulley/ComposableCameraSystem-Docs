
# ComposableCameraPositionalInertializer { #composablecamerapositionalinertializer }

```cpp
#include <ComposableCameraInertializedTransition.h>
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`ComposableCameraPositionalInertializer`](#composablecamerapositionalinertializer-1)  | Defaulted constructor. |
|  | [`ComposableCameraPositionalInertializer`](#composablecamerapositionalinertializer-2)  | Defaulted constructor. |
|  | [`ComposableCameraPositionalInertializer`](#composablecamerapositionalinertializer-3)  | Defaulted constructor. |
|  | [`ComposableCameraPositionalInertializer`](#composablecamerapositionalinertializer-4) `inline` |  |
| `FVector` | [`Evaluate`](#evaluate-8) `inline` |  |
| `FVector` | [`Evaluate`](#evaluate-9) `inline` |  |

---

#### ComposableCameraPositionalInertializer { #composablecamerapositionalinertializer-1 }

```cpp
ComposableCameraPositionalInertializer() = default
```

Defaulted constructor.

---

#### ComposableCameraPositionalInertializer { #composablecamerapositionalinertializer-2 }

```cpp
ComposableCameraPositionalInertializer(const ComposableCameraPositionalInertializer &) = default
```

Defaulted constructor.

---

#### ComposableCameraPositionalInertializer { #composablecamerapositionalinertializer-3 }

```cpp
ComposableCameraPositionalInertializer(ComposableCameraPositionalInertializer &&) = default
```

Defaulted constructor.

---

#### ComposableCameraPositionalInertializer { #composablecamerapositionalinertializer-4 }

`inline`

```cpp
inline ComposableCameraPositionalInertializer(const FComposableCameraPose & LastSourceCameraPose, const FComposableCameraPose & ThisSourceCameraPose, const FComposableCameraPose & ThisTargetCameraPose, float BlendTime, float DeltaTime)
```

---

#### Evaluate { #evaluate-8 }

`inline`

```cpp
inline FVector Evaluate(float BlendDuration, FVector TargetLocation)
```

---

#### Evaluate { #evaluate-9 }

`inline`

```cpp
inline FVector Evaluate(float BlendDuration, FVector TargetLocation, float BlendCurveValue, float BlendWeight)
```

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `float` | [`_InitialLength`](#_initiallength)  |  |
| `FVector` | [`_InitialDirection`](#_initialdirection)  |  |
| `ComposableCameraPolynomial< 5, float >` | [`Poly`](#poly)  |  |

---

#### _InitialLength { #_initiallength }

```cpp
float _InitialLength
```

---

#### _InitialDirection { #_initialdirection }

```cpp
FVector _InitialDirection
```

---

#### Poly { #poly }

```cpp
ComposableCameraPolynomial< 5, float > Poly
```
