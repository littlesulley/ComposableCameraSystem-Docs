# FComposableCameraDebugPrimitive { #fcomposablecameradebugprimitive }

```cpp
#include <ComposableCameraTraceTypes.h>
```

Serializable debug primitive captured from CCS node and transition gizmos for Rewind playback.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `EComposableCameraDebugPrimitiveKind` | `Kind` | Primitive type. |
| `FVector` | `A` | Primary point, center, or start. |
| `FVector` | `B` | Secondary point or end. |
| `FVector` | `C` | Tertiary point used by selected primitive kinds. |
| `FVector` | `Extent` | Box or plane extent. |
| `FRotator` | `Rotation` | Primitive rotation. |
| `FColor` | `Color` | Primitive color. |
| `float` | `Radius` | Sphere radius or related scalar. |
| `float` | `Size` | Point size or serialized segment count. |
| `float` | `Thickness` | Line thickness or frustum scale. |
| `uint8` | `Alpha` | Final alpha. |
| `uint8` | `DepthPriority` | SDPG depth-priority group. |
| `FName` | `Label` | Optional short label for sphere-like markers. |

Static factory methods create line, point, sphere, box, camera-frustum, and plane primitives. `Serialize` preserves a versioned primitive stream for trace storage.
