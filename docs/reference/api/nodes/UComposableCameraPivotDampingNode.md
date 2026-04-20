
# UComposableCameraPivotDampingNode { #ucomposablecamerapivotdampingnode }

```cpp
#include <ComposableCameraPivotDampingNode.h>
```

> **Inherits:** [`UComposableCameraCameraNodeBase`](../uobjects-other/UComposableCameraCameraNodeBase.md#ucomposablecameracameranodebase)

Node for damping (interpolating) the pivot position. This is done in the space projected onto the XY plane. <br/>
@InputParameter MaintainCameraSpacePivot: Whether to maintain camera space pivot position. <br/>
@InputParameter UpwardInterpolator: Interpolator when the pivot is moving upward. <br/>
@InputParameter DownwardInterpolator: Interpolator when the pivot is moving downward. <br/>
@InputParameter LeftwardInterpolator: Interpolator when the pivot is moving leftward. <br/>
@InputParameter RightwardInterpolator: Interpolator when the pivot is moving rightward. <br/>
@InputParameter ForwardInterpolator: Interpolator when the pivot is moving forward. <br/>
@InputParameter BackwardInterpolator: Interpolator when the pivot is moving backward. <br/>

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FVector` | [`PivotPosition`](#pivotposition-2)  |  |
| `bool` | [`bMaintainCameraSpacePivotPosition`](#bmaintaincameraspacepivotposition)  |  |
| `TObjectPtr< UComposableCameraInterpolatorBase >` | [`UpwardInterpolator`](#upwardinterpolator)  |  |
| `TObjectPtr< UComposableCameraInterpolatorBase >` | [`DownwardInterpolator`](#downwardinterpolator)  |  |
| `TObjectPtr< UComposableCameraInterpolatorBase >` | [`LeftwardInterpolator`](#leftwardinterpolator)  |  |
| `TObjectPtr< UComposableCameraInterpolatorBase >` | [`RightwardInterpolator`](#rightwardinterpolator)  |  |
| `TObjectPtr< UComposableCameraInterpolatorBase >` | [`ForwardInterpolator`](#forwardinterpolator)  |  |
| `TObjectPtr< UComposableCameraInterpolatorBase >` | [`BackwardInterpolator`](#backwardinterpolator)  |  |

---

#### PivotPosition { #pivotposition-2 }

```cpp
FVector PivotPosition { FVector::ZeroVector }
```

---

#### bMaintainCameraSpacePivotPosition { #bmaintaincameraspacepivotposition }

```cpp
bool bMaintainCameraSpacePivotPosition { true }
```

---

#### UpwardInterpolator { #upwardinterpolator }

```cpp
TObjectPtr< UComposableCameraInterpolatorBase > UpwardInterpolator
```

---

#### DownwardInterpolator { #downwardinterpolator }

```cpp
TObjectPtr< UComposableCameraInterpolatorBase > DownwardInterpolator
```

---

#### LeftwardInterpolator { #leftwardinterpolator }

```cpp
TObjectPtr< UComposableCameraInterpolatorBase > LeftwardInterpolator
```

---

#### RightwardInterpolator { #rightwardinterpolator }

```cpp
TObjectPtr< UComposableCameraInterpolatorBase > RightwardInterpolator
```

---

#### ForwardInterpolator { #forwardinterpolator }

```cpp
TObjectPtr< UComposableCameraInterpolatorBase > ForwardInterpolator
```

---

#### BackwardInterpolator { #backwardinterpolator }

```cpp
TObjectPtr< UComposableCameraInterpolatorBase > BackwardInterpolator
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`OnInitialize_Implementation`](#oninitialize_implementation-6) `virtual` |  |
| `void` | [`OnFirstTickNode_Implementation`](#onfirstticknode_implementation-1) `virtual` |  |
| `void` | [`OnTickNode_Implementation`](#onticknode_implementation-12) `virtual` |  |
| `void` | [`GetPinDeclarations_Implementation`](#getpindeclarations_implementation-11) `virtual` `const` |  |

---

#### OnInitialize_Implementation { #oninitialize_implementation-6 }

`virtual`

```cpp
virtual void OnInitialize_Implementation()
```

---

#### OnFirstTickNode_Implementation { #onfirstticknode_implementation-1 }

`virtual`

```cpp
virtual void OnFirstTickNode_Implementation()
```

---

#### OnTickNode_Implementation { #onticknode_implementation-12 }

`virtual`

```cpp
virtual void OnTickNode_Implementation(float DeltaTime, const FComposableCameraPose & CurrentCameraPose, FComposableCameraPose & OutCameraPose)
```

---

#### GetPinDeclarations_Implementation { #getpindeclarations_implementation-11 }

`virtual` `const`

```cpp
virtual void GetPinDeclarations_Implementation(TArray< FComposableCameraNodePinDeclaration > & OutPins) const
```

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TUniquePtr< TCameraInterpolator< TValueTypeWrapper< double > > >` | [`UpwardInterpolator_T`](#upwardinterpolator_t)  |  |
| `TUniquePtr< TCameraInterpolator< TValueTypeWrapper< double > > >` | [`DownwardInterpolator_T`](#downwardinterpolator_t)  |  |
| `TUniquePtr< TCameraInterpolator< TValueTypeWrapper< double > > >` | [`LeftwardInterpolator_T`](#leftwardinterpolator_t)  |  |
| `TUniquePtr< TCameraInterpolator< TValueTypeWrapper< double > > >` | [`RightwardInterpolator_T`](#rightwardinterpolator_t)  |  |
| `TUniquePtr< TCameraInterpolator< TValueTypeWrapper< double > > >` | [`ForwardInterpolator_T`](#forwardinterpolator_t)  |  |
| `TUniquePtr< TCameraInterpolator< TValueTypeWrapper< double > > >` | [`BackwardInterpolator_T`](#backwardinterpolator_t)  |  |
| `FVector` | [`LastPivotPosition`](#lastpivotposition)  |  |

---

#### UpwardInterpolator_T { #upwardinterpolator_t }

```cpp
TUniquePtr< TCameraInterpolator< TValueTypeWrapper< double > > > UpwardInterpolator_T
```

---

#### DownwardInterpolator_T { #downwardinterpolator_t }

```cpp
TUniquePtr< TCameraInterpolator< TValueTypeWrapper< double > > > DownwardInterpolator_T
```

---

#### LeftwardInterpolator_T { #leftwardinterpolator_t }

```cpp
TUniquePtr< TCameraInterpolator< TValueTypeWrapper< double > > > LeftwardInterpolator_T
```

---

#### RightwardInterpolator_T { #rightwardinterpolator_t }

```cpp
TUniquePtr< TCameraInterpolator< TValueTypeWrapper< double > > > RightwardInterpolator_T
```

---

#### ForwardInterpolator_T { #forwardinterpolator_t }

```cpp
TUniquePtr< TCameraInterpolator< TValueTypeWrapper< double > > > ForwardInterpolator_T
```

---

#### BackwardInterpolator_T { #backwardinterpolator_t }

```cpp
TUniquePtr< TCameraInterpolator< TValueTypeWrapper< double > > > BackwardInterpolator_T
```

---

#### LastPivotPosition { #lastpivotposition }

```cpp
FVector LastPivotPosition
```
