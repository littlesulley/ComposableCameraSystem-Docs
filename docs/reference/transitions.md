# Transition Catalog

Each shipped transition, what it does, and what parameters drive it. See [Concepts → Transitions](../user-guide/concepts/transitions.md) for the pose-only contract, the four-phase lifecycle, and the five-tier resolution chain; [User Guide → Transitions & Blending](../user-guide/transitions-and-blending.md) for authoring guidance.

Every transition inherits from `UComposableCameraTransitionBase`, which provides:

- `TransitionDuration` — total duration in seconds. Most transitions treat this as an exact duration; `InertializedTransition` can treat it as a minimum.
- `TransitionEnabled / OnBeginPlay / OnEvaluate / OnFinished` — the four-phase lifecycle. Subclasses typically override `OnBeginPlay` (to cache source-driven state) and `OnEvaluate` (to produce the blended pose).

The `OnEvaluate` contract is the same across every subclass: receive live source and target poses plus a normalized `Percentage` in `[0, 1]`, return the blended pose.

## `LinearTransition`

Straight linear interpolation of position and rotation. `Lerp(source, target, Percentage)`.

- **Parameters:** none beyond the base duration.
- **Velocity-aware:** no.
- **Typical use:** cheapest possible blend. Use as a baseline, or for UI-driven cuts where the source camera isn't moving.

## `CubicTransition`

Cubic easing — smooth start and smooth end, accelerating through the middle. No tunable exponent; a fixed cubic polynomial.

- **Parameters:** none beyond the base duration.
- **Velocity-aware:** no.
- **Typical use:** a visual step up from `LinearTransition` for moderate-duration blends where physical plausibility isn't required.

## `EaseTransition`

`EaseInOut` with a tunable exponent.

| Field | Type | Default | Purpose |
|---|---|---|---|
| `Exp` | `float` | `1.0` | Exponent. `1.0` behaves like a linear blend; higher values produce sharper in/out regions with a flatter middle. |

- **Velocity-aware:** no.
- **Typical use:** when you want a specific easing feel that neither `Cubic` nor `Smooth` quite hits. Start around `Exp = 2.0` and tune.

## `SmoothTransition`

Hermite smoothstep or smootherstep — a classic S-curve blend with zero derivative at both ends.

| Field | Type | Default | Purpose |
|---|---|---|---|
| `bSmootherStep` | `bool` | `false` | `false` → Hermite smoothstep `t²(3−2t)`. `true` → smootherstep `t³(t(6t−15)+10)`, a 5th-order polynomial with zero first *and* second derivative at both ends. |

- **Velocity-aware:** no.
- **Typical use:** UI-driven blends, cinematic establishing shots, anywhere you want a clean S-curve without the velocity recovery of inertialization.

## `CylindricalTransition`

Arcs the camera around a pivot derived from the intersection of the source and target look-at rays, instead of cutting a straight path between the two positions. The result reads like an orbital sweep rather than a teleport.

| Field | Type | Default | Purpose |
|---|---|---|---|
| `MinimumDistanceFromOrigin` | `float` | `10.0` | Minimum distance from the derived pivot along the look direction, so the arc never passes through the pivot itself. |
| `bLockToPivot` | `bool` | `true` | If true, the camera's rotation is locked toward the pivot throughout the arc. |

