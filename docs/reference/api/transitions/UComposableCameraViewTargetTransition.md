
# UComposableCameraViewTargetTransition { #ucomposablecameraviewtargettransition }

```cpp
#include <ComposableCameraViewTargetTransition.h>
```

> **Inherits:** [`UComposableCameraTransitionBase`](UComposableCameraTransitionBase.md#ucomposablecameratransitionbase)

A transition that emulates the engine's built-in view-target blend curves.

Created programmatically by the PCM's `SetViewTarget` override when external code (engine CameraCut handler, gameplay Possess, `SetViewTargetWithBlend`, etc.) calls `SetViewTarget` with non-zero `FViewTargetTransitionParams`. The transition delegates blend-curve evaluation to `FViewTargetTransitionParams::GetBlendAlpha()`, so every `EViewTargetBlendFunction` the engine supports is automatically available.

This class is NOT meant to be placed in a transition data asset by designers. It exists solely as the bridge between the engine's `SetViewTarget` blend params and CCS's pose-only transition system.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`InitFromViewTargetParams`](#initfromviewtargetparams)  | Initialize from engine transition params. Sets TransitionTime from BlendTime. |
| `FComposableCameraPose` | [`OnEvaluate_Implementation`](#onevaluate_implementation) `virtual` |  |

---

#### InitFromViewTargetParams { #initfromviewtargetparams }

```cpp
void InitFromViewTargetParams(const FViewTargetTransitionParams & InParams)
```

Initialize from engine transition params. Sets `TransitionTime` from `BlendTime`.

---

#### OnEvaluate_Implementation { #onevaluate_implementation }

`virtual`

```cpp
virtual FComposableCameraPose OnEvaluate_Implementation(float DeltaTime, const FComposableCameraPose & CurrentSourcePose, const FComposableCameraPose & CurrentTargetPose)
```
