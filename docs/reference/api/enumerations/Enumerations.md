

# Enumerations

#### EComposableCameraBuildStatus { #ecomposablecamerabuildstatus }

```cpp
enum EComposableCameraBuildStatus
```

| Value | Description |
|-------|-------------|
| `NotBuilt` |  |
| `Success` |  |
| `SuccessWithWarnings` |  |
| `Failed` |  |

Build status for camera type asset validation.

#### EComposableCameraActionExpirationType { #ecomposablecameraactionexpirationtype }

```cpp
enum EComposableCameraActionExpirationType
```

| Value | Description |
|-------|-------------|
| `None` |  |
| `Instant` |  |
| `Duration` |  |
| `Manual` |  |
| `Condition` |  |

#### EComposableCameraActionExecutionType { #ecomposablecameraactionexecutiontype }

```cpp
enum EComposableCameraActionExecutionType
```

| Value | Description |
|-------|-------------|
| `PreCameraTick` |  |
| `PreNodeTick` |  |
| `PostNodeTick` |  |
| `PostCameraTick` |  |

#### EComposableCameraResumeCameraTransformSchema { #ecomposablecameraresumecameratransformschema }

```cpp
enum EComposableCameraResumeCameraTransformSchema
```

| Value | Description |
|-------|-------------|
| `PreserveCurrent` |  |
| `PreserveResumed` |  |
| `Specified` |  |

#### EComposableCameraLookAtType { #ecomposablecameralookattype }

```cpp
enum EComposableCameraLookAtType
```

| Value | Description |
|-------|-------------|
| `ByPosition` |  |
| `ByActor` |  |

#### EComposableCameraLookAtConstraintType { #ecomposablecameralookatconstrainttype }

```cpp
enum EComposableCameraLookAtConstraintType
```

| Value | Description |
|-------|-------------|
| `Hard` |  |
| `Soft` |  |

#### EComposableCameraSplineNodeSplineType { #ecomposablecamerasplinenodesplinetype }

```cpp
enum EComposableCameraSplineNodeSplineType
```

| Value | Description |
|-------|-------------|
| `BuiltInSpline` |  |
| `Bezier` |  |
| `CubicHermite` |  |
| `BasicSpline` |  |
| `NURBS` |  |

#### EComposableCameraSplineNodeMoveMethod { #ecomposablecamerasplinenodemovemethod }

```cpp
enum EComposableCameraSplineNodeMoveMethod
```

| Value | Description |
|-------|-------------|
| `Automatic` |  |
| `ClosestPoint` |  |

#### EComposableCameraImpulseBoxDistanceType { #ecomposablecameraimpulseboxdistancetype }

```cpp
enum EComposableCameraImpulseBoxDistanceType
```

| Value | Description |
|-------|-------------|
| `BoxOrigin` |  |
| `XAxis` |  |
| `YAxis` |  |
| `ZAxis` |  |
| `XYPlane` |  |
| `XZPlane` |  |
| `YZPlane` |  |

#### EComposableCameraPinDirection { #ecomposablecamerapindirection }

```cpp
enum EComposableCameraPinDirection
```

| Value | Description |
|-------|-------------|
| `Input` |  |
| `Output` |  |

Direction of a camera node data pin.

#### EComposableCameraPinType { #ecomposablecamerapintype }

```cpp
enum EComposableCameraPinType
```

| Value | Description |
|-------|-------------|
| `Bool` |  |
| `Int32` |  |
| `Float` |  |
| `Double` |  |
| `Vector2D` |  |
| `Vector3D` |  |
| `Vector4` |  |
| `Rotator` |  |
| `Transform` |  |
| `Actor` |  |
| `Object` |  |
| `Struct` | Custom USTRUCT type. When this is selected, StructType must be set. |
| `Name` | FName value. Stored as FName in the data block (POD: NAME_INDEX + NAME_NUMBER). |
| `Enum` | UENUM value. Stored as a normalized int64 in the data block; the owning UEnum* is carried on the declaration and used to narrow-cast into the actual property's underlying width (uint8 / int32 / int64) at write time. When this is selected, EnumType must be set. |

Supported data types for camera node pins.

#### EComposableCameraExecEntryType { #ecomposablecameraexecentrytype }

