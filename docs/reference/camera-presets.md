# Camera Presets

The plugin ships a small set of starter assets under:

```text
ComposableCameraSystem/Content/CameraPresets/
```

Enable **Show Plugin Content** in the Content Browser if the folder is hidden. Treat these presets as editable starting points: duplicate them into your project content before heavy changes, then tune the copied asset for your own character scale, input setup, and cinematic language.

## Camera Type presets

These assets live in `CameraPresets/Preset_Cameras` and are regular `UComposableCameraTypeAsset` camera graphs.

| Preset | Use it for | Notes |
| --- | --- | --- |
| `Camera_BasicThirdPerson` | A baseline third-person gameplay follow camera. | Good first asset to inspect when learning the graph shape for pivot, offset, rotation, and collision-style gameplay cameras. |
| `Camera_BasicLockOn` | A player-follow camera with a stabilized lock-on aim target. | Demonstrates the two-`ScreenSpacePivotNode` lock-on chain with `LockOnAimPointNode` feeding the target framing pass. Exposes `AimActor` for the lock target while the follow point can resolve from the controlled pawn. |
| `Camera_BasicSoftLookAt` | A third-person follow camera with soft target pull. | Shows `LookAtNode` in soft mode, useful when the camera should bias toward a subject without fully taking rotation control away from the player. |
| `Camera_BasicTalk` | Dialogue or two-character conversation coverage. | Demonstrates activation-time midpoint and two-actor direction setup with the BeginPlay compute chain, useful for talk cameras that should initialize from both speakers before the frame-by-frame camera chain runs. |
| `Camera_CloseOTS` | Close over-the-shoulder gameplay or cinematic framing. | Useful for tighter shoulder framing, dialogue coverage, or aim-adjacent camera setups that still need a composable graph. |
| `Camera_BasicFixed` | A simple fixed or relative pose camera. | Useful as a minimal reference for authored transforms, fixed viewpoints, and testing transition behavior without follow-camera logic. |
| `Camera_BasicIsometric` | Isometric or top-down-style camera framing. | Demonstrates orthographic/isometric-style composition for strategy, tactics, or inspection cameras. |
| `Camera_BasicSpline` | Camera movement along a spline path. | Demonstrates `SplineNode` path following for authored rails and fixed-path cinematic moves. |
| `Camera_BasicSpiral` | A procedural orbit/spiral camera move. | Demonstrates `SpiralNode` with the bundled radius, height, and angle curve assets under `Preset_Cameras/Curves`. |
| `Camera_BasicVehicleExhibition` | Vehicle, mount, or object showcase framing. | Useful for inspecting pivot rotation and vehicle-style follow behavior where the camera should respect an actor's orientation. |
| `Camera_DirectionalMove` | A simple straight camera move. | Demonstrates `DirectionalMoveNode`: move from an initial transform along a local-space direction, optionally clamped by duration. |
| `Camera_TwoPointMove` | A one-shot move between two authored transforms. | Demonstrates `TwoPointMoveNode`: interpolate from source to target over a duration, with an optional curve. |

Use Camera Type presets with normal activation paths: Blueprint `Activate Camera`, DataTable-driven activation, Sequencer `AComposableCameraLevelSequenceActor`, or direct C++ activation.

## Shot presets

These assets live in `CameraPresets/Preset_Shots` and are `UComposableCameraShotAsset` templates for Shot-Based Keyframing.

| Preset group | Assets | Use it for |
| --- | --- | --- |
| OTS Wide | `CameraShot_OTS_Wide_L`, `CameraShot_OTS_Wide_R` | Wider over-the-shoulder coverage with left/right shoulder variants. |
| OTS Medium Wide | `CameraShot_OTS_MediumWide_L`, `CameraShot_OTS_MediumWide_R` | Medium-wide dialogue or two-character coverage. |
| OTS Medium | `CameraShot_OTS_Medium_L`, `CameraShot_OTS_Medium_R` | Standard over-the-shoulder framing for dialogue beats. |
| OTS Medium Close | `CameraShot_OTS_MediumClose_L`, `CameraShot_OTS_MediumClose_R` | Tighter character coverage while keeping the shoulder-side composition. |
| OTS Close | `CameraShot_OTS_Close_L`, `CameraShot_OTS_Close_R` | Close over-the-shoulder shots for emphasis. |
| OTS Extreme Close | `CameraShot_OTS_ExtClose_L`, `CameraShot_OTS_ExtClose_R` | Very tight reaction or detail shots. |

Drag a Shot preset onto a `AComposableCameraLevelSequenceShotActor` binding or assign it to a Composable Camera Shot Section in `AssetReference` mode. The section snapshots the Shot into local overrides, so Sequencer edits affect that section without mutating the shared preset asset.

## Transition presets

These assets live in `CameraPresets/Preset_Transitions` and are reusable
`UComposableCameraTransitionDataAsset` wrappers.

| Preset | Use it for | Notes |
| --- | --- | --- |
| `CameraTransaition_Preservation_TwoSeconds` | A two-second subject-preserving transition preset. | Demonstrates `CompositionPreservingTransition` as a reusable data asset. Use it when entering or routing between cameras where the selected subject should stay framed while the nested driving transition controls timing and rotation. |

Assign a Transition preset anywhere a transition data asset is accepted:
activation overrides, transition-table entries, camera type enter/exit
transitions, or Sequencer shot overlap transitions.

## Choosing a preset

Start with a Camera Type preset when you need a runnable camera graph. Start
with a Shot preset when Sequencer should solve framing from targets using the
Shot Editor and Composition Solver. Start with a Transition preset when you want
to reuse one tuned blend across multiple camera pairs or activation calls.

For gameplay cameras, duplicate a Camera Type preset and wire project-specific actor inputs, Enhanced Input actions, and collision settings. For cinematic framing, duplicate or reference a Shot preset, bind its targets in Sequencer, then tune Placement, Aim, Lens, Focus, and transition overlap in the Shot workflow.

## Related pages

- [Authoring Camera Types](../user-guide/authoring-camera-types.md) - how to build and tune TypeAsset camera graphs.
- [CCS Camera in Sequencer](../tutorials/level-sequence-authoring.md) - using Camera Type assets as Sequencer Spawnables.
- [Shot-Based Keyframing in Sequencer](../tutorials/shot-based-keyframing.md) - using Shot presets and Shot Sections.
- [Node Catalog](nodes.md) - behavior of the nodes used inside the Camera Type presets.
- [Transition Catalog](transitions.md) - behavior of the transitions used inside Transition presets.
