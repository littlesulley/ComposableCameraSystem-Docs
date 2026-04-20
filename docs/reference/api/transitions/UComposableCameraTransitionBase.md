
# UComposableCameraTransitionBase { #ucomposablecameratransitionbase }

```cpp
#include <ComposableCameraTransitionBase.h>
```

> **Inherits:** `UObject`
> **Subclassed by:** [`UComposableCameraCubicTransition`](UComposableCameraCubicTransition.md#ucomposablecameracubictransition), [`UComposableCameraCylindricalTransition`](UComposableCameraCylindricalTransition.md#ucomposablecameracylindricaltransition), [`UComposableCameraDynamicDeocclusionTransition`](UComposableCameraDynamicDeocclusionTransition.md#ucomposablecameradynamicdeocclusiontransition), [`UComposableCameraEaseTransition`](UComposableCameraEaseTransition.md#ucomposablecameraeasetransition), [`UComposableCameraInertializedTransition`](UComposableCameraInertializedTransition.md#ucomposablecamerainertializedtransition), [`UComposableCameraLinearTransition`](UComposableCameraLinearTransition.md#ucomposablecameralineartransition), [`UComposableCameraPathGuidedTransition`](UComposableCameraPathGuidedTransition.md#ucomposablecamerapathguidedtransition), [`UComposableCameraSmoothTransition`](UComposableCameraSmoothTransition.md#ucomposablecamerasmoothtransition), [`UComposableCameraSplineTransition`](UComposableCameraSplineTransition.md#ucomposablecamerasplinetransition), [`UComposableCameraViewTargetTransition`](UComposableCameraViewTargetTransition.md#ucomposablecameraviewtargettransition)

Base class for transition evaluation.

Transitions are pose-only operators: they receive source and target poses each tick, maintain their own internal blend state, and output a blended pose. They never reference cameras or Directors directly.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FOnTransitionFinishes` | [`OnTransitionFinishesDelegate`](#ontransitionfinishesdelegate)  |  |

---

#### OnTransitionFinishesDelegate { #ontransitionfinishesdelegate }

```cpp
FOnTransitionFinishes OnTransitionFinishesDelegate
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `FComposableCameraPose` | [`Evaluate`](#evaluate-6)  | Evaluate the transition for this frame, blending between source and target poses. |
| `void` | [`TransitionEnabled`](#transitionenabled)  | Initialize the transition with source pose data. Called once before the first Evaluate. |
| `void` | [`TransitionFinished`](#transitionfinished)  | Mark the transition as finished. |
| `void` | [`SetTransitionTime`](#settransitiontime)  |  |
| `void` | [`ResetTransitionState`](#resettransitionstate)  |  |
| `bool` | [`IsFinished`](#isfinished-1) `const` `inline` |  |
| `float` | [`GetRemainingTime`](#getremainingtime) `const` `inline` |  |
| `float` | [`GetTransitionTime`](#gettransitiontime) `const` `inline` |  |
| `float` | [`GetPercentage`](#getpercentage) `const` `inline` |  |

---

#### Evaluate { #evaluate-6 }

```cpp
FComposableCameraPose Evaluate(float DeltaTime, const FComposableCameraPose & CurrentSourcePose, const FComposableCameraPose & CurrentTargetPose)
```

Evaluate the transition for this frame, blending between source and target poses.

---

#### TransitionEnabled { #transitionenabled }

```cpp
void TransitionEnabled(const FComposableCameraTransitionInitParams & InInitParams)
```

Initialize the transition with source pose data. Called once before the first Evaluate.

---

#### TransitionFinished { #transitionfinished }

```cpp
void TransitionFinished()
```

Mark the transition as finished.

---

#### SetTransitionTime { #settransitiontime }

```cpp
void SetTransitionTime(float NewTransitionTime)
```

---

#### ResetTransitionState { #resettransitionstate }

```cpp
void ResetTransitionState()
```

---

#### IsFinished { #isfinished-1 }

`const` `inline`

```cpp
inline bool IsFinished() const
```

---

#### GetRemainingTime { #getremainingtime }

`const` `inline`

```cpp
inline float GetRemainingTime() const
```

---

#### GetTransitionTime { #gettransitiontime }

`const` `inline`

```cpp
inline float GetTransitionTime() const
```

---

#### GetPercentage { #getpercentage }

`const` `inline`

```cpp
inline float GetPercentage() const
```

### Protected Attributes

| Return | Name | Description |
|--------|------|-------------|
| `float` | [`TransitionTime`](#transitiontime)  |  |
| `float` | [`RemainingTime`](#remainingtime)  |  |
| `bool` | [`bFinished`](#bfinished)  |  |
| `bool` | [`bFirstFrame`](#bfirstframe)  |  |
| `FComposableCameraTransitionInitParams` | [`InitParams`](#initparams)  |  |
| `float` | [`Percentage`](#percentage)  |  |

---

#### TransitionTime { #transitiontime }

```cpp
float TransitionTime
```

---

#### RemainingTime { #remainingtime }

```cpp
float RemainingTime
```

---

#### bFinished { #bfinished }

```cpp
bool bFinished { false }
```

---

#### bFirstFrame { #bfirstframe }

```cpp
bool bFirstFrame { true }
```

---

#### InitParams { #initparams }

```cpp
FComposableCameraTransitionInitParams InitParams
```

---

#### Percentage { #percentage }

```cpp
float Percentage { 0.f }
```

### Protected Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`OnBeginPlay`](#onbeginplay)  | Begin Play event. Called on the first frame of the transition, before the first OnEvaluate. <br/> |
| `void` | [`OnBeginPlay_Implementation`](#onbeginplay_implementation) `virtual` `inline` |  |
| `FComposableCameraPose` | [`OnEvaluate`](#onevaluate)  | Event to customize the evaluation function for each tick. When calling this function, RemainingTime has already been decremented, and assured to not go below 0. <br/> |
| `FComposableCameraPose` | [`OnEvaluate_Implementation`](#onevaluate_implementation-1) `virtual` `inline` |  |
| `void` | [`OnFinished`](#onfinished)  | Event when the transition finishes. The base class simply sets bFinished to true. |

---

#### OnBeginPlay { #onbeginplay }

```cpp
void OnBeginPlay(float DeltaTime, const FComposableCameraPose & CurrentSourcePose, const FComposableCameraPose & CurrentTargetPose)
```

Begin Play event. Called on the first frame of the transition, before the first OnEvaluate. <br/>
Use this to construct or initialize internal parameters specialized for this type of transition. <br/>

**Parameters**

* `DeltaTime` World delta time. <br/>

* `CurrentSourcePose` Current source camera pose. <br/>

* `CurrentTargetPose` Current target camera pose. <br/>

---

#### OnBeginPlay_Implementation { #onbeginplay_implementation }

`virtual` `inline`

```cpp
virtual inline void OnBeginPlay_Implementation(float DeltaTime, const FComposableCameraPose & CurrentSourcePose, const FComposableCameraPose & CurrentTargetPose)
```

---

#### OnEvaluate { #onevaluate }

```cpp
FComposableCameraPose OnEvaluate(float DeltaTime, const FComposableCameraPose & CurrentSourcePose, const FComposableCameraPose & CurrentTargetPose)
```

Event to customize the evaluation function for each tick. When calling this function, RemainingTime has already been decremented, and assured to not go below 0. <br/>

**Parameters**

* `DeltaTime` World delta time. <br/>

* `CurrentSourcePose` Current source camera pose. <br/>

* `CurrentTargetPose` Current target camera pose. <br/>

**Returns**

Returns the new blended camera pose.

---

#### OnEvaluate_Implementation { #onevaluate_implementation-1 }

`virtual` `inline`

```cpp
virtual inline FComposableCameraPose OnEvaluate_Implementation(float DeltaTime, const FComposableCameraPose & CurrentSourcePose, const FComposableCameraPose & CurrentTargetPose)
```

---

#### OnFinished { #onfinished }

```cpp
void OnFinished()
```

Event when the transition finishes. The base class simply sets bFinished to true.
