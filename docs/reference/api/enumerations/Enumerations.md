

# Enumerations

#### EComposableCameraBuildStatus { #ecomposablecamerabuildstatus }

```cpp
enum EComposableCameraBuildStatus
```

| Value | Description |
|-------|-------------|
| `NotBuilt` |  |
| `Success` |  |
| `SuccessWithWarnings` |  |
| `Failed` |  |

Build status for camera type asset validation.

#### EComposableCameraActionExpirationType { #ecomposablecameraactionexpirationtype }

```cpp
enum EComposableCameraActionExpirationType
```

| Value | Description |
|-------|-------------|
| `None` |  |
| `Instant` |  |
| `Duration` |  |
| `Manual` |  |
| `Condition` |  |

#### EComposableCameraActionExecutionType { #ecomposablecameraactionexecutiontype }

```cpp
enum EComposableCameraActionExecutionType
```

| Value | Description |
|-------|-------------|
| `PreCameraTick` |  |
| `PreNodeTick` |  |
| `PostNodeTick` |  |
| `PostCameraTick` |  |

#### EComposableCameraResumeCameraTransformSchema { #ecomposablecameraresumecameratransformschema }

```cpp
enum EComposableCameraResumeCameraTransformSchema
```

| Value | Description |
|-------|-------------|
| `PreserveCurrent` |  |
| `PreserveResumed` |  |
| `Specified` |  |

#### EComposableCameraLookAtType { #ecomposablecameralookattype }

```cpp
enum EComposableCameraLookAtType
```

| Value | Description |
|-------|-------------|
| `ByPosition` |  |
| `ByActor` |  |

#### EComposableCameraLookAtConstraintType { #ecomposablecameralookatconstrainttype }

```cpp
enum EComposableCameraLookAtConstraintType
```

| Value | Description |
|-------|-------------|
| `Hard` |  |
| `Soft` |  |

#### EComposableCameraSpiralPivotSourceType { #ecomposablecameraspiralpivotsourcetype }

```cpp
enum EComposableCameraSpiralPivotSourceType
```

| Value | Description |
|-------|-------------|
| `FromActor` |  |
| `FromVector` |  |

Source of the pivot the spiral is built around.

FromActor — PivotActor->GetActorLocation() is sampled each frame. The actor's Up / Forward are also available as Spiral-Space axis sources. FromVector — PivotPosition is used directly. When this mode is active, RotationAxis = PivotActorUp and ReferenceDirection = PivotActorForward silently fall back to WorldUp / WorldX with a runtime warning — there is no actor to read from.

#### EComposableCameraSpiralRotationAxis { #ecomposablecameraspiralrotationaxis }

```cpp
enum EComposableCameraSpiralRotationAxis
```

| Value | Description |
|-------|-------------|
| `WorldUp` |  |
| `PivotActorUp` |  |
| `Custom` |  |

Axis around which the camera orbits. Defines Spiral Space's Up direction.

#### EComposableCameraSpiralReferenceDirection { #ecomposablecameraspiralreferencedirection }

```cpp
enum EComposableCameraSpiralReferenceDirection
```

| Value | Description |
|-------|-------------|
| `WorldX` |  |
| `PivotActorForward` |  |
| `CameraInitialForward` |  |
| `Custom` |  |

Direction that anchors θ = 0 in the plane perpendicular to the rotation axis. Defines Spiral Space's Forward direction after projection. The chosen direction is projected onto the plane perpendicular to the rotation axis and renormalized — it does not need to be pre-orthogonal to the axis.

CameraInitialForward captures the camera's forward vector on the first tick after activation and reuses it for the lifetime of the node, so the spiral starts seamlessly from the current camera orientation.

#### EComposableCameraSpiralPlayMode { #ecomposablecameraspiralplaymode }

```cpp
enum EComposableCameraSpiralPlayMode
```

| Value | Description |
|-------|-------------|
| `Once` |  |
| `Loop` |  |
| `PingPong` |  |

How the spiral evolves past Duration seconds. In every mode, θ / Radius / Height are direct curve evaluations at NormalizedTime — there is no per-frame integration and no accumulated state, so the pose at any arbitrary t is computable in O(1).

