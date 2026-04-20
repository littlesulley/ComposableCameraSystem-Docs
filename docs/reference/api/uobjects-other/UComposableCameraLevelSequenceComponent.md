
# UComposableCameraLevelSequenceComponent { #ucomposablecameralevelsequencecomponent }

```cpp
#include <ComposableCameraLevelSequenceComponent.h>
```

> **Inherits:** `UActorComponent`

Actor component that drives a composable camera in the Level Sequence path.

Holds a [FComposableCameraTypeAssetReference](../structs/FComposableCameraTypeAssetReference.md#fcomposablecameratypeassetreference) (TypeAsset + editable Parameters / Variables bags) and references an OutputCineCameraComponent on the same Actor. On activation, the component spawns a transient [AComposableCameraCameraBase](../actors/AComposableCameraCameraBase.md#acomposablecameracamerabase), runs its nodes each tick (without a PlayerCameraManager), and projects the resulting pose onto the CineCamera so Sequencer's Camera Cut Track and viewport Pilot both see the CCS camera natively via the standard UCameraComponent path.

Pure UActorComponent — NOT a USceneComponent. The component holds no transform of its own; it is a logic-and-data driver. The owning Actor is expected to provide a UCineCameraComponent as its RootComponent (that's what [AComposableCameraLevelSequenceActor](../actors/AComposableCameraLevelSequenceActor.md#acomposablecameralevelsequenceactor) does), and to hand us the reference via OutputCineCameraComponent during construction. If a designer adds this component to an arbitrary Actor (BlueprintSpawnableComponent), OnRegister falls back to FindComponentByClass<UCineCameraComponent>(GetOwner()) — the component will then drive whatever CineCamera is first found on the owning Actor, or be a no-op if none exists.

Why ActorComponent not SceneComponent ───────────────────────────────────── Previously this was a USceneComponent whose RootComponent role doubled as a parent for the CineCamera child. That arrangement collided with [UE](#ue)'s DefaultSubobject semantics (a component creating its own CreateDefaultSubobject<UCineCameraComponent> registered the CineCamera as a sub-subobject of the component, invisible to the Actor's component tree and therefore invisible to USceneComponent::GetChildrenComponents and AActor::FindComponentByClass<UCameraComponent>). PCM::SetViewTarget's implicit-activation filter relies on that traversal and silently bailed, which manifested as "second camera never activates" for blended Camera Cut sections — see the diagnostic log that uncovered it.

With the CineCamera as the Actor's RootComponent and this component as a plain sibling UActorComponent, the engine's standard "find a CameraComponent
on the actor" path trivially finds the root, PCM::SetViewTarget creates the proxy, and we go down the same fast path ACineCameraActor uses. No special-case walks needed.

Compatibility & responsibilities remain unchanged:

* PCM-independent evaluation (via [UE::ComposableCameras::ConstructCameraFromTypeAsset](../free-functions/Functions.md#constructcamerafromtypeasset)).

* Per-tick bag → RuntimeDataBlock re-sync before TickCamera.

* Pose projection to OutputCineCameraComponent (position + rotation only).

* On-demand tick gating via SetEvaluationEnabled.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FComposableCameraTypeAssetReference` | [`TypeAssetReference`](#typeassetreference)  | The TypeAsset reference + its per-instance parameter and variable bags. Editing TypeAsset from the Details panel rebuilds the bags on PostEditChangeProperty; editing individual parameter values rebuilds the internal camera so the new values are reflected in the pose. Not BlueprintReadWrite: the nested FInstancedPropertyBag fields are not Blueprint-supported (see the struct comment). |
| `TObjectPtr< UCineCameraComponent >` | [`OutputCineCameraComponent`](#outputcinecameracomponent)  | Reference to the Actor's UCineCameraComponent used as the viewport terminal. Assigned by the owning Actor's constructor (primary path) or resolved in OnRegister via FindComponentByClass (fallback for arbitrary Actor hosts). The component does not own lifetime of the CineCamera — the Actor does. |

---

#### TypeAssetReference { #typeassetreference }

```cpp
FComposableCameraTypeAssetReference TypeAssetReference
```

The TypeAsset reference + its per-instance parameter and variable bags. Editing TypeAsset from the Details panel rebuilds the bags on PostEditChangeProperty; editing individual parameter values rebuilds the internal camera so the new values are reflected in the pose. Not BlueprintReadWrite: the nested FInstancedPropertyBag fields are not Blueprint-supported (see the struct comment).

---

#### OutputCineCameraComponent { #outputcinecameracomponent }

```cpp
TObjectPtr< UCineCameraComponent > OutputCineCameraComponent
```

Reference to the Actor's UCineCameraComponent used as the viewport terminal. Assigned by the owning Actor's constructor (primary path) or resolved in OnRegister via FindComponentByClass (fallback for arbitrary Actor hosts). The component does not own lifetime of the CineCamera — the Actor does.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`UComposableCameraLevelSequenceComponent`](#ucomposablecameralevelsequencecomponent-1)  |  |
| `void` | [`OnRegister`](#onregister) `virtual` |  |
| `void` | [`BeginPlay`](#beginplay-3) `virtual` |  |
| `void` | [`EndPlay`](#endplay-2) `virtual` |  |
| `void` | [`TickComponent`](#tickcomponent) `virtual` |  |
| `void` | [`SetEvaluationEnabled`](#setevaluationenabled)  | Gate for on-demand ticking. Default: false — a future ECS parameter instantiator can flip this to true when the component is actively the Camera Cut target or a participant in a running blend. The V1.4 simplified path auto-enables from OnRegister so every spawned LS actor ticks while the Spawnable is alive; the gating hook is kept as a forward-compat surface. |
| `bool` | [`IsEvaluationEnabled`](#isevaluationenabled) `const` `inline` |  |
| `void` | [`SetParameterValue`](#setparametervalue)  | Forward-compat hooks for a future ECS instantiator. The V1.4 simplified path doesn't route through these — Sequencer's stock property tracks write the bag directly and the per-tick ApplyParameterBlock picks it up. Left in place (as no-ops) so external integrations don't have to be re-wired when a proper instantiator is added later. |
| `void` | [`SetVariableValue`](#setvariablevalue)  |  |
| `AComposableCameraCameraBase *` | [`GetInternalCamera`](#getinternalcamera) `const` `inline` | Access the internal camera for editor-side inspection / debugging. |

---

#### UComposableCameraLevelSequenceComponent { #ucomposablecameralevelsequencecomponent-1 }

```cpp
UComposableCameraLevelSequenceComponent()
```

---

#### OnRegister { #onregister }

`virtual`

```cpp
virtual void OnRegister()
```

---

#### BeginPlay { #beginplay-3 }

`virtual`

```cpp
virtual void BeginPlay()
```

---

#### EndPlay { #endplay-2 }

`virtual`

```cpp
virtual void EndPlay(const EEndPlayReason::Type EndPlayReason)
```

---

#### TickComponent { #tickcomponent }

`virtual`

```cpp
virtual void TickComponent(float DeltaTime, ELevelTick TickType, FActorComponentTickFunction * ThisTickFunction)
```

---

#### SetEvaluationEnabled { #setevaluationenabled }

```cpp
void SetEvaluationEnabled(bool bEnabled)
```

Gate for on-demand ticking. Default: false — a future ECS parameter instantiator can flip this to true when the component is actively the Camera Cut target or a participant in a running blend. The V1.4 simplified path auto-enables from OnRegister so every spawned LS actor ticks while the Spawnable is alive; the gating hook is kept as a forward-compat surface.

Toggling to false tears down the internal camera so the Actor can go fully idle; toggling back to true respawns it lazily on the first tick.

---

#### IsEvaluationEnabled { #isevaluationenabled }

`const` `inline`

```cpp
inline bool IsEvaluationEnabled() const
```

---

#### SetParameterValue { #setparametervalue }

```cpp
void SetParameterValue(FName Name, const void * Value, EComposableCameraPinType Type)
```

Forward-compat hooks for a future ECS instantiator. The V1.4 simplified path doesn't route through these — Sequencer's stock property tracks write the bag directly and the per-tick ApplyParameterBlock picks it up. Left in place (as no-ops) so external integrations don't have to be re-wired when a proper instantiator is added later.

---

#### SetVariableValue { #setvariablevalue }

```cpp
void SetVariableValue(FName Name, const void * Value, EComposableCameraPinType Type)
```

---

#### GetInternalCamera { #getinternalcamera }

`const` `inline`

```cpp
inline AComposableCameraCameraBase * GetInternalCamera() const
```

Access the internal camera for editor-side inspection / debugging.

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TObjectPtr< AComposableCameraCameraBase >` | [`InternalCamera`](#internalcamera)  | Transient internal camera — spawned lazily on first evaluation. Not added to any context stack or director; driven entirely by this component's TickComponent. |
| `bool` | [`bEvaluationEnabled`](#bevaluationenabled)  | Gate for on-demand ticking; see SetEvaluationEnabled. |

---

#### InternalCamera { #internalcamera }

```cpp
TObjectPtr< AComposableCameraCameraBase > InternalCamera
```

Transient internal camera — spawned lazily on first evaluation. Not added to any context stack or director; driven entirely by this component's TickComponent.

---

#### bEvaluationEnabled { #bevaluationenabled }

```cpp
bool bEvaluationEnabled = false
```

Gate for on-demand ticking; see SetEvaluationEnabled.

### Private Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`EnsureInternalCamera`](#ensureinternalcamera)  | Spawn InternalCamera if it doesn't exist yet, then call ConstructCameraFromTypeAsset with the current bag values. Safe to call repeatedly; reuses an existing camera when the TypeAsset hasn't changed. |
| `void` | [`RebuildInternalCamera`](#rebuildinternalcamera)  | Destroy InternalCamera and spawn a fresh one. Called from PostEditChangeProperty when TypeAsset changes. |
| `void` | [`ProjectPoseToCineCamera`](#projectposetocinecamera)  | Project a pose into OutputCineCameraComponent. Position and rotation are the only fields written; physical optics stay on the CineCamera (designer or Sequencer property tracks drive them). |
| `void` | [`DestroyInternalCamera`](#destroyinternalcamera)  | Destroy the internal camera actor if one exists. |

---

#### EnsureInternalCamera { #ensureinternalcamera }

```cpp
void EnsureInternalCamera()
```

Spawn InternalCamera if it doesn't exist yet, then call ConstructCameraFromTypeAsset with the current bag values. Safe to call repeatedly; reuses an existing camera when the TypeAsset hasn't changed.

---

#### RebuildInternalCamera { #rebuildinternalcamera }

```cpp
void RebuildInternalCamera()
```

Destroy InternalCamera and spawn a fresh one. Called from PostEditChangeProperty when TypeAsset changes.

---

#### ProjectPoseToCineCamera { #projectposetocinecamera }

```cpp
void ProjectPoseToCineCamera(const FComposableCameraPose & Pose)
```

Project a pose into OutputCineCameraComponent. Position and rotation are the only fields written; physical optics stay on the CineCamera (designer or Sequencer property tracks drive them).

---

#### DestroyInternalCamera { #destroyinternalcamera }

```cpp
void DestroyInternalCamera()
```

Destroy the internal camera actor if one exists.
