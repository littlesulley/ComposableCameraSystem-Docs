# FComposableCameraDebugDrawSink { #fcomposablecameradebugdrawsink }

```cpp
#include <ComposableCameraDebugDrawSink.h>
```

Abstract draw sink used by CCS debug gizmos. Live viewport drawing and Rewind trace capture share this interface so node and transition debug code emits one primitive contract instead of separate live and recorded paths.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `bool` | [`ShouldForceDrawAllNodeGizmos`](#shouldforcedrawallnodegizmos) `virtual` `const` | Returns true when the sink needs every node gizmo regardless of live viewport CVars. |
| `bool` | [`ShouldForceDrawAllTransitionGizmos`](#shouldforcedrawalltransitiongizmos) `virtual` `const` | Returns true when the sink needs every transition gizmo regardless of live viewport CVars. |
| `void` | `DrawLine` `pure virtual` | Emit a line primitive. |
| `void` | `DrawPoint` `pure virtual` | Emit a point primitive. |
| `void` | `DrawSphere` `pure virtual` | Emit a sphere primitive, optionally with a short label. |
| `void` | `DrawBox` `pure virtual` | Emit a box primitive. |
| `void` | `DrawPlane` `pure virtual` | Emit a plane primitive. |
| `void` | `DrawCameraFrustum` `pure virtual` | Emit a camera-frustum primitive. |

---

#### ShouldForceDrawAllNodeGizmos { #shouldforcedrawallnodegizmos }

```cpp
virtual bool ShouldForceDrawAllNodeGizmos() const
```

Returns true when the sink needs every node gizmo regardless of live viewport CVars. The live sink returns false; the primitive capture sink returns true for Rewind trace recording.

---

#### ShouldForceDrawAllTransitionGizmos { #shouldforcedrawalltransitiongizmos }

```cpp
virtual bool ShouldForceDrawAllTransitionGizmos() const
```

Returns true when the sink needs every transition gizmo regardless of live viewport CVars.

## FComposableCameraLiveDebugDrawSink { #fcomposablecameralivedebugdrawsink }

```cpp
#include <ComposableCameraDebugDrawSink.h>
```

Concrete draw sink that sends primitives to the live world/debug drawing path. It does not force disabled per-node or per-transition CVars.

## FComposableCameraPrimitiveCaptureSink { #fcomposablecameraprimitivecapturesink }

```cpp
#include <ComposableCameraDebugDrawSink.h>
```

Concrete draw sink that appends immutable `FComposableCameraDebugPrimitive` snapshots for Rewind trace recording. It forces all 3D node and transition gizmos so playback can show complete debug context independently of live viewport CVar state.
