
# ComposableCameraInitializer { #composablecamerainitializer }

```cpp
#include <ComposableCameraInertializedTransition.h>
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`ComposableCameraInitializer`](#composablecamerainitializer-1) `inline` |  |
|  | [`ComposableCameraInitializer`](#composablecamerainitializer-2) `inline` |  |
| `DataType` | [`Evaluate`](#evaluate-2) `inline` |  |
| `DataType` | [`Evaluate`](#evaluate-3) `inline` |  |

---

#### ComposableCameraInitializer { #composablecamerainitializer-1 }

`inline`

```cpp
inline ComposableCameraInitializer()
```

---

#### ComposableCameraInitializer { #composablecamerainitializer-2 }

`inline`

```cpp
inline ComposableCameraInitializer(const FComposableCameraPose & LastSourceCameraPose, const FComposableCameraPose & ThisSourceCameraPose, const FComposableCameraPose & ThisTargetCameraPose, float BlendTime, float DeltaTime)
```

---

#### Evaluate { #evaluate-2 }

`inline`

```cpp
inline DataType Evaluate(float TimeStamp, DataType TargetData)
```

---

#### Evaluate { #evaluate-3 }

`inline`

```cpp
inline DataType Evaluate(float TimeStamp, DataType TargetData, float BlendPct, UCurveFloat * Curve, float CurveWeight, float CurveShape)
```

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `ConcreteInertializerType` | [`ConcreteInertializer`](#concreteinertializer)  |  |

---

#### ConcreteInertializer { #concreteinertializer }

```cpp
ConcreteInertializerType ConcreteInertializer
```

### Private Static Methods

| Return | Name | Description |
|--------|------|-------------|
| `std::pair< float, float >` | [`GetBlendCurveValue`](#getblendcurvevalue) `static` `inline` |  |

---

#### GetBlendCurveValue { #getblendcurvevalue }

`static` `inline`

```cpp
static inline std::pair< float, float > GetBlendCurveValue(float BlendPct, UCurveFloat * Curve, float CurveWeight, float CurveShape)
```