Once — NormalizedTime clamps at 1 after Duration; all three curves hold their Y at X=1. The pose freezes at the terminal frame. Loop — NormalizedTime = Fmod(Elapsed, Duration) / Duration. θ visually wraps cleanly when AngleCurve's Y(1) - Y(0) is a multiple of 360 (trig periodicity absorbs the jump); non-multiples snap at the cycle seam, which is the author's explicit choice. PingPong — NormalizedTime oscillates 0 → 1 → 0 → 1 every 2 * Duration seconds. All three curves are sampled at the mirrored time, so θ / Radius / Height naturally retrace on the return half. No sign flip needed — the X mirror alone carries the symmetry.

#### EComposableCameraSplineNodeSplineType { #ecomposablecamerasplinenodesplinetype }

```cpp
enum EComposableCameraSplineNodeSplineType
```

| Value | Description |
|-------|-------------|
| `BuiltInSpline` |  |
| `Bezier` |  |
| `CubicHermite` |  |
| `BasicSpline` |  |
| `NURBS` |  |

#### EComposableCameraSplineNodeMoveMethod { #ecomposablecamerasplinenodemovemethod }

```cpp
enum EComposableCameraSplineNodeMoveMethod
```

| Value | Description |
|-------|-------------|
| `Automatic` |  |
| `ClosestPoint` |  |

#### EComposableCameraPatchExpirationType { #ecomposablecamerapatchexpirationtype }

```cpp
enum EComposableCameraPatchExpirationType
```

| Value | Description |
|-------|-------------|
| `None` |  |
| `Duration` | Expires after Duration seconds, counted from the moment the envelope reaches Active (alpha == 1). |
| `Manual` | Expires only when ExpirePatch(handle) is called. |
| `Condition` | Expires when the Patch asset's CanRemain() override returns false. |

Bitmask of expiration channels that may individually fire to retire a Patch.

Mirrors the spirit of EComposableCameraActionExpirationType but is tailored to Patch's "always has an enter/exit envelope" model — there is no Instant variant because every Patch ramps in and out via its envelope.

A Patch's effective expiration is the OR of its enabled channels: the first channel to fire flips Phase to Exiting. Bits are independent and stack additively — e.g. (Duration | Manual) means "expires after Duration seconds
OR when ExpirePatch is called, whichever comes first".

#### EComposableCameraPatchEase { #ecomposablecamerapatchease }

```cpp
enum EComposableCameraPatchEase
```

| Value | Description |
|-------|-------------|
| `Linear` |  |
| `EaseIn` |  |
| `EaseOut` |  |
| `EaseInOut` |  |
| `Smooth` |  |

Easing curve applied symmetrically to the enter and exit alpha ramps.

Asset-only in V1 — there is no per-AddPatch override (an enum has no natural sentinel value, and adding a parallel bool is worse than asset-only). If a future case requires a runtime override, add a sixth `Custom` member with a companion `FRuntimeFloatCurve` pin (see PatchSystemProposal §8.1).

#### EComposableCameraPatchPhase { #ecomposablecamerapatchphase }

```cpp
enum EComposableCameraPatchPhase
```

| Value | Description |
|-------|-------------|
| `Entering` |  |
| `Active` |  |
| `Exiting` |  |
| `Expired` |  |

Lifecycle phase of a Patch instance.

Entering : alpha ramping 0 → 1 over EnterDuration. Patch evaluator already ticks at full fidelity. Active : alpha == 1, expiration channels are evaluated each frame. Exiting : alpha ramping 1 → 0 over ExitDuration. Expired : terminal; instance is removed at the end of PatchManager::Apply.

#### EComposableCameraImpulseBoxDistanceType { #ecomposablecameraimpulseboxdistancetype }

```cpp
enum EComposableCameraImpulseBoxDistanceType
```

| Value | Description |
|-------|-------------|
| `BoxOrigin` |  |
| `XAxis` |  |
| `YAxis` |  |
| `ZAxis` |  |
| `XYPlane` |  |
| `XZPlane` |  |
| `YZPlane` |  |

#### EComposableCameraPinDirection { #ecomposablecamerapindirection }

```cpp
enum EComposableCameraPinDirection
```

| Value | Description |
|-------|-------------|
| `Input` |  |
| `Output` |  |

