
# UComposableCameraCollisionPushNode { #ucomposablecameracollisionpushnode }

```cpp
#include <ComposableCameraCollisionPushNode.h>
```

> **Inherits:** [`UComposableCameraCameraNodeBase`](../uobjects-other/UComposableCameraCameraNodeBase.md#ucomposablecameracameranodebase)

Node for resolving collision using self-spherical collision and trace collision.<br/>
This node does two things for collision: <br/>
(1) Casts a trace (either line or sphere) from camera to the target point and resolves any occlusion in-between; <br/>
(2) Carries a sphere around the camera and only resolves occlusion when the sphere collides with objects. <br/>
The first we call it TraceCollision, and the second SelfCollision, both dealt with collision channels. <br/>

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TObjectPtr< AActor >` | [`PivotActor`](#pivotactor-2)  |  |
| `TEnumAsByte< ETraceTypeQuery >` | [`TraceCollisionChannel`](#tracecollisionchannel)  |  |
| `bool` | [`bTraceUseSphere`](#btraceusesphere)  |  |
| `double` | [`TraceSphereRadius`](#tracesphereradius)  |  |
| `double` | [`TraceOcclusionExemptionTime`](#traceocclusionexemptiontime)  |  |
| `TEnumAsByte< ETraceTypeQuery >` | [`SelfCollisionChannel`](#selfcollisionchannel)  |  |
| `double` | [`SelfSphereRadius`](#selfsphereradius)  |  |
| `double` | [`SelfSphereDistanceOffsetFromCenter`](#selfspheredistanceoffsetfromcenter)  |  |
| `TArray< TSoftClassPtr< AActor > >` | [`ActorTypesToIgnore`](#actortypestoignore)  |  |
| `double` | [`ExtraPushDistance`](#extrapushdistance)  |  |
| `TObjectPtr< UComposableCameraInterpolatorBase >` | [`PushInterpolator`](#pushinterpolator)  |  |
| `TObjectPtr< UComposableCameraInterpolatorBase >` | [`PullInterpolator`](#pullinterpolator)  |  |
| `double` | [`PivotZOffset`](#pivotzoffset-1)  |  |
| `bool` | [`bUseBoneForDetection`](#busebonefordetection-1)  |  |
| `FName` | [`BoneName`](#bonename-1)  |  |

---

#### PivotActor { #pivotactor-2 }

```cpp
TObjectPtr< AActor > PivotActor
```

---

#### TraceCollisionChannel { #tracecollisionchannel }

```cpp
TEnumAsByte< ETraceTypeQuery > TraceCollisionChannel
```

---

#### bTraceUseSphere { #btraceusesphere }

```cpp
bool bTraceUseSphere { true }
```

---

#### TraceSphereRadius { #tracesphereradius }

```cpp
double TraceSphereRadius { 12. }
```

---

#### TraceOcclusionExemptionTime { #traceocclusionexemptiontime }

```cpp
double TraceOcclusionExemptionTime { 0. }
```

---

#### SelfCollisionChannel { #selfcollisionchannel }

```cpp
TEnumAsByte< ETraceTypeQuery > SelfCollisionChannel
```

---

#### SelfSphereRadius { #selfsphereradius }

```cpp
double SelfSphereRadius { 12. }
```

---

#### SelfSphereDistanceOffsetFromCenter { #selfspheredistanceoffsetfromcenter }

```cpp
double SelfSphereDistanceOffsetFromCenter { 10. }
```

---

#### ActorTypesToIgnore { #actortypestoignore }

```cpp
TArray< TSoftClassPtr< AActor > > ActorTypesToIgnore
```

---

#### ExtraPushDistance { #extrapushdistance }

```cpp
double ExtraPushDistance { 5. }
```

---

#### PushInterpolator { #pushinterpolator }

```cpp
TObjectPtr< UComposableCameraInterpolatorBase > PushInterpolator
```

---

#### PullInterpolator { #pullinterpolator }

```cpp
TObjectPtr< UComposableCameraInterpolatorBase > PullInterpolator
```

---

#### PivotZOffset { #pivotzoffset-1 }

```cpp
double PivotZOffset { 50. }
```

---

#### bUseBoneForDetection { #busebonefordetection-1 }

```cpp
bool bUseBoneForDetection { false }
```

---

#### BoneName { #bonename-1 }

```cpp
FName BoneName
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`OnInitialize_Implementation`](#oninitialize_implementation-9) `virtual` |  |
| `void` | [`OnTickNode_Implementation`](#onticknode_implementation-15) `virtual` |  |
| `void` | [`OnPreTick`](#onpretick-2) `virtual` |  |
| `void` | [`GetPinDeclarations_Implementation`](#getpindeclarations_implementation-14) `virtual` `const` |  |
| `void` | [`DrawNodeDebug`](#drawnodedebug-7) `virtual` `const` | Called each frame when the `CCS.Debug.Viewport` CVar is enabled, for every node on the currently running camera. Override to draw world-space debug gizmos via `DrawDebugHelpers` (DrawDebugSphere, DrawDebugLine, etc.) that visualise this node's runtime state — e.g. a pivot sphere for PivotOffsetNode, a look-at line for LookAtNode, the collision trace for CollisionPushNode, a sampled spline path for SplineNode. |

---

#### OnInitialize_Implementation { #oninitialize_implementation-9 }

`virtual`

```cpp
virtual void OnInitialize_Implementation()
```

---

#### OnTickNode_Implementation { #onticknode_implementation-15 }

`virtual`

```cpp
virtual void OnTickNode_Implementation(float DeltaTime, const FComposableCameraPose & CurrentCameraPose, FComposableCameraPose & OutCameraPose)
```

---

#### OnPreTick { #onpretick-2 }

`virtual`

```cpp
virtual void OnPreTick(float DeltaTime, const FComposableCameraPose & CurrentCameraPose, FComposableCameraPose & OutCameraPose)
```

---

#### GetPinDeclarations_Implementation { #getpindeclarations_implementation-14 }

`virtual` `const`

```cpp
virtual void GetPinDeclarations_Implementation(TArray< FComposableCameraNodePinDeclaration > & OutPins) const
```

---

#### DrawNodeDebug { #drawnodedebug-7 }

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
| `TUniquePtr< TCameraInterpolator< TValueTypeWrapper< double > > >` | [`PushInterpolator_T`](#pushinterpolator_t)  |  |
| `TUniquePtr< TCameraInterpolator< TValueTypeWrapper< double > > >` | [`PullInterpolator_T`](#pullinterpolator_t)  |  |
| `USkeletalMeshComponent *` | [`SkeletalMeshComponentForPivotActor`](#skeletalmeshcomponentforpivotactor)  |  |
| `double` | [`ElapsedExemptionTime`](#elapsedexemptiontime)  |  |
| `double` | [`CurrentDistanceFromCamera`](#currentdistancefromcamera)  |  |
| `FVector` | [`OriginalCameraPosition`](#originalcameraposition)  |  |
| `FVector` | [`LastTraceStart`](#lasttracestart)  | Cache populated in FindCollisionPoint each frame so DrawNodeDebug can repaint the trace + self-collision sphere without re-running the physics queries. All fields reset to ZeroVector / false each tick. |
| `FVector` | [`LastTraceEnd`](#lasttraceend)  |  |
| `FVector` | [`LastTraceHitLocation`](#lasttracehitlocation)  |  |
| `FVector` | [`LastSelfSphereCenter`](#lastselfspherecenter)  |  |
| `bool` | [`bLastTraceBlocked`](#blasttraceblocked)  |  |

---

#### PushInterpolator_T { #pushinterpolator_t }

```cpp
TUniquePtr< TCameraInterpolator< TValueTypeWrapper< double > > > PushInterpolator_T
```

---

#### PullInterpolator_T { #pullinterpolator_t }

```cpp
TUniquePtr< TCameraInterpolator< TValueTypeWrapper< double > > > PullInterpolator_T
```

---

#### SkeletalMeshComponentForPivotActor { #skeletalmeshcomponentforpivotactor }

```cpp
USkeletalMeshComponent * SkeletalMeshComponentForPivotActor { nullptr }
```

---

#### ElapsedExemptionTime { #elapsedexemptiontime }

```cpp
double ElapsedExemptionTime { 0. }
```

---

#### CurrentDistanceFromCamera { #currentdistancefromcamera }

```cpp
double CurrentDistanceFromCamera { 0. }
```

---

#### OriginalCameraPosition { #originalcameraposition }

```cpp
FVector OriginalCameraPosition
```

---

#### LastTraceStart { #lasttracestart }

```cpp
FVector LastTraceStart { FVector::ZeroVector }
```

Cache populated in FindCollisionPoint each frame so DrawNodeDebug can repaint the trace + self-collision sphere without re-running the physics queries. All fields reset to ZeroVector / false each tick.

---

#### LastTraceEnd { #lasttraceend }

```cpp
FVector LastTraceEnd { FVector::ZeroVector }
```

---

#### LastTraceHitLocation { #lasttracehitlocation }

```cpp
FVector LastTraceHitLocation { FVector::ZeroVector }
```

---

#### LastSelfSphereCenter { #lastselfspherecenter }

```cpp
FVector LastSelfSphereCenter { FVector::ZeroVector }
```

---

#### bLastTraceBlocked { #blasttraceblocked }

```cpp
bool bLastTraceBlocked { false }
```

### Private Methods

| Return | Name | Description |
|--------|------|-------------|
| `FComposableCameraHitResult` | [`FindCollisionPoint`](#findcollisionpoint)  |  |
| `FVector` | [`StartResolveCollision`](#startresolvecollision)  |  |
| `FVector` | [`ResumeFromCollision`](#resumefromcollision)  |  |

---

#### FindCollisionPoint { #findcollisionpoint }

```cpp
FComposableCameraHitResult FindCollisionPoint(double DeltaTime, const FVector & Start, const FVector & End, const FRotator & CameraRotation)
```

---

#### StartResolveCollision { #startresolvecollision }

```cpp
FVector StartResolveCollision(double DeltaTime, const FVector & TargetLocation, const FVector & CameraPosition)
```

---

#### ResumeFromCollision { #resumefromcollision }

```cpp
FVector ResumeFromCollision(double DeltaTime, const FVector & PivotPosition, const FVector & CameraPosition)
```
