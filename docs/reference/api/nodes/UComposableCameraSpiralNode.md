
# UComposableCameraSpiralNode { #ucomposablecameraspiralnode }

```cpp
#include <ComposableCameraSpiralNode.h>
```

> **Inherits:** [`UComposableCameraCameraNodeBase`](../uobjects-other/UComposableCameraCameraNodeBase.md#ucomposablecameracameranodebase)

Positions the camera on a helical path around a pivot point.

Position-only node — rotation is left untouched, to be authored by a downstream LookAtNode (or similar). The position formula, evaluated each tick, is: P(t) = EffectivePivot
     + Axis        * HeightCurve(NormalizedTime)
     + PerpDir(θ)  * RadiusCurve(NormalizedTime)

EffectivePivot = ResolvedPivot
               + Forward * PivotOffset.X
               + Right   * PivotOffset.Y
               + Axis    * PivotOffset.Z

PerpDir(θ) = Forward * cos(θ) + Right * sin(θ)
θ          = InitialAngleDegrees + AngleCurve(NormalizedTime)
 Where the Spiral-Space basis (Up, Forward, Right) is resolved from RotationAxis and ReferenceDirection each tick — Forward is the ReferenceDirection vector projected onto the plane perpendicular to Axis and renormalized, and Right = Cross(Axis, Forward).

Curve authoring convention (Progress pattern, matching SplineNode's AutomaticMoveCurve): all three curves use X ∈ [0, 1] as normalized time within Duration; Y in absolute world units — Radius / Height in cm, AngleCurve in degrees. Direct curve evaluation means position at any arbitrary t is O(1) computable — no integration history, no accumulated state. A Loop-mode orbit typically authors AngleCurve as Y(0)=0, Y(1)=360·N for a seamless N-turn cycle; non-360 multiples produce an intentional retrace at the cycle seam.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `EComposableCameraSpiralPivotSourceType` | [`PivotSourceType`](#pivotsourcetype)  | Whether the pivot comes from an Actor's location or a raw vector. |
| `TObjectPtr< AActor >` | [`PivotActor`](#pivotactor)  | Actor whose world location is used as the pivot. Typically driven by an upstream ReceivePivotActorNode's output, or set on the instance. |
| `FVector` | [`PivotPosition`](#pivotposition)  | Raw pivot position in world space. Typically driven by an upstream pivot-producing node via wire (PivotOffsetNode's output). |
| `FVector` | [`PivotOffset`](#pivotoffset)  | Offset applied to the resolved pivot, expressed in Spiral Space: X = along Forward, Y = along Right, Z = along Axis (Up). Spiral Space is re-derived from RotationAxis and ReferenceDirection each tick, so this offset automatically tracks a pivot actor's orientation when Spiral Space is anchored to the actor. |
| `EComposableCameraSpiralRotationAxis` | [`RotationAxis`](#rotationaxis)  | The axis around which the camera orbits. PivotActorUp silently falls back to WorldUp with a warning when PivotSourceType == FromVector. |
| `FVector` | [`CustomAxis`](#customaxis)  | Custom rotation axis (world space). Normalized at runtime; falls back to WorldUp if near-zero. |
| `EComposableCameraSpiralReferenceDirection` | [`ReferenceDirection`](#referencedirection)  | The direction that anchors θ = 0 in the plane perpendicular to RotationAxis. PivotActorForward silently falls back to WorldX with a warning when PivotSourceType == FromVector. |
| `FVector` | [`CustomDirection`](#customdirection)  | Custom θ = 0 direction (world space). Projected onto the plane perpendicular to the rotation axis at runtime. |
| `float` | [`InitialAngleDegrees`](#initialangledegrees)  | Starting angular offset applied to θ. Added to the value read from AngleCurve each tick, so the spiral can begin at any azimuth around the axis without re-authoring the curve. |
| `TObjectPtr< UCurveFloat >` | [`RadiusCurve`](#radiuscurve)  | Radial distance from Axis over normalized time. X ∈ [0,1], Y in cm. A null curve is treated as a constant 0 radius (camera collapses onto Axis). |
| `TObjectPtr< UCurveFloat >` | [`HeightCurve`](#heightcurve)  | Signed distance along Axis from the pivot over normalized time. X ∈ [0,1], Y in cm (positive = along Axis, negative = against Axis). A null curve is treated as a constant 0 height. |
| `TObjectPtr< UCurveFloat >` | [`AngleCurve`](#anglecurve)  | Angular position (degrees, absolute) over normalized time. X ∈ [0,1], Y in degrees — positive = right-handed rotation around Axis. Progress pattern, same as SplineNode's AutomaticMoveCurve: θ at any instant is a direct curve read, not an integral of speed. A null curve is treated as a constant 0 angle. |
| `float` | [`Duration`](#duration-3)  | Length of one "cycle" of the three curves, in seconds. Values at or below SMALL_NUMBER are treated as a degenerate duration — all three curves are sampled at NormalizedTime = 0 and the pose stays frozen at the initial frame. |
| `EComposableCameraSpiralPlayMode` | [`PlayMode`](#playmode)  | How the node behaves after the first cycle ends. See enum comment. |

---

#### PivotSourceType { #pivotsourcetype }

```cpp
EComposableCameraSpiralPivotSourceType PivotSourceType {  }
```

Whether the pivot comes from an Actor's location or a raw vector.

---

#### PivotActor { #pivotactor }

```cpp
TObjectPtr< AActor > PivotActor { nullptr }
```

Actor whose world location is used as the pivot. Typically driven by an upstream ReceivePivotActorNode's output, or set on the instance.

---

#### PivotPosition { #pivotposition }

```cpp
FVector PivotPosition { FVector::ZeroVector }
```

Raw pivot position in world space. Typically driven by an upstream pivot-producing node via wire (PivotOffsetNode's output).

---

#### PivotOffset { #pivotoffset }

```cpp
FVector PivotOffset { FVector::ZeroVector }
```

Offset applied to the resolved pivot, expressed in Spiral Space: X = along Forward, Y = along Right, Z = along Axis (Up). Spiral Space is re-derived from RotationAxis and ReferenceDirection each tick, so this offset automatically tracks a pivot actor's orientation when Spiral Space is anchored to the actor.

---

#### RotationAxis { #rotationaxis }

```cpp
EComposableCameraSpiralRotationAxis RotationAxis {  }
```

The axis around which the camera orbits. PivotActorUp silently falls back to WorldUp with a warning when PivotSourceType == FromVector.

---

#### CustomAxis { #customaxis }

```cpp
FVector CustomAxis { FVector::UpVector }
```

Custom rotation axis (world space). Normalized at runtime; falls back to WorldUp if near-zero.

---

#### ReferenceDirection { #referencedirection }

```cpp
EComposableCameraSpiralReferenceDirection ReferenceDirection {  }
```

The direction that anchors θ = 0 in the plane perpendicular to RotationAxis. PivotActorForward silently falls back to WorldX with a warning when PivotSourceType == FromVector.

---

#### CustomDirection { #customdirection }

```cpp
FVector CustomDirection { FVector::ForwardVector }
```

Custom θ = 0 direction (world space). Projected onto the plane perpendicular to the rotation axis at runtime.

---

#### InitialAngleDegrees { #initialangledegrees }

```cpp
float InitialAngleDegrees { 0.f }
```

Starting angular offset applied to θ. Added to the value read from AngleCurve each tick, so the spiral can begin at any azimuth around the axis without re-authoring the curve.

---

#### RadiusCurve { #radiuscurve }

```cpp
TObjectPtr< UCurveFloat > RadiusCurve { nullptr }
```

Radial distance from Axis over normalized time. X ∈ [0,1], Y in cm. A null curve is treated as a constant 0 radius (camera collapses onto Axis).

---

#### HeightCurve { #heightcurve }

```cpp
TObjectPtr< UCurveFloat > HeightCurve { nullptr }
```

Signed distance along Axis from the pivot over normalized time. X ∈ [0,1], Y in cm (positive = along Axis, negative = against Axis). A null curve is treated as a constant 0 height.

---

#### AngleCurve { #anglecurve }

```cpp
TObjectPtr< UCurveFloat > AngleCurve { nullptr }
```

Angular position (degrees, absolute) over normalized time. X ∈ [0,1], Y in degrees — positive = right-handed rotation around Axis. Progress pattern, same as SplineNode's AutomaticMoveCurve: θ at any instant is a direct curve read, not an integral of speed. A null curve is treated as a constant 0 angle.

---

#### Duration { #duration-3 }

```cpp
float Duration { 3.f }
```

Length of one "cycle" of the three curves, in seconds. Values at or below SMALL_NUMBER are treated as a degenerate duration — all three curves are sampled at NormalizedTime = 0 and the pose stays frozen at the initial frame.

---

#### PlayMode { #playmode }

```cpp
EComposableCameraSpiralPlayMode PlayMode {  }
```

How the node behaves after the first cycle ends. See enum comment.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`UComposableCameraSpiralNode`](#ucomposablecameraspiralnode-1) `inline` |  |
| `void` | [`OnInitialize_Implementation`](#oninitialize_implementation-1) `virtual` |  |
| `void` | [`OnTickNode_Implementation`](#onticknode_implementation-2) `virtual` |  |
| `void` | [`GetPinDeclarations_Implementation`](#getpindeclarations_implementation-2) `virtual` `const` |  |
| `void` | [`DrawNodeDebug`](#drawnodedebug-1) `virtual` `const` | Called each frame when the `CCS.Debug.Viewport` CVar is enabled, for every node on the currently running camera. Override to draw world-space debug gizmos via `DrawDebugHelpers` (DrawDebugSphere, DrawDebugLine, etc.) that visualise this node's runtime state — e.g. a pivot sphere for PivotOffsetNode, a look-at line for LookAtNode, the collision trace for CollisionPushNode, a sampled spline path for SplineNode. |

---

#### UComposableCameraSpiralNode { #ucomposablecameraspiralnode-1 }

`inline`

```cpp
inline UComposableCameraSpiralNode()
```

---

#### OnInitialize_Implementation { #oninitialize_implementation-1 }

`virtual`

```cpp
virtual void OnInitialize_Implementation()
```

---

#### OnTickNode_Implementation { #onticknode_implementation-2 }

`virtual`

```cpp
virtual void OnTickNode_Implementation(float DeltaTime, const FComposableCameraPose & CurrentCameraPose, FComposableCameraPose & OutCameraPose)
```

---

#### GetPinDeclarations_Implementation { #getpindeclarations_implementation-2 }

`virtual` `const`

```cpp
virtual void GetPinDeclarations_Implementation(TArray< FComposableCameraNodePinDeclaration > & OutPins) const
```

---

#### DrawNodeDebug { #drawnodedebug-1 }

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
| `float` | [`ElapsedTime`](#elapsedtime-3)  | Seconds elapsed since OnInitialize. Drives NormalizedTime. Accumulated unbounded — Fmod inside OnTickNode handles the wrap. Float precision on the ElapsedTime input to Fmod remains acceptable for realistic gameplay durations (hours at 60 fps); if this node is ever used for multi-day always-on installations, wrap ElapsedTime once per cycle. |
| `FVector` | [`CapturedInitialForward`](#capturedinitialforward)  | Camera forward vector captured on the first tick. Used only when ReferenceDirection == CameraInitialForward. |
| `bool` | [`bHasCapturedInitialForward`](#bhascapturedinitialforward)  | True once CapturedInitialForward has been written. Cleared in OnInitialize so re-activation captures a fresh forward. |
| `FVector` | [`DebugEffectivePivot`](#debugeffectivepivot)  |  |
| `FVector` | [`DebugAxis`](#debugaxis)  |  |
| `FVector` | [`DebugForward`](#debugforward)  |  |
| `FVector` | [`DebugRight`](#debugright)  |  |
| `float` | [`DebugCurrentAngleDegrees`](#debugcurrentangledegrees)  |  |
| `FVector` | [`DebugCurrentPosition`](#debugcurrentposition)  |  |

---

#### ElapsedTime { #elapsedtime-3 }

```cpp
float ElapsedTime { 0.f }
```

Seconds elapsed since OnInitialize. Drives NormalizedTime. Accumulated unbounded — Fmod inside OnTickNode handles the wrap. Float precision on the ElapsedTime input to Fmod remains acceptable for realistic gameplay durations (hours at 60 fps); if this node is ever used for multi-day always-on installations, wrap ElapsedTime once per cycle.

---

#### CapturedInitialForward { #capturedinitialforward }

```cpp
FVector CapturedInitialForward { FVector::ForwardVector }
```

Camera forward vector captured on the first tick. Used only when ReferenceDirection == CameraInitialForward.

---

#### bHasCapturedInitialForward { #bhascapturedinitialforward }

```cpp
bool bHasCapturedInitialForward { false }
```

True once CapturedInitialForward has been written. Cleared in OnInitialize so re-activation captures a fresh forward.

---

#### DebugEffectivePivot { #debugeffectivepivot }

```cpp
FVector DebugEffectivePivot { FVector::ZeroVector }
```

---

#### DebugAxis { #debugaxis }

```cpp
FVector DebugAxis { FVector::UpVector }
```

---

#### DebugForward { #debugforward }

```cpp
FVector DebugForward { FVector::ForwardVector }
```

---

#### DebugRight { #debugright }

```cpp
FVector DebugRight { FVector::RightVector }
```

---

#### DebugCurrentAngleDegrees { #debugcurrentangledegrees }

```cpp
float DebugCurrentAngleDegrees { 0.f }
```

---

#### DebugCurrentPosition { #debugcurrentposition }

```cpp
FVector DebugCurrentPosition { FVector::ZeroVector }
```

### Private Methods

| Return | Name | Description |
|--------|------|-------------|
| `bool` | [`ResolvePivot`](#resolvepivot) `const` | Resolve the pivot location from PivotSourceType + PivotActor/PivotPosition. Returns false and logs an error when the chosen source is invalid (null actor). Output is written to OutPivot. |
| `void` | [`ResolveSpiralBasis`](#resolvespiralbasis) `const` | Resolve the Spiral-Space basis (Axis, Forward, Right). Forward is the chosen ReferenceDirection projected onto the plane perpendicular to Axis and renormalized. Falls back to WorldUp / WorldX on degeneracy. |

---

#### ResolvePivot { #resolvepivot }

`const`

```cpp
bool ResolvePivot(FVector & OutPivot) const
```

Resolve the pivot location from PivotSourceType + PivotActor/PivotPosition. Returns false and logs an error when the chosen source is invalid (null actor). Output is written to OutPivot.

---

#### ResolveSpiralBasis { #resolvespiralbasis }

`const`

```cpp
void ResolveSpiralBasis(FVector & OutAxis, FVector & OutForward, FVector & OutRight) const
```

Resolve the Spiral-Space basis (Axis, Forward, Right). Forward is the chosen ReferenceDirection projected onto the plane perpendicular to Axis and renormalized. Falls back to WorldUp / WorldX on degeneracy.
