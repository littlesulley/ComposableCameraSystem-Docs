
# UComposableCameraEvaluationTree { #ucomposablecameraevaluationtree }

```cpp
#include <ComposableCameraEvaluationTree.h>
```

> **Inherits:** `UObject`

Evaluation tree for composable cameras. Manages the blending tree of active cameras and transitions.

The tree is structured as follows:

* Leaf nodes wrap a single active camera.

* Inner nodes wrap a transition that blends between a source (left child) and target (right child) subtree.

When a new camera is activated:

* With a transition: the current tree becomes the left (source) subtree, the new camera becomes a new right (target) leaf, and an inner node wrapping the transition becomes the new root.

* Without a transition (camera cut): the tree is replaced with a single leaf node for the new camera.

When a transition finishes, the tree is collapsed: the inner node is replaced by its right (target) subtree.

You should be very careful about *transient* cameras, because they may break the camera chain you'd expect.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`UComposableCameraEvaluationTree`](#ucomposablecameraevaluationtree-1)  |  |
| `FComposableCameraPose` | [`Evaluate`](#evaluate-5)  | Evaluate the full tree for this frame and return the final blended camera pose. |
| `void` | [`OnActivateNewCamera`](#onactivatenewcamera)  | Called when a new camera is activated, optionally with a transition from the current state. |
| `void` | [`OnActivateNewCameraWithReferenceSource`](#onactivatenewcamerawithreferencesource)  | Activate a new camera with a snapshot of another context's tree as the transition source. Used for inter-context PUSH transitions. |
| `void` | [`OnResumeCurrentTreeWithReferenceSource`](#onresumecurrenttreewithreferencesource)  | Wrap the current tree's `RootNode` (the resuming camera, intact with all its accumulated per-node state) as the TARGET of a new pop transition, with a reference leaf capturing `SourceDirector`'s tree root as a snapshot on the SOURCE side. Used by context-stack pops so the resumed camera is the ORIGINAL instance that was running before the push — not a fresh instance spawned at pop time with zeroed damping / interpolator / spline-progress / etc. state. |
| `bool` | [`HasActiveCamera`](#hasactivecamera) `const` | Returns true if the tree has at least one active camera. |
| `AComposableCameraCameraBase *` | [`GetRunningCamera`](#getrunningcamera-2) `const` `inline` | Get the current running camera (set when a camera is activated, updated on tree rebuild). |
| `const TSharedPtr< FComposableCameraEvaluationTreeNode > &` | [`GetRootNode`](#getrootnode) `const` `inline` | Read-only access to the current root node. Used by director-to-director inter-context APIs to capture a `TSharedPtr` snapshot of this tree's current shape when creating a reference leaf in another tree — the returned pointer is shared (not copied), so the snapshot keeps the captured subtree alive even if THIS tree later swaps its root. Returns null if no camera has been activated yet. |
| `void` | [`DestroyAll`](#destroyall-1)  | Destroy all cameras in the tree and reset to empty. |
| `void` | [`BuildDebugSnapshot`](#builddebugsnapshot-3) `const` | Build a flat DFS pre-order snapshot of the tree for every debug consumer (2D panel, `showdebug camera`, dump commands — all render from the snapshot through `[ComposableCameraDebug::AppendTreeNodeLine](../free-functions/Functions.md#appendtreenodeline)`). Appends to OutNodes (caller is responsible for Reset if starting fresh). Computes bIsDominantLeaf as part of the walk (root → Right* → leaf). |
| `void` | [`DrawTransitionsDebug`](#drawtransitionsdebug) `const` | Walk every Inner (transition) node reachable from the tree's root and invoke `[UComposableCameraTransitionBase::DrawTransitionDebug](../transitions/UComposableCameraTransitionBase.md#drawtransitiondebug-1)` on each. Each transition self-gates on its own `CCS.Debug.Viewport.Transitions.<Name>` CVar — if none are enabled, this call is effectively free. |

---

#### UComposableCameraEvaluationTree { #ucomposablecameraevaluationtree-1 }

```cpp
UComposableCameraEvaluationTree(const FObjectInitializer & ObjectInitializer)
```

---

#### Evaluate { #evaluate-5 }

```cpp
FComposableCameraPose Evaluate(float DeltaTime)
```

Evaluate the full tree for this frame and return the final blended camera pose.

---

#### OnActivateNewCamera { #onactivatenewcamera }

```cpp
void OnActivateNewCamera(AComposableCameraCameraBase * NewCamera, UComposableCameraTransitionBase * Transition, bool bFreezeSourceCamera)
```

Called when a new camera is activated, optionally with a transition from the current state.

When the root is an inter-context transition (left child is a reference leaf), the activation nests under the right (target) subtree instead of wrapping the entire tree. This preserves the inter-context blend at the root while allowing intra-context camera switches to happen underneath:

Before: After (nested): [InterCtx Transition] [InterCtx Transition] / \ / \ [RefLeaf] [CamB1] [RefLeaf] [IntraCtx Transition] / \ [CamB1] [CamB2]

When the inter-context transition finishes (the reference leaf side collapses), only the right subtree survives — which is the intra-context blend, exactly as expected.

---

#### OnActivateNewCameraWithReferenceSource { #onactivatenewcamerawithreferencesource }

```cpp
void OnActivateNewCameraWithReferenceSource(AComposableCameraCameraBase * NewCamera, UComposableCameraTransitionBase * Transition, UComposableCameraDirector * SourceDirector, bool bFreezeSourceCamera)
```

Activate a new camera with a snapshot of another context's tree as the transition source. Used for inter-context PUSH transitions.

The reference leaf built here captures `SourceDirector->GetEvaluationTree()->[GetRootNode()](#getrootnode)` by `TSharedPtr` at call time. Subsequent mutations to the source director's root (e.g. the source later being popped and wrapped by its own pop Inner) do NOT follow into this RefLeaf — it keeps evaluating the captured subtree verbatim. That is what prevents cycles during pop-while-push-still- active (see DesignDoc §"Inter-Context Transitions").

**Parameters**

* `NewCamera` The new camera to activate in this context. 

* `Transition` The transition to blend from the captured subtree's output to NewCamera. 

* `SourceDirector` The source director whose tree is being snapshotted RIGHT NOW. 

* `bFreezeSourceCamera` When true, the snapshot holds its last pose instead of re-evaluating each frame. Purely a semantic option for authors who want freeze-on-push behaviour; NOT required for correctness.

---

#### OnResumeCurrentTreeWithReferenceSource { #onresumecurrenttreewithreferencesource }

```cpp
void OnResumeCurrentTreeWithReferenceSource(UComposableCameraTransitionBase * Transition, UComposableCameraDirector * SourceDirector, bool bFreezeSourceCamera)
```

Wrap the current tree's `RootNode` (the resuming camera, intact with all its accumulated per-node state) as the TARGET of a new pop transition, with a reference leaf capturing `SourceDirector`'s tree root as a snapshot on the SOURCE side. Used by context-stack pops so the resumed camera is the ORIGINAL instance that was running before the push — not a fresh instance spawned at pop time with zeroed damping / interpolator / spline-progress / etc. state.

The snapshot-based RefLeaf (see comments on the RefLeaf wrapper and `OnActivateNewCameraWithReferenceSource`) is the reason this is safe even when the source director's tree still holds a push-side RefLeaf pointing back to us: snapshots don't follow root mutations, so the resulting reachable graph is a DAG, not a cycle.

Preserves the invariant "every camera is an instance; same-type
cameras don't share lifecycle": the pre-push camera keeps ticking through the push period (via the pushed context's reference leaf snapshot) and at pop it is re-wrapped — never destroyed, never replaced by a sibling instance.

Precondition: `RootNode` is non-null (there IS a camera to resume). Callers that don't have a pre-existing camera should use `OnActivateNewCameraWithReferenceSource` instead.

---

#### HasActiveCamera { #hasactivecamera }

`const`

```cpp
bool HasActiveCamera() const
```

Returns true if the tree has at least one active camera.

---

#### GetRunningCamera { #getrunningcamera-2 }

`const` `inline`

```cpp
inline AComposableCameraCameraBase * GetRunningCamera() const
```

Get the current running camera (set when a camera is activated, updated on tree rebuild).

---

#### GetRootNode { #getrootnode }

`const` `inline`

```cpp
inline const TSharedPtr< FComposableCameraEvaluationTreeNode > & GetRootNode() const
```

Read-only access to the current root node. Used by director-to-director inter-context APIs to capture a `TSharedPtr` snapshot of this tree's current shape when creating a reference leaf in another tree — the returned pointer is shared (not copied), so the snapshot keeps the captured subtree alive even if THIS tree later swaps its root. Returns null if no camera has been activated yet.

---

#### DestroyAll { #destroyall-1 }

```cpp
void DestroyAll()
```

Destroy all cameras in the tree and reset to empty.

---

#### BuildDebugSnapshot { #builddebugsnapshot-3 }

`const`

```cpp
void BuildDebugSnapshot(TArray< FComposableCameraTreeNodeSnapshot > & OutNodes) const
```

Build a flat DFS pre-order snapshot of the tree for every debug consumer (2D panel, `showdebug camera`, dump commands — all render from the snapshot through `[ComposableCameraDebug::AppendTreeNodeLine](../free-functions/Functions.md#appendtreenodeline)`). Appends to OutNodes (caller is responsible for Reset if starting fresh). Computes bIsDominantLeaf as part of the walk (root → Right* → leaf).

---

#### DrawTransitionsDebug { #drawtransitionsdebug }

`const`

```cpp
void DrawTransitionsDebug(class UWorld * World, bool bViewerIsOutsideCamera) const
```

Walk every Inner (transition) node reachable from the tree's root and invoke `[UComposableCameraTransitionBase::DrawTransitionDebug](../transitions/UComposableCameraTransitionBase.md#drawtransitiondebug-1)` on each. Each transition self-gates on its own `CCS.Debug.Viewport.Transitions.<Name>` CVar — if none are enabled, this call is effectively free.

When the walk hits a reference leaf, it recurses into the captured `SnapshotRoot` so any intra-context transition still in flight inside the snapshot is also drawn. Since snapshot RefLeaves form a DAG (multiple RefLeaves can share a SnapshotRoot; one Inner inside a snapshot can be reached via two paths), visited-node deduplication inside the recursive helper ensures each transition draws once per frame.

**Parameters**

* `World` World to draw into (routed through the LineBatcher → visible in every viewport). 

* `bViewerIsOutsideCamera` Same convention as node debug: true while the player is NOT looking through the blended camera. Passed through to each transition's override so it can gate frustum pieces.

Compiled out in shipping builds.

### Public Static Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`AddReferencedObjects`](#addreferencedobjects-1) `static` |  |

---

#### AddReferencedObjects { #addreferencedobjects-1 }

`static`

```cpp
static void AddReferencedObjects(UObject * InThis, FReferenceCollector & Collector)
```

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TSharedPtr< FComposableCameraEvaluationTreeNode >` | [`RootNode`](#rootnode)  | Root of the evaluation tree. Null if no camera has been activated yet. |
| `TObjectPtr< AComposableCameraCameraBase >` | [`RunningCamera`](#runningcamera-1)  | Currently running (target) camera. |
| `TArray< TSharedPtr< FComposableCameraEvaluationTreeNode > >` | [`PendingDestroyOldRoots`](#pendingdestroyoldroots)  | Subtrees detached from `RootNode` by a previous activation but whose camera actors must stay alive until the activation's transition finishes. |

---

#### RootNode { #rootnode }

```cpp
TSharedPtr< FComposableCameraEvaluationTreeNode > RootNode
```

Root of the evaluation tree. Null if no camera has been activated yet.

---

#### RunningCamera { #runningcamera-1 }

```cpp
TObjectPtr< AComposableCameraCameraBase > RunningCamera
```

Currently running (target) camera.

---

#### PendingDestroyOldRoots { #pendingdestroyoldroots }

```cpp
TArray< TSharedPtr< FComposableCameraEvaluationTreeNode > > PendingDestroyOldRoots
```

Subtrees detached from `RootNode` by a previous activation but whose camera actors must stay alive until the activation's transition finishes.

Why defer: `OnActivateNewCameraWithReferenceSource` replaces the root with `Inner(T, RefLeaf→source director snapshot, NewLeaf)`. If the source director had been PUSHED onto us earlier, its snapshot was captured FROM our old root — so the source director's RefLeaf holds a TSharedPtr to our pre-replacement RootNode. Destroying that subtree's cameras immediately would leave the source director's Tick path walking into `Leaf.RunningCamera` actors that were marked PendingKill mid-blend. Symptom (before fix): `[leaf] (destroyed)` rows in both context trees in the Debug Panel + `"RunningCamera is null or
destroyed when evaluating leaf node."` spam from `[FComposableCameraEvaluationTreeLeafNodeWrapper::Evaluate](../structs/FComposableCameraEvaluationTreeLeafNodeWrapper.md#evaluate-12)` while T is still in flight.

When it is safe to destroy: once T finishes, `CollapseFinishedTransitions` drops the RefLeaf branch from our new root. At that moment the old subtree is no longer reachable from *our* tree, so its actors can be destroyed without affecting anything this director walks.

Cleanup triggers (in priority order):

1. `InTransition->OnTransitionFinishesDelegate` — normal completion.

1. `[DestroyAll()](#destroyall-1)` — shutdown / context pop. Edge case: if the transition is replaced (another activation fires before T completes), the pending subtree lingers here until (2) eventually fires. That's a memory cost, not a correctness bug.

GC: the entries here are registered with the reference collector via `AddReferencedObjects` so the cameras/transitions inside stay alive until we explicitly destroy them below.

### Private Methods

| Return | Name | Description |
|--------|------|-------------|
| `TSharedPtr< FComposableCameraEvaluationTreeNode >` | [`CollapseFinishedTransitions`](#collapsefinishedtransitions)  | Collapse finished transitions in the tree. |
| `void` | [`DestroySubtreeCameras`](#destroysubtreecameras)  | Recursively destroy all camera actors referenced by a subtree. |

---

#### CollapseFinishedTransitions { #collapsefinishedtransitions }

```cpp
TSharedPtr< FComposableCameraEvaluationTreeNode > CollapseFinishedTransitions(const TSharedPtr< FComposableCameraEvaluationTreeNode > & Node)
```

Collapse finished transitions in the tree.

When an inner node's transition is finished (or its source is destroyed), the node is replaced by its right (target) subtree and the left (source) subtree's cameras are destroyed.

Transient cameras are not managed here — they live in separate contexts and their lifecycle is handled by the context stack's auto-pop mechanism.

**Returns**

The node that should replace the input node in the tree.

---

#### DestroySubtreeCameras { #destroysubtreecameras }

```cpp
void DestroySubtreeCameras(const TSharedPtr< FComposableCameraEvaluationTreeNode > & Node)
```

Recursively destroy all camera actors referenced by a subtree.

### Private Static Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`FreezeSubtree`](#freezesubtree) `static` | Recursively set bFrozen on all leaf and reference-leaf nodes in a subtree. Used when bFreezeSourceCamera is set on activation — the entire outgoing blend tree holds its last pose during the transition. |
| `void` | [`BuildNodeDebugSnapshot`](#buildnodedebugsnapshot) `static` | Recursively flatten a subtree into the snapshot node array. DominantNodePtr marks the one node along the root → Right* → leaf chain that should be tagged bIsDominantLeaf = true. bIsLastSibling is false for Left children of Inner nodes, true for Right children and for the tree root. AncestorLastFlagsBitmask carries the ancestor chain's last-child flags so the renderer can draw proper `├ / └` connectors and `│` continuations. |
| `void` | [`AddTreeReferencedObjects`](#addtreereferencedobjects) `static` | Recursively register UObject references in the tree for garbage collection. |
| `void` | [`DrawTransitionsNodeDebug`](#drawtransitionsnodedebug) `static` | Recursive companion to `DrawTransitionsDebug`. Inner → invoke the transition's override + recurse into both children. ReferenceLeaf → recurse into the captured SnapshotRoot so intra-blend transitions inside the snapshot still draw. Leaf → terminate. |

---

#### FreezeSubtree { #freezesubtree }

`static`

```cpp
static void FreezeSubtree(const TSharedPtr< FComposableCameraEvaluationTreeNode > & Node, bool bFrozen)
```

Recursively set bFrozen on all leaf and reference-leaf nodes in a subtree. Used when bFreezeSourceCamera is set on activation — the entire outgoing blend tree holds its last pose during the transition.

---

#### BuildNodeDebugSnapshot { #buildnodedebugsnapshot }

`static`

```cpp
static void BuildNodeDebugSnapshot(const TSharedPtr< FComposableCameraEvaluationTreeNode > & Node, int32 Depth, bool bIsLastSibling, uint32 AncestorLastFlagsBitmask, const FComposableCameraEvaluationTreeNode * DominantNodePtr, TArray< FComposableCameraTreeNodeSnapshot > & OutNodes, bool bInReferencedSubtree)
```

Recursively flatten a subtree into the snapshot node array. DominantNodePtr marks the one node along the root → Right* → leaf chain that should be tagged bIsDominantLeaf = true. bIsLastSibling is false for Left children of Inner nodes, true for Right children and for the tree root. AncestorLastFlagsBitmask carries the ancestor chain's last-child flags so the renderer can draw proper `├ / └` connectors and `│` continuations.

When the walk hits a ReferenceLeaf with a valid SnapshotRoot, it emits the RefLeaf node first and then recursively flattens the referenced subtree inline (depth bumped by 1). All nodes flattened from the referenced subtree get `bInReferencedSubtree = true`, and the subtree's root additionally gets `bIsReferencedRoot = true` so the renderer can suppress the `[from]/[to]` role prefix at the RefLeaf seam (the invariant "Depth > 0 ⇒ transition parent" does not hold across that boundary). `bInReferencedSubtree` is propagated through recursive calls via the extra argument; callers from a regular tree pass the default false. Dominant-leaf tagging is skipped inside referenced subtrees — the frozen source snapshot does not participate in the active tree's collapse chain.

---

#### AddTreeReferencedObjects { #addtreereferencedobjects }

`static`

```cpp
static void AddTreeReferencedObjects(const TSharedPtr< FComposableCameraEvaluationTreeNode > & Node, FReferenceCollector & Collector)
```

Recursively register UObject references in the tree for garbage collection.

---

#### DrawTransitionsNodeDebug { #drawtransitionsnodedebug }

`static`

```cpp
static void DrawTransitionsNodeDebug(const TSharedPtr< FComposableCameraEvaluationTreeNode > & Node, class UWorld * World, bool bViewerIsOutsideCamera, TSet< const FComposableCameraEvaluationTreeNode * > & VisitedNodes)
```

Recursive companion to `DrawTransitionsDebug`. Inner → invoke the transition's override + recurse into both children. ReferenceLeaf → recurse into the captured SnapshotRoot so intra-blend transitions inside the snapshot still draw. Leaf → terminate.

`VisitedNodes` is a DAG-deduplication set: two RefLeaves can share the same SnapshotRoot (or an Inner inside a snapshot can be reached via two paths). Skipping already-visited nodes prevents a transition from drawing its gizmos twice per frame.
