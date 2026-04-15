
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
| `void` | [`OnActivateNewCameraWithReferenceSource`](#onactivatenewcamerawithreferencesource)  | Activate a new camera with a reference to another context's Director as the transition source. Used for inter-context transitions: the reference leaf evaluates the source context live (not frozen), producing smooth blending between contexts. |
| `bool` | [`HasActiveCamera`](#hasactivecamera) `const` | Returns true if the tree has at least one active camera. |
| `AComposableCameraCameraBase *` | [`GetRunningCamera`](#getrunningcamera-2) `const` `inline` | Get the current running camera (set when a camera is activated, updated on tree rebuild). |
| `void` | [`DestroyAll`](#destroyall)  | Destroy all cameras in the tree and reset to empty. |
| `void` | [`BuildDebugString`](#builddebugstring-2) `const` | Build a debug string representation of the evaluation tree structure. |

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
void OnActivateNewCamera(AComposableCameraCameraBase * NewCamera, UComposableCameraTransitionBase * Transition)
```

Called when a new camera is activated, optionally with a transition from the current state.

---

#### OnActivateNewCameraWithReferenceSource { #onactivatenewcamerawithreferencesource }

```cpp
void OnActivateNewCameraWithReferenceSource(AComposableCameraCameraBase * NewCamera, UComposableCameraTransitionBase * Transition, UComposableCameraDirector * SourceDirector)
```

Activate a new camera with a reference to another context's Director as the transition source. Used for inter-context transitions: the reference leaf evaluates the source context live (not frozen), producing smooth blending between contexts.

**Parameters**

* `NewCamera` The new camera to activate in this context. 

* `Transition` The transition to blend from the referenced Director's output to NewCamera. 

* `SourceDirector` The Director from the source context to reference as the left (source) side.

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

#### DestroyAll { #destroyall }

```cpp
void DestroyAll()
```

Destroy all cameras in the tree and reset to empty.

---

#### BuildDebugString { #builddebugstring-2 }

`const`

```cpp
void BuildDebugString(TStringBuilder< 1024 > & OutString, int32 IndentLevel) const
```

Build a debug string representation of the evaluation tree structure.

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
| `void` | [`BuildNodeDebugString`](#buildnodedebugstring) `static` | Recursively build a debug string for a subtree. |
| `void` | [`AddTreeReferencedObjects`](#addtreereferencedobjects) `static` | Recursively register UObject references in the tree for garbage collection. |

---

#### BuildNodeDebugString { #buildnodedebugstring }

`static`

```cpp
static void BuildNodeDebugString(const TSharedPtr< FComposableCameraEvaluationTreeNode > & Node, TStringBuilder< 1024 > & OutString, int32 IndentLevel)
```

Recursively build a debug string for a subtree.

---

#### AddTreeReferencedObjects { #addtreereferencedobjects }

`static`

```cpp
static void AddTreeReferencedObjects(const TSharedPtr< FComposableCameraEvaluationTreeNode > & Node, FReferenceCollector & Collector)
```

Recursively register UObject references in the tree for garbage collection.
