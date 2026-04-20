
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
| `TObjectPtr< AActor >` | [`PivotActor`](#pivotactor)  |  |
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
| `double` | [`PivotZOffset`](#pivotzoffset)  |  |
| `bool` | [`bUseBoneForDetection`](#busebonefordetection)  |  |
| `FName` | [`BoneName`](#bonename)  |  |

---

#### PivotActor { #pivotactor }

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

#### PivotZOffset { #pivotzoffset }

```cpp
double PivotZOffset { 50. }
```

---

#### bUseBoneForDetection { #busebonefordetection }

```cpp
bool bUseBoneForDetection { false }
```

---

#### BoneName { #bonename }

```cpp
FName BoneName
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`OnInitialize_Implementation`](#oninitialize_implementation-7) `virtual` |  |
| `void` | [`OnTickNode_Implementation`](#onticknode_implementation-13) `virtual` |  |
| `void` | [`OnPreTick`](#onpretick-2) `virtual` |  |
| `void` | [`GetPinDeclarations_Implementation`](#getpindeclarations_implementation-12) `virtual` `const` |  |

---

#### OnInitialize_Implementation { #oninitialize_implementation-7 }

`virtual`

```cpp
virtual void OnInitialize_Implementation()
```

---

#### OnTickNode_Implementation { #onticknode_implementation-13 }

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

#### GetPinDeclarations_Implementation { #getpindeclarations_implementation-12 }

`virtual` `const`

```cpp
virtual void GetPinDeclarations_Implementation(TArray< FComposableCameraNodePinDeclaration > & OutPins) const
```

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TUniquePtr< TCameraInterpolator< TValueTypeWrapper< double > > >` | [`PushInterpolator_T`](#pushinterpolator_t)  |  |
| `TUniquePtr< TCameraInterpolator< TValueTypeWrapper< double > > >` | [`PullInterpolator_T`](#pullinterpolator_t)  |  |
| `USkeletalMeshComponent *` | [`SkeletalMeshComponentForPivotActor`](#skeletalmeshcomponentforpivotactor)  |  |
| `double` | [`ElapsedExemptionTime`](#elapsedexemptiontime)  |  |
| `double` | [`CurrentDistanceFromCamera`](#currentdistancefromcamera)  |  |
| `FVector` | [`OriginalCameraPosition`](#originalcameraposition)  |  |

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
