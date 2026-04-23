
# FComposableCameraEvaluationTreeInnerNodeWrapper { #fcomposablecameraevaluationtreeinnernodewrapper }

```cpp
#include <ComposableCameraEvaluationTree.h>
```

Inner node wrapper: wraps a transition that blends between a source (left) and target (right) subtree. Owns its child nodes via shared pointers.

Per-frame memoization (same rationale as LeafNodeWrapper): a snapshot DAG can traverse the same Inner node twice in one frame, and `Transition->Evaluate` decrements `RemainingTime` — so a naive re-entry would make the transition run at 2× speed. Cache the blended pose on first access and return it verbatim on every subsequent access in the same frame.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TObjectPtr< UComposableCameraTransitionBase >` | [`Transition`](#transition-2)  |  |
| `TSharedPtr< FComposableCameraEvaluationTreeNode >` | [`LeftNode`](#leftnode)  |  |
| `TSharedPtr< FComposableCameraEvaluationTreeNode >` | [`RightNode`](#rightnode)  |  |
| `uint64` | [`LastEvaluatedFrameCounter`](#lastevaluatedframecounter)  | GFrameCounter at the last time this node's Evaluate advanced the transition. |
| `FComposableCameraPose` | [`CachedBlendedPose`](#cachedblendedpose)  | Blended pose from the last Evaluate at `LastEvaluatedFrameCounter`. |

---

#### Transition { #transition-2 }

```cpp
TObjectPtr< UComposableCameraTransitionBase > Transition { nullptr }
```

---

#### LeftNode { #leftnode }

```cpp
TSharedPtr< FComposableCameraEvaluationTreeNode > LeftNode
```

---

#### RightNode { #rightnode }

```cpp
TSharedPtr< FComposableCameraEvaluationTreeNode > RightNode
```

---

#### LastEvaluatedFrameCounter { #lastevaluatedframecounter }

```cpp
uint64 LastEvaluatedFrameCounter { 0 }
```

GFrameCounter at the last time this node's Evaluate advanced the transition.

---

#### CachedBlendedPose { #cachedblendedpose }

```cpp
FComposableCameraPose CachedBlendedPose
```

Blended pose from the last Evaluate at `LastEvaluatedFrameCounter`.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `FComposableCameraPose` | [`Evaluate`](#evaluate-13)  |  |

---

#### Evaluate { #evaluate-13 }

```cpp
FComposableCameraPose Evaluate(float DeltaTime)
```
