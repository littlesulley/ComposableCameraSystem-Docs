
# UComposableCameraMixingCameraNode { #ucomposablecameramixingcameranode }

```cpp
#include <ComposableCameraMixingCameraNode.h>
```

> **Inherits:** [`UComposableCameraCameraNodeBase`](../uobjects-other/UComposableCameraCameraNodeBase.md#ucomposablecameracameranodebase)

Node for mixing multiple cameras. <br/>
This node will instantiate new camera instances specified by parameter Cameras. <br/>
During runtime, you should pass in a UpdateWeight function that provides weights for these cameras. Make sure all weights are greater than zero. <br/>
If one camera instance is not valid, its weight will be set to zero, then a squared normalization will be applied to normalize all weights.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `EComposableCameraMixingCameraMode` | [`MixMode`](#mixmode)  |  |
| `EComposableCameraMixingCameraWeightNormalizationMethod` | [`WeightNormalizationMethod`](#weightnormalizationmethod)  |  |
| `EComposableCameraMixingCameraRotationMethod` | [`MixRotationMethod`](#mixrotationmethod)  |  |
| `float` | [`CircularInterpEpsilon`](#circularinterpepsilon)  |  |
| `TArray< FComposableCameraMixingCameraNodeCameraDefinition >` | [`Cameras`](#cameras-1)  |  |
| `FOnReceiveMixingCameraWeights` | [`OnReceiveMixingCameraWeights`](#onreceivemixingcameraweights)  |  |

---

#### MixMode { #mixmode }

```cpp
EComposableCameraMixingCameraMode MixMode {  }
```

---

#### WeightNormalizationMethod { #weightnormalizationmethod }

```cpp
EComposableCameraMixingCameraWeightNormalizationMethod WeightNormalizationMethod {  }
```

---

#### MixRotationMethod { #mixrotationmethod }

```cpp
EComposableCameraMixingCameraRotationMethod MixRotationMethod {  }
```

---

#### CircularInterpEpsilon { #circularinterpepsilon }

```cpp
float CircularInterpEpsilon { 0.25f }
```

---

#### Cameras { #cameras-1 }

```cpp
TArray< FComposableCameraMixingCameraNodeCameraDefinition > Cameras
```

---

#### OnReceiveMixingCameraWeights { #onreceivemixingcameraweights }

```cpp
FOnReceiveMixingCameraWeights OnReceiveMixingCameraWeights
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`UComposableCameraMixingCameraNode`](#ucomposablecameramixingcameranode-1) `inline` |  |
| `void` | [`OnInitialize_Implementation`](#oninitialize_implementation-8) `virtual` |  |
| `void` | [`OnTickNode_Implementation`](#onticknode_implementation-13) `virtual` |  |
| `void` | [`BeginDestroy`](#begindestroy) `virtual` |  |
| `void` | [`GetPinDeclarations_Implementation`](#getpindeclarations_implementation-12) `virtual` `const` |  |
| `EComposableCameraNodeLevelSequenceCompatibility` | [`GetLevelSequenceCompatibility_Implementation`](#getlevelsequencecompatibility_implementation-2) `virtual` `const` `inline` |  |
| `EComposableCameraNodePatchCompatibility` | [`GetPatchCompatibility_Implementation`](#getpatchcompatibility_implementation-1) `virtual` `const` `inline` |  |
| `void` | [`SetUpdateWeights`](#setupdateweights)  |  |

---

#### UComposableCameraMixingCameraNode { #ucomposablecameramixingcameranode-1 }

`inline`

```cpp
inline UComposableCameraMixingCameraNode()
```

---

#### OnInitialize_Implementation { #oninitialize_implementation-8 }

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

#### BeginDestroy { #begindestroy }

`virtual`

```cpp
virtual void BeginDestroy()
```

---

#### GetPinDeclarations_Implementation { #getpindeclarations_implementation-12 }

`virtual` `const`

```cpp
virtual void GetPinDeclarations_Implementation(TArray< FComposableCameraNodePinDeclaration > & OutPins) const
```

---

#### GetLevelSequenceCompatibility_Implementation { #getlevelsequencecompatibility_implementation-2 }

`virtual` `const` `inline`

```cpp
virtual inline EComposableCameraNodeLevelSequenceCompatibility GetLevelSequenceCompatibility_Implementation() const
```

---

#### GetPatchCompatibility_Implementation { #getpatchcompatibility_implementation-1 }

`virtual` `const` `inline`

```cpp
virtual inline EComposableCameraNodePatchCompatibility GetPatchCompatibility_Implementation() const
```

---

#### SetUpdateWeights { #setupdateweights }

```cpp
void SetUpdateWeights(FOnReceiveMixingCameraWeights OnUpdateMixingCameraWeights)
```

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TArray< TObjectPtr< AComposableCameraCameraBase > >` | [`CameraInstances`](#camerainstances)  |  |
| `FVector4` | [`InitialEigenVector`](#initialeigenvector)  |  |

---

#### CameraInstances { #camerainstances }

```cpp
TArray< TObjectPtr< AComposableCameraCameraBase > > CameraInstances
```

---

#### InitialEigenVector { #initialeigenvector }

```cpp
FVector4 InitialEigenVector { 0, 0, 0, 1 }
```

### Private Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`NormalizeWeights`](#normalizeweights)  |  |
| `void` | [`TickCameras`](#tickcameras)  |  |
| `FVector` | [`GetMixedPosition`](#getmixedposition)  |  |
| `FRotator` | [`GetMixedRotation`](#getmixedrotation)  |  |
| `double` | [`GetMixedFieldOfView`](#getmixedfieldofview)  |  |

---

#### NormalizeWeights { #normalizeweights }

```cpp
void NormalizeWeights(TArray< float > & Array)
```

---

#### TickCameras { #tickcameras }

```cpp
void TickCameras(TArray< FComposableCameraPose > & Poses, float DeltaTime)
```

---

#### GetMixedPosition { #getmixedposition }

```cpp
FVector GetMixedPosition(const TArray< FComposableCameraPose > & Poses, const TArray< float > & Weights)
```

---

#### GetMixedRotation { #getmixedrotation }

```cpp
FRotator GetMixedRotation(const TArray< FComposableCameraPose > & Poses, const TArray< float > & Weights)
```

---

#### GetMixedFieldOfView { #getmixedfieldofview }

```cpp
double GetMixedFieldOfView(const TArray< FComposableCameraPose > & Poses, const TArray< float > & Weights)
```
