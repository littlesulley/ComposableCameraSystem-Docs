
# UComposableCameraViewTargetProxyNode { #ucomposablecameraviewtargetproxynode }

```cpp
#include <ComposableCameraViewTargetProxyNode.h>
```

> **Inherits:** [`UComposableCameraCameraNodeBase`](../uobjects-other/UComposableCameraCameraNodeBase.md#ucomposablecameracameranodebase)

A lightweight camera node that reads FMinimalViewInfo from a target actor's UCameraComponent each tick and converts it into a [FComposableCameraPose](../structs/FComposableCameraPose.md#fcomposablecamerapose).

This node is NOT meant to be placed in a camera type asset by designers. It is created programmatically by the PCM's SetViewTarget override (implicit camera activation) to relay an external camera's state into CCS.

[SetViewTargetActor()](#setviewtargetactor) points to a specific actor. The node reads from that actor's UCameraComponent every tick. If the target actor is missing or has no UCameraComponent, the node outputs the unmodified input pose.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`OnTickNode_Implementation`](#onticknode_implementation-20) `virtual` |  |
| `void` | [`SetViewTargetActor`](#setviewtargetactor)  | Set the actor and cache its UCameraComponent. |
| `AActor *` | [`GetViewTargetActor`](#getviewtargetactor) `const` `inline` | Get the current view target actor. |

---

#### OnTickNode_Implementation { #onticknode_implementation-20 }

`virtual`

```cpp
virtual void OnTickNode_Implementation(float DeltaTime, const FComposableCameraPose & CurrentCameraPose, FComposableCameraPose & OutCameraPose)
```

---

#### SetViewTargetActor { #setviewtargetactor }

```cpp
void SetViewTargetActor(AActor * InActor)
```

Set the actor and cache its UCameraComponent.

---

#### GetViewTargetActor { #getviewtargetactor }

`const` `inline`

```cpp
inline AActor * GetViewTargetActor() const
```

Get the current view target actor.

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TWeakObjectPtr< AActor >` | [`ViewTargetActor`](#viewtargetactor)  | The actor whose UCameraComponent provides the camera view each tick. |
| `TWeakObjectPtr< UCameraComponent >` | [`CachedCameraComponent`](#cachedcameracomponent)  | Cached camera component — resolved once in SetViewTargetActor. |

---

#### ViewTargetActor { #viewtargetactor }

```cpp
TWeakObjectPtr< AActor > ViewTargetActor
```

The actor whose UCameraComponent provides the camera view each tick.

---

#### CachedCameraComponent { #cachedcameracomponent }

```cpp
TWeakObjectPtr< UCameraComponent > CachedCameraComponent
```

Cached camera component — resolved once in SetViewTargetActor.
