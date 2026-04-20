
# UComposableCameraComputeDistanceToActorNode { #ucomposablecameracomputedistancetoactornode }

```cpp
#include <ComposableCameraComputeDistanceToActorNode.h>
```

> **Inherits:** [`UComposableCameraComputeNodeBase`](../uobjects-other/UComposableCameraComputeNodeBase.md#ucomposablecameracomputenodebase)

Example compute node: measures the distance between two actors at camera activation and publishes the result.

Typical use case: at activation time, compute the distance between the player and a target, then feed that into downstream camera nodes to scale a boom arm length, set an initial FOV, or pick a blend weight — values that are sampled once and held stable for the camera's lifetime.

Inputs:

* ActorA (Actor): first actor (e.g. the player pawn)

* ActorB (Actor): second actor (e.g. the look-at target)

Outputs:

* Distance (Float): Euclidean distance between the two actors

* Direction (Vector3D): unit direction from ActorA to ActorB

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`ExecuteBeginPlay`](#executebeginplay-1) `virtual` | Execute this compute node's one-shot work. |
| `void` | [`GetPinDeclarations_Implementation`](#getpindeclarations_implementation-19) `virtual` `const` |  |

---

#### ExecuteBeginPlay { #executebeginplay-1 }

`virtual`

```cpp
virtual void ExecuteBeginPlay()
```

Execute this compute node's one-shot work.

Called from [AComposableCameraCameraBase::BeginPlayCamera](../actors/AComposableCameraCameraBase.md#beginplaycamera), after every node on the camera (both camera nodes and compute nodes) has already had [Initialize()](../uobjects-other/UComposableCameraCameraNodeBase.md#initialize-1) / [OnInitialize_Implementation()](../uobjects-other/UComposableCameraCameraNodeBase.md#oninitialize_implementation-3) run. By the time this fires, OwningCamera / OwningPlayerCameraManager / RuntimeDataBlock are all wired, so GetInputPinValue / SetOutputPinValue / Get/SetInternalVariable are all safe to use.

The outgoing camera pose (the pose the previous camera was evaluating before this one became active) is available via OwningPlayerCameraManager->GetCurrentCameraPose() — this is the same value AActor::BeginPlay used to pass into BeginPlayCamera as a parameter before Step 4a removed that argument.

Plain virtual (not a BlueprintNativeEvent) for 4a. If Blueprint authoring of compute nodes becomes a requirement later, promote this to a BlueprintNativeEvent following the same OnFoo / OnFoo_Implementation pattern used by OnInitialize and OnTickNode on the parent class.

---

#### GetPinDeclarations_Implementation { #getpindeclarations_implementation-19 }

`virtual` `const`

```cpp
virtual void GetPinDeclarations_Implementation(TArray< FComposableCameraNodePinDeclaration > & OutPins) const
```
