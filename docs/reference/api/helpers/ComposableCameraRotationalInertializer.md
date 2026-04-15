
# ComposableCameraRotationalInertializer { #composablecamerarotationalinertializer }

```cpp
#include <ComposableCameraInertializedTransition.h>
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`ComposableCameraRotationalInertializer`](#composablecamerarotationalinertializer-1)  | Defaulted constructor. |
|  | [`ComposableCameraRotationalInertializer`](#composablecamerarotationalinertializer-2)  | Defaulted constructor. |
|  | [`ComposableCameraRotationalInertializer`](#composablecamerarotationalinertializer-3)  | Defaulted constructor. |
|  | [`ComposableCameraRotationalInertializer`](#composablecamerarotationalinertializer-4) `inline` |  |
| `FRotator` | [`Evaluate`](#evaluate-10) `inline` |  |
| `FRotator` | [`Evaluate`](#evaluate-11) `inline` |  |

---

#### ComposableCameraRotationalInertializer { #composablecamerarotationalinertializer-1 }

```cpp
ComposableCameraRotationalInertializer() = default
```

Defaulted constructor.

---

#### ComposableCameraRotationalInertializer { #composablecamerarotationalinertializer-2 }

```cpp
ComposableCameraRotationalInertializer(const ComposableCameraRotationalInertializer &) = default
```

Defaulted constructor.

---

#### ComposableCameraRotationalInertializer { #composablecamerarotationalinertializer-3 }

```cpp
ComposableCameraRotationalInertializer(ComposableCameraRotationalInertializer &&) = default
```

Defaulted constructor.

---

#### ComposableCameraRotationalInertializer { #composablecamerarotationalinertializer-4 }

`inline`

```cpp
inline ComposableCameraRotationalInertializer(const FComposableCameraPose & LastSourceCameraPose, const FComposableCameraPose & ThisSourceCameraPose, const FComposableCameraPose & ThisTargetCameraPose, float BlendTime, float DeltaTime)
```

---

#### Evaluate { #evaluate-10 }

`inline`

```cpp
inline FRotator Evaluate(float BlendDuration, FRotator TargetRotation)
```

---

#### Evaluate { #evaluate-11 }

`inline`

```cpp
inline FRotator Evaluate(float BlendDuration, FRotator TargetRotation, float BlendCurveValue, float BlendWeight)
```

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FVector` | [`_InitialDirection`](#_initialdirection-1)  |  |
| `ComposableCameraPolynomial< 5, FVector >` | [`Poly`](#poly-1)  |  |

---

#### _InitialDirection { #_initialdirection-1 }

```cpp
FVector _InitialDirection
```

---

#### Poly { #poly-1 }

```cpp
ComposableCameraPolynomial< 5, FVector > Poly
```
