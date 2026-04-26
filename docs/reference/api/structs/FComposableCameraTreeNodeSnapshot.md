
# FComposableCameraTreeNodeSnapshot { #fcomposablecameratreenodesnapshot }

```cpp
#include <ComposableCameraDebugPanelData.h>
```

One node in an evaluation tree, flattened. Produced by [UComposableCameraEvaluationTree::BuildDebugSnapshot](../core/UComposableCameraEvaluationTree.md#builddebugsnapshot-3).

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `EComposableCameraTreeNodeKind` | [`Kind`](#kind)  | Node kind. |
| `int32` | [`Depth`](#depth)  | Depth in the tree (root of this director's tree is 0). |
| `FString` | [`DisplayLabel`](#displaylabel)  | Primary display label (camera name / director name / transition class name). |
| `bool` | [`bDestroyed`](#bdestroyed)  | True if the underlying pointer was IsValid-false at snapshot time. |
| `bool` | [`bIsDominantLeaf`](#bisdominantleaf)  | True for the single "dominant" leaf in this tree — the one that would remain if every transition collapsed immediately. Computed by walking root → Right → Right → ... → leaf. Leaves that are part of an active transition's source (Left) side will have this as false. |
| `bool` | [`bIsLastSibling`](#bislastsibling)  | True if this node is the last child of its parent. For an InnerTransition parent, the Left (source) child has this false and the Right (target) child has this true. Trivially true for tree roots. Drives whether the connector glyph is drawn as `└` (last) or `├` (middle). |
| `uint32` | [`AncestorLastFlagsBitmask`](#ancestorlastflagsbitmask)  | Bitmask where bit L is set iff the ancestor at depth L was the last child of its parent. Drives whether a continuation stem `│` is drawn at column L for this line: stem present iff bit (L+1) is 0 (i.e. the ancestor at depth L+1 was NOT last, so its parent's subtree is still incomplete). |
| `bool` | [`bIsTransient`](#bistransient-2)  | True if the leaf's camera is marked transient. |
| `float` | [`LifeElapsed`](#lifeelapsed)  | Lifetime elapsed in seconds (only meaningful when bIsTransient). |
| `float` | [`LifeTotal`](#lifetotal)  | Total lifetime in seconds (only meaningful when bIsTransient). |
| `float` | [`TransitionProgress`](#transitionprogress)  | Transition progress in [0..1]. -1 if transition is null. |
| `float` | [`TransitionElapsed`](#transitionelapsed)  | Elapsed transition time in seconds. |
| `float` | [`TransitionTotal`](#transitiontotal)  | Total transition time in seconds. |
| `bool` | [`bInReferencedSubtree`](#binreferencedsubtree)  | True if this node was flattened from a ReferenceLeaf's `SnapshotRoot` — i.e. it belongs to the referenced *source* director's tree that has been inlined under a ReferenceLeaf during the snapshot build. Panel renderer uses this to pick a dimmer color (the referenced tree is a frozen source snapshot, not the active target tree). |
| `bool` | [`bIsReferencedRoot`](#bisreferencedroot)  | True only on the single node that is the direct child of a ReferenceLeaf (the referenced subtree's root). Suppresses the `[from]/[to]` role prefix at that seam — the usual "Depth > 0 ⇒ transition parent" invariant does not hold across the RefLeaf boundary (a RefLeaf is a leaf in the outer tree with a synthetic 1-child visual expansion; it is not a transition). |
| `TArray< float >` | [`BlendCurveSamples`](#blendcurvesamples)  | Blend-weight curve sampled at N+1 evenly spaced points in [0, 1], produced by calling `GetBlendWeightAt(i/N)` on the live transition at snapshot-build time. Drives the debug panel's in-row sparkline: amber "area-under-curve" filled up to `TransitionProgress` shows how far the blend has gone along its timing curve, and a thin outline shows the entire curve shape. |

---

#### Kind { #kind }

```cpp
EComposableCameraTreeNodeKind Kind = 
```

Node kind.

---

#### Depth { #depth }

```cpp
int32 Depth = 0
```

Depth in the tree (root of this director's tree is 0).

---

#### DisplayLabel { #displaylabel }

```cpp
FString DisplayLabel
```

Primary display label (camera name / director name / transition class name).

---

#### bDestroyed { #bdestroyed }

```cpp
bool bDestroyed = false
```

True if the underlying pointer was IsValid-false at snapshot time.

---

#### bIsDominantLeaf { #bisdominantleaf }

```cpp
bool bIsDominantLeaf = false
```

True for the single "dominant" leaf in this tree — the one that would remain if every transition collapsed immediately. Computed by walking root → Right → Right → ... → leaf. Leaves that are part of an active transition's source (Left) side will have this as false.

---

#### bIsLastSibling { #bislastsibling }

```cpp
bool bIsLastSibling = true
```

True if this node is the last child of its parent. For an InnerTransition parent, the Left (source) child has this false and the Right (target) child has this true. Trivially true for tree roots. Drives whether the connector glyph is drawn as `└` (last) or `├` (middle).

---

#### AncestorLastFlagsBitmask { #ancestorlastflagsbitmask }

```cpp
uint32 AncestorLastFlagsBitmask = 0
```

Bitmask where bit L is set iff the ancestor at depth L was the last child of its parent. Drives whether a continuation stem `│` is drawn at column L for this line: stem present iff bit (L+1) is 0 (i.e. the ancestor at depth L+1 was NOT last, so its parent's subtree is still incomplete).

A 32-bit mask caps tree depth at 32 for debug visualization, which is ~30 levels beyond anything a real camera composition produces.

---

#### bIsTransient { #bistransient-2 }

```cpp
bool bIsTransient = false
```

True if the leaf's camera is marked transient.

---

#### LifeElapsed { #lifeelapsed }

```cpp
float LifeElapsed = 0.f
```

Lifetime elapsed in seconds (only meaningful when bIsTransient).

---

#### LifeTotal { #lifetotal }

```cpp
float LifeTotal = 0.f
```

Total lifetime in seconds (only meaningful when bIsTransient).

---

#### TransitionProgress { #transitionprogress }

```cpp
float TransitionProgress = -1.f
```

Transition progress in [0..1]. -1 if transition is null.

---

#### TransitionElapsed { #transitionelapsed }

```cpp
float TransitionElapsed = 0.f
```

Elapsed transition time in seconds.

---

#### TransitionTotal { #transitiontotal }

```cpp
float TransitionTotal = 0.f
```

Total transition time in seconds.

---

#### bInReferencedSubtree { #binreferencedsubtree }

```cpp
bool bInReferencedSubtree = false
```

True if this node was flattened from a ReferenceLeaf's `SnapshotRoot` — i.e. it belongs to the referenced *source* director's tree that has been inlined under a ReferenceLeaf during the snapshot build. Panel renderer uses this to pick a dimmer color (the referenced tree is a frozen source snapshot, not the active target tree).

---

#### bIsReferencedRoot { #bisreferencedroot }

```cpp
bool bIsReferencedRoot = false
```

True only on the single node that is the direct child of a ReferenceLeaf (the referenced subtree's root). Suppresses the `[from]/[to]` role prefix at that seam — the usual "Depth > 0 ⇒ transition parent" invariant does not hold across the RefLeaf boundary (a RefLeaf is a leaf in the outer tree with a synthetic 1-child visual expansion; it is not a transition).

---

#### BlendCurveSamples { #blendcurvesamples }

```cpp
TArray< float > BlendCurveSamples
```

Blend-weight curve sampled at N+1 evenly spaced points in [0, 1], produced by calling `GetBlendWeightAt(i/N)` on the live transition at snapshot-build time. Drives the debug panel's in-row sparkline: amber "area-under-curve" filled up to `TransitionProgress` shows how far the blend has gone along its timing curve, and a thin outline shows the entire curve shape.

Empty for non-transition nodes and for transitions whose pointer was null at snapshot time. 24 samples (25 values) is the convention used by `BuildNodeDebugSnapshot` — enough for Ease / Cubic / Smoother shoulders to read distinctly at typical panel widths, while staying a trivial allocation cost.
