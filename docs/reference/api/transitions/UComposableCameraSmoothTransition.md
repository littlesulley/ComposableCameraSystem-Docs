
# UComposableCameraSmoothTransition { #ucomposablecamerasmoothtransition }

```cpp
#include <ComposableCameraSmoothTransition.h>
```

> **Inherits:** [`UComposableCameraTransitionBase`](UComposableCameraTransitionBase.md#ucomposablecameratransitionbase)

Smooth and smoother transition.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `bool` | [`bSmootherStep`](#bsmootherstep)  |  |

---

#### bSmootherStep { #bsmootherstep }

```cpp
bool bSmootherStep
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `FComposableCameraPose` | [`OnEvaluate_Implementation`](#onevaluate_implementation-4) `virtual` |  |

---

#### OnEvaluate_Implementation { #onevaluate_implementation-4 }

`virtual`

```cpp
virtual FComposableCameraPose OnEvaluate_Implementation(float DeltaTime, const FComposableCameraPose & CurrentSourcePose, const FComposableCameraPose & CurrentTargetPose)
```
