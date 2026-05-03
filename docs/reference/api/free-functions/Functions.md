

# Functions

#### DECLARE_DELEGATE_RetVal { #declare_delegate_retval }

```cpp
DECLARE_DELEGATE_RetVal(bool, FGetIsSimulatingInEditor)
```

#### DECLARE_DELEGATE_TwoParams { #declare_delegate_twoparams }

```cpp
DECLARE_DELEGATE_TwoParams(FOpenShotEditorRequest, FComposableCameraShot *, UObject *)
```

Bridge for "open the Shot Editor for this Shot" calls coming from runtime UFUNCTION(CallInEditor) buttons (currently `UComposableCameraCompositionFramingNode::OpenShotEditor`, future Phase E LS Section context menu).

The runtime module declares the hook and exposes a guarded execute helper; the editor module binds the hook in `FComposableCameraSystemEditorModule::StartupModule` to the actual tab-spawning logic in `Editors/ComposableCameraShotEditor.h`.

Parameters:

* `Shot` : pointer to the Shot data the editor should bind to. Must remain valid for as long as the host UObject is alive (the editor stores a raw pointer + a TWeakObjectPtr to the host for liveness checks).

* `HostObject`: the UObject that OWNS `Shot` (e.g. the `[UComposableCameraCompositionFramingNode](../nodes/UComposableCameraCompositionFramingNode.md#ucomposablecameracompositionframingnode)` whose UPROPERTY is the Shot, or the future LS Shot Section). Used by the editor for transaction context, MarkPackageDirty, and liveness invalidation when the host is GC'd.

#### DECLARE_DELEGATE_RetVal_OneParam { #declare_delegate_retval_oneparam }

```cpp
DECLARE_DELEGATE_RetVal_OneParam(bool, FGetActiveEditorViewportSize, FIntPoint &)
```

