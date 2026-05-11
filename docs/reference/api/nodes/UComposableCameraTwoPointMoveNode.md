# UComposableCameraTwoPointMoveNode { #ucomposablecameratwopointmovenode }

```cpp
#include <ComposableCameraTwoPointMoveNode.h>
```

> **Inherits:** `UComposableCameraCameraNodeBase`

Moves the camera from `SourceTransform` to `TargetTransform` over `Duration`.

The node resets its internal elapsed time on initialization. Each tick it computes normalized time, samples `Curve` when present, clamps the sampled alpha to `[0, 1]`, linearly interpolates position, and spherically interpolates rotation. If `Duration` is zero, the target transform is used immediately.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FTransform` | [`SourceTransform`](#sourcetransform) | Transform used at normalized time 0. |
| `FTransform` | [`TargetTransform`](#targettransform) | Transform used at normalized time 1 and held after `Duration`. |
| `TObjectPtr< UCurveFloat >` | [`Curve`](#curve) | Optional float curve sampled with X in `[0, 1]`; the returned value is clamped to `[0, 1]` and used as interpolation alpha. |
| `float` | [`Duration`](#duration) | Seconds spent moving from `SourceTransform` to `TargetTransform`. |

---

#### SourceTransform { #sourcetransform }

```cpp
FTransform SourceTransform { FTransform::Identity }
```

Transform used at normalized time 0.

---

#### TargetTransform { #targettransform }

```cpp
FTransform TargetTransform { FTransform::Identity }
```

Transform used at normalized time 1, and held after `Duration`.

---

#### Curve { #curve }

```cpp
TObjectPtr< UCurveFloat > Curve { nullptr }
```

Curve sampled with X in `[0, 1]`. The returned value is clamped to `[0, 1]`.

---

#### Duration { #duration }

```cpp
float Duration { 1.f }
```

Seconds spent moving from `SourceTransform` to `TargetTransform`.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`UComposableCameraTwoPointMoveNode`](#ucomposablecameratwopointmovenode-1) | Sets the palette category to `Position`. |
| `void` | [`OnInitialize_Implementation`](#oninitialize_implementation) `virtual` | Resets elapsed time. |
| `void` | [`OnTickNode_Implementation`](#onticknode_implementation) `virtual` | Applies the two-point move to the camera pose. |
| `void` | [`GetPinDeclarations_Implementation`](#getpindeclarations_implementation) `virtual` | Declares input pins for Source Transform, Target Transform, Curve, and Duration. |
| `EComposableCameraNodePatchCompatibility` | [`GetPatchCompatibility_Implementation`](#getpatchcompatibility_implementation) `virtual` | Returns `Incompatible`. |

---

#### UComposableCameraTwoPointMoveNode { #ucomposablecameratwopointmovenode-1 }

```cpp
UComposableCameraTwoPointMoveNode()
```

---

#### OnInitialize_Implementation { #oninitialize_implementation }

`virtual`

```cpp
void OnInitialize_Implementation()
```

---

#### OnTickNode_Implementation { #onticknode_implementation }

`virtual`

```cpp
void OnTickNode_Implementation(float DeltaTime, const FComposableCameraPose& CurrentCameraPose, FComposableCameraPose& OutCameraPose)
```

---

#### GetPinDeclarations_Implementation { #getpindeclarations_implementation }

`virtual`

```cpp
void GetPinDeclarations_Implementation(TArray<FComposableCameraNodePinDeclaration>& OutPins) const
```

---

#### GetPatchCompatibility_Implementation { #getpatchcompatibility_implementation }

`virtual`

```cpp
EComposableCameraNodePatchCompatibility GetPatchCompatibility_Implementation() const
```

