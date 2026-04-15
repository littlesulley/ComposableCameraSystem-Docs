
# ComposableCameraIndependentPositionalInertializer { #composablecameraindependentpositionalinertializer }

```cpp
#include <ComposableCameraInertializedTransition.h>
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`ComposableCameraIndependentPositionalInertializer`](#composablecameraindependentpositionalinertializer-1)  | Defaulted constructor. |
|  | [`ComposableCameraIndependentPositionalInertializer`](#composablecameraindependentpositionalinertializer-2)  | Defaulted constructor. |
|  | [`ComposableCameraIndependentPositionalInertializer`](#composablecameraindependentpositionalinertializer-3)  | Defaulted constructor. |
|  | [`ComposableCameraIndependentPositionalInertializer`](#composablecameraindependentpositionalinertializer-4) `inline` |  |
| `FVector` | [`Evaluate`](#evaluate-14) `inline` |  |
| `FVector` | [`Evaluate`](#evaluate-15) `inline` |  |

---

#### ComposableCameraIndependentPositionalInertializer { #composablecameraindependentpositionalinertializer-1 }

```cpp
ComposableCameraIndependentPositionalInertializer() = default
```

Defaulted constructor.

---

#### ComposableCameraIndependentPositionalInertializer { #composablecameraindependentpositionalinertializer-2 }

```cpp
ComposableCameraIndependentPositionalInertializer(const ComposableCameraIndependentPositionalInertializer &) = default
```

Defaulted constructor.

---

#### ComposableCameraIndependentPositionalInertializer { #composablecameraindependentpositionalinertializer-3 }

```cpp
ComposableCameraIndependentPositionalInertializer(ComposableCameraIndependentPositionalInertializer &&) = default
```

Defaulted constructor.

---

#### ComposableCameraIndependentPositionalInertializer { #composablecameraindependentpositionalinertializer-4 }

`inline`

```cpp
inline ComposableCameraIndependentPositionalInertializer(const FComposableCameraPose & LastSourceCameraPose, const FComposableCameraPose & ThisSourceCameraPose, const FComposableCameraPose & ThisTargetCameraPose, float BlendTime, float DeltaTime)
```

---

#### Evaluate { #evaluate-14 }

`inline`

```cpp
inline FVector Evaluate(float BlendDuration, FVector TargetLocation)
```

---

#### Evaluate { #evaluate-15 }

`inline`

```cpp
inline FVector Evaluate(float BlendDuration, FVector TargetLocation, float BlendCurveValue, float BlendWeight)
```

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FVector` | [`_InitialDirection`](#_initialdirection-2)  |  |
| `ComposableCameraPolynomial< 5, FVector >` | [`Poly`](#poly-2)  |  |

---

#### _InitialDirection { #_initialdirection-2 }

```cpp
FVector _InitialDirection
```

---

#### Poly { #poly-2 }

```cpp
ComposableCameraPolynomial< 5, FVector > Poly
```
