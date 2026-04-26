
# UComposableCameraDirector { #ucomposablecameradirector }

```cpp
#include <ComposableCameraDirector.h>
```

> **Inherits:** `UObject`

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`UComposableCameraDirector`](#ucomposablecameradirector-1)  |  |
| `AComposableCameraCameraBase *` | [`ResumeCamera`](#resumecamera)  |  |
| `AComposableCameraCameraBase *` | [`CreateNewCamera`](#createnewcamera)  |  |
| `AComposableCameraCameraBase *` | [`ActivateNewCamera`](#activatenewcamera)  |  |
| `AComposableCameraCameraBase *` | [`ActivateNewCamera`](#activatenewcamera-1)  | Activate a new camera using a raw transition instance (not wrapped in a DataAsset). Used by ActivateNewCameraFromTypeAsset when the type asset provides its own DefaultTransition as an instanced UComposableCameraTransitionBase*. The transition is duplicated into the Director's context before use. |
| `AComposableCameraCameraBase *` | [`ActivateNewCameraWithReferenceSource`](#activatenewcamerawithreferencesource)  | Activate a new camera with a reference to another Director as the transition source. Used for inter-context transitions: the reference leaf evaluates the source Director live. |
| `AComposableCameraCameraBase *` | [`ActivateNewCameraWithReferenceSource`](#activatenewcamerawithreferencesource-1)  | Inter-context activation using a raw transition instance. Used by ActivateNewCameraFromTypeAsset when the type asset provides a DefaultTransition. |
| `AComposableCameraCameraBase *` | [`ResumeCurrentCameraWithReferenceSource`](#resumecurrentcamerawithreferencesource)  | Resume this director's ALREADY-RUNNING camera with an inter-context transition whose source is `SourceDirector`'s output. |
| `AComposableCameraCameraBase *` | [`ReactivateCurrentCamera`](#reactivatecurrentcamera)  |  |
| `FComposableCameraPose` | [`Evaluate`](#evaluate)  |  |
| `AComposableCameraCameraBase *` | [`GetRunningCamera`](#getrunningcamera) `const` `inline` | Get the currently running (target) camera in this Director's evaluation tree. |
| `UComposableCameraEvaluationTree *` | [`GetEvaluationTree`](#getevaluationtree) `const` `inline` | Read-only access to the director's evaluation tree. Intended for debug tooling (viewport debug transition walker, snapshot builders, tests). Returns the raw pointer — do not cache it across activations, since the tree is torn down with the director. |
| `UComposableCameraPatchManager *` | [`GetPatchManager`](#getpatchmanager) `const` `inline` | Access to this director's PatchManager — owner of active CameraPatches. Lifetime: created in the director ctor, destroyed with the director. Stage 1 has the manager wired through but its Apply pass is a no-op stub (see [UComposableCameraPatchManager](../uobjects-other/UComposableCameraPatchManager.md#ucomposablecamerapatchmanager) doc comment for the staging plan). |
| `const FComposableCameraPose &` | [`GetLastEvaluatedPose`](#getlastevaluatedpose) `const` `inline` | Get the last evaluated (blended) pose from this Director. |
| `const FComposableCameraPose &` | [`GetPreviousEvaluatedPose`](#getpreviousevaluatedpose) `const` `inline` | Get the previous frame's evaluated (blended) pose from this Director. |
| `void` | [`DestroyAllCameras`](#destroyallcameras)  | Destroy all cameras in this Director's evaluation tree. Called when a context is popped. |
| `void` | [`BuildDebugSnapshot`](#builddebugsnapshot) `const` | Populate the context snapshot's director-owned fields: RunningCameraDisplay, LastPose, and the flattened TreeNodes (via the evaluation tree). The ContextName / active / base / pending-destroy flags are populated by the caller ([UComposableCameraContextStack::BuildDebugSnapshot](UComposableCameraContextStack.md#builddebugsnapshot-1)) since only the stack knows its own structure. |

---

#### UComposableCameraDirector { #ucomposablecameradirector-1 }

```cpp
UComposableCameraDirector(const FObjectInitializer & ObjectInitializer)
```

---

#### ResumeCamera { #resumecamera }

```cpp
AComposableCameraCameraBase * ResumeCamera(AComposableCameraCameraBase * ResumeCamera, UComposableCameraTransitionBase * Transition, const FTransform & Transform)
```

---

#### CreateNewCamera { #createnewcamera }

```cpp
AComposableCameraCameraBase * CreateNewCamera(AComposableCameraPlayerCameraManager * PlayerCameraManager, TSubclassOf< AComposableCameraCameraBase > CameraClass, const FComposableCameraActivateParams & ActivationParams)
```

---

#### ActivateNewCamera { #activatenewcamera }

```cpp
AComposableCameraCameraBase * ActivateNewCamera(AComposableCameraPlayerCameraManager * PlayerCameraManager, TSubclassOf< AComposableCameraCameraBase > CameraClass, UComposableCameraTransitionDataAsset * TransitionDataAsset, const FComposableCameraActivateParams & ActivationParams, FOnCameraFinishConstructed OnPreBeginplayEvent)
```

---

#### ActivateNewCamera { #activatenewcamera-1 }

```cpp
AComposableCameraCameraBase * ActivateNewCamera(AComposableCameraPlayerCameraManager * PlayerCameraManager, TSubclassOf< AComposableCameraCameraBase > CameraClass, UComposableCameraTransitionBase * TransitionInstance, const FComposableCameraActivateParams & ActivationParams, FOnCameraFinishConstructed OnPreBeginplayEvent)
```

Activate a new camera using a raw transition instance (not wrapped in a DataAsset). Used by ActivateNewCameraFromTypeAsset when the type asset provides its own DefaultTransition as an instanced UComposableCameraTransitionBase*. The transition is duplicated into the Director's context before use.

---

#### ActivateNewCameraWithReferenceSource { #activatenewcamerawithreferencesource }

```cpp
AComposableCameraCameraBase * ActivateNewCameraWithReferenceSource(AComposableCameraPlayerCameraManager * PlayerCameraManager, TSubclassOf< AComposableCameraCameraBase > CameraClass, UComposableCameraTransitionDataAsset * TransitionDataAsset, const FComposableCameraActivateParams & ActivationParams, FOnCameraFinishConstructed OnPreBeginplayEvent, UComposableCameraDirector * SourceDirector, UComposableCameraTransitionBase ** OutTransition)
```

Activate a new camera with a reference to another Director as the transition source. Used for inter-context transitions: the reference leaf evaluates the source Director live.

---

#### ActivateNewCameraWithReferenceSource { #activatenewcamerawithreferencesource-1 }

```cpp
AComposableCameraCameraBase * ActivateNewCameraWithReferenceSource(AComposableCameraPlayerCameraManager * PlayerCameraManager, TSubclassOf< AComposableCameraCameraBase > CameraClass, UComposableCameraTransitionBase * TransitionInstance, const FComposableCameraActivateParams & ActivationParams, FOnCameraFinishConstructed OnPreBeginplayEvent, UComposableCameraDirector * SourceDirector, UComposableCameraTransitionBase ** OutTransition)
```

Inter-context activation using a raw transition instance. Used by ActivateNewCameraFromTypeAsset when the type asset provides a DefaultTransition.

`OutTransition` (optional): the duplicated transition instance installed in the tree's new Inner. Callers that need to bind cleanup to the activation's lifecycle (e.g. the context stack, which demotes non-top transient contexts to PendingDestroyEntries and clears them from this transition's `OnTransitionFinishesDelegate`) read it via this out-parameter.

---

#### ResumeCurrentCameraWithReferenceSource { #resumecurrentcamerawithreferencesource }

```cpp
AComposableCameraCameraBase * ResumeCurrentCameraWithReferenceSource(AComposableCameraPlayerCameraManager * PlayerCameraManager, UComposableCameraTransitionBase * TransitionInstance, UComposableCameraDirector * SourceDirector, bool bFreezeSourceCamera)
```

Resume this director's ALREADY-RUNNING camera with an inter-context transition whose source is `SourceDirector`'s output.

Unlike `ActivateNewCameraWithReferenceSource`, this path does NOT spawn a new camera and does NOT destroy the current one — the existing `RunningCamera` stays in place and keeps all its per-node state (damping, interpolator, spline progress, etc.). The only mutation to the tree is wrapping its current `RootNode` as the right child of a new Inner node holding the pop transition + a `RefLeaf→SourceDirector` as the left child.

This is the correct code path for context-stack pops: the camera that was running before the push should resume with no state reset. Treat `ActivateNewCameraWithReferenceSource` as the "switch to a
fresh instance" path (used for pushes / new activations) and this as the "preserve existing instance" path.

**Parameters**

* `PlayerCameraManager` Owning PCM, used for DeltaTime on transition init. 

* `TransitionInstance` Already-duplicated transition (caller owns the DuplicateObject). 

* `SourceDirector` The popped director to reference as the blend source. 

* `bFreezeSourceCamera` If true, the RefLeaf returns SourceDirector's cached LastEvaluatedPose every frame instead of re-evaluating — use when the source context is about to be destroyed and its live evaluation would be wasted work. 

**Returns**

The resumed (unchanged) camera, or nullptr if the tree had no camera to resume.

---

#### ReactivateCurrentCamera { #reactivatecurrentcamera }

```cpp
AComposableCameraCameraBase * ReactivateCurrentCamera(AComposableCameraPlayerCameraManager * PlayerCameraManager, TSubclassOf< AComposableCameraCameraBase > CameraClass, UComposableCameraTransitionBase * Transition, const FOnCameraFinishConstructed & OnPreBeginplayEvent)
```

---

#### Evaluate { #evaluate }

```cpp
FComposableCameraPose Evaluate(float DeltaTime)
```

---

#### GetRunningCamera { #getrunningcamera }

`const` `inline`

```cpp
inline AComposableCameraCameraBase * GetRunningCamera() const
```

Get the currently running (target) camera in this Director's evaluation tree.

---

#### GetEvaluationTree { #getevaluationtree }

`const` `inline`

```cpp
inline UComposableCameraEvaluationTree * GetEvaluationTree() const
```

Read-only access to the director's evaluation tree. Intended for debug tooling (viewport debug transition walker, snapshot builders, tests). Returns the raw pointer — do not cache it across activations, since the tree is torn down with the director.

---

#### GetPatchManager { #getpatchmanager }

`const` `inline`

```cpp
inline UComposableCameraPatchManager * GetPatchManager() const
```

Access to this director's PatchManager — owner of active CameraPatches. Lifetime: created in the director ctor, destroyed with the director. Stage 1 has the manager wired through but its Apply pass is a no-op stub (see [UComposableCameraPatchManager](../uobjects-other/UComposableCameraPatchManager.md#ucomposablecamerapatchmanager) doc comment for the staging plan).

---

#### GetLastEvaluatedPose { #getlastevaluatedpose }

`const` `inline`

```cpp
inline const FComposableCameraPose & GetLastEvaluatedPose() const
```

Get the last evaluated (blended) pose from this Director.

---

#### GetPreviousEvaluatedPose { #getpreviousevaluatedpose }

`const` `inline`

```cpp
inline const FComposableCameraPose & GetPreviousEvaluatedPose() const
```

Get the previous frame's evaluated (blended) pose from this Director.

---

#### DestroyAllCameras { #destroyallcameras }

```cpp
void DestroyAllCameras()
```

Destroy all cameras in this Director's evaluation tree. Called when a context is popped.

---

#### BuildDebugSnapshot { #builddebugsnapshot }

`const`

```cpp
void BuildDebugSnapshot(FComposableCameraContextSnapshot & OutSnapshot) const
```

Populate the context snapshot's director-owned fields: RunningCameraDisplay, LastPose, and the flattened TreeNodes (via the evaluation tree). The ContextName / active / base / pending-destroy flags are populated by the caller ([UComposableCameraContextStack::BuildDebugSnapshot](UComposableCameraContextStack.md#builddebugsnapshot-1)) since only the stack knows its own structure.

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `UComposableCameraEvaluationTree *` | [`EvaluationTree`](#evaluationtree)  |  |
| `AComposableCameraCameraBase *` | [`RunningCamera`](#runningcamera)  |  |
| `TObjectPtr< UComposableCameraPatchManager >` | [`PatchManager`](#patchmanager)  |  |
| `FComposableCameraPose` | [`LastEvaluatedPose`](#lastevaluatedpose)  | Cached blended pose from the last [Evaluate()](#evaluate) call — represents the Director's actual output. |
| `FComposableCameraPose` | [`PreviousEvaluatedPose`](#previousevaluatedpose)  | Previous frame's blended pose — used for velocity estimation in transitions. |

---

#### EvaluationTree { #evaluationtree }

```cpp
UComposableCameraEvaluationTree * EvaluationTree { nullptr }
```

---

#### RunningCamera { #runningcamera }

```cpp
AComposableCameraCameraBase * RunningCamera { nullptr }
```

---

#### PatchManager { #patchmanager }

```cpp
TObjectPtr< UComposableCameraPatchManager > PatchManager
```

---

#### LastEvaluatedPose { #lastevaluatedpose }

```cpp
FComposableCameraPose LastEvaluatedPose
```

Cached blended pose from the last [Evaluate()](#evaluate) call — represents the Director's actual output.

---

#### PreviousEvaluatedPose { #previousevaluatedpose }

```cpp
FComposableCameraPose PreviousEvaluatedPose
```

Previous frame's blended pose — used for velocity estimation in transitions.

### Private Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`ForceCameraPoses`](#forcecameraposes)  |  |

---

#### ForceCameraPoses { #forcecameraposes }

```cpp
void ForceCameraPoses(AComposableCameraCameraBase * Camera, const FTransform & Transform)
```
