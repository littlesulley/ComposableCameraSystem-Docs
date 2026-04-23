
# UComposableCameraLinearTransition { #ucomposablecameralineartransition }

```cpp
#include <ComposableCameraLinearTransition.h>
```

> **Inherits:** [`UComposableCameraTransitionBase`](UComposableCameraTransitionBase.md#ucomposablecameratransitionbase)

Linear transition.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `FComposableCameraPose` | [`OnEvaluate_Implementation`](#onevaluate_implementation-3) `virtual` |  |
| `void` | [`DrawTransitionDebug`](#drawtransitiondebug-3) `virtual` `const` | Per-transition world-space debug hook. |

---

#### OnEvaluate_Implementation { #onevaluate_implementation-3 }

`virtual`

```cpp
virtual FComposableCameraPose OnEvaluate_Implementation(float DeltaTime, const FComposableCameraPose & CurrentSourcePose, const FComposableCameraPose & CurrentTargetPose)
```

---

#### DrawTransitionDebug { #drawtransitiondebug-3 }

`virtual` `const`

```cpp
virtual void DrawTransitionDebug(UWorld * World, bool bViewerIsOutsideCamera) const
```

Per-transition world-space debug hook.

Invoked from `[UComposableCameraEvaluationTree::DrawTransitionsDebug](../core/UComposableCameraEvaluationTree.md#drawtransitionsdebug)` while `CCS.Debug.Viewport` is on, once per frame for every transition that currently sits in an Inner node of the active director's tree (and, recursively, of any referenced director's tree — inter-context blends see both sides).

Default implementation is empty. Concrete transitions override, check their own `CCS.Debug.Viewport.Transitions.<Name>` CVar, and usually call `DrawStandardTransitionDebug` plus any type-specific extras (spline curve sample, feeler rays, etc.).

**Parameters**

* `World` World to draw into. Routes through the world's LineBatcher, so the draw is visible in every viewport that renders this world (game + F8-ejected editor). 

* `bViewerIsOutsideCamera` True when the player is NOT viewing through the camera (F8 eject / SIE). Overrides use this to skip gizmos that would occlude the near plane — mostly the source/target frustum pyramids.

Compiled out in shipping builds.
