# UComposableCameraPivotLookAheadNode { #ucomposablecamerapivotlookaheadnode }

```cpp
#include <ComposableCameraPivotLookAheadNode.h>
```

> **Inherits:** [`UComposableCameraCameraNodeBase`](../uobjects-other/UComposableCameraCameraNodeBase.md#ucomposablecameracameranodebase)

Projects a pivot position forward by a velocity-derived look-ahead offset.

Intended placement:
`ReceivePivotActor -> PivotLookAhead -> PivotOffset / ScreenSpacePivot -> LookAt -> CameraOffset`.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FVector` | [`PivotPosition`](#pivotposition)  | Pivot position to project. Usually wired from ReceivePivotActor or another pivot-producing node. |
| `EComposableCameraActorInputSource` | [`VelocityActorSource`](#velocityactorsource)  | Selects whether VelocityActor comes from the controlled pawn or an explicit actor. |
| `TObjectPtr< AActor >` | [`VelocityActor`](#velocityactor)  | Actor whose velocity drives look-ahead. If unresolved, the node falls back to frame-to-frame PivotPosition velocity. |
| `float` | [`LookAheadTime`](#lookaheadtime)  | Seconds into the future to project PivotPosition using the resolved velocity. |
| `float` | [`VelocityDampingTime`](#velocitydampingtime)  | Time used to damp velocity changes. Set to 0 for immediate velocity response. |

---

#### PivotPosition { #pivotposition }

```cpp
FVector PivotPosition { FVector::ZeroVector }
```

Pivot position to project. Usually wired from ReceivePivotActor or another pivot-producing node.

---

#### VelocityActorSource { #velocityactorsource }

```cpp
EComposableCameraActorInputSource VelocityActorSource { EComposableCameraActorInputSource::ExplicitActor }
```

Selects whether VelocityActor comes from the controlled pawn or an explicit actor.

---

#### VelocityActor { #velocityactor }

```cpp
TObjectPtr< AActor > VelocityActor { nullptr }
```

Actor whose velocity drives look-ahead. If unresolved, the node falls back to frame-to-frame PivotPosition velocity.

---

#### LookAheadTime { #lookaheadtime }

```cpp
float LookAheadTime { 0.f }
```

Seconds into the future to project PivotPosition using the resolved velocity.

---

#### VelocityDampingTime { #velocitydampingtime }

```cpp
float VelocityDampingTime { 0.f }
```

Time used to damp velocity changes. Set to 0 for immediate velocity response.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`UComposableCameraPivotLookAheadNode`](#ucomposablecamerapivotlookaheadnode-1) `inline` |  |
| `void` | [`OnInitialize_Implementation`](#oninitialize_implementation) `virtual` |  |
| `void` | [`OnFirstTickNode_Implementation`](#onfirstticknode_implementation) `virtual` |  |
| `void` | [`OnTickNode_Implementation`](#onticknode_implementation) `virtual` |  |
| `void` | [`GetPinDeclarations_Implementation`](#getpindeclarations_implementation) `virtual` `const` |  |
| `void` | [`DrawNodeDebug`](#drawnodedebug) `virtual` `const` | Called each frame when the `CCS.Debug.Viewport` CVar is enabled, for every node on the currently running camera. |

---

#### UComposableCameraPivotLookAheadNode { #ucomposablecamerapivotlookaheadnode-1 }

`inline`

```cpp
inline UComposableCameraPivotLookAheadNode()
```

---

#### OnInitialize_Implementation { #oninitialize_implementation }

`virtual`

```cpp
virtual void OnInitialize_Implementation()
```

---

#### OnFirstTickNode_Implementation { #onfirstticknode_implementation }

`virtual`

```cpp
virtual void OnFirstTickNode_Implementation()
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

Draws an orange sphere at the predicted pivot when `CCS.Debug.Viewport.PivotLookAhead 1` is enabled, or when `CCS.Debug.Viewport.Nodes.All 1` enables all node gizmos. Compiled out in shipping builds.

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FVector` | [`LastPivotPosition`](#lastpivotposition)  |  |
| `FVector` | [`SmoothedVelocity`](#smoothedvelocity)  |  |
| `FVector` | [`VelocitySmoothingVelocity`](#velocitysmoothingvelocity)  |  |
| `bool` | [`bHasLastPivotPosition`](#bhaslastpivotposition)  |  |
| `FVector` | [`LastOutputPivotPosition`](#lastoutputpivotposition)  | Last predicted pivot cached for non-shipping viewport debug drawing. |

---

#### LastPivotPosition { #lastpivotposition }

```cpp
FVector LastPivotPosition { FVector::ZeroVector }
```

---

#### SmoothedVelocity { #smoothedvelocity }

```cpp
FVector SmoothedVelocity { FVector::ZeroVector }
```

---

#### VelocitySmoothingVelocity { #velocitysmoothingvelocity }

```cpp
FVector VelocitySmoothingVelocity { FVector::ZeroVector }
```

---

#### bHasLastPivotPosition { #bhaslastpivotposition }

```cpp
bool bHasLastPivotPosition { false }
```

---

#### LastOutputPivotPosition { #lastoutputpivotposition }

```cpp
FVector LastOutputPivotPosition { FVector::ZeroVector }
```

Last predicted pivot cached for non-shipping viewport debug drawing.
