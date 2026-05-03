
# UComposableCameraOcclusionFadeNode { #ucomposablecameraocclusionfadenode }

```cpp
#include <ComposableCameraOcclusionFadeNode.h>
```

> **Inherits:** [`UComposableCameraCameraNodeBase`](../uobjects-other/UComposableCameraCameraNodeBase.md#ucomposablecameracameranodebase)

Fades objects between the camera and a target actor (or near the camera) by replacing their materials with a user-supplied transparency material.

Two independent detection paths feed the same material-swap pipeline:

A. **Line-of-sight occlusion** (bFadeOccluders). Async multi-sphere sweep from the camera to the target each frame; every primitive hit that passes the tag / mesh-type filters is fade-marked.

B. **Proximity fade** (bFadeNearbyActors). Sphere overlap at the camera position each frame; every actor of class ProximityActorClass within ProximityRadius has its fade-eligible components fade-marked.

Both paths produce a union set of primitives to fade this frame. Delta tracking against AppliedMaterialOverrides means we only call SetMaterial / CreateDynamicMaterialInstance on primitives entering or leaving the set — the steady state is zero per-frame material work.

Fade shape and timing are entirely encoded in OcclusionMaterial's shader (dither, fresnel, Time-driven opacity — your call). The node does instant material swaps; any smooth cross-fade lives in the shader. This follows Epic's UOcclusionMaterialCameraNode design: no material contract beyond "point at the occlusion material asset".

Lifecycle:

* OnInitialize seeds state and restores any stale overrides.

* OnTickNode runs both detection paths and applies the delta.

* BeginDestroy restores every remaining override — mandatory to avoid leaving actors stuck in the transparency material after the camera is popped / destroyed.

The sweep path uses the async trace API (submit frame N, consume frame N+1). Occluder decisions lag by one frame, which is visually acceptable and keeps the game thread off the physics query's critical path.

StaticMeshComponent-only is NOT enforced — unlike Epic's node, we consider any UPrimitiveComponent subclass (static mesh, skeletal mesh, instanced, geometry collection) subject to bAffectStaticMeshes / bAffectSkeletalMeshes.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TObjectPtr< AActor >` | [`PivotActor`](#pivotactor-5)  | Actor whose location (plus PivotZOffset, or bone socket) is the "protected end" of the line-of-sight sweep and the hit-test anchor for proximity fade. Typically the player pawn. Must be non-null when bFadeOccluders is true; otherwise the sweep is skipped with a warning. |
| `float` | [`PivotZOffset`](#pivotzoffset-3)  | World-Z offset added on top of the actor location when bUseBoneForDetection is false (or the requested bone can't be found). Typically ~50 to raise the target from foot to chest so the sweep line doesn't graze the floor. |
| `bool` | [`bUseBoneForDetection`](#busebonefordetection-3)  | When true, the target point is the named bone's world location on the actor's skeletal mesh (if present and the bone resolves). Falls back to ActorLocation + PivotZOffset on any failure. |
| `FName` | [`BoneName`](#bonename-4)  | Bone / socket name sampled on the actor's skeletal mesh when bUseBoneForDetection is true. |
| `TObjectPtr< UMaterialInterface >` | [`OcclusionMaterial`](#occlusionmaterial)  | Transparency material swapped onto every faded primitive's material slots. The shader inside this material owns the fade look — dither, fresnel, opacity — and any smooth fade-in/out animation. Must be set or the node no-ops. |
| `bool` | [`bAffectStaticMeshes`](#baffectstaticmeshes)  | Whether static mesh components are eligible for fade. |
| `bool` | [`bAffectSkeletalMeshes`](#baffectskeletalmeshes)  | Whether skeletal mesh components are eligible for fade. Enabled by default — Epic's node misses this, but NPCs / characters blocking the view are one of the most common fade cases. |
| `TArray< TObjectPtr< AActor > >` | [`ExtraIgnoredActors`](#extraignoredactors)  | Extra actors to exclude from both the sweep and the proximity query. PivotActor is ignored automatically — this list is for teammates, companions, vehicles, or any other actor that must not fade. |
| `bool` | [`bFadeOccluders`](#bfadeoccluders)  | Master switch for line-of-sight occlusion detection. |
| `TEnumAsByte< ECollisionChannel >` | [`OcclusionChannel`](#occlusionchannel)  | Collision channel used by the async sphere sweep from camera to target. |
| `float` | [`OcclusionSphereRadius`](#occlusionsphereradius)  | Radius of the sweep sphere in world units. Widen for short/thin occluders that a thin line trace would miss. |
| `FName` | [`OccluderComponentTag`](#occludercomponenttag)  | Optional component-tag filter. When NAME_None (default), every primitive the sweep hits is eligible (same behaviour as Epic's node, where collision channel alone decides). When non-empty, only components carrying this tag via UActorComponent::ComponentTags are considered — the usual way to say "walls on ECC_Camera stay solid, tagged foliage |
| `bool` | [`bFadeNearbyActors`](#bfadenearbyactors)  | Master switch for proximity-based fade. |
| `float` | [`ProximityRadius`](#proximityradius)  | Radius of the proximity overlap centred at the camera location. Actors of class ProximityActorClass whose bounding shape intersects this sphere are fade-marked. |
| `TSubclassOf< AActor >` | [`ProximityActorClass`](#proximityactorclass)  | Actor class filter for proximity fade. Null = treat as APawn. Use a narrower class (e.g. a game-specific ACharacter subclass) to exclude vehicles / AI turrets / etc. |
| `bool` | [`bIgnorePivotActorInProximity`](#bignorepivotactorinproximity)  | When true, PivotActor is excluded from proximity fade even if it lies within ProximityRadius. Defaults to false — the typical "fade the |

---

#### PivotActor { #pivotactor-5 }

```cpp
TObjectPtr< AActor > PivotActor { nullptr }
```

Actor whose location (plus PivotZOffset, or bone socket) is the "protected end" of the line-of-sight sweep and the hit-test anchor for proximity fade. Typically the player pawn. Must be non-null when bFadeOccluders is true; otherwise the sweep is skipped with a warning.

---

#### PivotZOffset { #pivotzoffset-3 }

```cpp
float PivotZOffset { 50.f }
```

World-Z offset added on top of the actor location when bUseBoneForDetection is false (or the requested bone can't be found). Typically ~50 to raise the target from foot to chest so the sweep line doesn't graze the floor.

---

#### bUseBoneForDetection { #busebonefordetection-3 }

```cpp
bool bUseBoneForDetection { false }
```

When true, the target point is the named bone's world location on the actor's skeletal mesh (if present and the bone resolves). Falls back to ActorLocation + PivotZOffset on any failure.

---

#### BoneName { #bonename-4 }

```cpp
FName BoneName
```

Bone / socket name sampled on the actor's skeletal mesh when bUseBoneForDetection is true.

---

#### OcclusionMaterial { #occlusionmaterial }

```cpp
TObjectPtr< UMaterialInterface > OcclusionMaterial { nullptr }
```

Transparency material swapped onto every faded primitive's material slots. The shader inside this material owns the fade look — dither, fresnel, opacity — and any smooth fade-in/out animation. Must be set or the node no-ops.

---

#### bAffectStaticMeshes { #baffectstaticmeshes }

```cpp
bool bAffectStaticMeshes { true }
```

Whether static mesh components are eligible for fade.

---

#### bAffectSkeletalMeshes { #baffectskeletalmeshes }

```cpp
bool bAffectSkeletalMeshes { true }
```

Whether skeletal mesh components are eligible for fade. Enabled by default — Epic's node misses this, but NPCs / characters blocking the view are one of the most common fade cases.

---

#### ExtraIgnoredActors { #extraignoredactors }

```cpp
TArray< TObjectPtr< AActor > > ExtraIgnoredActors
```

Extra actors to exclude from both the sweep and the proximity query. PivotActor is ignored automatically — this list is for teammates, companions, vehicles, or any other actor that must not fade.

---

#### bFadeOccluders { #bfadeoccluders }

```cpp
bool bFadeOccluders { true }
```

Master switch for line-of-sight occlusion detection.

---

#### OcclusionChannel { #occlusionchannel }

```cpp
TEnumAsByte< ECollisionChannel > OcclusionChannel { ECC_Camera }
```

Collision channel used by the async sphere sweep from camera to target.

---

#### OcclusionSphereRadius { #occlusionsphereradius }

```cpp
float OcclusionSphereRadius { 10.f }
```

Radius of the sweep sphere in world units. Widen for short/thin occluders that a thin line trace would miss.

---

#### OccluderComponentTag { #occludercomponenttag }

```cpp
FName OccluderComponentTag
```

Optional component-tag filter. When NAME_None (default), every primitive the sweep hits is eligible (same behaviour as Epic's node, where collision channel alone decides). When non-empty, only components carrying this tag via UActorComponent::ComponentTags are considered — the usual way to say "walls on ECC_Camera stay solid, tagged foliage
fades".

---

#### bFadeNearbyActors { #bfadenearbyactors }

```cpp
bool bFadeNearbyActors { true }
```

Master switch for proximity-based fade.

---

#### ProximityRadius { #proximityradius }

```cpp
float ProximityRadius { 100.f }
```

Radius of the proximity overlap centred at the camera location. Actors of class ProximityActorClass whose bounding shape intersects this sphere are fade-marked.

---

#### ProximityActorClass { #proximityactorclass }

```cpp
TSubclassOf< AActor > ProximityActorClass
```

Actor class filter for proximity fade. Null = treat as APawn. Use a narrower class (e.g. a game-specific ACharacter subclass) to exclude vehicles / AI turrets / etc.

---

#### bIgnorePivotActorInProximity { #bignorepivotactorinproximity }

```cpp
bool bIgnorePivotActorInProximity { false }
```

When true, PivotActor is excluded from proximity fade even if it lies within ProximityRadius. Defaults to false — the typical "fade the
player when camera vision gets too close" pattern wants PivotActor included. Flip on for cameras where the player body must never disappear (cinematic, over-shoulder with forced full-body view).

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`UComposableCameraOcclusionFadeNode`](#ucomposablecameraocclusionfadenode-1) `inline` |  |
| `void` | [`OnInitialize_Implementation`](#oninitialize_implementation-13) `virtual` |  |
| `void` | [`OnTickNode_Implementation`](#onticknode_implementation-19) `virtual` |  |
| `void` | [`GetPinDeclarations_Implementation`](#getpindeclarations_implementation-18) `virtual` `const` |  |
| `void` | [`BeginDestroy`](#begindestroy-1) `virtual` |  |
| `void` | [`DrawNodeDebug`](#drawnodedebug-9) `virtual` `const` | Called each frame when the `CCS.Debug.Viewport` CVar is enabled, for every node on the currently running camera. Override to draw world-space debug gizmos via `DrawDebugHelpers` (DrawDebugSphere, DrawDebugLine, etc.) that visualise this node's runtime state — e.g. a pivot sphere for PivotOffsetNode, a look-at line for LookAtNode, the collision trace for CollisionPushNode, a sampled spline path for SplineNode. |

---

#### UComposableCameraOcclusionFadeNode { #ucomposablecameraocclusionfadenode-1 }

`inline`

```cpp
inline UComposableCameraOcclusionFadeNode()
```

---

#### OnInitialize_Implementation { #oninitialize_implementation-13 }

`virtual`

```cpp
virtual void OnInitialize_Implementation()
```

---

#### OnTickNode_Implementation { #onticknode_implementation-19 }

`virtual`

```cpp
virtual void OnTickNode_Implementation(float DeltaTime, const FComposableCameraPose & CurrentCameraPose, FComposableCameraPose & OutCameraPose)
```

---

#### GetPinDeclarations_Implementation { #getpindeclarations_implementation-18 }

`virtual` `const`

```cpp
virtual void GetPinDeclarations_Implementation(TArray< FComposableCameraNodePinDeclaration > & OutPins) const
```

---

#### BeginDestroy { #begindestroy-1 }

`virtual`

```cpp
virtual void BeginDestroy()
```

---

#### DrawNodeDebug { #drawnodedebug-9 }

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
| `TArray< FComposableCameraOcclusionMaterialOverride >` | [`AppliedMaterialOverrides`](#appliedmaterialoverrides)  | Persistent record of every primitive we've swapped a material on. The struct pins the original materials via UPROPERTY TObjectPtr so GC doesn't collect them while we hold them. Pruned each tick for stale weak refs (actor destroyed) and for components leaving the faded set. |
| `FTraceHandle` | [`PendingSweepHandle`](#pendingsweephandle)  | Async trace handle for the sweep submitted last frame and consumed this frame. Invalidated after each successful read. |
| `FVector` | [`LastResolvedTargetPoint`](#lastresolvedtargetpoint)  | Cached target point resolved this tick — used both by the sweep submit and by debug draw. |
| `FVector` | [`LastCameraPosition`](#lastcameraposition)  | Cached camera position resolved this tick — same reason. |
| `FVector` | [`DebugSweepStart`](#debugsweepstart)  | Frame-snapshot of the sweep endpoints and proximity sphere, written by OnTickNode and read by DrawNodeDebug. |
| `FVector` | [`DebugSweepEnd`](#debugsweepend)  |  |
| `bool` | [`bDebugSweepSubmittedThisTick`](#bdebugsweepsubmittedthistick)  |  |

---

#### AppliedMaterialOverrides { #appliedmaterialoverrides }

```cpp
TArray< FComposableCameraOcclusionMaterialOverride > AppliedMaterialOverrides
```

Persistent record of every primitive we've swapped a material on. The struct pins the original materials via UPROPERTY TObjectPtr so GC doesn't collect them while we hold them. Pruned each tick for stale weak refs (actor destroyed) and for components leaving the faded set.

---

#### PendingSweepHandle { #pendingsweephandle }

```cpp
FTraceHandle PendingSweepHandle
```

Async trace handle for the sweep submitted last frame and consumed this frame. Invalidated after each successful read.

---

#### LastResolvedTargetPoint { #lastresolvedtargetpoint }

```cpp
FVector LastResolvedTargetPoint { FVector::ZeroVector }
```

Cached target point resolved this tick — used both by the sweep submit and by debug draw.

---

#### LastCameraPosition { #lastcameraposition }

```cpp
FVector LastCameraPosition { FVector::ZeroVector }
```

Cached camera position resolved this tick — same reason.

---

#### DebugSweepStart { #debugsweepstart }

```cpp
FVector DebugSweepStart { FVector::ZeroVector }
```

Frame-snapshot of the sweep endpoints and proximity sphere, written by OnTickNode and read by DrawNodeDebug.

---

#### DebugSweepEnd { #debugsweepend }

```cpp
FVector DebugSweepEnd { FVector::ZeroVector }
```

---

#### bDebugSweepSubmittedThisTick { #bdebugsweepsubmittedthistick }

```cpp
bool bDebugSweepSubmittedThisTick { false }
```

### Private Methods

| Return | Name | Description |
|--------|------|-------------|
| `bool` | [`ResolveTargetPoint`](#resolvetargetpoint-2) `const` | Resolve the target world location from PivotActor + BoneName / PivotZOffset. Returns false when PivotActor is null. |
| `void` | [`ConsumePendingSweep`](#consumependingsweep)  | Consume the result of a sweep submitted on a previous frame (if any) and insert its hits into OutFadableComponents after filtering. |
| `void` | [`SubmitOcclusionSweep`](#submitocclusionsweep)  | Submit a fresh async sphere sweep from camera to target. Handle stored in PendingSweepHandle for next frame's consume. |
| `void` | [`RunProximityQuery`](#runproximityquery) `const` | Run the synchronous proximity overlap at the camera position, collect all fadable components on matching actors into OutFadableComponents. |
| `bool` | [`PassesFadeFilters`](#passesfadefilters) `const` | Whether this primitive passes the mesh-type + component-tag filters. OccluderContext toggles the component-tag check (proximity fade does not use it; only the sweep path does). |
| `void` | [`CollectFadableComponentsOnActor`](#collectfadablecomponentsonactor) `const` | Gather every UPrimitiveComponent on Actor that passes the mesh-type filter into Out. The component-tag filter is deliberately skipped — it's sweep-only. |
| `void` | [`ApplyOcclusionMaterial`](#applyocclusionmaterial)  | Apply the occlusion material to every slot on Component, recording originals in AppliedMaterialOverrides. No-op if Component is already recorded. |
| `void` | [`RestoreAndRemoveOverrideAt`](#restoreandremoveoverrideat)  | Restore originals and remove the record at AppliedMaterialOverrides[Index]. Index must be valid; caller is responsible. The array is RemoveAtSwap'd so Index becomes invalid after the call — iterate backwards when removing many. |
| `void` | [`RestoreAllOverrides`](#restorealloverrides)  | Restore every currently-tracked override. Called from BeginDestroy and from OnInitialize (in case a re-activated node inherited stale state). |

---

#### ResolveTargetPoint { #resolvetargetpoint-2 }

`const`

```cpp
bool ResolveTargetPoint(FVector & OutTargetPoint) const
```

Resolve the target world location from PivotActor + BoneName / PivotZOffset. Returns false when PivotActor is null.

---

#### ConsumePendingSweep { #consumependingsweep }

```cpp
void ConsumePendingSweep(UWorld * World, TSet< UPrimitiveComponent * > & OutFadableComponents)
```

Consume the result of a sweep submitted on a previous frame (if any) and insert its hits into OutFadableComponents after filtering.

---

#### SubmitOcclusionSweep { #submitocclusionsweep }

```cpp
void SubmitOcclusionSweep(UWorld * World, const FVector & CameraPos, const FVector & TargetPos)
```

Submit a fresh async sphere sweep from camera to target. Handle stored in PendingSweepHandle for next frame's consume.

---

#### RunProximityQuery { #runproximityquery }

`const`

```cpp
void RunProximityQuery(UWorld * World, const FVector & CameraPos, TSet< UPrimitiveComponent * > & OutFadableComponents) const
```

Run the synchronous proximity overlap at the camera position, collect all fadable components on matching actors into OutFadableComponents.

---

#### PassesFadeFilters { #passesfadefilters }

`const`

```cpp
bool PassesFadeFilters(UPrimitiveComponent * Component, bool bApplyOccluderTagFilter) const
```

Whether this primitive passes the mesh-type + component-tag filters. OccluderContext toggles the component-tag check (proximity fade does not use it; only the sweep path does).

---

#### CollectFadableComponentsOnActor { #collectfadablecomponentsonactor }

`const`

```cpp
void CollectFadableComponentsOnActor(AActor * Actor, TSet< UPrimitiveComponent * > & Out) const
```

Gather every UPrimitiveComponent on Actor that passes the mesh-type filter into Out. The component-tag filter is deliberately skipped — it's sweep-only.

---

#### ApplyOcclusionMaterial { #applyocclusionmaterial }

```cpp
void ApplyOcclusionMaterial(UPrimitiveComponent * Component)
```

Apply the occlusion material to every slot on Component, recording originals in AppliedMaterialOverrides. No-op if Component is already recorded.

---

#### RestoreAndRemoveOverrideAt { #restoreandremoveoverrideat }

```cpp
void RestoreAndRemoveOverrideAt(int32 Index)
```

Restore originals and remove the record at AppliedMaterialOverrides[Index]. Index must be valid; caller is responsible. The array is RemoveAtSwap'd so Index becomes invalid after the call — iterate backwards when removing many.

---

#### RestoreAllOverrides { #restorealloverrides }

```cpp
void RestoreAllOverrides()
```

Restore every currently-tracked override. Called from BeginDestroy and from OnInitialize (in case a re-activated node inherited stale state).
