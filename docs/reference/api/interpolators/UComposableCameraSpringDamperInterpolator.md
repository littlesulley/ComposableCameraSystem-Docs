
# UComposableCameraSpringDamperInterpolator { #ucomposablecameraspringdamperinterpolator }

```cpp
#include <ComposableCameraSpringDamperInterpolator.h>
```

> **Inherits:** [`UComposableCameraInterpolatorBase`](UComposableCameraInterpolatorBase.md#ucomposablecamerainterpolatorbase)

Spring damper interpolator.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `float` | [`Frequency`](#frequency-1)  | Controls the frequency of oscillation and the speed of decay. |
| `float` | [`DampRatio`](#dampratio-1)  | Controls whether the spring is undamped (=0), underdamped (<1), critically damped (=1), or overdamped (>1). |

---

#### Frequency { #frequency-1 }

```cpp
float Frequency { 3.1415926 }
```

Controls the frequency of oscillation and the speed of decay.

---

#### DampRatio { #dampratio-1 }

```cpp
float DampRatio { 1.0 }
```

Controls whether the spring is undamped (=0), underdamped (<1), critically damped (=1), or overdamped (>1).
