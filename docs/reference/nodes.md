# Node Catalog

Every node shipped with the plugin, grouped by role. See [Concepts → Overview](../user-guide/concepts/overview.md) for the evaluation model and the layered picture; [User Guide → Authoring Camera Types](../user-guide/authoring-camera-types.md) for typical compositions and pin resolution authoring.

Nodes split into two execution chains:

- **Camera nodes** — subclasses of `UComposableCameraCameraNodeBase`. Run every frame on the camera chain to produce the pose.
- **Compute nodes** — subclasses of `UComposableCameraComputeNodeBase`. Run once on the BeginPlay chain at activation and publish results that camera nodes consume each frame.

Each node's authored per-property API reference (full field lists, types, ranges) lives in the auto-generated [Reference → API → Classes](api/index.md) section. This page covers what each node is *for* and when to reach for it.

---

## Pose helpers

### `FixedPoseNode`

Pass-through. Keeps the current pose unchanged. Useful as a placeholder while wiring other nodes, or as a terminator in a branch that shouldn't modify the pose.

### `RelativeFixedPoseNode`

Maintains the camera pose at a fixed offset relative to a reference transform or actor. Good for locked shots that need to track a moving actor without any additional logic (e.g. a side-scroller camera rigidly welded to the player).

---

## Pivot and subject

These nodes are the first stage of most cameras — they establish "what is this camera looking at / following" before any offset or rotation logic runs.

### `ReceivePivotActorNode`

Reads an actor's world position and writes it to an output `PivotPosition` pin. The actor typically comes in as a context parameter — see the Gameplay context pattern in [Authoring Camera Types → Typical compositions](../user-guide/authoring-camera-types.md#typical-compositions).

### `PivotOffsetNode`

Offsets the pivot position. Supports world-space, actor-space, or camera-space offsets — use actor-space for "one meter above the character's root" shoulder-height setups, world-space for gravity-aligned offsets, camera-space for screen-relative nudges.

### `PivotDampingNode`

Dampens pivot position changes using an Instanced interpolator (IIR, simple spring, or spring-damper). Smooths out jittery or teleport-style pivot updates — for example, when the pivot is bound to a character whose root bone snaps during a montage.

