
# UComposableCameraKeyframeSequenceNode { #ucomposablecamerakeyframesequencenode }

```cpp
#include <ComposableCameraKeyframeSequenceNode.h>
```

> **Inherits:** [`UComposableCameraCameraNodeBase`](../uobjects-other/UComposableCameraCameraNodeBase.md#ucomposablecameracameranodebase)

Node for playing a keyframed level sequence relative to some transform. <br/>
Your sequence MUST contain a CineCameraActor binding for camera transform and optionally a CameraComponent binding for FieldOfView. <br/>
This can be done by simply clicking the "Create a new camera and set it as the current cut" button on the level sequence panel. <br/>
Only transform and FOV are used. Other parameters bound in the level sequence will not be used.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TObjectPtr< ULevelSequence >` | [`CameraSequence`](#camerasequence)  |  |
| `EComposableCameraRelativeFixedPoseMethod` | [`Method`](#method)  |  |
| `FTransform` | [`RelativeTransform`](#relativetransform)  |  |
| `TObjectPtr< AActor >` | [`RelativeActor`](#relativeactor)  |  |
| `FName` | [`RelativeSocket`](#relativesocket)  |  |
| `float` | [`StayAtLastFrameTime`](#stayatlastframetime)  |  |

---

#### CameraSequence { #camerasequence }

```cpp
TObjectPtr< ULevelSequence > CameraSequence { nullptr }
```

---

#### Method { #method }

```cpp
EComposableCameraRelativeFixedPoseMethod Method
```

---

#### RelativeTransform { #relativetransform }

```cpp
FTransform RelativeTransform
```

---

#### RelativeActor { #relativeactor }

```cpp
TObjectPtr< AActor > RelativeActor
```

---

#### RelativeSocket { #relativesocket }

```cpp
FName RelativeSocket
```

---

#### StayAtLastFrameTime { #stayatlastframetime }

```cpp
float StayAtLastFrameTime { 0.0f }
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`OnInitialize_Implementation`](#oninitialize_implementation-9) `virtual` |  |
| `void` | [`OnTickNode_Implementation`](#onticknode_implementation-15) `virtual` |  |
| `void` | [`GetPinDeclarations_Implementation`](#getpindeclarations_implementation-15) `virtual` `const` |  |

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

#### GetPinDeclarations_Implementation { #getpindeclarations_implementation-15 }

`virtual` `const`

```cpp
virtual void GetPinDeclarations_Implementation(TArray< FComposableCameraNodePinDeclaration > & OutPins) const
```

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `bool` | [`bValidCameraSequence`](#bvalidcamerasequence)  |  |
| `ULevelSequencePlayer *` | [`CameraPlayer`](#cameraplayer)  |  |
| `UMovieSceneFloatSection *` | [`FOVSection`](#fovsection)  |  |
| `UMovieScene3DTransformSection *` | [`TransformSection`](#transformsection)  |  |
| `USkeletalMeshComponent *` | [`SkeletalMeshComponentForRelativeActor`](#skeletalmeshcomponentforrelativeactor)  |  |
| `FFrameTime` | [`ElapsedFrames`](#elapsedframes)  |  |
| `float` | [`ElapsedTime`](#elapsedtime-3)  |  |
| `float` | [`ElapsedStayAtLastFrameTime`](#elapsedstayatlastframetime)  |  |

---

#### bValidCameraSequence { #bvalidcamerasequence }

```cpp
bool bValidCameraSequence { true }
```

---

#### CameraPlayer { #cameraplayer }

```cpp
ULevelSequencePlayer * CameraPlayer { nullptr }
```

---

#### FOVSection { #fovsection }

```cpp
UMovieSceneFloatSection * FOVSection { nullptr }
```

---

#### TransformSection { #transformsection }

```cpp
UMovieScene3DTransformSection * TransformSection { nullptr }
```

---

#### SkeletalMeshComponentForRelativeActor { #skeletalmeshcomponentforrelativeactor }

```cpp
USkeletalMeshComponent * SkeletalMeshComponentForRelativeActor { nullptr }
```

---

#### ElapsedFrames { #elapsedframes }

```cpp
FFrameTime ElapsedFrames { 0 }
```

---

#### ElapsedTime { #elapsedtime-3 }

```cpp
float ElapsedTime { 0.0f }
```

---

#### ElapsedStayAtLastFrameTime { #elapsedstayatlastframetime }

```cpp
float ElapsedStayAtLastFrameTime { 0.f }
```

### Private Methods

| Return | Name | Description |
|--------|------|-------------|
| `std::pair< float, FTransform >` | [`GetTargetTransform`](#gettargettransform)  |  |

---

#### GetTargetTransform { #gettargettransform }

```cpp
std::pair< float, FTransform > GetTargetTransform(FFrameTime FrameTime)
```