Direction of a camera node data pin.

#### EComposableCameraPinType { #ecomposablecamerapintype }

```cpp
enum EComposableCameraPinType
```

| Value | Description |
|-------|-------------|
| `Bool` |  |
| `Int32` |  |
| `Float` |  |
| `Double` |  |
| `Vector2D` |  |
| `Vector3D` |  |
| `Vector4` |  |
| `Rotator` |  |
| `Transform` |  |
| `Actor` |  |
| `Object` |  |
| `Struct` | Custom USTRUCT type. When this is selected, StructType must be set. |
| `Name` | FName value. Stored as FName in the data block (POD: NAME_INDEX + NAME_NUMBER). |
| `Enum` | UENUM value. Stored as a normalized int64 in the data block; the owning UEnum* is carried on the declaration and used to narrow-cast into the actual property's underlying width (uint8 / int32 / int64) at write time. When this is selected, EnumType must be set. |
| `Delegate` | Single-cast dynamic delegate (FScriptDelegate). NOT stored in the data block — delegates carry heap-owned state and cannot be memcpy'd. Instead they are stored in a parallel map on [FComposableCameraParameterBlock](../structs/FComposableCameraParameterBlock.md#fcomposablecameraparameterblock) and applied at activation time via reflection (FDelegateProperty). Per-frame auto-resolve skips this type. When this is selected, SignatureFunction must be set to the UFunction defining the delegate's parameter/return signature. |

Supported data types for camera node pins.

#### EComposableCameraExecEntryType { #ecomposablecameraexecentrytype }

```cpp
enum EComposableCameraExecEntryType
```

| Value | Description |
|-------|-------------|
| `CameraNode` | Execute a camera node by its index in NodeTemplates. |
| `SetVariable` | Execute an internal-variable Set operation: copy the source camera node's output pin into the internal variable identified by VariableGuid. |

Tag for entries in the serialized execution chain.

