
# UComposableCameraFocusPullNode { #ucomposablecamerafocuspullnode }

```cpp
#include <ComposableCameraFocusPullNode.h>
```

> **Inherits:** [`UComposableCameraCameraNodeBase`](../uobjects-other/UComposableCameraCameraNodeBase.md#ucomposablecameracameranodebase)

Dynamically drives the camera pose's `FocusDistance` from the distance to a target actor. Single-responsibility node — it only touches `FocusDistance`. Everything else DoF needs (aperture, blade count, filmback, and the `PhysicalCameraBlendWeight` that gates whether DoF is applied at all) is expected to come from an upstream `LensNode`. The intended composition: ... → LensNode(FocalLength, Aperture, BlendWeight=1, FocusDistance=-1)
    → FocusPullNode(drives FocusDistance from PivotActor)
    → ...
 LensNode's `FocusDistance = -1` sentinel is the "leave for downstream" signal that pairs cleanly with this node. If LensNode instead writes a concrete focus distance, FocusPullNode will **overwrite** it (last writer wins on the pose) — both work, the sentinel just makes the intent obvious at read time.

Without any LensNode upstream, the pose's default `PhysicalCameraBlendWeight` is 0 — `ApplyPhysicalCameraSettings()` will not route `FocusDistance` into the post-process DoF slots regardless of what this node writes. Add a LensNode (or at minimum wire `PhysicalCameraBlendWeight > 0` some other way) or the node is a no-op at the renderer level.

Target resolution matches the plugin's `CollisionPushNode` / `OcclusionFadeNode` pattern (PivotActor + bone/socket + Z offset) so the same context-parameter wiring flows to all three. Damping is optional and uses the standard interpolator system (SpringDamper / IIR / SimpleSpring) so the focus-pull rate matches the project's broader camera tuning.

Per-tick formula: TargetPoint  = Resolve(PivotActor, BoneName | PivotZOffset)
CameraFwd    = OutCameraPose.Rotation.Vector()
Depth        = (TargetPoint - OutCameraPose.Position) · CameraFwd
if Depth <= 0: pass-through this tick (target is behind camera)
Raw          = Depth + FocusDistanceOffset
if bClampFocusDistance: Raw = FMath::Clamp(Raw, Clamp.Min, Clamp.Max)
if FocusInterpolator:   Raw = Interp.Run(LastFocus → Raw, DeltaTime)
OutCameraPose.FocusDistance = Raw
`FocusDistance` is camera-space depth (distance along the view axis), NOT Euclidean distance — that's what `ApplyPhysicalCameraSettings` and the renderer's DoF system consume. For an off-axis target the two diverge significantly (10 m @ 45° has depth ~7 m), so projecting onto the camera forward is the correct reduction.

First tick after activation bypasses the damping so the initial focus distance snaps to the real depth (avoids a visible focus ramp from whatever the pose's previous FocusDistance was).

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TObjectPtr< AActor >` | [`PivotActor`](#pivotactor-1)  | Actor whose distance from the camera drives the focus distance. Typically the player pawn or a narrative focal actor. Required — the node pass-throughs with a warning each tick when unset. |
| `bool` | [`bUseBoneForDetection`](#busebonefordetection)  | When true, the target point is sampled at the named bone / socket on PivotActor's skeletal mesh (if present and resolvable). Falls back to ActorLocation + PivotZOffset on any failure. |
| `FName` | [`BoneName`](#bonename)  | Bone / socket name, sampled when bUseBoneForDetection is true. |
| `float` | [`PivotZOffset`](#pivotzoffset)  | World-Z offset added to ActorLocation when bUseBoneForDetection is false (or the requested bone can't be found). Typical 50–80 to land on a chest/head target rather than foot. |
| `bool` | [`bEnableFocusPull`](#benablefocuspull)  | Master toggle. When false, the node is a no-op pass-through this tick — the previous FocusDistance on the pose is preserved. Useful for Blueprint-driven "focus hold" moments (aim down sights, cinematic freeze, etc.) where external logic wants to take over. |
| `float` | [`FocusDistanceOffset`](#focusdistanceoffset)  | Constant offset added to the on-axis camera→target depth before clamp and damping. Positive = focus farther along the view axis than the target (e.g. focus slightly past the subject); negative = focus nearer. Applied to the projected depth, not Euclidean distance, so it stays visually consistent regardless of how off-axis the target is. |
| `bool` | [`bClampFocusDistance`](#bclampfocusdistance)  | When true, the resolved focus distance is clamped to FocusDistanceClamp. |
| `FFloatInterval` | [`FocusDistanceClamp`](#focusdistanceclamp)  | Min/max range applied when bClampFocusDistance is true. Min clamps against micro-distances (rarely useful below ~10 cm; the renderer's near plane usually dominates before that). Max clamps against the "background"-tier distances that would produce no visible DoF anyway. |
| `TObjectPtr< UComposableCameraInterpolatorBase >` | [`FocusInterpolator`](#focusinterpolator)  | Optional interpolator applied to the focus distance each tick. When null, the node is stateless and the pose's FocusDistance equals the raw (clamped, offset-adjusted) distance every frame — visually this means focus tracks the target with zero lag, which is jittery for fast-moving targets. Pick any of the built-in interpolators (SpringDamper / IIR / SimpleSpring) to get a smooth "focus pull" that matches the camera's broader tuning. First tick after activation bypasses the interpolator to avoid a visible ramp from the previous FocusDistance value. |

---

#### PivotActor { #pivotactor-1 }

```cpp
TObjectPtr< AActor > PivotActor { nullptr }
```

Actor whose distance from the camera drives the focus distance. Typically the player pawn or a narrative focal actor. Required — the node pass-throughs with a warning each tick when unset.

---

#### bUseBoneForDetection { #busebonefordetection }

```cpp
bool bUseBoneForDetection { false }
```

When true, the target point is sampled at the named bone / socket on PivotActor's skeletal mesh (if present and resolvable). Falls back to ActorLocation + PivotZOffset on any failure.

---

#### BoneName { #bonename }

```cpp
FName BoneName
```

Bone / socket name, sampled when bUseBoneForDetection is true.

---

#### PivotZOffset { #pivotzoffset }

```cpp
float PivotZOffset { 50.f }
```

World-Z offset added to ActorLocation when bUseBoneForDetection is false (or the requested bone can't be found). Typical 50–80 to land on a chest/head target rather than foot.

---

#### bEnableFocusPull { #benablefocuspull }

```cpp
bool bEnableFocusPull { true }
```

Master toggle. When false, the node is a no-op pass-through this tick — the previous FocusDistance on the pose is preserved. Useful for Blueprint-driven "focus hold" moments (aim down sights, cinematic freeze, etc.) where external logic wants to take over.

---

#### FocusDistanceOffset { #focusdistanceoffset }

```cpp
float FocusDistanceOffset { 0.f }
```

Constant offset added to the on-axis camera→target depth before clamp and damping. Positive = focus farther along the view axis than the target (e.g. focus slightly past the subject); negative = focus nearer. Applied to the projected depth, not Euclidean distance, so it stays visually consistent regardless of how off-axis the target is.

---

#### bClampFocusDistance { #bclampfocusdistance }

```cpp
bool bClampFocusDistance { false }
```

When true, the resolved focus distance is clamped to FocusDistanceClamp.

---

#### FocusDistanceClamp { #focusdistanceclamp }

```cpp
FFloatInterval FocusDistanceClamp { 10.f, 100000.f }
```

Min/max range applied when bClampFocusDistance is true. Min clamps against micro-distances (rarely useful below ~10 cm; the renderer's near plane usually dominates before that). Max clamps against the "background"-tier distances that would produce no visible DoF anyway.

---

#### FocusInterpolator { #focusinterpolator }

```cpp
TObjectPtr< UComposableCameraInterpolatorBase > FocusInterpolator
```

Optional interpolator applied to the focus distance each tick. When null, the node is stateless and the pose's FocusDistance equals the raw (clamped, offset-adjusted) distance every frame — visually this means focus tracks the target with zero lag, which is jittery for fast-moving targets. Pick any of the built-in interpolators (SpringDamper / IIR / SimpleSpring) to get a smooth "focus pull" that matches the camera's broader tuning. First tick after activation bypasses the interpolator to avoid a visible ramp from the previous FocusDistance value.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`OnInitialize_Implementation`](#oninitialize_implementation-3) `virtual` |  |
| `void` | [`OnTickNode_Implementation`](#onticknode_implementation-5) `virtual` |  |
| `void` | [`GetPinDeclarations_Implementation`](#getpindeclarations_implementation-5) `virtual` `const` |  |
| `void` | [`DrawNodeDebug`](#drawnodedebug-3) `virtual` `const` | Called each frame when the `CCS.Debug.Viewport` CVar is enabled, for every node on the currently running camera. Override to draw world-space debug gizmos via `DrawDebugHelpers` (DrawDebugSphere, DrawDebugLine, etc.) that visualise this node's runtime state — e.g. a pivot sphere for PivotOffsetNode, a look-at line for LookAtNode, the collision trace for CollisionPushNode, a sampled spline path for SplineNode. |

---

#### OnInitialize_Implementation { #oninitialize_implementation-3 }

`virtual`

```cpp
virtual void OnInitialize_Implementation()
```

---

#### OnTickNode_Implementation { #onticknode_implementation-5 }

`virtual`

```cpp
virtual void OnTickNode_Implementation(float DeltaTime, const FComposableCameraPose & CurrentCameraPose, FComposableCameraPose & OutCameraPose)
```

---

#### GetPinDeclarations_Implementation { #getpindeclarations_implementation-5 }

`virtual` `const`

```cpp
virtual void GetPinDeclarations_Implementation(TArray< FComposableCameraNodePinDeclaration > & OutPins) const
```

---

#### DrawNodeDebug { #drawnodedebug-3 }

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
| `TUniquePtr< TCameraInterpolator< TValueTypeWrapper< double > > >` | [`FocusInterpolator_T`](#focusinterpolator_t)  | Runtime instance built from FocusInterpolator in OnInitialize. Null when no interpolator is configured or the asset's BuildDoubleInterpolator returns null. |
| `double` | [`LastSmoothedFocusDistance`](#lastsmoothedfocusdistance)  | Persistent smoothed focus distance between frames. Seeded on the first tick from the raw distance so frame-zero doesn't drift in from an arbitrary sentinel. |
| `bool` | [`bHasSeededSmoothing`](#bhasseededsmoothing)  | Cleared in OnInitialize; set true on first successful tick so re- activation re-seeds. |
| `FVector` | [`DebugTargetPoint`](#debugtargetpoint)  |  |
| `FVector` | [`DebugCameraPosition`](#debugcameraposition)  |  |
| `FRotator` | [`DebugCameraRotation`](#debugcamerarotation)  |  |
| `double` | [`DebugResolvedFocusDistance`](#debugresolvedfocusdistance)  |  |
| `bool` | [`bDebugWasDrivenThisTick`](#bdebugwasdriventhistick)  |  |

---

#### FocusInterpolator_T { #focusinterpolator_t }

```cpp
TUniquePtr< TCameraInterpolator< TValueTypeWrapper< double > > > FocusInterpolator_T
```

Runtime instance built from FocusInterpolator in OnInitialize. Null when no interpolator is configured or the asset's BuildDoubleInterpolator returns null.

---

#### LastSmoothedFocusDistance { #lastsmoothedfocusdistance }

```cpp
double LastSmoothedFocusDistance { 0.0 }
```

Persistent smoothed focus distance between frames. Seeded on the first tick from the raw distance so frame-zero doesn't drift in from an arbitrary sentinel.

---

#### bHasSeededSmoothing { #bhasseededsmoothing }

```cpp
bool bHasSeededSmoothing { false }
```

Cleared in OnInitialize; set true on first successful tick so re- activation re-seeds.

---

#### DebugTargetPoint { #debugtargetpoint }

```cpp
FVector DebugTargetPoint { FVector::ZeroVector }
```

---

#### DebugCameraPosition { #debugcameraposition }

```cpp
FVector DebugCameraPosition { FVector::ZeroVector }
```

---

#### DebugCameraRotation { #debugcamerarotation }

```cpp
FRotator DebugCameraRotation { FRotator::ZeroRotator }
```

---

#### DebugResolvedFocusDistance { #debugresolvedfocusdistance }

```cpp
double DebugResolvedFocusDistance { 0.0 }
```

---

#### bDebugWasDrivenThisTick { #bdebugwasdriventhistick }

```cpp
bool bDebugWasDrivenThisTick { false }
```

### Private Methods

| Return | Name | Description |
|--------|------|-------------|
| `bool` | [`ResolveTargetPoint`](#resolvetargetpoint) `const` | Resolve the target world location from PivotActor + BoneName / PivotZOffset. Returns false when PivotActor is null. Mirrors OcclusionFadeNode::ResolveTargetPoint. |

---

#### ResolveTargetPoint { #resolvetargetpoint }

`const`

```cpp
bool ResolveTargetPoint(FVector & OutTargetPoint) const
```

Resolve the target world location from PivotActor + BoneName / PivotZOffset. Returns false when PivotActor is null. Mirrors OcclusionFadeNode::ResolveTargetPoint.
