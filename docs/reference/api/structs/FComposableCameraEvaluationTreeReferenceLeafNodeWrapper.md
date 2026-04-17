
# FComposableCameraEvaluationTreeReferenceLeafNodeWrapper { #fcomposablecameraevaluationtreereferenceleafnodewrapper }

```cpp
#include <ComposableCameraEvaluationTree.h>
```

Reference leaf node wrapper: a lightweight leaf that evaluates another context's Director rather than owning a camera. Used for inter-context transitions so that the source context continues to tick live while the target context blends in.

This node does NOT own any cameras — it just forwards evaluation to the referenced Director. When the transition collapses, this node is simply discarded (no cameras to destroy).

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TObjectPtr< UComposableCameraDirector >` | [`ReferencedDirector`](#referenceddirector)  | The Director from another context that this node evaluates. |
| `bool` | [`bFrozen`](#bfrozen-1)  | When true, Evaluate returns the Director's last evaluated pose without re-evaluating it. |

---

#### ReferencedDirector { #referenceddirector }

```cpp
TObjectPtr< UComposableCameraDirector > ReferencedDirector { nullptr }
```

The Director from another context that this node evaluates.

---

#### bFrozen { #bfrozen-1 }

```cpp
bool bFrozen { false }
```

When true, Evaluate returns the Director's last evaluated pose without re-evaluating it.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `FComposableCameraPose` | [`Evaluate`](#evaluate-16)  |  |

---

#### Evaluate { #evaluate-16 }

```cpp
FComposableCameraPose Evaluate(float DeltaTime)
```
