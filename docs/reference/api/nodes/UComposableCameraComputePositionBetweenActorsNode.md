# UComposableCameraComputePositionBetweenActorsNode { #ucomposablecameracomputepositionbetweenactorsnode }

```cpp
#include <ComposableCameraComputePositionBetweenActorsNode.h>
```

> **Inherits:** [`UComposableCameraComputeNodeBase`](../uobjects-other/UComposableCameraComputeNodeBase.md#ucomposablecameracomputenodebase)

Computes one activation-time world position between two resolved actors.

Position = `Lerp(FirstActor.Location, SecondActor.Location, Alpha) + WorldZ(HeightOffset)`.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `EComposableCameraActorInputSource` | [`FirstActorSource`](#firstactorsource) | Selects whether FirstActor comes from an explicit actor or the controller's controlled pawn. |
| `TObjectPtr< AActor >` | [`FirstActor`](#firstactor) | Explicit first actor. Used when FirstActorSource is ExplicitActor. |
| `EComposableCameraActorInputSource` | [`SecondActorSource`](#secondactorsource) | Selects whether SecondActor comes from an explicit actor or the controller's controlled pawn. |
| `TObjectPtr< AActor >` | [`SecondActor`](#secondactor) | Explicit second actor. Used when SecondActorSource is ExplicitActor. |
| `float` | [`Alpha`](#alpha) | Normalized position between first actor (0) and second actor (1). |
| `float` | [`HeightOffset`](#heightoffset) | World-Z offset applied after interpolation. |

---

#### FirstActorSource { #firstactorsource }

```cpp
EComposableCameraActorInputSource FirstActorSource { EComposableCameraActorInputSource::ExplicitActor }
```

Selects whether FirstActor comes from an explicit actor or the controller's controlled pawn.

---

#### FirstActor { #firstactor }

```cpp
TObjectPtr< AActor > FirstActor { nullptr }
```

Explicit first actor. Used when FirstActorSource is ExplicitActor.

---

#### SecondActorSource { #secondactorsource }

```cpp
EComposableCameraActorInputSource SecondActorSource { EComposableCameraActorInputSource::ExplicitActor }
```

Selects whether SecondActor comes from an explicit actor or the controller's controlled pawn.

---

#### SecondActor { #secondactor }

```cpp
TObjectPtr< AActor > SecondActor { nullptr }
```

Explicit second actor. Used when SecondActorSource is ExplicitActor.

---

#### Alpha { #alpha }

```cpp
float Alpha { 0.5f }
```

Normalized position between first actor (0) and second actor (1).

---

#### HeightOffset { #heightoffset }

```cpp
float HeightOffset { 0.f }
```

World-Z offset applied after interpolation.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`UComposableCameraComputePositionBetweenActorsNode`](#ucomposablecameracomputepositionbetweenactorsnode-1) `inline` |  |
| `void` | [`ExecuteBeginPlay`](#executebeginplay) `virtual` | Execute this compute node's one-shot work. |
| `void` | [`GetPinDeclarations_Implementation`](#getpindeclarations_implementation) `virtual` `const` |  |

---

#### UComposableCameraComputePositionBetweenActorsNode { #ucomposablecameracomputepositionbetweenactorsnode-1 }

`inline`

```cpp
inline UComposableCameraComputePositionBetweenActorsNode()
```

---

#### ExecuteBeginPlay { #executebeginplay }

`virtual`

```cpp
virtual void ExecuteBeginPlay()
```

Execute this compute node's one-shot work.

Resolves the two actor endpoints, writes the interpolated `Position` output pin when both are valid, and outputs zero with a warning when either endpoint is missing.

---

#### GetPinDeclarations_Implementation { #getpindeclarations_implementation }

`virtual` `const`

```cpp
virtual void GetPinDeclarations_Implementation(TArray< FComposableCameraNodePinDeclaration > & OutPins) const
```
