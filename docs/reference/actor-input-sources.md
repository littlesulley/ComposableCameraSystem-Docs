# Actor Input Sources

Several camera nodes can resolve their actor input from either an explicit actor property or from the local controller's currently controlled pawn.

This is controlled by `EComposableCameraActorInputSource`:

| Value | Meaning |
|---|---|
| `ExplicitActor` | Use the node's explicit actor field, such as `PivotActor`, `RotationInputActor`, `LookAtActor`, or `PrimaryActor`. This preserves the older workflow and is the right choice for Sequencer, cutscenes, AI cameras, shared camera assets, or any camera that should target a specific actor passed by a parameter. |
| `ControllerControlledPawn` | Ask the owning `AComposableCameraPlayerCameraManager` for its `PlayerController`, then use `PlayerController->GetPawn()`. This is convenient for player-centric gameplay cameras where the target is always the possessed pawn. |

When a source field is set to `ControllerControlledPawn`, the matching explicit actor picker is hidden in Details by the node's edit condition. At runtime, nodes first ask their owning player camera manager for its player controller. Nodes that pass a world context can also fall back to the world's first player controller when no camera manager is available. If no controller or pawn resolves, the node resolves no actor and follows its normal missing-actor fallback.

## Where It Applies

| Node | Source field | Explicit actor field |
|---|---|---|
| `ReceivePivotActorNode` | `PivotActorSource` | `PivotActor` |
| `CollisionPushNode` | `PivotActorSource` | `PivotActor` |
| `ControlRotateNode` | `RotationInputActorSource` | `RotationInputActor` |
| `FocusPullNode` | `PivotActorSource` | `PivotActor` |
| `HitchcockZoomNode` | `PivotActorSource` | `PivotActor` |
| `LookAtNode` | `LookAtActorSource` | `LookAtActor` |
| `OcclusionFadeNode` | `PivotActorSource` | `PivotActor` |
| `PivotOffsetNode` | `ActorForLocalSpaceSource` | `ActorForLocalSpace` |
| `PivotLookAheadNode` | `VelocityActorSource` | `VelocityActor` |
| `PivotRotateNode` | `PivotActorSource` | `PivotActor` |
| `RelativeFixedPoseNode` | `RelativeActorSource` | `RelativeActor` |
| `RotationConstraints` | `ActorForYawConstrainSource`, `ActorForPitchConstrainSource` | `ActorForYawConstrain`, `ActorForPitchConstrain` |
| `SetRotationNode` / `BeginPlaySetRotationNode` | `RotationActorSource` | `RotationActor` |
| `ScreenSpaceConstraintsNode` | `PivotActorSource` | `PivotActor` |
| `ScreenSpacePivotNode` | `PivotActorSource` | `PivotActor` |
| `SpiralNode` | `PivotActorSource` | `PivotActor` |
| `SplineNode` | `ClosestMoveMethodPivotActorSource` | `ClosestMoveMethodPivotActor` |
| `AutoRotateNode` | `PrimaryActorSource` | `PrimaryActor` |

## Choosing a Source

Use `ControllerControlledPawn` for the common single-player or local-player follow camera path. It reduces boilerplate because the camera asset no longer needs an exposed actor parameter just to find the possessed pawn.

Use `ExplicitActor` when the camera must work without a PlayerCameraManager, when Sequencer drives the camera through `UComposableCameraLevelSequenceComponent`, or when the target actor is not necessarily the possessed pawn. Level Sequence shot authoring should generally stay explicit because Sequencer may run in editor preview or scrub contexts where there is no gameplay controller.

Existing assets keep `ExplicitActor` by default, so previously authored pins and exposed parameters keep working. To simplify a gameplay camera, set the source field to `Controller Controlled Pawn`, remove the now-unused explicit actor pin or exposed variable, and rebuild the asset.
