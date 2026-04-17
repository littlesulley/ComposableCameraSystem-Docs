

# Functions

#### DECLARE_DELEGATE_RetVal { #declare_delegate_retval }

```cpp
DECLARE_DELEGATE_RetVal(bool, FGetIsSimulatingInEditor)
```

#### DECLARE_DYNAMIC_MULTICAST_DELEGATE_OneParam { #declare_dynamic_multicast_delegate_oneparam }

```cpp
DECLARE_DYNAMIC_MULTICAST_DELEGATE_OneParam(FOnTickFloatCurve, float, Value)
```

#### DECLARE_DYNAMIC_MULTICAST_DELEGATE { #declare_dynamic_multicast_delegate }

```cpp
DECLARE_DYNAMIC_MULTICAST_DELEGATE(FOnCompleteFloatCurve)
```

#### DECLARE_DYNAMIC_MULTICAST_DELEGATE_OneParam { #declare_dynamic_multicast_delegate_oneparam-1 }

```cpp
DECLARE_DYNAMIC_MULTICAST_DELEGATE_OneParam(FOnTickVectorCurve, FVector, Value)
```

#### DECLARE_DYNAMIC_MULTICAST_DELEGATE { #declare_dynamic_multicast_delegate-1 }

```cpp
DECLARE_DYNAMIC_MULTICAST_DELEGATE(FOnCompleteVectorCurve)
```

#### DECLARE_MULTICAST_DELEGATE_ThreeParams { #declare_multicast_delegate_threeparams }

```cpp
DECLARE_MULTICAST_DELEGATE_ThreeParams(FOnPreTick, float, const FComposableCameraPose &, FComposableCameraPose &)
```

Called before any internal node is executed.

#### DECLARE_MULTICAST_DELEGATE_ThreeParams { #declare_multicast_delegate_threeparams-1 }

```cpp
DECLARE_MULTICAST_DELEGATE_ThreeParams(FOnPostTick, float, const FComposableCameraPose &, FComposableCameraPose &)
```

Called after all internal nodes are executed.

#### DECLARE_DYNAMIC_MULTICAST_DELEGATE_ThreeParams { #declare_dynamic_multicast_delegate_threeparams }

```cpp
DECLARE_DYNAMIC_MULTICAST_DELEGATE_ThreeParams(FOnActionPreTick, float, DeltaTime, const FComposableCameraPose &, CurrentCameraPose, FComposableCameraPose &, OutputPose)
```

Called before any internal node is executed for camera actions.

#### DECLARE_DYNAMIC_MULTICAST_DELEGATE_ThreeParams { #declare_dynamic_multicast_delegate_threeparams-1 }

```cpp
DECLARE_DYNAMIC_MULTICAST_DELEGATE_ThreeParams(FOnActionPostTick, float, DeltaTime, const FComposableCameraPose &, CurrentCameraPose, FComposableCameraPose &, OutputPose)
```

Called after all internal nodes are executed for camera actions.

#### DECLARE_DYNAMIC_DELEGATE_OneParam { #declare_dynamic_delegate_oneparam }

```cpp
DECLARE_DYNAMIC_DELEGATE_OneParam(FOnCameraFinishConstructed, AComposableCameraCameraBase *, Camera)
```

Called when the camera finishes constructed, before BeginPlay is called.

#### DECLARE_LOG_CATEGORY_EXTERN { #declare_log_category_extern }

```cpp
DECLARE_LOG_CATEGORY_EXTERN(LogComposableCameraSystem, Log, All)
```

#### TryMapPropertyToPinType { #trymappropertytopintype }

```cpp
inline bool TryMapPropertyToPinType(const FProperty * Property, EComposableCameraPinType & OutPinType, UScriptStruct *& OutStructType, UEnum *& OutEnumType, UFunction ** OutSignatureFunction)
```

Attempt to map an FProperty (from UClass reflection) to an EComposableCameraPinType.

Returns true if the property type has a direct pin-type mapping. Returns false for unsupported types (arrays, maps, sets, Instanced object properties, FString, etc.).

For Enum-typed properties (`FEnumProperty` for `enum class`, or `FByteProperty` whose IntPropertyEnum is set), OutEnumType receives the backing UEnum*. For Struct-typed properties that aren't one of the hard-coded math types, OutStructType receives the specific UScriptStruct*. Both are cleared on entry.

Used by DeclareSubobjectPins to auto-discover exposable sub-properties of an Instanced UObject, and by ApplySubobjectPinValues to dispatch typed reads.

