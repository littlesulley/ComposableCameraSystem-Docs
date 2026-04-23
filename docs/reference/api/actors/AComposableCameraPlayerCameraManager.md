
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
| `void` | [`RemoveCameraAction`](#removecameraaction)  |  |
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
| `bool` | [`IsPoseHistoryFrozen`](#isposehistoryfrozen) `static` | Whether the pose-history ring buffer is currently frozen (driven by `CCS.Debug.Panel.PoseHistory.Freeze`). Read-only accessor for the debug panel so it can render a `[FROZEN]` indicator in the title bar without having to duplicate the CVar declaration. Debug-only; not declared outside `!UE_BUILD_SHIPPING`. |

---

#### IsPoseHistoryFrozen { #isposehistoryfrozen }

`static`

```cpp
static bool IsPoseHistoryFrozen()
```

Whether the pose-history ring buffer is currently frozen (driven by `CCS.Debug.Panel.PoseHistory.Freeze`). Read-only accessor for the debug panel so it can render a `[FROZEN]` indicator in the title bar without having to duplicate the CVar declaration. Debug-only; not declared outside `!UE_BUILD_SHIPPING`.

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
| `void` | [`UpdateActions`](#updateactions)  |  |
| `void` | [`BuildModifierDebugString`](#buildmodifierdebugstring)  |  |
| `void` | [`OnTypeAssetCameraConstructed`](#ontypeassetcameraconstructed)  | Called by the dynamic delegate during type-asset-based camera activation. |
| `void` | [`CaptureCurrentFrameToPoseHistory`](#capturecurrentframetoposehistory)  | Capture one frame into the ring. Called from `DoUpdateCamera` after `CurrentCameraPose` is finalized. |

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
