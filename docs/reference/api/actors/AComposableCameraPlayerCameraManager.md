
# AComposableCameraPlayerCameraManager { #acomposablecameraplayercameramanager }

```cpp
#include <ComposableCameraPlayerCameraManager.h>
```

> **Inherits:** `APlayerCameraManager`

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `bool` | [`bSyncToControlRotation`](#bsynctocontrolrotation)  |  |
| `FName` | [`CurrentContext`](#currentcontext)  |  |
| `AComposableCameraCameraBase *` | [`RunningCamera`](#runningcamera-2)  |  |
| `FComposableCameraPose` | [`CurrentCameraPose`](#currentcamerapose)  |  |
| `TSet< UComposableCameraActionBase * >` | [`CameraActions`](#cameraactions)  |  |
| `TArray< UComposableCameraActionBase * >` | [`CameraActionsRemovalScratch`](#cameraactionsremovalscratch)  | Per-frame scratch buffer for `UpdateActions`: collects pointers of expired/null actions during the iteration so the actual `Remove`s happen in a second pass (safe — TSet mutation during iteration is not). Member-scoped so the TArray's heap allocation amortizes across frames; `Reset()` keeps capacity. Earlier code constructed a fresh `TSet<UObject*>` every tick — TSet allocates a node per insert and may rehash, so even an empty set paid one heap alloc per frame and a populated set paid more. Move to a `TArray` of raw pointers since (a) we never look up by key, (b) actions can't appear twice in the source set so dedup-via-set buys nothing. |
| `TArray< TObjectPtr< UComposableCameraActionBase > >` | [`CameraActionsPendingAddScratch`](#cameraactionspendingaddscratch)  | Re-entrancy companion to `CameraActionsRemovalScratch`. When `bIsUpdatingActions` is set, `AddCameraAction` queues newly- constructed actions here instead of mutating `CameraActions` immediately; the post-loop sweep (after the removals sweep) drains this list, adding to `CameraActions` AND binding to RunningCamera in one shot. Net effect: an Action's `OnCanExecute` callback is allowed to call `PCM->AddCameraAction(...)` without invalidating the range- for iterator over `CameraActions`. The newly-added Action takes effect on the NEXT frame's UpdateActions tick (it does not retroactively join the iteration that spawned it). |
| `FOnCameraFinishConstructed` | [`CurrentOnPreBeginplayEvent`](#currentonprebeginplayevent)  |  |

---

#### bSyncToControlRotation { #bsynctocontrolrotation }

```cpp
bool bSyncToControlRotation { false }
```

---

#### CurrentContext { #currentcontext }

```cpp
FName CurrentContext
```

---

#### RunningCamera { #runningcamera-2 }

```cpp
AComposableCameraCameraBase * RunningCamera
```

---

#### CurrentCameraPose { #currentcamerapose }

```cpp
FComposableCameraPose CurrentCameraPose
```

---

#### CameraActions { #cameraactions }

```cpp
TSet< UComposableCameraActionBase * > CameraActions
```

---

#### CameraActionsRemovalScratch { #cameraactionsremovalscratch }

```cpp
TArray< UComposableCameraActionBase * > CameraActionsRemovalScratch
```

Per-frame scratch buffer for `UpdateActions`: collects pointers of expired/null actions during the iteration so the actual `Remove`s happen in a second pass (safe — TSet mutation during iteration is not). Member-scoped so the TArray's heap allocation amortizes across frames; `Reset()` keeps capacity. Earlier code constructed a fresh `TSet<UObject*>` every tick — TSet allocates a node per insert and may rehash, so even an empty set paid one heap alloc per frame and a populated set paid more. Move to a `TArray` of raw pointers since (a) we never look up by key, (b) actions can't appear twice in the source set so dedup-via-set buys nothing.

**Lifetime contract**: this scratch is intentionally NOT UPROPERTY and NOT TWeakObjectPtr. It must therefore be EMPTY whenever control is outside `UpdateActions` — `Reset()` runs both at the start AND at the end of the function so a GC sweep between frames cannot encounter stale raw `UObject*` entries here. Do not add any code path that leaves entries live across the function boundary; if a future use case requires that, switch the storage to `TArray<TWeakObjectPtr<[UComposableCameraActionBase](../actions/UComposableCameraActionBase.md#ucomposablecameraactionbase)>>`.

---

#### CameraActionsPendingAddScratch { #cameraactionspendingaddscratch }

```cpp
TArray< TObjectPtr< UComposableCameraActionBase > > CameraActionsPendingAddScratch
```

Re-entrancy companion to `CameraActionsRemovalScratch`. When `bIsUpdatingActions` is set, `AddCameraAction` queues newly- constructed actions here instead of mutating `CameraActions` immediately; the post-loop sweep (after the removals sweep) drains this list, adding to `CameraActions` AND binding to RunningCamera in one shot. Net effect: an Action's `OnCanExecute` callback is allowed to call `PCM->AddCameraAction(...)` without invalidating the range- for iterator over `CameraActions`. The newly-added Action takes effect on the NEXT frame's UpdateActions tick (it does not retroactively join the iteration that spawned it).

This list IS `UPROPERTY(Transient)` because — unlike `CameraActionsRemovalScratch` whose entries are still members of the GC-visible `CameraActions` TSet for the duration of the function — pending-add entries are freshly `NewObject`ed and have NOT been registered into any reflected container yet. A GC pass triggered re-entrantly from inside an Action's `OnCanExecute` (sync `LoadObject`, BP exception during eval, slow Blueprint that yields, etc.) would reclaim the half-constructed Action and the post-loop drain would then read a dangling pointer. The TObjectPtr inside a UPROPERTY array makes the Action root- reachable for the whole gap, closing that window without introducing any per-frame allocation cost (the array's storage amortises across activations the same way the raw form did).

---

#### CurrentOnPreBeginplayEvent { #currentonprebeginplayevent }

```cpp
FOnCameraFinishConstructed CurrentOnPreBeginplayEvent
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`AComposableCameraPlayerCameraManager`](#acomposablecameraplayercameramanager-1)  |  |
| `void` | [`BeginPlay`](#beginplay-2) `virtual` |  |
| `void` | [`InitializeFor`](#initializefor) `virtual` |  |
| `void` | [`SetViewTarget`](#setviewtarget) `virtual` |  |
| `void` | [`ProcessViewRotation`](#processviewrotation) `virtual` |  |
| `void` | [`DisplayDebug`](#displaydebug) `virtual` |  |
| `AComposableCameraCameraBase *` | [`CreateNewCamera`](#createnewcamera-1)  |  |
| `AComposableCameraCameraBase *` | [`ActivateNewCamera`](#activatenewcamera-2)  | Activate a new camera, optionally specifying which context it belongs to. If ContextName is valid and that context isn't on the stack yet, it is auto-pushed. If ContextName is NAME_None, the camera activates on the current active context. When switching to a different context, the new context's evaluation tree gets a reference leaf pointing to the previous context's Director for inter-context blending. |
| `AComposableCameraCameraBase *` | [`ActivateNewCamera`](#activatenewcamera-3)  | Activate a new camera using a raw transition instance (not wrapped in a DataAsset). Used internally by ActivateNewCameraFromTypeAsset when the type asset provides its own DefaultTransition as an instanced UComposableCameraTransitionBase*. |
| `AComposableCameraCameraBase *` | [`ActivateNewCameraFromTypeAsset`](#activatenewcamerafromtypeasset)  | Activate a new camera from a Camera Type Asset (data-driven workflow). Creates a default [AComposableCameraCameraBase](AComposableCameraCameraBase.md#acomposablecameracamerabase), duplicates node templates from the type asset, wires the RuntimeDataBlock, and applies caller-provided parameter values. |
| `AComposableCameraCameraBase *` | [`ReactivateCurrentCamera`](#reactivatecurrentcamera-1)  |  |
| `void` | [`ResumeCamera`](#resumecamera-1)  |  |
| `const TSet< UComposableCameraActionBase * > &` | [`GetCameraActions`](#getcameraactions)  |  |
| `void` | [`AddModifier`](#addmodifier-2)  |  |
| `void` | [`RemoveModifier`](#removemodifier-2)  |  |
| `void` | [`ApplyModifiers`](#applymodifiers-1)  |  |
| `void` | [`OnModifierChanged`](#onmodifierchanged)  |  |
| `UComposableCameraActionBase *` | [`AddCameraAction`](#addcameraaction)  |  |
| `UComposableCameraActionBase *` | [`FindCameraAction`](#findcameraaction)  |  |
| `void` | [`RemoveCameraAction`](#removecameraaction)  | Public API: fully remove an action — unbind from RunningCamera AND drop it from the `CameraActions` TSet so neither `FindCameraAction` returns it nor `BindCameraActionsForNewCamera` re-binds it onto the next camera. Previously this only unbound from RunningCamera, leaving the action strongly referenced by the PCM's TSet — external callers that expected "remove" semantics ended up with the action zombie-bound to every subsequent camera switch. |
| `void` | [`ExpireCameraAction`](#expirecameraaction)  |  |
| `void` | [`BindCameraActionsForNewCamera`](#bindcameraactionsfornewcamera)  |  |
| `void` | [`PopCameraContext`](#popcameracontext-1)  | Pop a specific camera context by name. If this is the active context, the previous context resumes with an optional transition. Cannot pop the base context if it is the last one remaining. |
| `void` | [`TerminateCurrentCamera`](#terminatecurrentcamera-1)  | Terminate the current camera context — pops the active (top) context off the stack. The previous context resumes with an optional transition. Cannot pop the base context. This is the explicit way to end a context. Transient cameras trigger this automatically. |
| `int32` | [`GetContextStackDepth`](#getcontextstackdepth) `const` | Get the number of contexts on the stack. |
| `FName` | [`GetActiveContextName`](#getactivecontextname-2) `const` | Get the name of the currently active (top) context. |
| `AComposableCameraCameraBase *` | [`GetRunningCamera`](#getrunningcamera-3) `const` `inline` |  |
| `FComposableCameraPose` | [`GetCurrentCameraPose`](#getcurrentcamerapose) `const` `inline` |  |
| `const UComposableCameraContextStack *` | [`GetContextStack`](#getcontextstack) `const` `inline` | Read-only access to the Tier-1 context stack. Intended for debug tooling ([FComposableCameraDebugPanel](../structs/FComposableCameraDebugPanel.md#fcomposablecameradebugpanel), editor inspectors, tests). Gameplay code should go through the PCM's ActivateCamera / Pop* methods — do not mutate the stack through this pointer. |
| `const UComposableCameraModifierManager *` | [`GetModifierManager`](#getmodifiermanager) `const` `inline` | Read-only access to the modifier manager. Intended for debug tooling ([FComposableCameraDebugPanel](../structs/FComposableCameraDebugPanel.md#fcomposablecameradebugpanel)'s Modifier region). Gameplay code should go through `AddModifier` / `RemoveModifier` on the PCM, which also triggers reactivation on change. |
| `void` | [`GetPoseHistory`](#getposehistory) `const` | Copy the per-frame pose history ring into `OutHistory`, oldest entry first. The PCM captures one entry per `DoUpdateCamera` tick after the current-frame pose is finalized; capacity caps at `PoseHistoryCapacity` frames (~2 s at 60 fps). |
| `UComposableCameraTransitionBase *` | [`ResolveTransition`](#resolvetransition) `const` | Resolve which transition to use when switching from one type-asset camera to another. Implements the five-tier resolution chain: |
| `FOnCameraFinishConstructed` | [`PrepareResumeCallback`](#prepareresumecallback)  | Prepare the pending type-asset state for a camera that is being resumed (e.g. after a context pop). If the camera was originally built from a type asset, this restores PendingTypeAsset / PendingParameterBlock and returns a callback bound to OnTypeAssetCameraConstructed. If not a type-asset camera, returns an empty (unbound) delegate. |

---

#### AComposableCameraPlayerCameraManager { #acomposablecameraplayercameramanager-1 }

```cpp
AComposableCameraPlayerCameraManager(const FObjectInitializer & ObjectInitializer)
```

---

#### BeginPlay { #beginplay-2 }

`virtual`

```cpp
virtual void BeginPlay()
```

---

#### InitializeFor { #initializefor }

`virtual`

```cpp
virtual void InitializeFor(APlayerController * PlayerController)
```

---

#### SetViewTarget { #setviewtarget }

`virtual`

```cpp
virtual void SetViewTarget(AActor * NewViewTarget, FViewTargetTransitionParams TransitionParams)
```

---

#### ProcessViewRotation { #processviewrotation }

`virtual`

```cpp
virtual void ProcessViewRotation(float DeltaTime, FRotator & OutViewRotation, FRotator & OutDeltaRot)
```

---

#### DisplayDebug { #displaydebug }

`virtual`

```cpp
virtual void DisplayDebug(class UCanvas * Canvas, const class FDebugDisplayInfo & DebugDisplay, float & YL, float & YPos)
```

---

#### CreateNewCamera { #createnewcamera-1 }

```cpp
AComposableCameraCameraBase * CreateNewCamera(TSubclassOf< AComposableCameraCameraBase > CameraClass, const FComposableCameraActivateParams & ActivationParams)
```

---

#### ActivateNewCamera { #activatenewcamera-2 }

```cpp
AComposableCameraCameraBase * ActivateNewCamera(TSubclassOf< AComposableCameraCameraBase > CameraClass, UComposableCameraTransitionDataAsset * Transition, const FComposableCameraActivateParams & ActivationParams, FOnCameraFinishConstructed OnPreBeginplayEvent, FName ContextName)
```

Activate a new camera, optionally specifying which context it belongs to. If ContextName is valid and that context isn't on the stack yet, it is auto-pushed. If ContextName is NAME_None, the camera activates on the current active context. When switching to a different context, the new context's evaluation tree gets a reference leaf pointing to the previous context's Director for inter-context blending.

---

#### ActivateNewCamera { #activatenewcamera-3 }

```cpp
AComposableCameraCameraBase * ActivateNewCamera(TSubclassOf< AComposableCameraCameraBase > CameraClass, UComposableCameraTransitionBase * TransitionInstance, const FComposableCameraActivateParams & ActivationParams, FOnCameraFinishConstructed OnPreBeginplayEvent, FName ContextName)
```

Activate a new camera using a raw transition instance (not wrapped in a DataAsset). Used internally by ActivateNewCameraFromTypeAsset when the type asset provides its own DefaultTransition as an instanced UComposableCameraTransitionBase*.

---

#### ActivateNewCameraFromTypeAsset { #activatenewcamerafromtypeasset }

```cpp
AComposableCameraCameraBase * ActivateNewCameraFromTypeAsset(UComposableCameraTypeAsset * CameraTypeAsset, UComposableCameraTransitionDataAsset * TransitionOverride, const FComposableCameraActivateParams & ActivationParams, const FComposableCameraParameterBlock & Parameters, FName ContextName)
```

Activate a new camera from a Camera Type Asset (data-driven workflow). Creates a default [AComposableCameraCameraBase](AComposableCameraCameraBase.md#acomposablecameracamerabase), duplicates node templates from the type asset, wires the RuntimeDataBlock, and applies caller-provided parameter values.

**Parameters**

* `CameraTypeAsset` The type asset defining the camera's node composition and parameters. 

* `TransitionOverride` Optional transition override. If nullptr, uses the type asset's DefaultTransition. 

* `ActivationParams` Standard activation parameters (transient, lifetime, pose preservation). 

* `Parameters` The caller-provided parameter block with exposed parameter values. 

* `ContextName` Context to activate in (NAME_None = current active context). 

**Returns**

The activated camera instance, or nullptr on failure.

---

#### ReactivateCurrentCamera { #reactivatecurrentcamera-1 }

```cpp
AComposableCameraCameraBase * ReactivateCurrentCamera(UComposableCameraTransitionBase * Transition)
```

---

#### ResumeCamera { #resumecamera-1 }

```cpp
void ResumeCamera(AComposableCameraCameraBase * ResumeCamera, UComposableCameraTransitionBase * Transition, EComposableCameraResumeCameraTransformSchema TransformSchema, FTransform SpecifiedTransform, bool bUseSpecifiedRotation)
```

---

#### GetCameraActions { #getcameraactions }

```cpp
const TSet< UComposableCameraActionBase * > & GetCameraActions()
```

---

#### AddModifier { #addmodifier-2 }

```cpp
void AddModifier(UComposableCameraNodeModifierDataAsset * ModifierAsset)
```

---

#### RemoveModifier { #removemodifier-2 }

```cpp
void RemoveModifier(UComposableCameraNodeModifierDataAsset * ModifierAsset)
```

---

#### ApplyModifiers { #applymodifiers-1 }

```cpp
void ApplyModifiers(AComposableCameraCameraBase * Camera, bool bRefreshModifierData)
```

---

#### OnModifierChanged { #onmodifierchanged }

```cpp
void OnModifierChanged()
```

---

#### AddCameraAction { #addcameraaction }

```cpp
UComposableCameraActionBase * AddCameraAction(TSubclassOf< UComposableCameraActionBase > ActionClass, bool bOnlyForCurrentCamera)
```

---

#### FindCameraAction { #findcameraaction }

```cpp
UComposableCameraActionBase * FindCameraAction(TSubclassOf< UComposableCameraActionBase > ActionClass)
```

---

#### RemoveCameraAction { #removecameraaction }

```cpp
void RemoveCameraAction(UComposableCameraActionBase * Action)
```

Public API: fully remove an action — unbind from RunningCamera AND drop it from the `CameraActions` TSet so neither `FindCameraAction` returns it nor `BindCameraActionsForNewCamera` re-binds it onto the next camera. Previously this only unbound from RunningCamera, leaving the action strongly referenced by the PCM's TSet — external callers that expected "remove" semantics ended up with the action zombie-bound to every subsequent camera switch.

---

#### ExpireCameraAction { #expirecameraaction }

```cpp
void ExpireCameraAction(TSubclassOf< UComposableCameraActionBase > ActionClass)
```

---

#### BindCameraActionsForNewCamera { #bindcameraactionsfornewcamera }

```cpp
void BindCameraActionsForNewCamera(AComposableCameraCameraBase * Camera)
```

---

#### PopCameraContext { #popcameracontext-1 }

```cpp
void PopCameraContext(FName ContextName, UComposableCameraTransitionDataAsset * TransitionOverride, const FComposableCameraActivateParams & ActivationParams)
```

Pop a specific camera context by name. If this is the active context, the previous context resumes with an optional transition. Cannot pop the base context if it is the last one remaining.

**Parameters**

* `ContextName` The name identifying which context to pop. 

* `TransitionOverride` Optional transition. If nullptr, falls back to the resume camera's DefaultTransition. 

* `ActivationParams` Optional activation params for the resume camera.

---

#### TerminateCurrentCamera { #terminatecurrentcamera-1 }

```cpp
void TerminateCurrentCamera(UComposableCameraTransitionDataAsset * TransitionOverride, const FComposableCameraActivateParams & ActivationParams)
```

Terminate the current camera context — pops the active (top) context off the stack. The previous context resumes with an optional transition. Cannot pop the base context. This is the explicit way to end a context. Transient cameras trigger this automatically.

**Parameters**

* `TransitionOverride` Optional transition. If nullptr, falls back to the resume camera's DefaultTransition. 

* `ActivationParams` Optional activation params for the resume camera.

---

#### GetContextStackDepth { #getcontextstackdepth }

`const`

```cpp
int32 GetContextStackDepth() const
```

Get the number of contexts on the stack.

---

#### GetActiveContextName { #getactivecontextname-2 }

`const`

```cpp
FName GetActiveContextName() const
```

Get the name of the currently active (top) context.

---

#### GetRunningCamera { #getrunningcamera-3 }

`const` `inline`

```cpp
inline AComposableCameraCameraBase * GetRunningCamera() const
```

---

#### GetCurrentCameraPose { #getcurrentcamerapose }

`const` `inline`

```cpp
inline FComposableCameraPose GetCurrentCameraPose() const
```

---

#### GetContextStack { #getcontextstack }

`const` `inline`

```cpp
inline const UComposableCameraContextStack * GetContextStack() const
```

Read-only access to the Tier-1 context stack. Intended for debug tooling ([FComposableCameraDebugPanel](../structs/FComposableCameraDebugPanel.md#fcomposablecameradebugpanel), editor inspectors, tests). Gameplay code should go through the PCM's ActivateCamera / Pop* methods — do not mutate the stack through this pointer.

---

#### GetModifierManager { #getmodifiermanager }

`const` `inline`

```cpp
inline const UComposableCameraModifierManager * GetModifierManager() const
```

Read-only access to the modifier manager. Intended for debug tooling ([FComposableCameraDebugPanel](../structs/FComposableCameraDebugPanel.md#fcomposablecameradebugpanel)'s Modifier region). Gameplay code should go through `AddModifier` / `RemoveModifier` on the PCM, which also triggers reactivation on change.

---

#### GetPoseHistory { #getposehistory }

`const`

```cpp
void GetPoseHistory(TArray< FComposableCameraPoseHistoryEntry > & OutHistory) const
```

Copy the per-frame pose history ring into `OutHistory`, oldest entry first. The PCM captures one entry per `DoUpdateCamera` tick after the current-frame pose is finalized; capacity caps at `PoseHistoryCapacity` frames (~2 s at 60 fps).

Debug-only consumer: the Pose History panel reads this every frame to render sparklines and hover tooltips. Not exposed to Blueprint — gameplay code should not depend on it.

In shipping builds this is a no-op returning an empty array (the ring itself is `#if !UE_BUILD_SHIPPING`). The signature is kept in all configurations so panel code can call it unconditionally without per-config `#if` guards at every call site.

---

#### ResolveTransition { #resolvetransition }

`const`

```cpp
UComposableCameraTransitionBase * ResolveTransition(const UComposableCameraTypeAsset * SourceTypeAsset, const UComposableCameraTypeAsset * TargetTypeAsset, UComposableCameraTransitionDataAsset * CallerOverride) const
```

Resolve which transition to use when switching from one type-asset camera to another. Implements the five-tier resolution chain:

1. CallerOverride (returned directly if non-null)

1. Transition table lookup (exact A→B pair from project settings)

1. Source's ExitTransition (SourceTypeAsset field — "always leave this way")

1. Target's EnterTransition (TargetTypeAsset field — "always enter this way")

1. nullptr (hard cut)

The table (tier 2) performs exact-match only — no wildcards. Per-camera ExitTransition and EnterTransition (tiers 3/4) serve as the per-camera fallbacks when no explicit pair is defined in the table.

**Parameters**

* `SourceTypeAsset` The type asset of the currently-running camera (may be nullptr). 

* `TargetTypeAsset` The type asset being activated (may be nullptr). 

* `CallerOverride` Explicit caller transition — if non-null, wins unconditionally. 

**Returns**

The resolved transition instance (owned by the type asset or table entry), or nullptr for a hard cut. Caller must DuplicateObject before mutating.

---

#### PrepareResumeCallback { #prepareresumecallback }

```cpp
FOnCameraFinishConstructed PrepareResumeCallback(AComposableCameraCameraBase * Camera)
```

Prepare the pending type-asset state for a camera that is being resumed (e.g. after a context pop). If the camera was originally built from a type asset, this restores PendingTypeAsset / PendingParameterBlock and returns a callback bound to OnTypeAssetCameraConstructed. If not a type-asset camera, returns an empty (unbound) delegate.

Called by ContextStack::PopActiveContextInternal so the resumed camera is fully reconstructed from its original type asset instead of producing an empty shell.

### Public Static Attributes

| Return | Name | Description |
|--------|------|-------------|
| `constexpr int32` | [`PoseHistoryCapacity`](#posehistorycapacity) `static` | Fixed ring-buffer capacity. 120 frames ≈ 2 seconds at 60 fps, which is enough to catch the "what happened half a second ago?" class of debug questions without blowing memory. Per-entry footprint is ~48 bytes so total is ~6 KB per PCM. |

---

#### PoseHistoryCapacity { #posehistorycapacity }

`static`

```cpp
constexpr int32 PoseHistoryCapacity = 120
```

Fixed ring-buffer capacity. 120 frames ≈ 2 seconds at 60 fps, which is enough to catch the "what happened half a second ago?" class of debug questions without blowing memory. Per-entry footprint is ~48 bytes so total is ~6 KB per PCM.

### Public Static Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`AddReferencedObjects`](#addreferencedobjects-7) `static` |  |
| `bool` | [`IsPoseHistoryFrozen`](#isposehistoryfrozen) `static` | Whether the pose-history ring buffer is currently frozen (driven by `CCS.Debug.Panel.PoseHistory.Freeze`). Read-only accessor for the debug panel so it can render a `[FROZEN]` indicator in the title bar without having to duplicate the CVar declaration. Shipping builds return false because the debug CVar is compiled out. |

---

#### AddReferencedObjects { #addreferencedobjects-7 }

`static`

```cpp
static void AddReferencedObjects(UObject * InThis, FReferenceCollector & Collector)
```

---

#### IsPoseHistoryFrozen { #isposehistoryfrozen }

`static`

```cpp
static bool IsPoseHistoryFrozen()
```

Whether the pose-history ring buffer is currently frozen (driven by `CCS.Debug.Panel.PoseHistory.Freeze`). Read-only accessor for the debug panel so it can render a `[FROZEN]` indicator in the title bar without having to duplicate the CVar declaration. Shipping builds return false because the debug CVar is compiled out.

### Protected Methods

| Return | Name | Description |
|--------|------|-------------|
| `FMinimalViewInfo` | [`GetCameraViewFromCameraPose`](#getcameraviewfromcamerapose) `const` |  |
| `void` | [`DoUpdateCamera`](#doupdatecamera) `virtual` |  |

---

#### GetCameraViewFromCameraPose { #getcameraviewfromcamerapose }

`const`

```cpp
FMinimalViewInfo GetCameraViewFromCameraPose(const FComposableCameraPose & OutPose) const
```

---

#### DoUpdateCamera { #doupdatecamera }

`virtual`

```cpp
virtual void DoUpdateCamera(float DeltaTime)
```

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TObjectPtr< UComposableCameraTypeAsset >` | [`PendingTypeAsset`](#pendingtypeasset)  |  |
| `FComposableCameraParameterBlock` | [`PendingParameterBlock`](#pendingparameterblock)  | Pending parameter block for the type-asset activation callback. Not a UPROPERTY — plain struct. |
| `TObjectPtr< UComposableCameraContextStack >` | [`ContextStack`](#contextstack)  |  |
| `TObjectPtr< UComposableCameraModifierManager >` | [`ModifierManager`](#modifiermanager)  |  |
| `FMinimalViewInfo` | [`LastDesiredView`](#lastdesiredview)  |  |
| `bool` | [`bIsImplicitlyActivating`](#bisimplicitlyactivating)  | Guard against re-entrant SetViewTarget calls during implicit activation. When the PCM calls ActivateNewCamera internally, the Director may call Super::SetViewTarget as part of its bookkeeping — the guard prevents that from recursing back into implicit activation. |
| `bool` | [`bIsUpdatingActions`](#bisupdatingactions)  | True only inside `UpdateActions`'s range-for over `CameraActions`. The public `RemoveCameraAction` checks this — when set, it performs the unbind half + queues the action into `CameraActionsRemovalScratch` instead of mutating the TSet directly. UpdateActions then does a single post-loop sweep that drains the scratch with `Remove`. Without this gate, an `Action->OnCanExecute` callback that calls `PCM->RemoveCameraAction(this)` would mutate the very TSet the caller is iterating, invalidating the range-for's hash buckets and crashing on the next advance. Outside UpdateActions, RemoveCameraAction is the regular "unbind + drop from TSet" public API. |
| `TArray< FComposableCameraPoseHistoryEntry >` | [`PoseHistoryRing`](#posehistoryring)  |  |
| `int32` | [`PoseHistoryHead`](#posehistoryhead)  |  |
| `int32` | [`PoseHistoryCountUsed`](#posehistorycountused)  |  |

---

#### PendingTypeAsset { #pendingtypeasset }

```cpp
TObjectPtr< UComposableCameraTypeAsset > PendingTypeAsset
```

---

#### PendingParameterBlock { #pendingparameterblock }

```cpp
FComposableCameraParameterBlock PendingParameterBlock
```

Pending parameter block for the type-asset activation callback. Not a UPROPERTY — plain struct.

---

#### ContextStack { #contextstack }

```cpp
TObjectPtr< UComposableCameraContextStack > ContextStack
```

---

#### ModifierManager { #modifiermanager }

```cpp
TObjectPtr< UComposableCameraModifierManager > ModifierManager
```

---

#### LastDesiredView { #lastdesiredview }

```cpp
FMinimalViewInfo LastDesiredView
```

---

#### bIsImplicitlyActivating { #bisimplicitlyactivating }

```cpp
bool bIsImplicitlyActivating { false }
```

Guard against re-entrant SetViewTarget calls during implicit activation. When the PCM calls ActivateNewCamera internally, the Director may call Super::SetViewTarget as part of its bookkeeping — the guard prevents that from recursing back into implicit activation.

---

#### bIsUpdatingActions { #bisupdatingactions }

```cpp
bool bIsUpdatingActions { false }
```

True only inside `UpdateActions`'s range-for over `CameraActions`. The public `RemoveCameraAction` checks this — when set, it performs the unbind half + queues the action into `CameraActionsRemovalScratch` instead of mutating the TSet directly. UpdateActions then does a single post-loop sweep that drains the scratch with `Remove`. Without this gate, an `Action->OnCanExecute` callback that calls `PCM->RemoveCameraAction(this)` would mutate the very TSet the caller is iterating, invalidating the range-for's hash buckets and crashing on the next advance. Outside UpdateActions, RemoveCameraAction is the regular "unbind + drop from TSet" public API.

---

#### PoseHistoryRing { #posehistoryring }

```cpp
TArray< FComposableCameraPoseHistoryEntry > PoseHistoryRing
```

---

#### PoseHistoryHead { #posehistoryhead }

```cpp
int32 PoseHistoryHead = 0
```

---

#### PoseHistoryCountUsed { #posehistorycountused }

```cpp
int32 PoseHistoryCountUsed = 0
```

### Private Methods

| Return | Name | Description |
|--------|------|-------------|
| `UComposableCameraDirector *` | [`GetActiveDirectorSafe`](#getactivedirectorsafe) `const` | Safe accessor for the current active director. Returns nullptr if `ContextStack` itself is null (subobject creation failed, post-teardown reentry, etc.) so callers can branch on the result without paying for a manual `ContextStack ? ... : nullptr` expression at every site. Public-edge call sites that need a guaranteed non-null director should use `ResolveActiveDirectorOrFallback` instead. |
| `UComposableCameraDirector *` | [`ResolveActiveDirectorOrFallback`](#resolveactivedirectororfallback)  | Resolve a non-null director by: |
| `void` | [`UnbindCameraActionFromCamera`](#unbindcameraactionfromcamera)  | Unbind an action's delegates / node hooks from the running camera, but do NOT touch the `CameraActions` TSet — used by `UpdateActions`'s iterate-then-remove pattern (mutating the TSet during iteration is unsafe; the scratch + post-loop `Remove` handles the membership side). External callers wanting "remove and forget" should call the public `RemoveCameraAction`, which composes this helper with the TSet drop. |
| `void` | [`BindCameraActionToRunningCamera`](#bindcameraactiontorunningcamera)  | Mirror of `UnbindCameraActionFromCamera` — the bind side of the per-Action delegate / node-hook setup. Pulled out of the public `AddCameraAction` body so the post-loop sweep in `UpdateActions` can finish the deferred-add path without duplicating the dispatch switch. No-op if Action or RunningCamera is null. |
| `void` | [`UpdateActions`](#updateactions)  |  |
| `void` | [`BuildModifierDebugString`](#buildmodifierdebugstring)  |  |
| `void` | [`OnTypeAssetCameraConstructed`](#ontypeassetcameraconstructed)  | Called by the dynamic delegate during type-asset-based camera activation. |
| `void` | [`CaptureCurrentFrameToPoseHistory`](#capturecurrentframetoposehistory)  | Capture one frame into the ring. Called from `DoUpdateCamera` after `CurrentCameraPose` is finalized. |

---

#### GetActiveDirectorSafe { #getactivedirectorsafe }

`const`

```cpp
UComposableCameraDirector * GetActiveDirectorSafe() const
```

Safe accessor for the current active director. Returns nullptr if `ContextStack` itself is null (subobject creation failed, post-teardown reentry, etc.) so callers can branch on the result without paying for a manual `ContextStack ? ... : nullptr` expression at every site. Public-edge call sites that need a guaranteed non-null director should use `ResolveActiveDirectorOrFallback` instead.

---

#### ResolveActiveDirectorOrFallback { #resolveactivedirectororfallback }

```cpp
UComposableCameraDirector * ResolveActiveDirectorOrFallback(const TCHAR * Caller)
```

Resolve a non-null director by:

1. Trying the current active director (via `GetActiveDirectorSafe`)

1. Falling back to ensuring the project-settings base context Returns nullptr only if both paths fail (no stack, no configured context names). The single shared implementation prevents the "n public APIs, n−1 of them remembered to fall back" drift pattern that recurs whenever a new public entry-point is added. `Caller` is used purely to attribute the failure log — pass a literal string.

---

#### UnbindCameraActionFromCamera { #unbindcameraactionfromcamera }

```cpp
void UnbindCameraActionFromCamera(UComposableCameraActionBase * Action)
```

Unbind an action's delegates / node hooks from the running camera, but do NOT touch the `CameraActions` TSet — used by `UpdateActions`'s iterate-then-remove pattern (mutating the TSet during iteration is unsafe; the scratch + post-loop `Remove` handles the membership side). External callers wanting "remove and forget" should call the public `RemoveCameraAction`, which composes this helper with the TSet drop.

---

#### BindCameraActionToRunningCamera { #bindcameraactiontorunningcamera }

```cpp
void BindCameraActionToRunningCamera(UComposableCameraActionBase * Action)
```

Mirror of `UnbindCameraActionFromCamera` — the bind side of the per-Action delegate / node-hook setup. Pulled out of the public `AddCameraAction` body so the post-loop sweep in `UpdateActions` can finish the deferred-add path without duplicating the dispatch switch. No-op if Action or RunningCamera is null.

---

#### UpdateActions { #updateactions }

```cpp
void UpdateActions(float DeltaTime)
```

---

#### BuildModifierDebugString { #buildmodifierdebugstring }

```cpp
void BuildModifierDebugString(FDisplayDebugManager & DisplayDebugManager)
```

---

#### OnTypeAssetCameraConstructed { #ontypeassetcameraconstructed }

```cpp
void OnTypeAssetCameraConstructed(AComposableCameraCameraBase * Camera)
```

Called by the dynamic delegate during type-asset-based camera activation.

---

#### CaptureCurrentFrameToPoseHistory { #capturecurrentframetoposehistory }

```cpp
void CaptureCurrentFrameToPoseHistory()
```

Capture one frame into the ring. Called from `DoUpdateCamera` after `CurrentCameraPose` is finalized.
