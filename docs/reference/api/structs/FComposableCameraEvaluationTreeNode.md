
# FComposableCameraEvaluationTreeNode { #fcomposablecameraevaluationtreenode }

```cpp
#include <ComposableCameraEvaluationTree.h>
```

A node in the evaluation tree. Can be a leaf (camera), a reference leaf (another context's Director), or an inner (transition) node.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TVariant< FComposableCameraEvaluationTreeLeafNodeWrapper, FComposableCameraEvaluationTreeReferenceLeafNodeWrapper, FComposableCameraEvaluationTreeInnerNodeWrapper >` | [`Wrapper`](#wrapper)  |  |

---

#### Wrapper { #wrapper }

```cpp
TVariant< FComposableCameraEvaluationTreeLeafNodeWrapper, FComposableCameraEvaluationTreeReferenceLeafNodeWrapper, FComposableCameraEvaluationTreeInnerNodeWrapper > Wrapper
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `FComposableCameraPose` | [`Evaluate`](#evaluate-7)  |  |
| `bool` | [`IsLeaf`](#isleaf) `const` | Returns true if this is a leaf node (wraps a camera). |
| `bool` | [`IsReferenceLeaf`](#isreferenceleaf) `const` | Returns true if this is a reference leaf node (wraps another context's Director). |
| `bool` | [`IsInner`](#isinner) `const` | Returns true if this is an inner node (wraps a transition). |
| `FComposableCameraEvaluationTreeLeafNodeWrapper &` | [`AsLeaf`](#asleaf)  | Access the leaf wrapper. Only valid when [IsLeaf()](#isleaf) is true. |
| `const FComposableCameraEvaluationTreeLeafNodeWrapper &` | [`AsLeaf`](#asleaf-1) `const` |  |
| `FComposableCameraEvaluationTreeReferenceLeafNodeWrapper &` | [`AsReferenceLeaf`](#asreferenceleaf)  | Access the reference leaf wrapper. Only valid when [IsReferenceLeaf()](#isreferenceleaf) is true. |
| `const FComposableCameraEvaluationTreeReferenceLeafNodeWrapper &` | [`AsReferenceLeaf`](#asreferenceleaf-1) `const` |  |
| `FComposableCameraEvaluationTreeInnerNodeWrapper &` | [`AsInner`](#asinner)  | Access the inner wrapper. Only valid when [IsInner()](#isinner) is true. |
| `const FComposableCameraEvaluationTreeInnerNodeWrapper &` | [`AsInner`](#asinner-1) `const` |  |

---

#### Evaluate { #evaluate-7 }

```cpp
FComposableCameraPose Evaluate(float DeltaTime)
```

---

#### IsLeaf { #isleaf }

`const`

```cpp
bool IsLeaf() const
```

Returns true if this is a leaf node (wraps a camera).

---

#### IsReferenceLeaf { #isreferenceleaf }

`const`

```cpp
bool IsReferenceLeaf() const
```

Returns true if this is a reference leaf node (wraps another context's Director).

---

#### IsInner { #isinner }

`const`

```cpp
bool IsInner() const
```

Returns true if this is an inner node (wraps a transition).

---

#### AsLeaf { #asleaf }

```cpp
FComposableCameraEvaluationTreeLeafNodeWrapper & AsLeaf()
```

Access the leaf wrapper. Only valid when [IsLeaf()](#isleaf) is true.

---

#### AsLeaf { #asleaf-1 }

`const`

```cpp
const FComposableCameraEvaluationTreeLeafNodeWrapper & AsLeaf() const
```

---

#### AsReferenceLeaf { #asreferenceleaf }

```cpp
FComposableCameraEvaluationTreeReferenceLeafNodeWrapper & AsReferenceLeaf()
```

Access the reference leaf wrapper. Only valid when [IsReferenceLeaf()](#isreferenceleaf) is true.

---

#### AsReferenceLeaf { #asreferenceleaf-1 }

`const`

```cpp
const FComposableCameraEvaluationTreeReferenceLeafNodeWrapper & AsReferenceLeaf() const
```

---

#### AsInner { #asinner }

```cpp
FComposableCameraEvaluationTreeInnerNodeWrapper & AsInner()
```

Access the inner wrapper. Only valid when [IsInner()](#isinner) is true.

---

#### AsInner { #asinner-1 }

`const`

```cpp
const FComposableCameraEvaluationTreeInnerNodeWrapper & AsInner() const
```
