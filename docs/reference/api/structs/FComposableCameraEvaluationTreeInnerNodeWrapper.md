
# FComposableCameraEvaluationTreeInnerNodeWrapper { #fcomposablecameraevaluationtreeinnernodewrapper }

```cpp
#include <ComposableCameraEvaluationTree.h>
```

Inner node wrapper: wraps a transition that blends between a source (left) and target (right) subtree. Owns its child nodes via shared pointers.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TObjectPtr< UComposableCameraTransitionBase >` | [`Transition`](#transition-2)  |  |
| `TSharedPtr< FComposableCameraEvaluationTreeNode >` | [`LeftNode`](#leftnode)  |  |
| `TSharedPtr< FComposableCameraEvaluationTreeNode >` | [`RightNode`](#rightnode)  |  |

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

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `FComposableCameraPose` | [`Evaluate`](#evaluate-13)  |  |

---

#### Evaluate { #evaluate-13 }

```cpp
FComposableCameraPose Evaluate(float DeltaTime)
```
