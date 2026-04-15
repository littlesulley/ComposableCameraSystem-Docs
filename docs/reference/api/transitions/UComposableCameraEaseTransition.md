
# UComposableCameraEaseTransition { #ucomposablecameraeasetransition }

```cpp
#include <ComposableCameraEaseTransition.h>
```

> **Inherits:** [`UComposableCameraTransitionBase`](UComposableCameraTransitionBase.md#ucomposablecameratransitionbase)

EaseInOut transition.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `float` | [`Exp`](#exp)  |  |

---

#### Exp { #exp }

```cpp
float Exp { 1.f }
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `FComposableCameraPose` | [`OnEvaluate_Implementation`](#onevaluate_implementation) `virtual` |  |

---

#### OnEvaluate_Implementation { #onevaluate_implementation }

`virtual`

```cpp
virtual FComposableCameraPose OnEvaluate_Implementation(float DeltaTime, const FComposableCameraPose & CurrentSourcePose, const FComposableCameraPose & CurrentTargetPose)
```