#### GetPinTypeSize { #getpintypesize }

```cpp
inline int32 GetPinTypeSize(EComposableCameraPinType PinType, UScriptStruct * StructType)
```

Returns the size in bytes of a given pin type. For Struct types, returns 0 — caller must query StructType->GetStructureSize().

#### GetPinTypeAlignment { #getpintypealignment }

```cpp
inline int32 GetPinTypeAlignment(EComposableCameraPinType PinType, UScriptStruct * StructType)
```

Returns the alignment requirement of a given pin type.

#### DECLARE_MULTICAST_DELEGATE { #declare_multicast_delegate }

```cpp
DECLARE_MULTICAST_DELEGATE(FOnTransitionFinishes)
```

#### DECLARE_DYNAMIC_DELEGATE_RetVal { #declare_dynamic_delegate_retval }

```cpp
DECLARE_DYNAMIC_DELEGATE_RetVal(TArray< float >, FOnReceiveMixingCameraWeights)
```

# ComposableCameraDebug { #composablecameradebug }

Namespace for debug formatting utilities used by both the ShowDebug HUD (runtime) and the editor debug overlay (WITH_EDITOR).

All functions allocate FStrings — they are intended for debug display, not hot-path evaluation.

### Functions

| Return | Name | Description |
|--------|------|-------------|
| `FString` | [`FormatFloat`](#formatfloat) `inline` | Format a float to a compact display string. |
| `FString` | [`FormatVector`](#formatvector) `inline` | Format an FVector to a compact display string. |
| `FString` | [`FormatRotator`](#formatrotator) `inline` | Format an FRotator to a compact display string. |
| `FString` | [`FormatTransform`](#formattransform) `inline` | Format an FTransform to a compact display string. |
| `FString` | [`FormatTypedValue`](#formattypedvalue) `inline` | Read a typed value at a known byte offset from the data block and format as string. EnumType is consulted only when PinType == Enum; when supplied, the int64 slot is formatted as the corresponding entry name (e.g. "EMyEnum::Alpha"). When omitted for an Enum slot the raw int64 value is printed instead — debug-only fallback. |
| `FString` | [`FormatOutputPinValue`](#formatoutputpinvalue) `inline` | Read a typed output pin value from the data block and format as string. |

---

#### FormatFloat { #formatfloat }

`inline`

```cpp
inline FString FormatFloat(double Value)
```

Format a float to a compact display string.

---

#### FormatVector { #formatvector }

`inline`

```cpp
inline FString FormatVector(const FVector & V)
```

Format an FVector to a compact display string.

---

#### FormatRotator { #formatrotator }

`inline`

```cpp
inline FString FormatRotator(const FRotator & R)
```

Format an FRotator to a compact display string.

---

#### FormatTransform { #formattransform }

`inline`

```cpp
inline FString FormatTransform(const FTransform & T)
```

Format an FTransform to a compact display string.

---

#### FormatTypedValue { #formattypedvalue }

`inline`

```cpp
inline FString FormatTypedValue(const FComposableCameraRuntimeDataBlock & DataBlock, int32 Offset, EComposableCameraPinType PinType, const UEnum * EnumType)
```

Read a typed value at a known byte offset from the data block and format as string. EnumType is consulted only when PinType == Enum; when supplied, the int64 slot is formatted as the corresponding entry name (e.g. "EMyEnum::Alpha"). When omitted for an Enum slot the raw int64 value is printed instead — debug-only fallback.

---

#### FormatOutputPinValue { #formatoutputpinvalue }

`inline`

```cpp
inline FString FormatOutputPinValue(const FComposableCameraRuntimeDataBlock & DataBlock, int32 NodeIndex, FName PinName, EComposableCameraPinType PinType, const UEnum * EnumType)
```

Read a typed output pin value from the data block and format as string.

# ComposableCameraSystem { #composablecamerasystem }

### Functions

| Return | Name | Description |
|--------|------|-------------|
| `float` | [`SmoothStep`](#smoothstep) `inline` |  |
| `float` | [`SmootherStep`](#smootherstep) `inline` |  |
| `double` | [`SimpleExpDamp`](#simpleexpdamp) `inline` |  |
| `double` | [`NormalizeYaw`](#normalizeyaw) `inline` |  |
| `FVector4` | [`NormalizeVector4`](#normalizevector4) `inline` |  |
| `FVector` | [`SlerpNormalized`](#slerpnormalized) `inline` | Apply Slerp to two normalized vectors. |
| `FVector` | [`Slerp`](#slerp) `inline` | Apply Slerp to two vectors, no normalization is needed. |
| `float` | [`UnsignedAngleBetweenVectors`](#unsignedanglebetweenvectors) `inline` | Get the unsigned angle between two vectors. |
| `float` | [`SignedAngleBetweenVectors`](#signedanglebetweenvectors) `inline` | Get the signed angle between two vectors. |
| `FQuat` | [`ApplyAdditiveCameraRotation`](#applyadditivecamerarotation) `inline` | Apply an additive rotation to camera rotation. First about world space yaw using AdditiveRotation.X, then about local space pitch using AdditiveRotation.Y. |
| `FVector2D` | [`GetCameraRotationFromTarget`](#getcamerarotationfromtarget) `inline` | Get world space yaw and local space pitch change from a camera rotation to a look-at direction. |
| `FQuat` | [`GetCameraRotationFromVectors`](#getcamerarotationfromvectors) `inline` | Get camera rotation from V1 to V2 with up vector Up. |
| `FVector4` | [`FindEigenVectorByPowerIteration`](#findeigenvectorbypoweriteration) `inline` | Power iteration to find eigenvector. Ref [https://en.wikipedia.org/wiki/Power_iteration](https://en.wikipedia.org/wiki/Power_iteration) Rayleigh quotient iteration converges faster, but involving computing matrix inverse. Ref [https://en.wikipedia.org/wiki/Rayleigh_quotient_iteration](https://en.wikipedia.org/wiki/Rayleigh_quotient_iteration) |
| `std::pair< FRotator, FVector4 >` | [`MatrixInterpRotation`](#matrixinterprotation) `inline` |  |
| `FRotator` | [`CircularInterpRotation`](#circularinterprotation) `inline` |  |
| `FRotator` | [`QuaternionInterpRotation`](#quaternioninterprotation) `inline` |  |
| `FRotator` | [`AngleInterpRotation`](#angleinterprotation) `inline` |  |
| `float` | [`GetClosestAngleDegree`](#getclosestangledegree) `inline` |  |
| `float` | [`GetProjectPerpLength`](#getprojectperplength) `inline` | Get the perpendicular vector's length from any vector B projecting onto a unit vector A. i.e., (B - A * (A.Dot(B)).Length(). |
| `FVector` | [`GetProjectedPoint`](#getprojectedpoint) `inline` | Get the point projected from B to a unit vector A. |

---

#### SmoothStep { #smoothstep }

`inline`

```cpp
inline float SmoothStep(float T)
```

---

#### SmootherStep { #smootherstep }

`inline`

```cpp
inline float SmootherStep(float T)
```

---

#### SimpleExpDamp { #simpleexpdamp }

`inline`

```cpp
inline double SimpleExpDamp(float DeltaTime, float DampTime, float Input)
```

---

#### NormalizeYaw { #normalizeyaw }

`inline`

```cpp
inline double NormalizeYaw(double InYaw)
```

---

#### NormalizeVector4 { #normalizevector4 }

`inline`

```cpp
inline FVector4 NormalizeVector4(const FVector4 & V, float Tolerance)
```

---

#### SlerpNormalized { #slerpnormalized }

`inline`

```cpp
inline FVector SlerpNormalized(const FVector & Start, const FVector & End, float Alpha)
```

Apply Slerp to two normalized vectors.

---

#### Slerp { #slerp }

`inline`

```cpp
inline FVector Slerp(const FVector & Start, const FVector & End, float Alpha)
```

Apply Slerp to two vectors, no normalization is needed.

---

#### UnsignedAngleBetweenVectors { #unsignedanglebetweenvectors }

`inline`

```cpp
inline float UnsignedAngleBetweenVectors(FVector V1, FVector V2)
```

Get the unsigned angle between two vectors.

---

#### SignedAngleBetweenVectors { #signedanglebetweenvectors }

`inline`

```cpp
inline float SignedAngleBetweenVectors(FVector V1, FVector V2, FVector Up)
```

Get the signed angle between two vectors.

---

#### ApplyAdditiveCameraRotation { #applyadditivecamerarotation }

`inline`

```cpp
inline FQuat ApplyAdditiveCameraRotation(FQuat CameraRotation, FVector2D AdditiveRotation)
```

Apply an additive rotation to camera rotation. First about world space yaw using AdditiveRotation.X, then about local space pitch using AdditiveRotation.Y.

---

#### GetCameraRotationFromTarget { #getcamerarotationfromtarget }

`inline`

```cpp
inline FVector2D GetCameraRotationFromTarget(FQuat CameraRotation, FVector LookAtDirection)
```

Get world space yaw and local space pitch change from a camera rotation to a look-at direction.

---

#### GetCameraRotationFromVectors { #getcamerarotationfromvectors }

`inline`

```cpp
inline FQuat GetCameraRotationFromVectors(FVector V1, FVector V2, FVector Up)
```

Get camera rotation from V1 to V2 with up vector Up.

---

#### FindEigenVectorByPowerIteration { #findeigenvectorbypoweriteration }

`inline`

```cpp
inline FVector4 FindEigenVectorByPowerIteration(const FMatrix & M, const FVector4 & V, const int Steps, const float Epsilon)
```

Power iteration to find eigenvector. Ref [https://en.wikipedia.org/wiki/Power_iteration](https://en.wikipedia.org/wiki/Power_iteration) Rayleigh quotient iteration converges faster, but involving computing matrix inverse. Ref [https://en.wikipedia.org/wiki/Rayleigh_quotient_iteration](https://en.wikipedia.org/wiki/Rayleigh_quotient_iteration)

---

#### MatrixInterpRotation { #matrixinterprotation }

`inline`

```cpp
inline std::pair< FRotator, FVector4 > MatrixInterpRotation(const TArray< FRotator > & Rotations, const TArray< float > & Weights, FVector4 InitialEigenVector)
```

---

#### CircularInterpRotation { #circularinterprotation }

`inline`

```cpp
inline FRotator CircularInterpRotation(const TArray< FRotator > & Rotations, const TArray< float > & Weights, float Epsilon)
```

---

#### QuaternionInterpRotation { #quaternioninterprotation }

`inline`

```cpp
inline FRotator QuaternionInterpRotation(const TArray< FRotator > & Rotations, const TArray< float > & Weights)
```

---

#### AngleInterpRotation { #angleinterprotation }

`inline`

```cpp
inline FRotator AngleInterpRotation(const TArray< FRotator > & Rotations, const TArray< float > & Weights)
```

---

#### GetClosestAngleDegree { #getclosestangledegree }

`inline`

```cpp
template<typename... Args> inline float GetClosestAngleDegree(float InAngle, Args... Angles)
```

---

#### GetProjectPerpLength { #getprojectperplength }

`inline`

```cpp
inline float GetProjectPerpLength(const FVector & A, const FVector & B)
```

Get the perpendicular vector's length from any vector B projecting onto a unit vector A. i.e., (B - A * (A.Dot(B)).Length().

---

#### GetProjectedPoint { #getprojectedpoint }

`inline`

```cpp
inline FVector GetProjectedPoint(const FVector & A, const FVector & B)
```

Get the point projected from B to a unit vector A.

# ComposableCameraModifier { #composablecameramodifier }

### Classes

| Name | Description |
|------|-------------|
| [`FModifierEntry`](../structs/FModifierEntry.md#fmodifierentry) |  |

### Typedefs

| Return | Name | Description |
|--------|------|-------------|
| `TSubclassOf< UComposableCameraCameraNodeBase >` | [`T_NodeClass`](#t_nodeclass)  |  |
| `TMap< T_NodeClass, FModifierEntry >` | [`T_NodeModifier`](#t_nodemodifier)  |  |
| `TMap< T_NodeClass, TArray< FModifierEntry > >` | [`T_NodeModifierArray`](#t_nodemodifierarray)  |  |
| `TMap< FGameplayTag, T_NodeModifierArray >` | [`T_CameraModifier`](#t_cameramodifier)  |  |

---

#### T_NodeClass { #t_nodeclass }

```cpp
TSubclassOf< UComposableCameraCameraNodeBase > T_NodeClass()
```

---

#### T_NodeModifier { #t_nodemodifier }

```cpp
TMap< T_NodeClass, FModifierEntry > T_NodeModifier()
```

---

#### T_NodeModifierArray { #t_nodemodifierarray }

```cpp
TMap< T_NodeClass, TArray< FModifierEntry > > T_NodeModifierArray()
```

---

#### T_CameraModifier { #t_cameramodifier }

```cpp
TMap< FGameplayTag, T_NodeModifierArray > T_CameraModifier()
```