```cpp
enum EComposableCameraExecEntryType
```

| Value | Description |
|-------|-------------|
| `CameraNode` | Execute a camera node by its index in NodeTemplates. |
| `SetVariable` | Execute an internal-variable Set operation: copy the source camera node's output pin into the internal variable identified by VariableGuid. |

Tag for entries in the serialized execution chain.

The execution chain is a linear sequence of operations the camera runs each frame: camera nodes do the actual pose computation, and internal-variable Set operations write scratch values between camera nodes. See [FComposableCameraExecEntry](../structs/FComposableCameraExecEntry.md#fcomposablecameraexecentry).

#### ECameraPivotOffset { #ecamerapivotoffset }

```cpp
enum ECameraPivotOffset
```

| Value | Description |
|-------|-------------|
| `WorldSpace` |  |
| `ActorLocalSpace` |  |
| `CameraSpace` |  |

#### EComposableCameraMixingCameraWeightNormalizationMethod { #ecomposablecameramixingcameraweightnormalizationmethod }

```cpp
enum EComposableCameraMixingCameraWeightNormalizationMethod
```

| Value | Description |
|-------|-------------|
| `L1` |  |
| `L2` |  |
| `SoftMax` |  |

Weight normalization method.

#### EComposableCameraMixingCameraMode { #ecomposablecameramixingcameramode }

```cpp
enum EComposableCameraMixingCameraMode
```

| Value | Description |
|-------|-------------|
| `PositionOnly` |  |
| `RotationOnly` |  |
| `Both` |  |

Mixing camera node mode.

#### EComposableCameraMixingCameraRotationMethod { #ecomposablecameramixingcamerarotationmethod }

```cpp
enum EComposableCameraMixingCameraRotationMethod
```

| Value | Description |
|-------|-------------|
| `MatrixInterp` |  |
| `CircularInterp` |  |
| `QuaternionInterpolation` |  |
| `AngleInterpolation` |  |

Different methods to average rotations. Ref: [https://sulley.cc/2024/01/11/20/06/](https://sulley.cc/2024/01/11/20/06/).

#### EComposableCameraSplineTransitionType { #ecomposablecamerasplinetransitiontype }

```cpp
enum EComposableCameraSplineTransitionType
```

| Value | Description |
|-------|-------------|
| `Hermite` |  |
| `Bezier` |  |
| `CatmullRom` |  |
| `Arc` |  |

#### EComposableCameraSplineTransitionEvaluationCurveType { #ecomposablecamerasplinetransitionevaluationcurvetype }

```cpp
enum EComposableCameraSplineTransitionEvaluationCurveType
```

| Value | Description |
|-------|-------------|
| `Smooth` |  |
| `Smoother` |  |
| `Linear` |  |
| `Cubic` |  |

#### EComposableCameraRotationConstrainType { #ecomposablecamerarotationconstraintype }

```cpp
enum EComposableCameraRotationConstrainType
```

| Value | Description |
|-------|-------------|
| `WorldSpace` |  |
| `ActorSpace` |  |
| `VectorSpace` |  |

#### EComposableCameraScreenSpaceMethod { #ecomposablecamerascreenspacemethod }

```cpp
enum EComposableCameraScreenSpaceMethod
```

| Value | Description |
|-------|-------------|
| `Translate` |  |
| `Rotate` |  |

#### EComposableCameraScreenSpacePivotSource { #ecomposablecamerascreenspacepivotsource }

```cpp
enum EComposableCameraScreenSpacePivotSource
```

| Value | Description |
|-------|-------------|
| `WorldPosition` |  |
| `ActorPosition` |  |

#### EComposableCameraPathGuidedTransitionType { #ecomposablecamerapathguidedtransitiontype }

```cpp
enum EComposableCameraPathGuidedTransitionType
```

| Value | Description |
|-------|-------------|
| `Inertialized` |  |
| `Auto` |  |

#### EComposableCameraRelativeFixedPoseMethod { #ecomposablecamerarelativefixedposemethod }

```cpp
enum EComposableCameraRelativeFixedPoseMethod
```

| Value | Description |
|-------|-------------|
| `RelativeToTransform` |  |
| `RelativeToActor` |  |