
# UComposableCameraOrthographicNode { #ucomposablecameraorthographicnode }

```cpp
#include <ComposableCameraOrthographicNode.h>
```

> **Inherits:** [`UComposableCameraCameraNodeBase`](../uobjects-other/UComposableCameraCameraNodeBase.md#ucomposablecameracameranodebase)

Switches the camera pose into orthographic projection and authors the associated ortho parameters (view width and clip planes). Mirrors Epic's UOrthographicCameraNode, but uses the CCS pose-authoritative policy: values written here override whatever CineCameraComponent defaults would otherwise apply, and transitions snap the projection-mode boolean at 50% blend weight per the BlendBy() contract in [FComposableCameraPose](../structs/FComposableCameraPose.md#fcomposablecamerapose).

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TEnumAsByte< ECameraProjectionMode::Type >` | [`ProjectionMode`](#projectionmode-1)  | Projection mode to write onto the pose. Defaults to Orthographic since the point of this node is to author an ortho setup — authors who want a perspective camera should simply not place this node. Exposed anyway so the mode can be toggled at runtime via a wire (e.g. a blueprint action flipping between ortho and perspective views). |
| `float` | [`OrthographicWidth`](#orthographicwidth-1)  | Orthographic view width in world units. |
| `float` | [`OrthoNearClipPlane`](#orthonearclipplane-1)  | Ortho near clip plane in world units. 0 is valid (= near clip at camera origin). |
| `float` | [`OrthoFarClipPlane`](#orthofarclipplane-1)  | Ortho far clip plane in world units. Must be > OrthoNearClipPlane. |

---

#### ProjectionMode { #projectionmode-1 }

```cpp
TEnumAsByte< ECameraProjectionMode::Type > ProjectionMode { ECameraProjectionMode::Orthographic }
```

Projection mode to write onto the pose. Defaults to Orthographic since the point of this node is to author an ortho setup — authors who want a perspective camera should simply not place this node. Exposed anyway so the mode can be toggled at runtime via a wire (e.g. a blueprint action flipping between ortho and perspective views).

---

#### OrthographicWidth { #orthographicwidth-1 }

```cpp
float OrthographicWidth { 512.f }
```

Orthographic view width in world units.

---

#### OrthoNearClipPlane { #orthonearclipplane-1 }

```cpp
float OrthoNearClipPlane { 0.f }
```

Ortho near clip plane in world units. 0 is valid (= near clip at camera origin).

---

#### OrthoFarClipPlane { #orthofarclipplane-1 }

```cpp
float OrthoFarClipPlane { 10000.f }
```

Ortho far clip plane in world units. Must be > OrthoNearClipPlane.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`UComposableCameraOrthographicNode`](#ucomposablecameraorthographicnode-1) `inline` |  |
| `void` | [`OnTickNode_Implementation`](#onticknode_implementation-14) `virtual` |  |
| `void` | [`GetPinDeclarations_Implementation`](#getpindeclarations_implementation-13) `virtual` `const` |  |

---

#### UComposableCameraOrthographicNode { #ucomposablecameraorthographicnode-1 }

`inline`

```cpp
inline UComposableCameraOrthographicNode()
```

---

#### OnTickNode_Implementation { #onticknode_implementation-14 }

`virtual`

```cpp
virtual void OnTickNode_Implementation(float DeltaTime, const FComposableCameraPose & CurrentCameraPose, FComposableCameraPose & OutCameraPose)
```

---

#### GetPinDeclarations_Implementation { #getpindeclarations_implementation-13 }

`virtual` `const`

```cpp
virtual void GetPinDeclarations_Implementation(TArray< FComposableCameraNodePinDeclaration > & OutPins) const
```
