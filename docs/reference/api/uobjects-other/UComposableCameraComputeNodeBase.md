
# UComposableCameraComputeNodeBase { #ucomposablecameracomputenodebase }

```cpp
#include <ComposableCameraComputeNodeBase.h>
```

> **Inherits:** [`UComposableCameraCameraNodeBase`](UComposableCameraCameraNodeBase.md#ucomposablecameracameranodebase)
> **Subclassed by:** [`UComposableCameraComputeDistanceToActorNode`](../nodes/UComposableCameraComputeDistanceToActorNode.md#ucomposablecameracomputedistancetoactornode)

Base class for one-shot compute nodes that run on the BeginPlay chain.

Compute nodes are NOT camera nodes in the per-frame-evaluated sense. They run exactly once, between per-node Initialize and the first TickCamera, and their job is to perform arbitrary math / data shaping in C++ and publish the result to camera-level internal variables (or to output pins that are then plumbed through the graph).

Why a dedicated base class instead of "just use a camera node"? ──────────────────────────────────────────────────────────────

* Camera nodes are walked per-frame by TickCamera and multicast through OnPreTick / OnPostTick. A compute node must not touch any of that — it would otherwise burn hot-path time on values that never change.

* Compute nodes still need the pin system (GetInputPinValue / SetOutputPinValue / Set/GetInternalVariable), which only lives on [UComposableCameraCameraNodeBase](UComposableCameraCameraNodeBase.md#ucomposablecameracameranodebase). Inheriting from it is the cheapest way to get that plumbing without duplicating the RuntimeDataBlock wiring.

* The editor-side graph hosts these on a separate BeginPlay chain rooted at UComposableCameraBeginPlayStartGraphNode, parallel to how regular camera nodes wire off the main Start sentinel. The sync/rebuild phases classify a UComposableCameraNodeGraphNode as camera-chain vs compute-chain by testing IsA<UComposableCameraComputeNodeBase> on its underlying NodeTemplate, which is exactly this base class — so the runtime discriminator "this belongs on the BeginPlay chain" is the same type check the editor uses.

Why a dedicated class instead of UObject? ─────────────────────────────────────────

* K2 math graph nodes from the BlueprintGraph module do not work in our custom UEdGraph without significant engineering. The pragmatic Option B is: author a compute node in C++, use FMath / FVector / FQuat / UKismetMathLibrary directly, publish the result to internal variables, and let downstream camera nodes consume them.

* Subclasses describe their inputs and outputs with the same pin declaration system as camera nodes (GetPinDeclarations), which keeps editor palette / pin rendering / type-asset authoring uniform.

Lifecycle ─────────

1. Camera activation fires [AComposableCameraCameraBase::InitializeNodes](../actors/AComposableCameraCameraBase.md#initializenodes).

1. Each compute node has OnInitialize_Implementation invoked via the inherited [Initialize()](UComposableCameraCameraNodeBase.md#initialize-1) path (same machinery camera nodes use). This is where one-time setup, ref caching, and exposed-parameter reads belong.

1. AActor::BeginPlay fires, which calls [AComposableCameraCameraBase::BeginPlayCamera()](../actors/AComposableCameraCameraBase.md#beginplaycamera), which walks the ComputeNodes array in order and calls [ExecuteBeginPlay()](#executebeginplay) on each.

1. First TickCamera then runs with whatever internal variables / output pins the compute chain published.

Compute nodes must NOT register for OnPreTick / OnPostTick and must NOT override OnTickNode_Implementation — they are not per-frame nodes. The camera's InitializeNodes loop intentionally skips tick-delegate wiring for compute nodes for exactly this reason.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`ExecuteBeginPlay`](#executebeginplay) `virtual` `inline` | Execute this compute node's one-shot work. |

---

#### ExecuteBeginPlay { #executebeginplay }

`virtual` `inline`

```cpp
virtual inline void ExecuteBeginPlay()
```

Execute this compute node's one-shot work.

Called from [AComposableCameraCameraBase::BeginPlayCamera](../actors/AComposableCameraCameraBase.md#beginplaycamera), after every node on the camera (both camera nodes and compute nodes) has already had [Initialize()](UComposableCameraCameraNodeBase.md#initialize-1) / [OnInitialize_Implementation()](UComposableCameraCameraNodeBase.md#oninitialize_implementation-3) run. By the time this fires, OwningCamera / OwningPlayerCameraManager / RuntimeDataBlock are all wired, so GetInputPinValue / SetOutputPinValue / Get/SetInternalVariable are all safe to use.

The outgoing camera pose (the pose the previous camera was evaluating before this one became active) is available via OwningPlayerCameraManager->GetCurrentCameraPose() — this is the same value AActor::BeginPlay used to pass into BeginPlayCamera as a parameter before Step 4a removed that argument.

Plain virtual (not a BlueprintNativeEvent) for 4a. If Blueprint authoring of compute nodes becomes a requirement later, promote this to a BlueprintNativeEvent following the same OnFoo / OnFoo_Implementation pattern used by OnInitialize and OnTickNode on the parent class.