Editor-world viewport size resolver. Bound by the editor module to `GEditor->GetActiveViewport()->GetSizeXY()` (or the perspective level viewport's size). Lets runtime helpers — `TryGetEffectiveViewportSize` specifically — return the actual editor-scrub viewport dimensions instead of a hardcoded 1920×1080 fallback. Without this, the Composition Solver runs with a wrong aspect during editor scrub of LS Spawnables, causing anchor screen positions to drift from what designers see in the Shot Editor preview.

Returns false when no editor viewport is resolvable (cooked builds, very early startup, headless commandlet) — caller falls back through later resolution steps.

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

#### DECLARE_STATS_GROUP { #declare_stats_group }

```cpp
DECLARE_STATS_GROUP(TEXT("ComposableCamera"), STATGROUP_CCS, STATCAT_Advanced)
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

Debug formatters used by the ShowDebug HUD (runtime) and the editor debug overlay (WITH_EDITOR). Two faces per formatter:

AppendX(Builder, ...) — writes into a caller-provided FStringBuilderBase. Zero-alloc as long as the builder's inline buffer is big enough (TStringBuilder<256> comfortably fits any single pin value). Use this on any hot path that produces one text line per tick.

FormatX(...) — returns a freshly-allocated FString. Thin wrapper around AppendX. Kept for cold call sites (property customizations, tests, showdebug sub-headers). Do NOT introduce new hot-path uses.

### Functions

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`AppendFloat`](#appendfloat) `inline` | Append a float to the builder with 2-decimal precision. |
| `void` | [`AppendVector`](#appendvector) `inline` | Append an FVector in `(X, Y, Z)` form, 1-decimal precision. |
| `void` | [`AppendRotator`](#appendrotator) `inline` | Append an FRotator in `(P=..., Y=..., R=...)` form, 1-decimal precision. |
| `void` | [`AppendTransform`](#appendtransform) `inline` | Append an FTransform with Loc/Rot/Scale components. |
| `void` | [`AppendTypedValue`](#appendtypedvalue) `inline` | Read a typed value at a byte offset from the data block and append as text. EnumType is consulted only when PinType == Enum; when supplied, the int64 slot is rendered as the authored entry name. When omitted for an Enum slot, the raw int64 is printed so debug output never silently lies about the slot. |
| `void` | [`AppendOutputPinValue`](#appendoutputpinvalue) `inline` | Read a typed output pin value from the data block and append as text. |
| `void` | [`AppendIndent`](#appendindent) `inline` | Append `N` spaces to the builder. |
| `void` | [`AppendTreeNodeLine`](#appendtreenodeline) `inline` | Append one tree-node snapshot as a single text line (no trailing newline). `BaseIndentCols` is the number of spaces prefixed before the per-depth indent (2 spaces per Depth level). Used by both `showdebug camera` and any future dump command that emits the tree as text. |
| `FString` | [`FormatFloat`](#formatfloat) `inline` |  |
| `FString` | [`FormatVector`](#formatvector) `inline` |  |
| `FString` | [`FormatRotator`](#formatrotator) `inline` |  |
| `FString` | [`FormatTransform`](#formattransform) `inline` |  |
| `FString` | [`FormatTypedValue`](#formattypedvalue) `inline` |  |
| `FString` | [`FormatOutputPinValue`](#formatoutputpinvalue) `inline` |  |

---

#### AppendFloat { #appendfloat }

`inline`

```cpp
inline void AppendFloat(FStringBuilderBase & Builder, double Value)
```

Append a float to the builder with 2-decimal precision.

---

#### AppendVector { #appendvector }

`inline`

```cpp
inline void AppendVector(FStringBuilderBase & Builder, const FVector & V)
```

Append an FVector in `(X, Y, Z)` form, 1-decimal precision.

---

#### AppendRotator { #appendrotator }

`inline`

```cpp
inline void AppendRotator(FStringBuilderBase & Builder, const FRotator & R)
```

Append an FRotator in `(P=..., Y=..., R=...)` form, 1-decimal precision.

---

#### AppendTransform { #appendtransform }

`inline`

```cpp
inline void AppendTransform(FStringBuilderBase & Builder, const FTransform & T)
```

Append an FTransform with Loc/Rot/Scale components.

---

#### AppendTypedValue { #appendtypedvalue }

`inline`

```cpp
inline void AppendTypedValue(FStringBuilderBase & Builder, const FComposableCameraRuntimeDataBlock & DataBlock, int32 Offset, EComposableCameraPinType PinType, const UEnum * EnumType)
```

Read a typed value at a byte offset from the data block and append as text. EnumType is consulted only when PinType == Enum; when supplied, the int64 slot is rendered as the authored entry name. When omitted for an Enum slot, the raw int64 is printed so debug output never silently lies about the slot.

---

#### AppendOutputPinValue { #appendoutputpinvalue }

`inline`

```cpp
inline void AppendOutputPinValue(FStringBuilderBase & Builder, const FComposableCameraRuntimeDataBlock & DataBlock, int32 NodeIndex, FName PinName, EComposableCameraPinType PinType, const UEnum * EnumType)
```

Read a typed output pin value from the data block and append as text.

---

#### AppendIndent { #appendindent }

`inline`

```cpp
inline void AppendIndent(FStringBuilderBase & Builder, int32 N)
```

Append `N` spaces to the builder.

---

#### AppendTreeNodeLine { #appendtreenodeline }

`inline`

```cpp
inline void AppendTreeNodeLine(FStringBuilderBase & Builder, const FComposableCameraTreeNodeSnapshot & Node, int32 BaseIndentCols)
```

Append one tree-node snapshot as a single text line (no trailing newline). `BaseIndentCols` is the number of spaces prefixed before the per-depth indent (2 spaces per Depth level). Used by both `showdebug camera` and any future dump command that emits the tree as text.

---

#### FormatFloat { #formatfloat }

`inline`

```cpp
inline FString FormatFloat(double Value)
```

---

#### FormatVector { #formatvector }

`inline`

```cpp
inline FString FormatVector(const FVector & V)
```

---

#### FormatRotator { #formatrotator }

`inline`

```cpp
inline FString FormatRotator(const FRotator & R)
```

---

#### FormatTransform { #formattransform }

`inline`

```cpp
inline FString FormatTransform(const FTransform & T)
```

---

#### FormatTypedValue { #formattypedvalue }

`inline`

```cpp
inline FString FormatTypedValue(const FComposableCameraRuntimeDataBlock & DataBlock, int32 Offset, EComposableCameraPinType PinType, const UEnum * EnumType)
```

---

#### FormatOutputPinValue { #formatoutputpinvalue }

`inline`

```cpp
inline FString FormatOutputPinValue(const FComposableCameraRuntimeDataBlock & DataBlock, int32 NodeIndex, FName PinName, EComposableCameraPinType PinType, const UEnum * EnumType)
```

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
| `std::pair< float, float >` | [`SolveCameraRotationForScreenTarget`](#solvecamerarotationforscreentarget) `inline` | Closed-form solver for (Pitch X, Yaw Y) rotation (Roll = 0) such that the world-space ray `Direction` (from camera origin) projects onto the normalized screen coords `(ScreenX, ScreenY)` ∈ [-0.5, 0.5]². Returns { Pitch, Yaw } in degrees, UE convention (positive pitch = up, positive yaw = right). Replaces the iterative Newton solver formerly duplicated inside ScreenSpacePivotNode and ScreenSpaceConstraintsNode. |
| `bool` | [`ProjectWorldPointToScreen`](#projectworldpointtoscreen) `inline` | Forward projection: a world point → normalized screen coords [-0.5, 0.5]², matching the convention used by SafeZoneCenter on ScreenSpacePivotNode and Placement.ScreenPosition / Aim.ScreenPosition on the Shot data structs. |
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

#### SolveCameraRotationForScreenTarget { #solvecamerarotationforscreentarget }

`inline`

```cpp
inline std::pair< float, float > SolveCameraRotationForScreenTarget(float TanHalfHOR, float AspectRatio, const FVector & Direction, float ScreenX, float ScreenY)
```

Closed-form solver for (Pitch X, Yaw Y) rotation (Roll = 0) such that the world-space ray `Direction` (from camera origin) projects onto the normalized screen coords `(ScreenX, ScreenY)` ∈ [-0.5, 0.5]². Returns { Pitch, Yaw } in degrees, UE convention (positive pitch = up, positive yaw = right). Replaces the iterative Newton solver formerly duplicated inside ScreenSpacePivotNode and ScreenSpaceConstraintsNode.

──** Derivation**

Camera basis under (Pitch X, Yaw Y, Roll 0), expressed in world frame: F = ( cos X cos Y,  cos X sin Y,  sin X)        // forward (cam +X)
R = (-sin Y,        cos Y,        0    )        // right   (cam +Y)
U = (-sin X cos Y, -sin X sin Y,  cos X)        // up      (cam +Z)
 Direction in camera space is Px = F·D, Py = R·D, Pz = U·D, with D = (A, B, C) = Direction.

Screen mapping is Py / (2·m·Px) and Pz / (2·n·Px) where m = TanHalfHOR and n = TanHalfHOR / AspectRatio. Letting u = 2·ScreenX·m, v = 2·ScreenY·n, the constraint is Py = u·Px,    Pz = v·Px                                   (★)
 (★) ⇔ (Px, Py, Pz) ∝ (1, u, v). Geometrically: the pivot must lie on the ray from camera origin through the screen-plane point (1, u, v). The unit direction in camera space is therefore d_cam = (1, u, v) / s,    s = √(1 + u² + v²)
 The same physical ray in world frame is d_world = D / L, with L = ‖D‖. With R the camera-to-world rotation matrix (whose columns are F, R, U), R · (1, u, v)ᵀ = K · (A, B, C)ᵀ        where K ≡ s / L
 Component-wise: cos X cos Y - u sin Y - v sin X cos Y = K·A           (I)
cos X sin Y + u cos Y - v sin X sin Y = K·B           (II)
sin X            + v cos X            = K·C           (III)
 (III) contains only X — that is why the system decouples.

Solve X. By the harmonic identity sin X + v cos X = √(1+v²) · sin(X + arctan v), (III) becomes X = arcsin(K·C / √(1+v²)) - arctan v ─── (X) The other branch X = π - arcsin(...) - arctan v corresponds to a back-facing camera and is discarded.

Solve Y. With X known, let α = cos X - v sin X. (I)+(II) become a 2×2 linear system in (cos Y, sin Y): [α  -u] [cos Y]     [A]
[u   α] [sin Y] = K [B]
 Determinant α² + u² > 0 generically, Cramer gives a Y where K cancels: Y = atan2(α·B - u·A,  α·A + u·B)                   ─── (Y)
 Y is independent of ‖D‖ — depends only on the direction of D.

Consistency. (X)+(III) automatically imply α² + u² = K²(A² + B²), i.e. (cos Y, sin Y) lies on the unit circle — no extra check required in the regular regime.

──** Edge cases**

|T| > 1, T ≡ K·C / √(1+v²) The pivot cannot be placed at (ScreenX, ScreenY) without exceeding the FOV cone. Clamped to ±1 so the pivot lands at the closest reachable on-FOV pitch. EnsureWithinBoundsRotation callers usually pre-clamp to a safe zone, so this hits only when the pivot direction itself is outside the FOV.

A² + B² → 0 Direction parallel to world ±Z (gimbal lock). Yaw is genuinely indeterminate at this configuration — a property of the Pitch+Yaw parameterization, not of the algorithm. Returns Yaw = 0 as the stable choice.

L < ε Zero-length Direction (pivot at camera position). Returns (0, 0); upstream code should guard before calling here.

---

#### ProjectWorldPointToScreen { #projectworldpointtoscreen }

`inline`

```cpp
inline bool ProjectWorldPointToScreen(const FVector & WorldPoint, const FVector & CameraPos, const FRotator & CameraRot, float TanHalfHOR, float AspectRatio, FVector2D & OutScreenCoord)
```

Forward projection: a world point → normalized screen coords [-0.5, 0.5]², matching the convention used by SafeZoneCenter on ScreenSpacePivotNode and Placement.ScreenPosition / Aim.ScreenPosition on the Shot data structs.

Companion to SolveCameraRotationForScreenTarget (which goes the other direction). Both use the same projection model and the same screen-coord convention so callers can round-trip cleanly.

1. Transform WorldPoint into camera space: P_cam = R⁻¹ · (WorldPoint - CameraPos) where R is the camera-to-world rotation. Px = depth (forward), Py = right, Pz = up.

1. If Px <= 0, the point is behind the camera or on the near plane — no valid screen projection. Returns false; OutScreenCoord left unchanged.

1. Apply the perspective division using the screen-coord convention (Py / (2m·Px), Pz / (2n·Px)) where m = tan(FOV_h/2), n = m / AspectRatio.

**Parameters**

* `WorldPoint` Point to project. 

* `CameraPos` Camera world position. 

* `CameraRot` Camera world rotation (Pitch, Yaw, Roll allowed). 

* `TanHalfHOR` tan(FOV_horizontal / 2). Same input convention as SolveCameraRotationForScreenTarget. 

* `AspectRatio` Viewport aspect ratio (width / height). 

* `OutScreenCoord` Normalized screen coords in [-0.5, 0.5]² when the point is on screen — but values OUTSIDE that range are returned for off-screen points (no clamping). The Composition Solver's micro-refinement pass uses the unclamped values as a gradient signal.

**Returns**

True iff the point is in front of the camera (Px > 0).

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
| `float` | [`GetEffectiveAspectRatioForCineCamera`](#geteffectiveaspectratioforcinecamera)  | Resolve the effective render aspect for a specific `UCineCameraComponent` — what the renderer ACTUALLY uses, not just the viewport raw aspect. |

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

---

#### GetEffectiveAspectRatioForCineCamera { #geteffectiveaspectratioforcinecamera }

```cpp
float GetEffectiveAspectRatioForCineCamera(const UCineCameraComponent * CineCam, const AComposableCameraPlayerCameraManager * OptionalPCM)
```

Resolve the effective render aspect for a specific `UCineCameraComponent` — what the renderer ACTUALLY uses, not just the viewport raw aspect.

* `CineCam->bConstrainAspectRatio == true` → return `CineCam->AspectRatio` (filmback-derived). Renderer letterboxes to this aspect regardless of the viewport's actual shape, so the solver should match.

* `CineCam->bConstrainAspectRatio == false` → return the actual viewport aspect (PCM / GameViewport / editor viewport via `TryGetEffectiveViewportSize`). Renderer adapts to viewport, so the solver tracks real-time when designers resize the level viewport.

Used by the Composition Solver via `FShotSolveContext::ViewportAspectRatio` so anchor screen positions match between the Shot Editor preview and LS playback regardless of CineCam constraint state. Falls back to `GetEffectiveViewportAspectRatio` when `CineCam` is null.

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
