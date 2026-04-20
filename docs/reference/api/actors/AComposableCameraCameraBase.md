
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
| `FComposableCameraPose` | [`CameraPose`](#camerapose)  |  |
| `FComposableCameraPose` | [`LastFrameCameraPose`](#lastframecamerapose)  |  |
| `bool` | [`bIsTransient`](#bistransient)  |  |
| `float` | [`LifeTime`](#lifetime)  |  |
| `float` | [`RemainingLifeTime`](#remaininglifetime)  |  |
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
| `UComposableCameraCameraNodeBase *` | [`GetNodeByClass`](#getnodebyclass)  |  |
| `AComposableCameraPlayerCameraManager *` | [`GetOwningPlayerCameraManager`](#getowningplayercameramanager) `inline` |  |
| `FComposableCameraPose` | [`GetCameraPose`](#getcamerapose) `const` `inline` |  |
| `FComposableCameraPose` | [`GetLastFrameCameraPose`](#getlastframecamerapose) `const` `inline` |  |
| `bool` | [`IsTransient`](#istransient) `const` `inline` |  |
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
