
# UComposableCameraComputeRandomOffsetNode { #ucomposablecameracomputerandomoffsetnode }

```cpp
#include <ComposableCameraComputeRandomOffsetNode.h>
```

> **Inherits:** [`UComposableCameraComputeNodeBase`](../uobjects-other/UComposableCameraComputeNodeBase.md#ucomposablecameracomputenodebase)

Example compute node: generates a random offset vector at camera activation and publishes it as an output pin.

Typical use case: spawn-time camera shake seed, randomized starting position jitter, or any one-shot random value that downstream camera nodes consume every frame but that should remain stable across the camera's lifetime.

The random offset is generated once in ExecuteBeginPlay and written to the "RandomOffset" output pin. Downstream camera nodes (e.g. PivotOffset, CameraOffset) can wire this into their input pins to apply the offset every frame.

Inputs:

* MinOffset (Vector3D): minimum bound for each axis (default -50, -50, -50)

* MaxOffset (Vector3D): maximum bound for each axis (default 50, 50, 50)

Outputs:

* RandomOffset (Vector3D): the generated random vector, stable for the camera's lifetime

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FVector` | [`MinOffset`](#minoffset)  | Minimum bound for each axis of the random offset. |
| `FVector` | [`MaxOffset`](#maxoffset)  | Maximum bound for each axis of the random offset. |

---

#### MinOffset { #minoffset }

```cpp
FVector MinOffset = FVector(-50.0, -50.0, -50.0)
```

Minimum bound for each axis of the random offset.

---

#### MaxOffset { #maxoffset }

```cpp
FVector MaxOffset = FVector(50.0, 50.0, 50.0)
```

Maximum bound for each axis of the random offset.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`ExecuteBeginPlay`](#executebeginplay-1) `virtual` | Execute this compute node's one-shot work. |
| `void` | [`GetPinDeclarations_Implementation`](#getpindeclarations_implementation-18) `virtual` `const` |  |

---

#### ExecuteBeginPlay { #executebeginplay-1 }

`virtual`

```cpp
virtual void ExecuteBeginPlay()
```

Execute this compute node's one-shot work.

Called from [AComposableCameraCameraBase::BeginPlayCamera](../actors/AComposableCameraCameraBase.md#beginplaycamera), after every node on the camera (both camera nodes and compute nodes) has already had [Initialize()](../uobjects-other/UComposableCameraCameraNodeBase.md#initialize-1) / [OnInitialize_Implementation()](../uobjects-other/UComposableCameraCameraNodeBase.md#oninitialize_implementation-3) run. By the time this fires, OwningCamera / OwningPlayerCameraManager / RuntimeDataBlock are all wired, so GetInputPinValue / SetOutputPinValue / Get/SetInternalVariable are all safe to use.

The outgoing camera pose (the pose the previous camera was evaluating before this one became active) is available via OwningPlayerCameraManager->GetCurrentCameraPose() — this is the same value AActor::BeginPlay used to pass into BeginPlayCamera as a parameter before Step 4a removed that argument.

Plain virtual (not a BlueprintNativeEvent) for 4a. If Blueprint authoring of compute nodes becomes a requirement later, promote this to a BlueprintNativeEvent following the same OnFoo / OnFoo_Implementation pattern used by OnInitialize and OnTickNode on the parent class.

---

#### GetPinDeclarations_Implementation { #getpindeclarations_implementation-18 }

`virtual` `const`

```cpp
virtual void GetPinDeclarations_Implementation(TArray< FComposableCameraNodePinDeclaration > & OutPins) const
```