- **Velocity-aware:** no (but inherits the pivot from a ray intersection of the endpoints' look directions).
- **Typical use:** orbital feels, "camera swoops around hero" moments, boss-reveal swings. Avoid for short gameplay blends — the arc reads as motion for its own sake.

## `InertializedTransition`

Physics-plausible 5th-order polynomial blend. The polynomial is constructed so that, at the start of the transition, position and rotation match the source with the correct velocity (recovered from `InitParams` via `(CurrentSourcePose − PreviousSourcePose) / DeltaTime`); and at the end, position and rotation reach the target with zero velocity *and* zero acceleration. This produces a blend that visually respects the source camera's momentum instead of snapping to zero velocity at `t=0`.

| Field | Type | Default | Purpose |
|---|---|---|---|
| `bAutoTransitionTime` | `bool` | `false` | If true, the transition auto-computes its own duration from `MaxAcceleration` instead of using `TransitionDuration`. |
| `MaxAcceleration` | `float` | `100.0` | Acceleration cap (cm/s²) used when `bAutoTransitionTime` is on. Lower values produce longer, softer blends. |
| `AdditiveCurve` | `UCurveFloat*` | `nullptr` | Optional normalized curve (`x∈[0,1]`, `y∈[0,1]`, `f(0)=1`, `f(1)=0`) added to the polynomial output. Lets you reshape the blend without abandoning the inertialized math. |
| `AdditiveCurveWeight` | `float` | `0.5` | Overall contribution of the additive curve. |
| `AdditiveCurveShape` | `float` | `10.0` | Per-phase falloff for the additive curve (how quickly it blends in near the midpoint and out near the ends). |

- **Velocity-aware:** yes — the default for most gameplay blends.
- **Typical use:** gameplay cuts, camera-to-camera blends while the player is moving, any blend where snapping to zero velocity at the start would be visible as a kink.

See [Concepts → Transitions → InitParams](../user-guide/concepts/transitions.md#initparams-why-velocity-matters) for why velocity matters and how `FComposableCameraTransitionInitParams` delivers it.

## `SplineTransition`

The camera follows a computed spline from source to target. The spline shape is authored directly as tangents, control points, or an arc descriptor — there's no external rail actor involved (unlike `PathGuidedTransition`).

| Field | Type | Default | Purpose |
|---|---|---|---|
| `SplineType` | enum | `Hermite` | `Hermite` / `Bezier` / `CatmullRom` / `Arc`. Controls which geometry fields apply. |
| `EvaluationCurveType` | enum | `Smoother` | `Linear` / `Cubic` / `Smooth` / `Smoother`. How the camera's `t` parameter is evolved along the spline. |
| `StartTangent` | `FVector` | `(0, 100, 0)` | *(Hermite only)* tangent at source, in a local frame aligned with source→target. |
| `EndTangent` | `FVector` | `(0, 100, 0)` | *(Hermite only)* tangent at target. |
| `StartControlPoint` | `FVector` | `(0, 100, 0)` | *(Bezier only)* cubic control point attached to source. |
| `EndControlPoint` | `FVector` | `(0, 100, 0)` | *(Bezier only)* cubic control point attached to target. |
| `ControlPoints` | `TArray<FVector>` | — | *(CatmullRom only)* intermediate knots. |
| `ArcAngle` | `float` | `180` | *(Arc only)* span in degrees — 180 is a half circle, 90 a quarter circle, 270 a quarter circle going the long way. |
| `ArcRoll` | `float` | `0` | *(Arc only)* roll along the source→target axis, in degrees. |

- **Velocity-aware:** no (the spline is pre-computed at `OnBeginPlay`).
- **Typical use:** cinematic blends where the exact path matters and is worth authoring by hand. For rail-driven paths, prefer `PathGuidedTransition`.

## `PathGuidedTransition`

Three-phase cinematic: enter from source onto a rail, follow the rail, exit to the target. An intermediate camera is spawned on the rail as a carrier. Uses two internal `InertializedTransition`s (for enter and exit) around a rail-follow middle phase.

| Field | Type | Default | Purpose |
|---|---|---|---|
| `DrivingTransition` | `UComposableCameraTransitionBase*` (instanced) | — | Transition used to drive the base camera's motion underneath the path phase. Typically an `InertializedTransition`. |
| `Type` | enum | `Inertialized` | `Inertialized` (two inertialized bridges) or `Auto` (auto-generated splines). `Auto` does not update the target pose each frame — don't use it if the target camera is moving. |
| `RailActor` | `TSoftObjectPtr<ACameraRig_Rail>` | — | The `CameraRig_Rail` whose spline the camera follows in the middle phase. |
| `GuideRange` | `FVector2D` | `(0.25, 0.75)` | Normalized percentages marking the start and end of the guide phase. The blend spends `[0, start]` entering the rail, `[start, end]` following it, `[end, 1]` exiting. |
| `SplineMoveCurve` | `UCurveFloat*` | — | Optional normalized curve (`[0, 1] → [0, 1]`) controlling how fast the intermediate camera progresses along the rail. |

- **Velocity-aware:** yes on enter and exit (via the inertialized bridges).
- **Cost:** higher than other transitions — spawns an intermediate camera actor and duplicates the rail's spline component. Use for set pieces, not gameplay.
- **Typical use:** cinematic swoops, lift-off shots, "camera leaves the player and flies to the vista" moments.

## `DynamicDeocclusionTransition`

A wrapper around another transition. Each frame it casts one or more "feeler" rays from the wrapped transition's output pose toward the target; if any feeler is blocked, it nudges the output pose along the unblocked feeler direction, preventing the blend from passing through occluders. Clears back to the base pose when occlusion resolves.

| Field | Type | Default | Purpose |
|---|---|---|---|
| `DrivingTransition` | `UComposableCameraTransitionBase*` (instanced) | — | The wrapped transition that actually computes the base blended pose. The deocclusion pass runs on top of that. |
| `Feelers` | `TArray<FComposableCameraRayFeeler>` | — | Rays to probe for occlusion. Each feeler has `Yaw`, `Pitch`, `Length`, `Radius`, `Offset`, and a `StrengthCurve`. |
| `TraceChannel` | `TEnumAsByte<ETraceTypeQuery>` | — | Collision channel used for all feeler traces. |
| `ActorTypesToIgnore` | `TArray<TSoftClassPtr<AActor>>` | — | Actor classes whose instances are ignored by the feelers. |
| `DeocclusionSpeed` | `float` | `1.0` | How fast the camera pushes off an occlusion. |
| `ResumeWaitingTime` | `float` | `0.2` | Seconds to wait with no occlusion detected before returning to the base pose. |
| `DeadPercentage` | `float` | `0.8` | Past this normalized blend percentage, deocclusion is ignored — the transition commits to the target. |
| `ResumeSpeed` | `float` | `0.8` | How fast the camera returns to the base pose once deocclusion clears. |

- **Velocity-aware:** depends on the `DrivingTransition`. Usually wrap an `InertializedTransition`.
- **Typical use:** long blends in geometry-dense environments — cinematic pans through corridors, third-person → aim transitions around corners, anywhere the blend path might pass through a wall.

---

## `ViewTargetTransition`

!!! note "Auto-drafted from header — please review"
    This entry was generated by the auto-updater from the class's doc comment. Expand with usage notes, pin descriptions, and an example when you have a moment.

Internal-only transition — not intended for placement in transition data assets by designers. Created programmatically by the PCM's `SetViewTarget` override when external code (engine CameraCut handler, gameplay Possess, `SetViewTargetWithBlend`, etc.) calls `SetViewTarget` with non-zero `FViewTargetTransitionParams`. Delegates blend-curve evaluation to `FViewTargetTransitionParams::GetBlendAlpha()`, making every `EViewTargetBlendFunction` the engine supports automatically available through CCS's pose-only transition system.

**Header:** `ComposableCameraViewTargetTransition.h`
**C++ reference:** [`UComposableCameraViewTargetTransition`](api/transitions/UComposableCameraViewTargetTransition.md)

---

*See also:* [User Guide → Transitions & Blending](../user-guide/transitions-and-blending.md) for authoring and tuning; [Extending → Custom Transitions](../extending/custom-transitions.md) for writing your own.
