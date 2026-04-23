
# FComposableCameraEvaluationTreeReferenceLeafNodeWrapper { #fcomposablecameraevaluationtreereferenceleafnodewrapper }

```cpp
#include <ComposableCameraEvaluationTree.h>
```

Reference leaf node wrapper: a lightweight leaf that re-evaluates a captured SUBTREE SNAPSHOT, not a live Director.

Semantics (snapshot, not live): The RefLeaf holds a `TSharedPtr` to the node that was the source director's tree root AT THE TIME THE REFLEAF WAS CREATED. Even if the source director's tree root is later swapped out (e.g. wrapped by a pop Inner), the RefLeaf keeps pointing at the original snapshot.

Why snapshot instead of live: A live reference produces self-recursion during a pop-while-push scenario: A.tree.root is now Inner(pop, RefLeaf→B, OldA), B.tree.root is still Inner(push, RefLeaf→A, CamB); evaluating A → B → A loops. A snapshot captures exactly the subtree that should contribute to the blend (the original OldA leaf, not the new wrapped root), so the topology becomes a DAG with no cycles.

Ownership: Does NOT own cameras. Shared `TSharedPtr<Node>` means the subtree stays alive as long as any RefLeaf references it. Cameras inside the snapshot are owned by their original Director and destroyed on that Director's DestroyAllCameras (usually fired from the transition- finished delegate after this RefLeaf has already been collapsed).

Debug-only Director pointer: `DebugSourceDirector` is kept purely for label display (e.g. "[RefLeaf] -> Director_Gameplay" in the debug panel). The runtime path never calls through it — use only the SnapshotRoot.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TSharedPtr< FComposableCameraEvaluationTreeNode >` | [`SnapshotRoot`](#snapshotroot)  | Captured subtree to re-evaluate. Non-owning in the UObject sense — `TSharedPtr` keeps the tree struct alive; UObject references inside the subtree are tracked via `AddTreeReferencedObjects`. |
| `TWeakObjectPtr< UComposableCameraDirector >` | [`DebugSourceDirector`](#debugsourcedirector)  | Debug-only: the director that provided the snapshot. Used for human-readable labels; never dereferenced on the evaluation path. |
| `bool` | [`bFrozen`](#bfrozen-1)  | When true, Evaluate returns the last cached pose from the snapshot without re-evaluating it — the whole captured subtree is held frozen for the duration of this RefLeaf's life. |
| `FComposableCameraPose` | [`CachedPose`](#cachedpose)  | Cached pose from the last live evaluation — used both for the `bFrozen == true` path and as the cheap answer when the caller already retrieved it earlier this frame. |
| `uint64` | [`LastEvaluatedFrameCounter`](#lastevaluatedframecounter-1)  | GFrameCounter at the last time the snapshot was evaluated. |

---

#### SnapshotRoot { #snapshotroot }

```cpp
TSharedPtr< FComposableCameraEvaluationTreeNode > SnapshotRoot
```

Captured subtree to re-evaluate. Non-owning in the UObject sense — `TSharedPtr` keeps the tree struct alive; UObject references inside the subtree are tracked via `AddTreeReferencedObjects`.

---

#### DebugSourceDirector { #debugsourcedirector }

```cpp
TWeakObjectPtr< UComposableCameraDirector > DebugSourceDirector
```

Debug-only: the director that provided the snapshot. Used for human-readable labels; never dereferenced on the evaluation path.

---

#### bFrozen { #bfrozen-1 }

```cpp
bool bFrozen { false }
```

When true, Evaluate returns the last cached pose from the snapshot without re-evaluating it — the whole captured subtree is held frozen for the duration of this RefLeaf's life.

---

#### CachedPose { #cachedpose }

```cpp
FComposableCameraPose CachedPose
```

Cached pose from the last live evaluation — used both for the `bFrozen == true` path and as the cheap answer when the caller already retrieved it earlier this frame.

---

#### LastEvaluatedFrameCounter { #lastevaluatedframecounter-1 }

```cpp
uint64 LastEvaluatedFrameCounter { 0 }
```

GFrameCounter at the last time the snapshot was evaluated.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `FComposableCameraPose` | [`Evaluate`](#evaluate-16)  |  |

---

#### Evaluate { #evaluate-16 }

```cpp
FComposableCameraPose Evaluate(float DeltaTime)
```
