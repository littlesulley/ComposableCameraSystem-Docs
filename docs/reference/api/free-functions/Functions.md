

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

#### DECLARE_DYNAMIC_MULTICAST_DELEGATE { #declare_dynamic_multicast_delegate-1 }

```cpp
DECLARE_DYNAMIC_MULTICAST_DELEGATE(FOnCutsceneSequenceFinished)
```

#### DECLARE_DYNAMIC_MULTICAST_DELEGATE_OneParam { #declare_dynamic_multicast_delegate_oneparam-1 }

```cpp
DECLARE_DYNAMIC_MULTICAST_DELEGATE_OneParam(FOnTickVectorCurve, FVector, Value)
```

#### DECLARE_DYNAMIC_MULTICAST_DELEGATE { #declare_dynamic_multicast_delegate-2 }

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

# ComposableCameras { #composablecameras }

Helpers that bridge CCS's own pin-type taxonomy (EComposableCameraPinType) to the generic FInstancedPropertyBag taxonomy (EPropertyBagPropertyType).

Used by [FComposableCameraTypeAssetReference](../structs/FComposableCameraTypeAssetReference.md#fcomposablecameratypeassetreference) to generate Parameters / Variables bags from a TypeAsset's ExposedParameters / ExposedVariables, and to read values back from those bags into an [FComposableCameraParameterBlock](../structs/FComposableCameraParameterBlock.md#fcomposablecameraparameterblock) at camera activation time.

Delegate pin type is intentionally not supported here — delegates cannot round-trip through a property bag (they carry heap-owned bindings). Delegate exposed parameters flow through the existing [FComposableCameraParameterBlock](../structs/FComposableCameraParameterBlock.md#fcomposablecameraparameterblock) delegate path at activation time; the Level Sequence component bag covers only POD-style parameters.

Viewport-size helpers for camera nodes that need to know the window / view dimensions without hard-wiring a PlayerCameraManager dereference.

Background: the original ScreenSpacePivot / ScreenSpaceConstraints nodes computed aspect ratio as `PCM->GetOwningPlayerController()->GetViewportSize()`. That path works for the PCM-driven runtime but falls over in the Level Sequence component path, where there is no PCM. The PCM, however, isn't a hard requirement for the underlying question — "what are the viewport
dimensions right now?" — because the engine already tracks that through GEngine->GameViewport in game worlds and through GEditor->GetActiveViewport() in editor worlds. This utility consolidates the resolution chain so node code can just ask and doesn't need to carry the decision tree itself.

Resolution order (first source that returns a valid size wins):

1. PCM → PlayerController → viewport (legacy / multiplayer-aware; honors split-screen per-player viewports).

1. GEngine->GameViewport (game worlds: PIE, standalone, packaged).

1. GEditor->GetActiveViewport() in WITH_EDITOR builds (editor preview of LS Spawnables, piloted actors in the level editor).

1. A 1920×1080 sentinel last-resort fallback so math never divides by zero. NaNs are worse than a slightly-wrong aspect ratio.

### Functions

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`ConstructCameraFromTypeAsset`](#constructcamerafromtypeasset)  | Populate a freshly-spawned [AComposableCameraCameraBase](../actors/AComposableCameraCameraBase.md#acomposablecameracamerabase) from a type asset and a caller-provided parameter block. |
| `bool` | [`PinTypeToPropertyBagType`](#pintypetopropertybagtype)  | Map an EComposableCameraPinType (+ struct / enum metadata) to the matching EPropertyBagPropertyType and ValueTypeObject expected by FInstancedPropertyBag::AddProperty. |
| `bool` | [`TryGetEffectiveViewportSize`](#trygeteffectiveviewportsize)  | Get the effective viewport size in pixels. Returns true when the value came from a real source (PCM / GameViewport / editor viewport); false when OutSize is the fallback 1920×1080. Callers that need a different fallback behavior can branch on the return value. |
| `float` | [`GetEffectiveViewportAspectRatio`](#geteffectiveviewportaspectratio)  | Convenience wrapper — returns aspect ratio (width / height) from the resolved viewport size. Always returns a finite positive number; falls back to 16:9 if no real source is available. |

---

#### ConstructCameraFromTypeAsset { #constructcamerafromtypeasset }

```cpp
void ConstructCameraFromTypeAsset(AComposableCameraCameraBase * Camera, UComposableCameraTypeAsset * TypeAsset, const FComposableCameraParameterBlock & ParameterBlock)
```

Populate a freshly-spawned [AComposableCameraCameraBase](../actors/AComposableCameraCameraBase.md#acomposablecameracamerabase) from a type asset and a caller-provided parameter block.

Does all the work that used to live exclusively inside AComposableCameraPlayerCameraManager::OnTypeAssetCameraConstructed:

* Duplicates node templates into Camera->CameraNodes / Camera->ComputeNodes (nulling out orphans — nodes not referenced by any execution chain — to preserve index correspondence with TypeAsset->NodeTemplates while saving memory and init cost).

* Allocates Camera->OwnedRuntimeDataBlock via TypeAsset->BuildRuntimeDataLayout.

* Applies ParameterBlock via TypeAsset->ApplyParameterBlock (POD bytes) and TypeAsset->ApplyDelegateBindings (delegate UPROPERTYs — can't live in the POD data block).

* Wires the data block to each node via SetRuntimeDataBlock(..., NodeIndex). Compute nodes use the offset index space NodeIndex = TypeAsset->NodeTemplates.Num() + ComputeIdx to match the layout that BuildRuntimeDataLayout allocated.

* Copies FullExecChain / ComputeFullExecChain from the asset onto the camera.

* Performs the legacy ComputeNodes reorder only when ComputeFullExecChain is empty (pre-existing compatibility for assets saved before the full exec chain existed).

* Calls Camera->InitializeNodes() so every populated node's OnInitialize fires exactly once, with OwningCamera / OwningPlayerCameraManager / RuntimeDataBlock all wired.

* Duplicates the type asset's EnterTransition onto the camera.

PCM-independent by construction: does not read or write any PCM state. The existing PCM activation path calls this from its OnTypeAssetCameraConstructed dynamic-delegate callback (a thin wrapper); the Level Sequence component path will call this directly after spawning its internal camera with a null PCM. Nodes on the camera see whatever CameraManager value was passed into Camera->Initialize earlier (nullptr is valid — see [AComposableCameraCameraBase::Initialize](../actors/AComposableCameraCameraBase.md#initialize) and individual node GetLevelSequenceCompatibility overrides).

Early-returns if Camera or TypeAsset is null; does not log.

**Parameters**

* `Camera` Target camera actor. Expected freshly spawned with CameraNodes / ComputeNodes empty; any pre-existing entries are cleared inside. 

* `TypeAsset` Source type asset. Its NodeTemplates / ComputeNodeTemplates are duplicated into Camera; the asset itself is not modified. 

* `ParameterBlock` Caller-provided parameter values. Stored on Camera as SourceParameterBlock for reactivation on modifier changes.

---

#### PinTypeToPropertyBagType { #pintypetopropertybagtype }

```cpp
bool PinTypeToPropertyBagType(EComposableCameraPinType InPinType, const UScriptStruct * InStructType, const UEnum * InEnumType, EPropertyBagPropertyType & OutBagPropertyType, const UObject *& OutValueTypeObject)
```

Map an EComposableCameraPinType (+ struct / enum metadata) to the matching EPropertyBagPropertyType and ValueTypeObject expected by FInstancedPropertyBag::AddProperty.

Returns false for unsupported pin types (currently just Delegate); callers should skip those entries rather than adding them to the bag.

**Parameters**

* `InPinType` Source pin type. 

* `InStructType` Only read when InPinType == Struct; ignored otherwise. 

* `InEnumType` Only read when InPinType == Enum; ignored otherwise. 

* `OutBagPropertyType` Resulting bag property type. 

* `OutValueTypeObject` Struct / class / enum object carried alongside OutBagPropertyType. nullptr for POD types.

---

#### TryGetEffectiveViewportSize { #trygeteffectiveviewportsize }

```cpp
bool TryGetEffectiveViewportSize(const AComposableCameraPlayerCameraManager * OptionalPCM, FIntPoint & OutSize)
```

Get the effective viewport size in pixels. Returns true when the value came from a real source (PCM / GameViewport / editor viewport); false when OutSize is the fallback 1920×1080. Callers that need a different fallback behavior can branch on the return value.

---

#### GetEffectiveViewportAspectRatio { #geteffectiveviewportaspectratio }

```cpp
float GetEffectiveViewportAspectRatio(const AComposableCameraPlayerCameraManager * OptionalPCM)
```

Convenience wrapper — returns aspect ratio (width / height) from the resolved viewport size. Always returns a finite positive number; falls back to 16:9 if no real source is available.

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