The execution chain is a linear sequence of operations the camera runs each frame: camera nodes do the actual pose computation, and internal-variable Set operations write scratch values between camera nodes. See [FComposableCameraExecEntry](../structs/FComposableCameraExecEntry.md#fcomposablecameraexecentry).

#### EComposableCameraTreeNodeKind { #ecomposablecameratreenodekind }

```cpp
enum EComposableCameraTreeNodeKind
```

| Value | Description |
|-------|-------------|
| `Leaf` |  |
| `ReferenceLeaf` |  |
| `InnerTransition` |  |

Runtime debug snapshot structures consumed by [FComposableCameraDebugPanel](../structs/FComposableCameraDebugPanel.md#fcomposablecameradebugpanel).

These are distinct from the editor-side FComposableCameraDebugSnapshot ([Core/ComposableCameraDebugSnapshot.h](#composablecameradebugsnapshoth), WITH_EDITOR only). The editor one captures a SINGLE camera's per-node state for the Type Asset Editor's graph overlay. These structs capture the entire Tier-1 context stack + each context's Tier-2 evaluation tree, for the in-viewport debug panel (runtime, always available).

Design:

* Tree nodes are flattened DFS pre-order with a Depth field, so the renderer does not need recursion and can pick connector glyphs (vertical stem + elbow) from a single pass.

* All pointer data is resolved eagerly into display strings at snapshot time — consumers never deref anything runtime-owned. This makes the snapshot safe to cache and freeze.

* Progress / lifetime fields are captured as floats, not pre-formatted strings, so the renderer can draw real progress bars instead of parsing text. Kind of an evaluation-tree node. Parallels the TVariant in [FComposableCameraEvaluationTreeNode](../structs/FComposableCameraEvaluationTreeNode.md#fcomposablecameraevaluationtreenode).

#### EComposableCameraPatchSource { #ecomposablecamerapatchsource }

```cpp
enum EComposableCameraPatchSource
```

| Value | Description |
|-------|-------------|
| `BlueprintLibrary` | Added via BP `AddCameraPatch` library / runtime PCM path. Lives on the Director's PatchManager; uses stateful envelope. |
| `Sequencer` | Driven by a Sequencer `[UMovieSceneComposableCameraPatchTrack](../uobjects-other/UMovieSceneComposableCameraPatchTrack.md#umoviescenecomposablecamerapatchtrack)` section bound to an `[AComposableCameraLevelSequenceActor](../actors/AComposableCameraLevelSequenceActor.md#acomposablecameralevelsequenceactor)` via `TargetActorBinding`. Lives on the LS Component's overlay map; uses stateless envelope. |

Where a patch entry was sourced from — drives the row's prefix label so the designer can tell which path is producing each visible patch.

#### EComposableCameraAutoRotateDirectionMode { #ecomposablecameraautorotatedirectionmode }

```cpp
enum EComposableCameraAutoRotateDirectionMode
```

| Value | Description |
|-------|-------------|
| `Direction` |  |
| `ActorForward` |  |

#### EComposableCameraNodeLevelSequenceCompatibility { #ecomposablecameranodelevelsequencecompatibility }

```cpp
enum EComposableCameraNodeLevelSequenceCompatibility
```

| Value | Description |
|-------|-------------|
| `Compatible` | Node evaluates correctly without a PCM. Safe in Level Sequence. |
| `RequiresPCM` | Node requires a live PCM (viewport, player controller, HUD, spawn new cameras mid-init, etc.). In LS the node is a no-op and the Details panel warns. |
| `ComputeOnly` | Node lives on the BeginPlay compute chain and is never per-frame-evaluated in LS (LS skips the compute chain). Warning is informational. |

How a node class behaves when evaluated in a Level-Sequence context, where the camera is driven by a [UComposableCameraLevelSequenceComponent](../uobjects-other/UComposableCameraLevelSequenceComponent.md#ucomposablecameralevelsequencecomponent) and no UComposableCameraPlayerCameraManager is present.

Queried by the LS Details-panel customization (to warn the designer) and by the LS component's tick path (to decide whether to evaluate the node at all).

Default is Compatible; override in node classes that cannot run without a PCM, or on compute-chain nodes that are never evaluated in LS by design.

#### EComposableCameraNodePatchCompatibility { #ecomposablecameranodepatchcompatibility }

```cpp
enum EComposableCameraNodePatchCompatibility
```

| Value | Description |
|-------|-------------|
| `Compatible` | Reads upstream pose, mutates it. Safe in a Patch graph. |
| `Incompatible` | Initializes pose from scratch or delegates to external sources — ignores InPose. Meaningless in a Patch context; editor emits an error build message. |
| `CompatibleWithCaveat` | Works but with surprising semantics (e.g. overrides a single pose field in a way that may discard useful upstream data). Editor emits a warning build message so the author can confirm intent. |

Declares how a node behaves when placed in a Camera Patch graph (per PatchSystemProposal §11). A Patch evaluator receives an upstream pose each frame and expects its nodes to read-modify-write that pose — nodes that synthesize pose from scratch or delegate to external sources produce surprising results in a Patch context.

Queried by the Patch asset's editor-time validation (to warn the designer via Build messages) and by future runtime tooling (no current runtime gate, so Incompatible nodes do run — they just produce wrong output). The classification is authoring-side guidance, not a runtime safety net.

Default is Compatible; override in nodes that have surprising semantics.

#### ECameraPivotOffset { #ecamerapivotoffset }

```cpp
enum ECameraPivotOffset
```

| Value | Description |
|-------|-------------|
| `WorldSpace` |  |
| `ActorLocalSpace` |  |
| `CameraSpace` |  |

#### EComposableCameraMixingCameraWeightNormalizationMethod { #ecomposablecameramixingcameraweightnormalizationmethod }

```cpp
enum EComposableCameraMixingCameraWeightNormalizationMethod
```

| Value | Description |
|-------|-------------|
| `L1` |  |
| `L2` |  |
| `SoftMax` |  |

Weight normalization method.

#### EComposableCameraMixingCameraMode { #ecomposablecameramixingcameramode }

```cpp
enum EComposableCameraMixingCameraMode
```

| Value | Description |
|-------|-------------|
| `PositionOnly` |  |
| `RotationOnly` |  |
| `Both` |  |

Mixing camera node mode.

#### EComposableCameraMixingCameraRotationMethod { #ecomposablecameramixingcamerarotationmethod }

```cpp
enum EComposableCameraMixingCameraRotationMethod
```

| Value | Description |
|-------|-------------|
| `MatrixInterp` |  |
| `CircularInterp` |  |
| `QuaternionInterpolation` |  |
| `AngleInterpolation` |  |

Different methods to average rotations. Ref: [https://sulley.cc/2024/01/11/20/06/](https://sulley.cc/2024/01/11/20/06/).

#### EComposableCameraSplineTransitionType { #ecomposablecamerasplinetransitiontype }

```cpp
enum EComposableCameraSplineTransitionType
```

| Value | Description |
|-------|-------------|
| `Hermite` |  |
| `Bezier` |  |
| `CatmullRom` |  |
| `Arc` |  |

#### EComposableCameraSplineTransitionEvaluationCurveType { #ecomposablecamerasplinetransitionevaluationcurvetype }

```cpp
enum EComposableCameraSplineTransitionEvaluationCurveType
```

| Value | Description |
|-------|-------------|
| `Smooth` |  |
| `Smoother` |  |
| `Linear` |  |
| `Cubic` |  |

#### EComposableCameraHitchcockZoomDriver { #ecomposablecamerahitchcockzoomdriver }

```cpp
enum EComposableCameraHitchcockZoomDriver
```

| Value | Description |
|-------|-------------|
| `FromFOVDelta` |  |
| `FromDistanceDelta` |  |

Which authored quantity the node drives. The other is solved from the frame-zero lock constant.

FromFOVDelta — author `FOVDeltaCurve`, derive camera distance. Natural when you think about the look of the effect ("background should distort to N degrees wider"). FromDistanceDelta — author `DistanceDeltaCurve`, derive FOV. Natural when you think about the physical move ("camera dollies back 3 metres").

Both paths preserve the same `distance · tan(FOV/2) = LockConstant` invariant captured on the first tick, so the two authoring styles are physically equivalent — the choice is purely about which curve is easier to shape in the project's authoring pipeline.

#### EComposableCameraRotationConstrainType { #ecomposablecamerarotationconstraintype }

```cpp
enum EComposableCameraRotationConstrainType
```

| Value | Description |
|-------|-------------|
| `WorldSpace` |  |
| `ActorSpace` |  |
| `VectorSpace` |  |

#### EComposableCameraScreenSpaceMethod { #ecomposablecamerascreenspacemethod }

```cpp
enum EComposableCameraScreenSpaceMethod
```

| Value | Description |
|-------|-------------|
| `Translate` |  |
| `Rotate` |  |

#### EComposableCameraScreenSpacePivotSource { #ecomposablecamerascreenspacepivotsource }

```cpp
enum EComposableCameraScreenSpacePivotSource
```

| Value | Description |
|-------|-------------|
| `WorldPosition` |  |
| `ActorPosition` |  |

#### EComposableCameraVolumeSource { #ecomposablecameravolumesource }

```cpp
enum EComposableCameraVolumeSource
```

| Value | Description |
|-------|-------------|
| `FromActor` |  |
| `Inline` |  |

How the constraint volume is sourced.

FromActor — Pull the shape from the first `UShapeComponent` on VolumeActor. UBoxComponent and USphereComponent are supported; the component's world transform + scaled extents drive the volume. Capsule and other shape subclasses are rejected with a warning. Inline — The node carries its own world-space volume definition via VolumeCenter / VolumeRotation / BoxExtents / SphereRadius.

#### EComposableCameraVolumeShape { #ecomposablecameravolumeshape }

```cpp
enum EComposableCameraVolumeShape
```

| Value | Description |
|-------|-------------|
| `Box` |  |
| `Sphere` |  |

Shape of the constraint volume in Inline mode. FromActor mode resolves the shape from the component's concrete class.

#### EComposableCameraPathGuidedTransitionType { #ecomposablecamerapathguidedtransitiontype }

```cpp
enum EComposableCameraPathGuidedTransitionType
```

| Value | Description |
|-------|-------------|
| `Inertialized` |  |
| `Auto` |  |

#### EComposableCameraRelativeFixedPoseMethod { #ecomposablecamerarelativefixedposemethod }

```cpp
enum EComposableCameraRelativeFixedPoseMethod
```

| Value | Description |
|-------|-------------|
| `RelativeToTransform` |  |
| `RelativeToActor` |  |