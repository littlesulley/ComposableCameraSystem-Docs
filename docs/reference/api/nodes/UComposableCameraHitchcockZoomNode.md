
# UComposableCameraHitchcockZoomNode { #ucomposablecamerahitchcockzoomnode }

```cpp
#include <ComposableCameraHitchcockZoomNode.h>
```

> **Inherits:** [`UComposableCameraCameraNodeBase`](../uobjects-other/UComposableCameraCameraNodeBase.md#ucomposablecameracameranodebase)

The Hitchcock Zoom (also known as the Vertigo effect, dolly zoom, or trombone shot): the camera dollies along its view axis while the FOV changes in the opposite direction, such that the target subject keeps roughly the same on-screen size while the background perspective warps dramatically.

Per-tick math: let InitialDistance = |UpstreamPos_0 - TargetPoint_0|
let InitialFOV      = InitialFOVOverride if > 0
                      else OutCameraPose.GetEffectiveFieldOfView()
let LockConstant    = InitialDistance * tan(radians(InitialFOV / 2))

NormalizedTime = min(ElapsedTime / Duration, 1)   // Once-only: clamps
Direction      = (UpstreamPos - TargetPoint).SafeNormal()

if Driver == FromFOVDelta:
    FOV(t)  = InitialFOV + FOVDeltaCurve(NormalizedTime)
    Dist(t) = LockConstant / tan(radians(FOV(t) / 2))
else:  // FromDistanceDelta
    Dist(t) = InitialDistance + DistanceDeltaCurve(NormalizedTime)
    FOV(t)  = 2 * degrees(atan(LockConstant / Dist(t)))

OutPose.Position    = TargetPoint + Direction * Dist(t)
OutPose.FieldOfView = FOV(t)
OutPose.FocalLength = -1                 // sentinel: FOV-mode authoritative
**Curve convention — additive delta, Y(0) = 0.** Both curves express the *change* from the captured initial state, not the absolute trajectory. A curve of Y(0)=0, Y(1)=-30 on FOVDeltaCurve says "narrow the FOV by 30
degrees over the duration", regardless of whether InitialFOV was 60 or

1. This keeps curves portable across cameras and guarantees the first tick outputs `InitialFOV` / `InitialDistance` exactly — no seam at t=0.

**Direction is resampled every tick** from the upstream pose, not frozen at activation. This lets an upstream LookAt / CameraOffset continue to steer the view direction during the effect — Hitchcock only owns the radial distance + FOV, leaving rotation composable with the rest of the chain.

**FOV ownership.** The node writes `FieldOfView` and clears `FocalLength` to -1 (pose's "FOV-mode" sentinel). If an upstream LensNode is in the chain, set its `bOverrideFieldOfViewFromFocalLength` to false so it doesn't fight for FOV authorship — LensNode's focal length / aperture / blade count still flow through, but FOV stays under this node's control. Alternatively, place HitchcockZoom *after* any FOV-writing node and it will simply overwrite them (last writer wins on the pose).

PlayMode is implicit: Once. There is no Loop / PingPong — authors who need a cyclic dolly zoom can drive the node externally (via re- activation or by repeatedly resetting the camera context).

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TObjectPtr< AActor >` | [`PivotActor`](#pivotactor-4)  | The subject the effect locks on. Camera dollies along the camera→subject axis; FOV compensates so this subject stays the same on-screen size. Required — the node is a pass-through with a warning when null. |
| `bool` | [`bUseBoneForDetection`](#busebonefordetection-2)  | When true, target point is the named bone / socket on PivotActor's skeletal mesh (if resolvable). Falls back to ActorLocation + PivotZOffset on any failure. |
| `FName` | [`BoneName`](#bonename-3)  | Bone / socket name. Sampled when bUseBoneForDetection is true. |
| `float` | [`PivotZOffset`](#pivotzoffset-2)  | World-Z offset added to ActorLocation when bUseBoneForDetection is false (or the bone can't be found). Typical 50–80 to land on chest / head rather than foot. |
| `float` | [`InitialFOVOverride`](#initialfovoverride)  | Baseline FOV (degrees) captured as InitialFOV on the first tick. When > 0, this value wins regardless of what the upstream pose carried for FieldOfView — the typical case for camera type assets that have no `FieldOfViewNode` / `LensNode` upstream and would otherwise inherit a renderer default on the first tick. |
| `EComposableCameraHitchcockZoomDriver` | [`Driver`](#driver)  | Which authored curve drives the effect. The other quantity is solved from the lock constant captured on the first tick. |
| `TObjectPtr< UCurveFloat >` | [`FOVDeltaCurve`](#fovdeltacurve)  | Additive FOV delta (degrees) over normalized time. X ∈ [0, 1], Y is DELTA from InitialFOV — author Y(0) = 0 so the first tick preserves InitialFOV exactly. Positive Y widens the FOV, negative narrows (the classic "zoom in as the camera dollies out" is a curve with negative Y values). |
| `TObjectPtr< UCurveFloat >` | [`DistanceDeltaCurve`](#distancedeltacurve)  | Additive distance delta (world units) over normalized time. X ∈ [0, 1], Y is DELTA from InitialDistance — author Y(0) = 0. Positive Y dollies the camera back (away from subject), negative Y pushes in. |
| `float` | [`Duration`](#duration-7)  | Seconds the effect takes to play from start to end state. After Duration elapses, the curves are evaluated at NormalizedTime = 1 and the pose freezes at the final state for as long as the node remains active. |
| `bool` | [`bEnable`](#benable)  | Master toggle. When false, the node is a pass-through this tick (no camera dolly, no FOV override). Useful for Blueprint-gated effects: trigger the activation + enable on cue, disable on cut. |
| `bool` | [`bClampCameraDistance`](#bclampcameradistance)  | When true, the derived camera distance is clamped to CameraDistanceClamp. Prevents pathological curve shapes from flying the camera off to kilometres away (very narrow FOV) or plunging into / past the subject (very wide FOV). |
| `FFloatInterval` | [`CameraDistanceClamp`](#cameradistanceclamp)  | Min/max on the camera-to-subject distance when bClampCameraDistance is true. Min should be larger than the subject's extent so the camera doesn't end up inside the actor; Max bounds the "infinite |

---

#### PivotActor { #pivotactor-4 }

```cpp
TObjectPtr< AActor > PivotActor { nullptr }
```

The subject the effect locks on. Camera dollies along the camera→subject axis; FOV compensates so this subject stays the same on-screen size. Required — the node is a pass-through with a warning when null.

---

#### bUseBoneForDetection { #busebonefordetection-2 }

```cpp
bool bUseBoneForDetection { false }
```

When true, target point is the named bone / socket on PivotActor's skeletal mesh (if resolvable). Falls back to ActorLocation + PivotZOffset on any failure.

---

#### BoneName { #bonename-3 }

```cpp
FName BoneName
```

Bone / socket name. Sampled when bUseBoneForDetection is true.

---

#### PivotZOffset { #pivotzoffset-2 }

```cpp
float PivotZOffset { 50.f }
```

World-Z offset added to ActorLocation when bUseBoneForDetection is false (or the bone can't be found). Typical 50–80 to land on chest / head rather than foot.

---

#### InitialFOVOverride { #initialfovoverride }

```cpp
float InitialFOVOverride { -1.f }
```

Baseline FOV (degrees) captured as InitialFOV on the first tick. When > 0, this value wins regardless of what the upstream pose carried for FieldOfView — the typical case for camera type assets that have no `FieldOfViewNode` / `LensNode` upstream and would otherwise inherit a renderer default on the first tick.

When ≤ 0 (the default `-1` sentinel matches the plugin's FOV-mode sentinel in LensNode and `[FComposableCameraPose](../structs/FComposableCameraPose.md#fcomposablecamerapose)`), falls back to `OutCameraPose.GetEffectiveFieldOfView()` as read from the upstream chain — the previous behaviour.

Only consulted on the first tick the node captures state. After that, `LockConstant` is frozen against whichever FOV was used, and subsequent ticks derive FOV from the Driver curve.

---

#### Driver { #driver }

```cpp
EComposableCameraHitchcockZoomDriver Driver {  }
```

Which authored curve drives the effect. The other quantity is solved from the lock constant captured on the first tick.

---

#### FOVDeltaCurve { #fovdeltacurve }

```cpp
TObjectPtr< UCurveFloat > FOVDeltaCurve { nullptr }
```

Additive FOV delta (degrees) over normalized time. X ∈ [0, 1], Y is DELTA from InitialFOV — author Y(0) = 0 so the first tick preserves InitialFOV exactly. Positive Y widens the FOV, negative narrows (the classic "zoom in as the camera dollies out" is a curve with negative Y values).

A null curve is treated as identically zero — the node then leaves FOV at InitialFOV and camera at InitialDistance for the full duration, which is useful as a placeholder during blockout.

---

#### DistanceDeltaCurve { #distancedeltacurve }

```cpp
TObjectPtr< UCurveFloat > DistanceDeltaCurve { nullptr }
```

Additive distance delta (world units) over normalized time. X ∈ [0, 1], Y is DELTA from InitialDistance — author Y(0) = 0. Positive Y dollies the camera back (away from subject), negative Y pushes in.

---

#### Duration { #duration-7 }

```cpp
float Duration { 3.f }
```

Seconds the effect takes to play from start to end state. After Duration elapses, the curves are evaluated at NormalizedTime = 1 and the pose freezes at the final state for as long as the node remains active.

---

#### bEnable { #benable }

```cpp
bool bEnable { true }
```

Master toggle. When false, the node is a pass-through this tick (no camera dolly, no FOV override). Useful for Blueprint-gated effects: trigger the activation + enable on cue, disable on cut.

---

#### bClampCameraDistance { #bclampcameradistance }

```cpp
bool bClampCameraDistance { false }
```

When true, the derived camera distance is clamped to CameraDistanceClamp. Prevents pathological curve shapes from flying the camera off to kilometres away (very narrow FOV) or plunging into / past the subject (very wide FOV).

---

#### CameraDistanceClamp { #cameradistanceclamp }

```cpp
FFloatInterval CameraDistanceClamp { 50.f, 10000.f }
```

Min/max on the camera-to-subject distance when bClampCameraDistance is true. Min should be larger than the subject's extent so the camera doesn't end up inside the actor; Max bounds the "infinite
corridor" look that a near-zero derived FOV produces.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`UComposableCameraHitchcockZoomNode`](#ucomposablecamerahitchcockzoomnode-1) `inline` |  |
| `void` | [`OnInitialize_Implementation`](#oninitialize_implementation-12) `virtual` |  |
| `void` | [`OnTickNode_Implementation`](#onticknode_implementation-18) `virtual` |  |
| `void` | [`GetPinDeclarations_Implementation`](#getpindeclarations_implementation-17) `virtual` `const` |  |
| `void` | [`DrawNodeDebug`](#drawnodedebug-8) `virtual` `const` | Called each frame when the `CCS.Debug.Viewport` CVar is enabled, for every node on the currently running camera. Override to draw world-space debug gizmos via `DrawDebugHelpers` (DrawDebugSphere, DrawDebugLine, etc.) that visualise this node's runtime state — e.g. a pivot sphere for PivotOffsetNode, a look-at line for LookAtNode, the collision trace for CollisionPushNode, a sampled spline path for SplineNode. |

---

#### UComposableCameraHitchcockZoomNode { #ucomposablecamerahitchcockzoomnode-1 }

`inline`

```cpp
inline UComposableCameraHitchcockZoomNode()
```

---

#### OnInitialize_Implementation { #oninitialize_implementation-12 }

`virtual`

```cpp
virtual void OnInitialize_Implementation()
```

---

#### OnTickNode_Implementation { #onticknode_implementation-18 }

`virtual`

```cpp
virtual void OnTickNode_Implementation(float DeltaTime, const FComposableCameraPose & CurrentCameraPose, FComposableCameraPose & OutCameraPose)
```

---

#### GetPinDeclarations_Implementation { #getpindeclarations_implementation-17 }

`virtual` `const`

```cpp
virtual void GetPinDeclarations_Implementation(TArray< FComposableCameraNodePinDeclaration > & OutPins) const
```

---

#### DrawNodeDebug { #drawnodedebug-8 }

`virtual` `const`

```cpp
virtual void DrawNodeDebug(UWorld * World, bool bViewerIsOutsideCamera) const
```

Called each frame when the `CCS.Debug.Viewport` CVar is enabled, for every node on the currently running camera. Override to draw world-space debug gizmos via `DrawDebugHelpers` (DrawDebugSphere, DrawDebugLine, etc.) that visualise this node's runtime state — e.g. a pivot sphere for PivotOffsetNode, a look-at line for LookAtNode, the collision trace for CollisionPushNode, a sampled spline path for SplineNode.

Access the owning camera via `OwningCamera` and current-frame pin values via the usual `GetInputPinValue<T>()` / member-read path — this hook fires AFTER TickNode, so pin-backed UPROPERTYs still hold the resolved values from the most recent evaluation.

`bViewerIsOutsideCamera` mirrors the ticker's frustum-draw flag: true when the viewer is observing the camera from outside (F8 eject, SIE, or `CCS.Debug.Viewport.AlwaysShow`), false when the player is looking through the camera. Most gizmos (pivot spheres at distant characters, lines to look-at targets, spline polylines far in the world) can ignore this and draw unconditionally. Gizmos that sit AT the camera's own position (e.g. `CollisionPushNode`'s self-collision sphere) should gate on this bool so they don't hermetically seal the player inside the wireframe during live gameplay.

Default implementation does nothing. Compiled out in shipping builds.

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `float` | [`ElapsedTime`](#elapsedtime-4)  | Elapsed seconds since the effect first ran. Drives NormalizedTime. |
| `double` | [`InitialDistance`](#initialdistance)  | Captured on the first tick the node actually runs (PivotActor resolved, bEnable true). FOV is the *effective* FOV of the upstream pose (handles FOV-mode / FocalLength-mode conversion via `GetEffectiveFieldOfView`). |
| `double` | [`InitialFOVDegrees`](#initialfovdegrees)  |  |
| `double` | [`LockConstant`](#lockconstant)  | Invariant preserved for the full effect duration: `distance * tan(radians(FOV / 2))`. Captured from the initial distance and FOV on the first tick. |
| `bool` | [`bHasCapturedInitialState`](#bhascapturedinitialstate)  | Cleared in OnInitialize; set true once the initial state has been captured. Re-activation resets via OnInitialize. |
| `FVector` | [`DebugTargetPoint`](#debugtargetpoint-1)  |  |
| `FVector` | [`DebugCameraPosition`](#debugcameraposition-1)  |  |
| `FRotator` | [`DebugCameraRotation`](#debugcamerarotation-1)  |  |
| `double` | [`DebugCurrentDistance`](#debugcurrentdistance)  |  |
| `double` | [`DebugCurrentFOV`](#debugcurrentfov)  |  |
| `bool` | [`bDebugDrivenThisTick`](#bdebugdriventhistick)  |  |

---

#### ElapsedTime { #elapsedtime-4 }

```cpp
float ElapsedTime { 0.f }
```

Elapsed seconds since the effect first ran. Drives NormalizedTime.

---

#### InitialDistance { #initialdistance }

```cpp
double InitialDistance { 0.0 }
```

Captured on the first tick the node actually runs (PivotActor resolved, bEnable true). FOV is the *effective* FOV of the upstream pose (handles FOV-mode / FocalLength-mode conversion via `GetEffectiveFieldOfView`).

---

#### InitialFOVDegrees { #initialfovdegrees }

```cpp
double InitialFOVDegrees { 0.0 }
```

---

#### LockConstant { #lockconstant }

```cpp
double LockConstant { 0.0 }
```

Invariant preserved for the full effect duration: `distance * tan(radians(FOV / 2))`. Captured from the initial distance and FOV on the first tick.

---

#### bHasCapturedInitialState { #bhascapturedinitialstate }

```cpp
bool bHasCapturedInitialState { false }
```

Cleared in OnInitialize; set true once the initial state has been captured. Re-activation resets via OnInitialize.

---

#### DebugTargetPoint { #debugtargetpoint-1 }

```cpp
FVector DebugTargetPoint { FVector::ZeroVector }
```

---

#### DebugCameraPosition { #debugcameraposition-1 }

```cpp
FVector DebugCameraPosition { FVector::ZeroVector }
```

---

#### DebugCameraRotation { #debugcamerarotation-1 }

```cpp
FRotator DebugCameraRotation { FRotator::ZeroRotator }
```

---

#### DebugCurrentDistance { #debugcurrentdistance }

```cpp
double DebugCurrentDistance { 0.0 }
```

---

#### DebugCurrentFOV { #debugcurrentfov }

```cpp
double DebugCurrentFOV { 0.0 }
```

---

#### bDebugDrivenThisTick { #bdebugdriventhistick }

```cpp
bool bDebugDrivenThisTick { false }
```

### Private Methods

| Return | Name | Description |
|--------|------|-------------|
| `bool` | [`ResolveTargetPoint`](#resolvetargetpoint-1) `const` | Resolve the target world location from PivotActor + BoneName / PivotZOffset. Returns false when PivotActor is null. |

---

#### ResolveTargetPoint { #resolvetargetpoint-1 }

`const`

```cpp
bool ResolveTargetPoint(FVector & OutTargetPoint) const
```

Resolve the target world location from PivotActor + BoneName / PivotZOffset. Returns false when PivotActor is null.
