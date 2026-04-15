
# UComposableCameraDynamicDeocclusionTransition { #ucomposablecameradynamicdeocclusiontransition }

```cpp
#include <ComposableCameraDynamicDeocclusionTransition.h>
```

> **Inherits:** [`UComposableCameraTransitionBase`](UComposableCameraTransitionBase.md#ucomposablecameratransitionbase)

A dynamically deocclusive transition.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `UComposableCameraTransitionBase *` | [`DrivingTransition`](#drivingtransition-1)  |  |
| `TArray< FComposableCameraRayFeeler >` | [`Feelers`](#feelers)  |  |
| `TEnumAsByte< ETraceTypeQuery >` | [`TraceChannel`](#tracechannel)  |  |
| `TArray< TSoftClassPtr< AActor > >` | [`ActorTypesToIgnore`](#actortypestoignore-1)  |  |
| `float` | [`DeocclusionSpeed`](#deocclusionspeed)  |  |
| `float` | [`ResumeWaitingTime`](#resumewaitingtime)  |  |
| `float` | [`DeadPercentage`](#deadpercentage)  |  |
| `float` | [`ResumeSpeed`](#resumespeed)  |  |

---

#### DrivingTransition { #drivingtransition-1 }

```cpp
UComposableCameraTransitionBase * DrivingTransition
```

---

#### Feelers { #feelers }

```cpp
TArray< FComposableCameraRayFeeler > Feelers
```

---

#### TraceChannel { #tracechannel }

```cpp
TEnumAsByte< ETraceTypeQuery > TraceChannel
```

---

#### ActorTypesToIgnore { #actortypestoignore-1 }

```cpp
TArray< TSoftClassPtr< AActor > > ActorTypesToIgnore
```

---

#### DeocclusionSpeed { #deocclusionspeed }

```cpp
float DeocclusionSpeed { 1.f }
```

---

#### ResumeWaitingTime { #resumewaitingtime }

```cpp
float ResumeWaitingTime { 0.2f }
```

---

#### DeadPercentage { #deadpercentage }

```cpp
float DeadPercentage { 0.8f }
```

---

#### ResumeSpeed { #resumespeed }

```cpp
float ResumeSpeed { 0.8f }
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`OnBeginPlay_Implementation`](#onbeginplay_implementation-5) `virtual` |  |
| `FComposableCameraPose` | [`OnEvaluate_Implementation`](#onevaluate_implementation-9) `virtual` |  |

---

#### OnBeginPlay_Implementation { #onbeginplay_implementation-5 }

`virtual`

```cpp
virtual void OnBeginPlay_Implementation(float DeltaTime, const FComposableCameraPose & CurrentSourcePose, const FComposableCameraPose & CurrentTargetPose)
```

---

#### OnEvaluate_Implementation { #onevaluate_implementation-9 }

`virtual`

```cpp
virtual FComposableCameraPose OnEvaluate_Implementation(float DeltaTime, const FComposableCameraPose & CurrentSourcePose, const FComposableCameraPose & CurrentTargetPose)
```

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FVector` | [`PreviousOffset`](#previousoffset)  |  |
| `float` | [`ElapsedWaitingTime`](#elapsedwaitingtime)  |  |
| `TArray< AActor * >` | [`ActorsToIgnore`](#actorstoignore)  |  |
| `EDrawDebugTrace::Type` | [`DrawDebugType`](#drawdebugtype)  |  |

---

#### PreviousOffset { #previousoffset }

```cpp
FVector PreviousOffset { FVector::ZeroVector }
```

---

#### ElapsedWaitingTime { #elapsedwaitingtime }

```cpp
float ElapsedWaitingTime { 0.f }
```

---

#### ActorsToIgnore { #actorstoignore }

```cpp
TArray< AActor * > ActorsToIgnore
```

---

#### DrawDebugType { #drawdebugtype }

```cpp
EDrawDebugTrace::Type DrawDebugType
```
