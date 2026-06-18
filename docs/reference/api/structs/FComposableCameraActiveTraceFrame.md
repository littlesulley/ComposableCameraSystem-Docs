# FComposableCameraActiveTraceFrame { #fcomposablecameraactivetraceframe }

```cpp
#include <ComposableCameraTraceTypes.h>
```

Rewind trace frame describing the camera pose actually rendered for an active player/view target at a frame time.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `uint64` | `FrameCycle` | Frame cycle used to correlate active-camera and CCS evaluation events. |
| `double` | `RecordingTime` | Trace recording time. |
| `uint64` | `WorldId` | Recorded world object id. |
| `uint64` | `PlayerControllerId` | Recorded player controller id. |
| `uint64` | `PawnId` | Recorded pawn id. |
| `uint64` | `PlayerCameraManagerId` | Recorded player camera manager id. |
| `uint64` | `ViewTargetActorId` | Recorded view-target actor id. |
| `uint64` | `CameraComponentId` | Recorded camera component id. |
| `EComposableCameraTraceSourceKind` | `SourceKind` | Camera source kind. |
| `FComposableCameraTracePose` | `RenderedPose` | Authoritative historical rendered pose. |
