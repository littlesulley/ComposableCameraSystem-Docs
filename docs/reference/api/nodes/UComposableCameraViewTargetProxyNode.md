
# UComposableCameraViewTargetProxyNode { #ucomposablecameraviewtargetproxynode }

```cpp
#include <ComposableCameraViewTargetProxyNode.h>
```

> **Inherits:** [`UComposableCameraCameraNodeBase`](../uobjects-other/UComposableCameraCameraNodeBase.md#ucomposablecameracameranodebase)

A lightweight camera node that reads `FMinimalViewInfo` from a target actor's `UCameraComponent` each tick and converts it into a `FComposableCameraPose`.

This node is NOT meant to be placed in a camera type asset by designers. It is created programmatically by the PCM's `SetViewTarget` override (implicit camera activation) to relay an external camera's state into CCS.

`SetViewTargetActor()` points to a specific actor. The node reads from that actor's `UCameraComponent` every tick. If the target actor is missing or has no `UCameraComponent`, the node outputs the unmodified input pose.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`OnTickNode_Implementation`](#onticknode_implementation) `virtual` |  |
| `void` | [`SetViewTargetActor`](#setviewtargetactor)  | Set the actor and cache its UCameraComponent. |
| `AActor *` | [`GetViewTargetActor`](#getviewtargetactor) `const` `inline` | Get the current view target actor. |

---

#### OnTickNode_Implementation { #onticknode_implementation }

`virtual`

```cpp
virtual void OnTickNode_Implementation(float DeltaTime, const FComposableCameraPose & CurrentCameraPose, FComposableCameraPose & OutCameraPose)
```

---

#### SetViewTargetActor { #setviewtargetactor }

```cpp
void SetViewTargetActor(AActor * InActor)
```

Set the actor and cache its `UCameraComponent`.

---

#### GetViewTargetActor { #getviewtargetactor }

`const` `inline`

```cpp
AActor * GetViewTargetActor() const
```

Get the current view target actor.
