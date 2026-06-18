# FComposableCameraEvaluationTraceFrame { #fcomposablecameraevaluationtraceframe }

```cpp
#include <ComposableCameraTraceTypes.h>
```

Rewind trace frame describing a CCS camera evaluation and its captured debug primitives.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `uint64` | `FrameCycle` | Frame cycle used to correlate active-camera and CCS evaluation events. |
| `double` | `RecordingTime` | Trace recording time. |
| `uint64` | `WorldId` | Recorded world object id. |
| `uint64` | `SourceObjectId` | Source object that emitted the CCS evaluation frame. |
| `uint64` | `OwnerPawnId` | Owning pawn id when available. |
| `uint64` | `PlayerControllerId` | Player controller id when available. |
| `uint64` | `ViewTargetActorId` | View-target actor id when available. |
| `EComposableCameraTraceSourceKind` | `SourceKind` | CCS evaluation source kind. |
| `EComposableCameraTraceProjectionStatus` | `ProjectionStatus` | Projection result for the evaluated CCS pose. |
| `FName` | `CameraTypeAssetName` | Camera type asset name captured for the frame. |
| `FName` | `ContextName` | CCS context name captured for the frame. |
| `FComposableCameraTracePose` | `CCSPose` | CCS internal pose for the frame. |
| `TArray< FComposableCameraDebugPrimitive >` | `Primitives` | Captured node and transition debug primitives. |
