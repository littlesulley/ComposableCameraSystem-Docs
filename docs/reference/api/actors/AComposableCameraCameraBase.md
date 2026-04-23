
# AComposableCameraCameraBase { #acomposablecameracamerabase }

```cpp
#include <ComposableCameraCameraBase.h>
```

> **Inherits:** `ACameraActor`
> **Subclassed by:** [`AComposableCameraGeneralThirdPersonCamera`](AComposableCameraGeneralThirdPersonCamera.md#acomposablecamerageneralthirdpersoncamera)

Base camera class.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FGameplayTag` | [`CameraTag`](#cameratag-1)  | Tag for this camera. Used by modifiers to distinguish different cameras. |
| `UComposableCameraTransitionBase *` | [`EnterTransition`](#entertransition-2)  | Enter transition. Usually used for returning back to this camera from a transient camera. |
| `bool` | [`bDefaultPreserveCameraPose`](#bdefaultpreservecamerapose-1)  | Whether to preserve last camera's pose when resuming this camera. |
| `TArray< UComposableCameraCameraNodeBase * >` | [`CameraNodes`](#cameranodes)  | Nodes for this camera. They're executed in the order they are placed in this array. Each node reads input pin values, applies its logic, and writes output pin values. Inter-node data flow is handled entirely through the pin-based RuntimeDataBlock system. |
| `TArray< TObjectPtr< UComposableCameraComputeNodeBase > >` | [`ComputeNodes`](#computenodes)  | One-shot compute nodes that run during BeginPlayCamera, after every node (both camera nodes and compute nodes) has had [Initialize()](#initialize) run. They are walked in array order and each has ExecuteBeginPlay() called exactly once. |
| `FOnPreTick` | [`OnPreTick`](#onpretick)  |  |
| `FOnPostTick` | [`OnPostTick`](#onposttick)  |  |
| `FOnActionPreTick` | [`OnActionPreTick`](#onactionpretick)  |  |
| `FOnActionPostTick` | [`OnActionPostTick`](#onactionposttick)  |  |
| `TArray< UComposableCameraActionBase * >` | [`PreNodeTickActions`](#prenodetickactions)  | Node-scoped actions fired around each node's TickNode. The PCM registers actions here when their ExecutionType is PreNodeTick / PostNodeTick (see [AComposableCameraPlayerCameraManager::AddCameraAction](AComposableCameraPlayerCameraManager.md#addcameraaction) / BindCameraActionsForNewCamera). Matching is by exact class (Node->GetClass() == Action->TargetNodeClass), same rule as the Modifier system. |
| `TArray< UComposableCameraActionBase * >` | [`PostNodeTickActions`](#postnodetickactions)  |  |
| `FComposableCameraPose` | [`CameraPose`](#camerapose)  |  |
| `FComposableCameraPose` | [`LastFrameCameraPose`](#lastframecamerapose)  |  |
| `bool` | [`bIsTransient`](#bistransient)  |  |
| `float` | [`LifeTime`](#lifetime)  |  |
| `float` | [`RemainingLifeTime`](#remaininglifetime)  |  |
| `uint64` | [`LastTickedFrameCounter`](#lasttickedframecounter)  | Per-frame tick memoization. |
| `TArray< FComposableCameraExecEntry >` | [`FullExecChain`](#fullexecchain-1)  | Full execution chain for the per-frame camera tick, including both camera-node steps and internal-variable Set operations. Copied from [UComposableCameraTypeAsset::FullExecChain](../data-assets/UComposableCameraTypeAsset.md#fullexecchain) during OnTypeAssetCameraConstructed. |
| `TArray< FComposableCameraExecEntry >` | [`ComputeFullExecChain`](#computefullexecchain-1)  | Full execution chain for the BeginPlay compute pass, including both compute-node steps and internal-variable Set operations. Copied from [UComposableCameraTypeAsset::ComputeFullExecChain](../data-assets/UComposableCameraTypeAsset.md#computefullexecchain) during OnTypeAssetCameraConstructed. |
| `int32` | [`TypeAssetNodeTemplateCount`](#typeassetnodetemplatecount)  | The number of entries in TypeAsset::NodeTemplates at construction time. Used as the base offset for compute-node pin keys in the RuntimeDataBlock (compute node i has pin key NodeIndex = TypeAssetNodeTemplateCount + i). |
| `TUniquePtr< FComposableCameraRuntimeDataBlock >` | [`OwnedRuntimeDataBlock`](#ownedruntimedatablock)  | Owned RuntimeDataBlock for type-asset-based cameras. Allocated during activation from a [UComposableCameraTypeAsset](../data-assets/UComposableCameraTypeAsset.md#ucomposablecameratypeasset). Nodes hold raw pointers into this block — they never outlive the camera. |
| `TWeakObjectPtr< UComposableCameraTypeAsset >` | [`SourceTypeAsset`](#sourcetypeasset)  | The type asset that was used to construct this camera. Stored so that ReactivateCurrentCamera (triggered by modifier changes) can fully reconstruct the camera from the same source asset instead of producing an empty shell. |
| `FComposableCameraParameterBlock` | [`SourceParameterBlock`](#sourceparameterblock)  | The parameter block that was applied when this camera was activated from a type asset. Stored alongside SourceTypeAsset so reactivation preserves the original caller-provided parameter values. |

---

#### CameraTag { #cameratag-1 }

```cpp
FGameplayTag CameraTag {}
```

Tag for this camera. Used by modifiers to distinguish different cameras.

---

#### EnterTransition { #entertransition-2 }

```cpp
UComposableCameraTransitionBase * EnterTransition
```

Enter transition. Usually used for returning back to this camera from a transient camera.

---

#### bDefaultPreserveCameraPose { #bdefaultpreservecamerapose-1 }

```cpp
bool bDefaultPreserveCameraPose { true }
```

Whether to preserve last camera's pose when resuming this camera.

---

#### CameraNodes { #cameranodes }

```cpp
TArray< UComposableCameraCameraNodeBase * > CameraNodes
```

Nodes for this camera. They're executed in the order they are placed in this array. Each node reads input pin values, applies its logic, and writes output pin values. Inter-node data flow is handled entirely through the pin-based RuntimeDataBlock system.

@NOTE: This property is exposed as EditAnywhere, only for debug purposes at runtime. You should NEVER modify this for instances.

---

#### ComputeNodes { #computenodes }

```cpp
TArray< TObjectPtr< UComposableCameraComputeNodeBase > > ComputeNodes
```

One-shot compute nodes that run during BeginPlayCamera, after every node (both camera nodes and compute nodes) has had [Initialize()](#initialize) run. They are walked in array order and each has ExecuteBeginPlay() called exactly once.

Compute nodes are NOT per-frame-ticked. They exist to perform C++ math / data shaping at activation time and publish the result via internal variables or output pins. Downstream camera nodes then read those values in their own Initialize or TickNode bodies.

Populated during type-asset activation: AComposableCameraPlayerCameraManager::OnTypeAssetCameraConstructed duplicates every non-null entry of [UComposableCameraTypeAsset::ComputeNodeTemplates](../data-assets/UComposableCameraTypeAsset.md#computenodetemplates) into this array, then reorders by the type asset's ComputeExecutionOrder (built from the editor's BeginPlay compute chain rooted at UComposableCameraBeginPlayStartGraphNode — see EditorDesignDoc §8 "Dual exec chains: camera chain vs BeginPlay compute chain").

@NOTE: Like CameraNodes, this is EditAnywhere only for debug inspection. Do not mutate at runtime.

---

#### OnPreTick { #onpretick }

```cpp
FOnPreTick OnPreTick
```

---

#### OnPostTick { #onposttick }

```cpp
FOnPostTick OnPostTick
```

---

#### OnActionPreTick { #onactionpretick }

```cpp
FOnActionPreTick OnActionPreTick
```

---

#### OnActionPostTick { #onactionposttick }

```cpp
FOnActionPostTick OnActionPostTick
```

---

#### PreNodeTickActions { #prenodetickactions }

```cpp
TArray< UComposableCameraActionBase * > PreNodeTickActions
```

Node-scoped actions fired around each node's TickNode. The PCM registers actions here when their ExecutionType is PreNodeTick / PostNodeTick (see [AComposableCameraPlayerCameraManager::AddCameraAction](AComposableCameraPlayerCameraManager.md#addcameraaction) / BindCameraActionsForNewCamera). Matching is by exact class (Node->GetClass() == Action->TargetNodeClass), same rule as the Modifier system.

These are NOT UPROPERTY — ownership lives on the PCM's CameraActions UPROPERTY TSet, which is the GC root. This camera-local view is just a hot-path iteration cache; the PCM clears it via UnregisterNodeAction when an action expires, and EndPlay clears it defensively.

---

#### PostNodeTickActions { #postnodetickactions }

```cpp
TArray< UComposableCameraActionBase * > PostNodeTickActions
```

---

#### CameraPose { #camerapose }

```cpp
FComposableCameraPose CameraPose
```

---

#### LastFrameCameraPose { #lastframecamerapose }

```cpp
FComposableCameraPose LastFrameCameraPose
```

---

#### bIsTransient { #bistransient }

```cpp
bool bIsTransient { false }
```

---

#### LifeTime { #lifetime }

```cpp
float LifeTime { 0.f }
```

---

#### RemainingLifeTime { #remaininglifetime }

```cpp
float RemainingLifeTime { 0.f }
```

---

#### LastTickedFrameCounter { #lasttickedframecounter }

```cpp
uint64 LastTickedFrameCounter { 0 }
```

Per-frame tick memoization.

When the evaluation DAG (produced by snapshot-based RefLeaves) reaches the same camera via multiple paths in a single frame — e.g. the pop transition's target subtree AND the RefLeaf→B → push-source RefLeaf both bottom out at the same original A leaf — a second TickCamera would double-advance the camera's per-node state (damping, interpolator `bStartFrame`, spline progress, noise seeds, etc.). TickCamera compares GFrameCounter against this value: if it matches, the cached CameraPose is returned verbatim and the node chain is NOT walked again.

0 is a valid sentinel: GFrameCounter starts above 0 in any real engine session, so a freshly-constructed camera (counter = 0) will always take the full-tick path on its first evaluation. Not a UPROPERTY — purely transient evaluation-time scratch.

---

#### FullExecChain { #fullexecchain-1 }

```cpp
TArray< FComposableCameraExecEntry > FullExecChain
```

Full execution chain for the per-frame camera tick, including both camera-node steps and internal-variable Set operations. Copied from [UComposableCameraTypeAsset::FullExecChain](../data-assets/UComposableCameraTypeAsset.md#fullexecchain) during OnTypeAssetCameraConstructed.

CameraNodeIndex in each entry references the author-order index in CameraNodes (which is parallel to TypeAsset::NodeTemplates).

---

#### ComputeFullExecChain { #computefullexecchain-1 }

```cpp
TArray< FComposableCameraExecEntry > ComputeFullExecChain
```

Full execution chain for the BeginPlay compute pass, including both compute-node steps and internal-variable Set operations. Copied from [UComposableCameraTypeAsset::ComputeFullExecChain](../data-assets/UComposableCameraTypeAsset.md#computefullexecchain) during OnTypeAssetCameraConstructed.

CameraNodeIndex in each entry references the author-order index in ComputeNodes (which is parallel to TypeAsset::ComputeNodeTemplates when ComputeFullExecChain is non-empty — in that case OnTypeAssetCameraConstructed skips the legacy reorder to preserve index correspondence).

---

#### TypeAssetNodeTemplateCount { #typeassetnodetemplatecount }

```cpp
int32 TypeAssetNodeTemplateCount = 0
```

The number of entries in TypeAsset::NodeTemplates at construction time. Used as the base offset for compute-node pin keys in the RuntimeDataBlock (compute node i has pin key NodeIndex = TypeAssetNodeTemplateCount + i).

Stored explicitly because CameraNodes.Num() can differ from NodeTemplates.Num() if OnTypeAssetCameraConstructed skips null templates during duplication.

---

#### OwnedRuntimeDataBlock { #ownedruntimedatablock }

```cpp
TUniquePtr< FComposableCameraRuntimeDataBlock > OwnedRuntimeDataBlock
```

Owned RuntimeDataBlock for type-asset-based cameras. Allocated during activation from a [UComposableCameraTypeAsset](../data-assets/UComposableCameraTypeAsset.md#ucomposablecameratypeasset). Nodes hold raw pointers into this block — they never outlive the camera.

---

#### SourceTypeAsset { #sourcetypeasset }

```cpp
TWeakObjectPtr< UComposableCameraTypeAsset > SourceTypeAsset
```

The type asset that was used to construct this camera. Stored so that ReactivateCurrentCamera (triggered by modifier changes) can fully reconstruct the camera from the same source asset instead of producing an empty shell.

---

#### SourceParameterBlock { #sourceparameterblock }

```cpp
FComposableCameraParameterBlock SourceParameterBlock
```

The parameter block that was applied when this camera was activated from a type asset. Stored alongside SourceTypeAsset so reactivation preserves the original caller-provided parameter values.

Empty for type-asset cameras activated without any parameter overrides.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`AComposableCameraCameraBase`](#acomposablecameracamerabase-1)  |  |
| `void` | [`BeginPlay`](#beginplay) `virtual` |  |
| `void` | [`EndPlay`](#endplay) `virtual` |  |
| `void` | [`Initialize`](#initialize)  |  |
| `void` | [`InitializeNodes`](#initializenodes)  | Per-node initialization loop. Walks CameraNodes and ComputeNodes, calls Node->Initialize on each, and wires OnPreTick/OnPostTick delegates for CameraNodes only. Compute nodes are initialized but NOT wired to the per-frame tick multicasts — they only run once, from BeginPlayCamera. |
| `void` | [`ApplyModifiers`](#applymodifiers)  |  |
| `void` | [`BeginPlayCamera`](#beginplaycamera)  | Runs the BeginPlay compute chain: walks ComputeNodes in order and calls ExecuteBeginPlay on each. Called exactly once per activation from AActor::BeginPlay, after per-node Initialize has run for every node. |
| `FComposableCameraPose` | [`TickCamera`](#tickcamera)  |  |
| `void` | [`RegisterNodeAction`](#registernodeaction)  |  |
| `void` | [`UnregisterNodeAction`](#unregisternodeaction)  |  |
| `UComposableCameraCameraNodeBase *` | [`GetNodeByClass`](#getnodebyclass)  |  |
| `AComposableCameraPlayerCameraManager *` | [`GetOwningPlayerCameraManager`](#getowningplayercameramanager) `inline` |  |
| `FComposableCameraPose` | [`GetCameraPose`](#getcamerapose) `const` `inline` |  |
| `FComposableCameraPose` | [`GetLastFrameCameraPose`](#getlastframecamerapose) `const` `inline` |  |
| `bool` | [`IsTransient`](#istransient) `const` `inline` |  |
| `void` | [`DrawCameraDebug`](#drawcameradebug) `const` | Draw world-space debug primitives for this camera. |
| `void` | [`DrawCameraDebug2D`](#drawcameradebug2d) `const` | 2D counterpart to DrawCameraDebug. Walks `CameraNodes` and invokes each node's `DrawNodeDebug2D` override. Called by the viewport debug service's "Game"-channel hook (HUD pass) — fires during PIE possessed play, not during F8 eject. Each node gates its own output on its per-node CVar, same pattern as the 3D path. |
| `float` | [`GetLifeTime`](#getlifetime) `const` `inline` |  |
| `float` | [`GetRemainingLifeTime`](#getremaininglifetime) `const` `inline` |  |
| `bool` | [`IsFinished`](#isfinished) `const` `inline` |  |

---

#### AComposableCameraCameraBase { #acomposablecameracamerabase-1 }

```cpp
AComposableCameraCameraBase(const FObjectInitializer & ObjectInitializer)
```

---

#### BeginPlay { #beginplay }

`virtual`

```cpp
virtual void BeginPlay()
```

---

#### EndPlay { #endplay }

`virtual`

```cpp
virtual void EndPlay(const EEndPlayReason::Type EndPlayReason)
```

---

#### Initialize { #initialize }

```cpp
void Initialize(AComposableCameraPlayerCameraManager * Manager)
```

---

#### InitializeNodes { #initializenodes }

```cpp
void InitializeNodes()
```

Per-node initialization loop. Walks CameraNodes and ComputeNodes, calls Node->Initialize on each, and wires OnPreTick/OnPostTick delegates for CameraNodes only. Compute nodes are initialized but NOT wired to the per-frame tick multicasts — they only run once, from BeginPlayCamera.

Called twice during type-asset activation: first from [Initialize()](#initialize) (where CameraNodes is still empty — a no-op), then again from OnTypeAssetCameraConstructed once templates have been duplicated and the RuntimeDataBlock wired, so every node's [Initialize()](#initialize) runs exactly once.

---

#### ApplyModifiers { #applymodifiers }

```cpp
void ApplyModifiers(const T_NodeModifier & Modifiers)
```

---

#### BeginPlayCamera { #beginplaycamera }

```cpp
void BeginPlayCamera()
```

Runs the BeginPlay compute chain: walks ComputeNodes in order and calls ExecuteBeginPlay on each. Called exactly once per activation from AActor::BeginPlay, after per-node Initialize has run for every node.

Compute nodes that need the outgoing camera pose read it from OwningPlayerCameraManager->GetCurrentCameraPose() — which is why this function no longer takes a pose parameter.

---

#### TickCamera { #tickcamera }

```cpp
FComposableCameraPose TickCamera(float DeltaTime)
```

---

#### RegisterNodeAction { #registernodeaction }

```cpp
void RegisterNodeAction(UComposableCameraActionBase * Action)
```

---

#### UnregisterNodeAction { #unregisternodeaction }

```cpp
void UnregisterNodeAction(UComposableCameraActionBase * Action)
```

---

#### GetNodeByClass { #getnodebyclass }

```cpp
UComposableCameraCameraNodeBase * GetNodeByClass(TSubclassOf< UComposableCameraCameraNodeBase > NodeClass)
```

---

#### GetOwningPlayerCameraManager { #getowningplayercameramanager }

`inline`

```cpp
inline AComposableCameraPlayerCameraManager * GetOwningPlayerCameraManager()
```

---

#### GetCameraPose { #getcamerapose }

`const` `inline`

```cpp
inline FComposableCameraPose GetCameraPose() const
```

---

#### GetLastFrameCameraPose { #getlastframecamerapose }

`const` `inline`

```cpp
inline FComposableCameraPose GetLastFrameCameraPose() const
```

---

#### IsTransient { #istransient }

`const` `inline`

```cpp
inline bool IsTransient() const
```

---

#### DrawCameraDebug { #drawcameradebug }

`const`

```cpp
void DrawCameraDebug(class UWorld * World, bool bDrawFrustum) const
```

Draw world-space debug primitives for this camera.

Invoked from the viewport debug ticker when `CCS.Debug.Viewport` is enabled. Two independently gated pieces:

* Frustum pyramid at the camera's current pose — drawn only when `bDrawFrustum` is true. The ticker passes true only while the player is NOT viewing through the camera (F8 eject / SIE / `CCS.Debug.Viewport.AlwaysShow`), because otherwise the pyramid just occludes the near plane.

* A walk over `CameraNodes` calling each node's `DrawNodeDebug`. Always invoked — each node's override checks its own per-node CVar (`CCS.Debug.Viewport.<NodeName>`) and early-outs when zero. Per-node gizmos are therefore visible in BOTH possessed play and ejected state, because they rarely occlude the viewpoint.

Reads `CameraPose` (the leaf-local evaluated pose), not the PCM's blended pose — for the running camera in a steady state these are the same; during a transition, this shows the pose this camera is contributing, not the blended result.

Compiled out in shipping builds.

---

#### DrawCameraDebug2D { #drawcameradebug2d }

`const`

```cpp
void DrawCameraDebug2D(class UCanvas * Canvas, class APlayerController * PC) const
```

2D counterpart to DrawCameraDebug. Walks `CameraNodes` and invokes each node's `DrawNodeDebug2D` override. Called by the viewport debug service's "Game"-channel hook (HUD pass) — fires during PIE possessed play, not during F8 eject. Each node gates its own output on its per-node CVar, same pattern as the 3D path.

---

#### GetLifeTime { #getlifetime }

`const` `inline`

```cpp
inline float GetLifeTime() const
```

---

#### GetRemainingLifeTime { #getremaininglifetime }

`const` `inline`

```cpp
inline float GetRemainingLifeTime() const
```

---

#### IsFinished { #isfinished }

`const` `inline`

```cpp
inline bool IsFinished() const
```

### Protected Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TObjectPtr< AComposableCameraPlayerCameraManager >` | [`CameraManager`](#cameramanager)  |  |

---

#### CameraManager { #cameramanager }

```cpp
TObjectPtr< AComposableCameraPlayerCameraManager > CameraManager
```
