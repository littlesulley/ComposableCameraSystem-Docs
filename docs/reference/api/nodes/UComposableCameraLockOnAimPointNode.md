# UComposableCameraLockOnAimPointNode { #ucomposablecameralockonaimpointnode }

```cpp
#include <ComposableCameraLockOnAimPointNode.h>
```

> **Inherits:** [`UComposableCameraCameraNodeBase`](../uobjects-other/UComposableCameraCameraNodeBase.md#ucomposablecameracameranodebase)

Builds a per-frame virtual aim point for lock-on composition.

Intended placement:
`ScreenSpacePivot(follow) -> LockOnAimPoint -> ScreenSpacePivot(aim)`.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `EComposableCameraLockOnAimPointSource` | [`FollowSource`](#followsource) | How the player/follow point is resolved at runtime. |
| `EComposableCameraActorInputSource` | [`FollowActorSource`](#followactorsource) | Selects whether the follow actor is the controller's controlled pawn or an explicit actor. |
| `FVector` | [`FollowWorldPosition`](#followworldposition) | Follow pivot in world space. Used when FollowSource == WorldPosition. |
| `TObjectPtr< AActor >` | [`FollowActor`](#followactor) | Actor whose world location supplies the follow point. Used when FollowSource == ActorPosition. |
| `float` | [`FollowWorldUpOffset`](#followworldupoffset) | World-up offset added to FollowActor->GetActorLocation(). |
| `EComposableCameraLockOnAimPointSource` | [`AimSource`](#aimsource) | How the lock target/aim point is resolved at runtime. |
| `EComposableCameraActorInputSource` | [`AimActorSource`](#aimactorsource) | Selects whether the aim actor is the controller's controlled pawn or an explicit actor. |
| `FVector` | [`AimWorldPosition`](#aimworldposition) | Raw lock target pivot in world space. Used when AimSource == WorldPosition. |
| `TObjectPtr< AActor >` | [`AimActor`](#aimactor) | Actor whose world location supplies the raw aim point. Used when AimSource == ActorPosition. |
| `float` | [`AimWorldUpOffset`](#aimworldupoffset) | World-up offset added to AimActor->GetActorLocation(). |
| `float` | [`Radius`](#radius) | Minimum horizontal projected distance before correction activates. |
| `FVector2D` | [`PitchRange`](#pitchrange) | Min/max pitch in degrees used by the pitch-preserving term while inside Radius. |
| `float` | [`BlendOutTime`](#blendouttime) | Seconds used to fade the correction offset back to zero after leaving Radius. |
| `FVector` | [`Weights`](#weights) | Blend weights for pitch-preserving, camera-to-aim, and camera-forward additions. |

---

#### FollowSource { #followsource }

```cpp
EComposableCameraLockOnAimPointSource FollowSource { EComposableCameraLockOnAimPointSource::WorldPosition }
```

How the player/follow point is resolved at runtime.

---

#### FollowActorSource { #followactorsource }

```cpp
EComposableCameraActorInputSource FollowActorSource { EComposableCameraActorInputSource::ExplicitActor }
```

Selects whether the follow actor is the controller's controlled pawn or an explicit actor.

---

#### FollowWorldPosition { #followworldposition }

```cpp
FVector FollowWorldPosition { FVector::ZeroVector }
```

Follow pivot in world space. Used when FollowSource == WorldPosition.

---

#### FollowActor { #followactor }

```cpp
TObjectPtr< AActor > FollowActor { nullptr }
```

Actor whose world location supplies the follow point. Used when FollowSource == ActorPosition.

---

#### FollowWorldUpOffset { #followworldupoffset }

```cpp
float FollowWorldUpOffset { 0.f }
```

World-up offset added to FollowActor->GetActorLocation().

---

#### AimSource { #aimsource }

```cpp
EComposableCameraLockOnAimPointSource AimSource { EComposableCameraLockOnAimPointSource::WorldPosition }
```

How the lock target/aim point is resolved at runtime.

---

#### AimActorSource { #aimactorsource }

```cpp
EComposableCameraActorInputSource AimActorSource { EComposableCameraActorInputSource::ExplicitActor }
```

Selects whether the aim actor is the controller's controlled pawn or an explicit actor.

---

#### AimWorldPosition { #aimworldposition }

```cpp
FVector AimWorldPosition { FVector::ZeroVector }
```

Raw lock target pivot in world space. Used when AimSource == WorldPosition.

---

#### AimActor { #aimactor }

```cpp
TObjectPtr< AActor > AimActor { nullptr }
```

Actor whose world location supplies the raw aim point. Used when AimSource == ActorPosition.

---

#### AimWorldUpOffset { #aimworldupoffset }

```cpp
float AimWorldUpOffset { 0.f }
```

World-up offset added to AimActor->GetActorLocation().

---

#### Radius { #radius }

```cpp
float Radius { 500.f }
```

Minimum horizontal projected distance before correction activates.

---

#### PitchRange { #pitchrange }

```cpp
FVector2D PitchRange { -45.f, 45.f }
```

Min/max pitch in degrees used by the pitch-preserving term while inside Radius.

---

#### BlendOutTime { #blendouttime }

```cpp
float BlendOutTime { 0.15f }
```

Seconds used to fade the correction offset back to zero after leaving Radius.

---

#### Weights { #weights }

```cpp
FVector Weights { 0.2f, 0.5f, 0.3f }
```

Blend weights for pitch-preserving, camera-to-aim, and camera-forward additions.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`UComposableCameraLockOnAimPointNode`](#ucomposablecameralockonaimpointnode-1) `inline` |  |
| `void` | [`OnInitialize_Implementation`](#oninitialize_implementation) `virtual` |  |
| `void` | [`OnTickNode_Implementation`](#onticknode_implementation) `virtual` |  |
| `void` | [`GetPinDeclarations_Implementation`](#getpindeclarations_implementation) `virtual` `const` |  |
| `void` | [`DrawNodeDebug`](#drawnodedebug) `virtual` `const` | Draws the stable aim-point gizmo when viewport debug is enabled. |

---

#### UComposableCameraLockOnAimPointNode { #ucomposablecameralockonaimpointnode-1 }

`inline`

```cpp
inline UComposableCameraLockOnAimPointNode()
```

---

#### OnInitialize_Implementation { #oninitialize_implementation }

`virtual`

```cpp
virtual void OnInitialize_Implementation()
```

---

#### OnTickNode_Implementation { #onticknode_implementation }

`virtual`

```cpp
virtual void OnTickNode_Implementation(float DeltaTime, const FComposableCameraPose & CurrentCameraPose, FComposableCameraPose & OutCameraPose)
```

---

#### GetPinDeclarations_Implementation { #getpindeclarations_implementation }

`virtual` `const`

```cpp
virtual void GetPinDeclarations_Implementation(TArray< FComposableCameraNodePinDeclaration > & OutPins) const
```

---

#### DrawNodeDebug { #drawnodedebug }

`virtual` `const`

```cpp
virtual void DrawNodeDebug(FComposableCameraDebugDrawSink & Draw, bool bViewerIsOutsideCamera) const
```

Draws a blue sphere at the stable virtual aim point when `CCS.Debug.Viewport.LockOnAimPoint 1` is enabled, or when `CCS.Debug.Viewport.Nodes.All 1` enables all node gizmos. During correction and F8 eject, draws a line from the raw aim point to the corrected aim point. Compiled out in shipping builds.

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FComposableCameraLockOnAimPointState` | [`AimPointState`](#aimpointstate) | Runtime state used to retain and blend out the current correction offset. |
| `FVector` | [`LastRawAimPosition`](#lastrawaimposition) | Last raw aim point cached for non-shipping viewport debug drawing. |
| `FVector` | [`LastOutputPivotPosition`](#lastoutputpivotposition) | Last stable aim point cached for non-shipping viewport debug drawing. |
| `bool` | [`bLastAppliedCorrection`](#blastappliedcorrection) | Whether the last output differed from the raw aim point. |