The interpolator is a subobject UPROPERTY, so its individual parameters (`Speed`, `DampTime`, etc.) are [auto-exposed as subobject pins](../user-guide/authoring-camera-types.md#exposing-parameters) and can be wired or overridden from the type asset.

---

## Camera offset and rotation

Once the pivot is set, these nodes position and orient the camera relative to that pivot.

### `CameraOffsetNode`

Applies an offset in camera-local space — "behind and to the right of the pivot, at some distance". The camera-local frame follows the camera's rotation, so the offset stays coherent as the player orbits.

### `ControlRotateNode`

The input handler for third-person and free-look cameras. Reads an Enhanced Input `InputAction` from a nominated `RotationInputActor` (typically the player pawn, passed in via a context parameter) and applies yaw/pitch.

| Field | Purpose |
|---|---|
| `RotationInputActor` | Actor owning the `EnhancedInputComponent`. |
| `RotateAction` | The `UInputAction` whose `Axis2D` value drives rotation. |
| `HorizontalSpeed` / `VerticalSpeed` | Degrees per second per unit of input. |
| `HorizontalDamping` / `VerticalDamping` | `FVector2f` of `(acceleration, deceleration)` time-to-reach. Damps instantaneous snap of stick input. |
| `bInvertPitch` | Inverts pitch axis. |

Requires Enhanced Input — add `EnhancedInput` to the project's module dependencies if it isn't already there.

### `AutoRotateNode`

Auto-rotates within a range around a main direction. Used for gentle idle sweeps, breathing-style motion in cinematic framings, or subtle attention-directing motion toward a threat.

### `RotationConstraints`

Constrains yaw and/or pitch within defined ranges. Typically placed after `ControlRotateNode` to stop the player from looking straight up or spinning 360°. Ranges are authored in degrees.

---

## Look-at

### `LookAtNode`

Rotates the camera to face a target. Supports:

- **Target by position** (`ByPosition`) or **by actor** (`ByActor`, with an optional `LookAtSocket` for skeletal-mesh attachment).
- **Hard constraint** (`Hard`) — the player cannot control camera rotation; look-at is absolute.
- **Soft constraint** (`Soft`) — the player keeps control within a radius, and the node pulls the camera back toward the target when the player stops inputting. Parameters: `SoftLookAtRange` (degrees), `SoftLookAtWeight` (0–1; higher = snappier return), and an Instanced `SoftLookAtInterpolator` (typically `SpringDamperInterpolator`) for the smoothing curve.

Place after `ControlRotateNode` in a third-person chain to implement "soft lock-on" for melee targeting.

### `ScreenSpacePivotNode`

Keeps the pivot within a configurable screen-space rectangle. Instead of re-orienting the camera to face the subject, it *translates* the camera so that the subject's projected position stays inside the authored bounds. Useful for cinematic over-the-shoulder framings where the subject should always be in the right third of frame.

### `ScreenSpaceConstraintsNode`

Generalized screen-space constraint solver — combines multiple constraints (pivot position, look-at angle, subject margin) into one solver pass. Choose this over `ScreenSpacePivotNode` when you need more than one screen-space condition simultaneously.

---

## Lens, FOV, and projection

These nodes author the pose's lens and projection fields. They typically appear near the end of the node chain, after the camera's position and orientation are settled.

### `FieldOfViewNode`

Sets FOV in degrees. Writes to `FComposableCameraPose::FieldOfView` and clears `FocalLength`, so the pose resolves FOV directly rather than from focal-length/sensor math.

Optional "dynamic FOV" driven by an actor's scale (e.g. zoom out when the character grows during a power-up).

### `LensNode`

Authors physical-lens parameters on the pose: `FocalLength`, `Aperture`, `FocusDistance`, `DiaphragmBladeCount`, `PhysicalCameraBlendWeight`. When `bOverrideFieldOfViewFromFocalLength` is true, also clears `FieldOfView` so the pose resolves FOV from `FocalLength + SensorWidth`.

`PhysicalCameraBlendWeight` gates depth-of-field and auto-exposure post-process contribution — dial to 0 for "game FOV" feel, 1 for "cinematic lens" feel.

### `FilmbackNode`

Authors sensor and aspect-ratio parameters: `SensorWidth`, `SensorHeight`, `SqueezeFactor`, `Overscan`, `ConstrainAspectRatio`, `OverrideAspectRatioAxisConstraint`, `AspectRatioAxisConstraint`. Sensor dimensions feed into the pose's focal-length-mode FOV resolution, so place this alongside `LensNode` when using physical lens authoring.

### `PostProcessNode`

Applies post-process settings to the camera pose. Works like a `PostProcessVolume` but scoped to a single camera type — only properties whose `bOverride_*` flag is true take effect; all others pass through from the camera component's baseline or from earlier nodes.

Multiple `PostProcessNode`s in the same camera stack compose in execution order: later nodes override earlier ones for the same `bOverride_*` property. No pins are declared — `FPostProcessSettings` is configured entirely through the Details panel, matching the `PostProcessVolume` workflow UE artists are already familiar with.

### `OrthographicNode`

Switches the pose into orthographic projection and authors `OrthographicWidth`, `OrthoNearClipPlane`, `OrthoFarClipPlane`. For top-down, side-scrolling, or isometric cameras.

!!! note "Projection-mode snapping at 50% blend"
    Transitions between an orthographic camera and a perspective camera snap `ProjectionMode` at 50% blend weight per the pose `BlendBy()` contract — you cannot cross-blend projection modes smoothly. Design your blends to hit an intermediate perspective pose before crossing, or accept the snap.

---

## Collision and impulses

### `CollisionPushNode`

Dual-mode collision resolver, and one of the largest single nodes in the plugin.

**Trace collision** — casts a line or sphere trace from pivot to camera each frame. On occlusion, pushes the camera toward the pivot, optionally with an exemption time window (brief occlusions don't react).

**Self collision** — carries a sphere around the camera. When the sphere overlaps an obstacle, pushes the camera to the *far side* of the obstacle via a reverse sphere sweep from beyond the camera back toward the pivot. Good for thin walls that line traces miss.

Both modes share the same interpolator pair (push/pull) and ignored-actor list. The two interpolators are Instanced subobjects — their parameters are [subobject-pin-exposed](../user-guide/authoring-camera-types.md#exposing-parameters) (e.g. `PushInterpolator.Speed`, `PullInterpolator.DampTime`) so they can be tuned from the type asset's Details panel or wired from gameplay.

### `ImpulseResolutionNode`

Resolves impulse forces applied via volumes — the "camera got pushed by an explosion" channel. Listens for impulse events registered on trigger volumes in the level and integrates them into the pose with configurable damping.

---

## Movement and authored motion

### `SplineNode`

Places the camera on a spline, with multiple spline math backends: BuiltInSpline (wraps `USplineComponent`), BezierSpline, CubicHermiteSpline, BasicSpline (B-spline), NURBSpline. Useful for rail-style fixed-path cameras — boss intro flyovers, zone-entry establishing shots — where the path is authored, not derived.

!!! note "Level Sequence integration"
    Sequencer-driven cinematics are now handled by the [Play Cutscene Sequence](../tutorials/level-sequence-camera.md) Blueprint node, which manages context pushing, CameraCut-driven camera switching, and cleanup automatically. See the [Level Sequence Integration](../tutorials/level-sequence-camera.md) tutorial.

---

## Composition

### `MixingCameraNode`

Mixes the output of multiple child cameras into one pose. The child cameras are themselves full composable cameras (auxiliary, spawned via the PCM's C++-only `CreateNewCamera` / `ActivateNewCamera` entry points). Use for custom multi-subject cameras (framing two players, boss-and-hero cameras) where each subject needs its own evaluation tree.

Mixing weights and the blend function are authored as node parameters.

### `BlueprintCameraNode`

A camera node whose `OnTickNode` is implemented in Blueprint. Lets gameplay programmers prototype or ship one-off node behavior without touching C++. For production code intended to ship on the per-frame hot path, migrate to a C++ subclass — Blueprint VM overhead is non-trivial when called every frame per camera.

---

## Compute nodes

Compute nodes run once at camera activation on the BeginPlay chain. They publish output values that camera nodes downstream read once and cache — not reread each frame.

### `ComputeRandomOffsetNode`

Generates a random offset vector within min/max bounds. Use for spawn-time jitter (to avoid two cameras of the same type starting at identical positions), shake seeds, or randomized starting positions that remain stable across the camera's lifetime.

**Inputs:** `MinOffset`, `MaxOffset` (Vector3D).
**Output:** `RandomOffset` (Vector3D).

### `ComputeDistanceToActorNode`

Measures the distance and direction between two actors at activation time. Use to scale boom-arm length, set initial FOV, or derive blend weights from actor proximity at the moment the camera spawns.

**Inputs:** `ActorA`, `ActorB` (Actor).
**Outputs:** `Distance` (Float), `Direction` (Vector3D).

---

## Node base class

### `UComposableCameraCameraNodeBase`

Abstract. The base every camera node derives from. Exposes:

- `Initialize()` (non-virtual wrapper) → `OnInitialize_Implementation()`. Called once after pin resolution and subobject pin application, before the first tick.
- `TickNode()` (non-virtual wrapper) → `OnTickNode_Implementation(DeltaTime, CurrentPose, OutPose)`. Called every frame on the camera chain.
- `GetPinDeclarations_Implementation(OutPins)`. Declares the node's pin schema.

See [Extending → Custom Nodes](../extending/custom-nodes.md) for the authoring recipe.

### `UComposableCameraComputeNodeBase`

Abstract. The base every compute node derives from. Overrides one method:

- `OnComputeNodeInitialize_Implementation()`. Called once on the BeginPlay chain. Read inputs, compute, write outputs.

---

## `PostProcessNode`

!!! note "Auto-drafted from header — please review"
    This entry was generated by the auto-updater from the class's doc comment. Expand with usage notes, pin descriptions, and an example when you have a moment.

Works like a `PostProcessVolume` but scoped to a single camera type. Properties are applied once per tick via `FPostProcessUtils::OverridePostProcessSettings` onto `OutCameraPose.PostProcessSettings`. Configured entirely through the Details panel (no graph pins) — toggle `bOverride_*` flags to control which properties this node contributes. Multiple `PostProcessNode` instances in the same camera stack compose in execution order; later nodes win for the same property.

**Header:** `ComposableCameraPostProcessNode.h`
**C++ reference:** [`UComposableCameraPostProcessNode`](api/nodes/UComposableCameraPostProcessNode.md)

---

## `ViewTargetProxyNode`

!!! note "Auto-drafted from header — please review"
    This entry was generated by the auto-updater from the class's doc comment. Expand with usage notes, pin descriptions, and an example when you have a moment.

Internal-only node — not intended for placement in camera type assets by designers. Created programmatically by the PCM's `SetViewTarget` override (implicit camera activation) to relay an external `UCameraComponent`'s `FMinimalViewInfo` into CCS as an `FComposableCameraPose` each tick. If the target actor is missing or has no `UCameraComponent`, the node passes through the unmodified input pose.

**Header:** `ComposableCameraViewTargetProxyNode.h`
**C++ reference:** [`UComposableCameraViewTargetProxyNode`](api/nodes/UComposableCameraViewTargetProxyNode.md)

---

*See also:* the auto-generated [API Reference](api/index.md) for per-class property tables; [Extending → Custom Nodes](../extending/custom-nodes.md) for writing your own; [User Guide → Graph Editor](../user-guide/graph-editor.md) for the authoring surface.
