# FComposableCameraTracePose { #fcomposablecameratracepose }

```cpp
#include <ComposableCameraTraceTypes.h>
```

Serializable camera pose used by CCS Rewind trace events.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FVector` | `Location` | World-space location. |
| `FRotator` | `Rotation` | World-space rotation. |
| `float` | `FieldOfView` | Perspective FOV in degrees. |
| `TEnumAsByte< ECameraProjectionMode::Type >` | `ProjectionMode` | Perspective or orthographic projection mode. |
| `float` | `OrthoWidth` | Orthographic width. |
| `float` | `OrthoNearClipPlane` | Orthographic near clip. |
| `float` | `OrthoFarClipPlane` | Orthographic far clip. |
| `bool` | `bConstrainAspectRatio` | Whether the source camera constrained aspect ratio. |

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | `Serialize` | Serializes the trace pose into an archive. |
