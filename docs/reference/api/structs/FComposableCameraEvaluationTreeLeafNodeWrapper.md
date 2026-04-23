
# FComposableCameraEvaluationTreeLeafNodeWrapper { #fcomposablecameraevaluationtreeleafnodewrapper }

```cpp
#include <ComposableCameraEvaluationTree.h>
```

Leaf node wrapper: wraps a single running camera.

No per-wrapper memoization is kept here. Multiple TSharedPtrs may point at the SAME Leaf-wrapped node (that's exactly what makes the evaluation graph a DAG under the snapshot-RefLeaf scheme) but they all call into the same `[AComposableCameraCameraBase::TickCamera](../actors/AComposableCameraCameraBase.md#tickcamera)`, which itself short-circuits on `LastTickedFrameCounter == GFrameCounter` and returns the cached pose without re-walking the node chain. Caching at that layer is authoritative for any caller.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TObjectPtr< AComposableCameraCameraBase >` | [`RunningCamera`](#runningcamera-3)  |  |
| `bool` | [`bFrozen`](#bfrozen)  | When true, Evaluate returns the camera's cached pose without ticking it. |

---

#### RunningCamera { #runningcamera-3 }

```cpp
TObjectPtr< AComposableCameraCameraBase > RunningCamera { nullptr }
```

---

#### bFrozen { #bfrozen }

```cpp
bool bFrozen { false }
```

When true, Evaluate returns the camera's cached pose without ticking it.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `FComposableCameraPose` | [`Evaluate`](#evaluate-12)  |  |

---

#### Evaluate { #evaluate-12 }

```cpp
FComposableCameraPose Evaluate(float DeltaTime)
```
