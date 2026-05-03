
# UComposableCameraCameraNodeBase { #ucomposablecameracameranodebase }

```cpp
#include <ComposableCameraCameraNodeBase.h>
```

> **Inherits:** `UObject`
> **Subclassed by:** [`UComposableCameraAutoRotateNode`](../nodes/UComposableCameraAutoRotateNode.md#ucomposablecameraautorotatenode), [`UComposableCameraBlueprintCameraNode`](../nodes/UComposableCameraBlueprintCameraNode.md#ucomposablecamerablueprintcameranode), [`UComposableCameraCameraOffsetNode`](../nodes/UComposableCameraCameraOffsetNode.md#ucomposablecameracameraoffsetnode), [`UComposableCameraCollisionPushNode`](../nodes/UComposableCameraCollisionPushNode.md#ucomposablecameracollisionpushnode), [`UComposableCameraCompositionFramingNode`](../nodes/UComposableCameraCompositionFramingNode.md#ucomposablecameracompositionframingnode), [`UComposableCameraComputeNodeBase`](UComposableCameraComputeNodeBase.md#ucomposablecameracomputenodebase), [`UComposableCameraControlRotateNode`](../nodes/UComposableCameraControlRotateNode.md#ucomposablecameracontrolrotatenode), [`UComposableCameraFieldOfViewNode`](../nodes/UComposableCameraFieldOfViewNode.md#ucomposablecamerafieldofviewnode), [`UComposableCameraFilmbackNode`](../nodes/UComposableCameraFilmbackNode.md#ucomposablecamerafilmbacknode), [`UComposableCameraFocusPullNode`](../nodes/UComposableCameraFocusPullNode.md#ucomposablecamerafocuspullnode), [`UComposableCameraHitchcockZoomNode`](../nodes/UComposableCameraHitchcockZoomNode.md#ucomposablecamerahitchcockzoomnode), [`UComposableCameraImpulseResolutionNode`](../nodes/UComposableCameraImpulseResolutionNode.md#ucomposablecameraimpulseresolutionnode), [`UComposableCameraLensNode`](../nodes/UComposableCameraLensNode.md#ucomposablecameralensnode), [`UComposableCameraLookAtNode`](../nodes/UComposableCameraLookAtNode.md#ucomposablecameralookatnode), [`UComposableCameraMixingCameraNode`](../nodes/UComposableCameraMixingCameraNode.md#ucomposablecameramixingcameranode), [`UComposableCameraOcclusionFadeNode`](../nodes/UComposableCameraOcclusionFadeNode.md#ucomposablecameraocclusionfadenode), [`UComposableCameraOrthographicNode`](../nodes/UComposableCameraOrthographicNode.md#ucomposablecameraorthographicnode), [`UComposableCameraPivotDampingNode`](../nodes/UComposableCameraPivotDampingNode.md#ucomposablecamerapivotdampingnode), [`UComposableCameraPivotOffsetNode`](../nodes/UComposableCameraPivotOffsetNode.md#ucomposablecamerapivotoffsetnode), [`UComposableCameraPivotRotateNode`](../nodes/UComposableCameraPivotRotateNode.md#ucomposablecamerapivotrotatenode), [`UComposableCameraPostProcessNode`](../nodes/UComposableCameraPostProcessNode.md#ucomposablecamerapostprocessnode), [`UComposableCameraReceivePivotActorNode`](../nodes/UComposableCameraReceivePivotActorNode.md#ucomposablecamerareceivepivotactornode), [`UComposableCameraRelativeFixedPoseNode`](../nodes/UComposableCameraRelativeFixedPoseNode.md#ucomposablecamerarelativefixedposenode), [`UComposableCameraRotationConstraints`](UComposableCameraRotationConstraints.md#ucomposablecamerarotationconstraints), [`UComposableCameraScreenSpaceConstraintsNode`](../nodes/UComposableCameraScreenSpaceConstraintsNode.md#ucomposablecamerascreenspaceconstraintsnode), [`UComposableCameraScreenSpacePivotNode`](../nodes/UComposableCameraScreenSpacePivotNode.md#ucomposablecamerascreenspacepivotnode), [`UComposableCameraSpiralNode`](../nodes/UComposableCameraSpiralNode.md#ucomposablecameraspiralnode), [`UComposableCameraSplineNode`](../splines/UComposableCameraSplineNode.md#ucomposablecamerasplinenode), [`UComposableCameraViewTargetProxyNode`](../nodes/UComposableCameraViewTargetProxyNode.md#ucomposablecameraviewtargetproxynode), [`UComposableCameraVolumeConstraintNode`](../nodes/UComposableCameraVolumeConstraintNode.md#ucomposablecameravolumeconstraintnode)

Base node for all camera nodes.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FName` | [`PaletteCategory`](#palettecategory)  | Palette category in the camera-editor "Add Node" context menu. The schema reads this off the CDO and nests it under the existing "Camera Nodes" / "Compute Nodes" root via UE's "\|"-separated category path, so a value of "Rotation" surfaces as Camera Nodes → Rotation. C++ nodes set this in their constructor; Blueprint nodes (subclasses of [UComposableCameraBlueprintCameraNode](../nodes/UComposableCameraBlueprintCameraNode.md#ucomposablecamerablueprintcameranode)) set it in Class Defaults. Default "Misc" is intentional — unset nodes still appear, but they cluster in one bucket so the author notices and assigns a real category. Stored as FName for POD comparison and pool reuse; mapped to FText at palette-build time via FText::FromName. |

---

#### PaletteCategory { #palettecategory }

```cpp
FName PaletteCategory = TEXT("Misc")
```

Palette category in the camera-editor "Add Node" context menu. The schema reads this off the CDO and nests it under the existing "Camera Nodes" / "Compute Nodes" root via UE's "|"-separated category path, so a value of "Rotation" surfaces as Camera Nodes → Rotation. C++ nodes set this in their constructor; Blueprint nodes (subclasses of [UComposableCameraBlueprintCameraNode](../nodes/UComposableCameraBlueprintCameraNode.md#ucomposablecamerablueprintcameranode)) set it in Class Defaults. Default "Misc" is intentional — unset nodes still appear, but they cluster in one bucket so the author notices and assigns a real category. Stored as FName for POD comparison and pool reuse; mapped to FText at palette-build time via FText::FromName.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`Initialize`](#initialize-3)  |  |
| `void` | [`TickNode`](#ticknode)  |  |
| `FGameplayTag` | [`GetOwningCameraTag`](#getowningcameratag) `const` |  |
| `AComposableCameraCameraBase *` | [`GetOwningCamera`](#getowningcamera) `const` `inline` |  |
| `AComposableCameraPlayerCameraManager *` | [`GetOwningPlayerCameraManager`](#getowningplayercameramanager-1) `const` `inline` |  |
| `EComposableCameraNodeLevelSequenceCompatibility` | [`GetLevelSequenceCompatibility`](#getlevelsequencecompatibility) `const` | Declare how this node behaves when evaluated without a PCM (Level Sequence path). Default: Compatible. Override on nodes that need the viewport / player controller / HUD, or that spawn new cameras through the PCM. See the enum comment. |
| `EComposableCameraNodeLevelSequenceCompatibility` | [`GetLevelSequenceCompatibility_Implementation`](#getlevelsequencecompatibility_implementation) `virtual` `const` `inline` |  |
| `EComposableCameraNodePatchCompatibility` | [`GetPatchCompatibility`](#getpatchcompatibility) `const` | Declare how this node behaves when placed in a Camera Patch graph (PatchSystemProposal §11). Default: Compatible. Override on nodes that synthesize pose from scratch (Incompatible) or have surprising semantics when reading from an upstream pose (CompatibleWithCaveat). |
| `EComposableCameraNodePatchCompatibility` | [`GetPatchCompatibility_Implementation`](#getpatchcompatibility_implementation) `virtual` `const` `inline` |  |
| `void` | [`GetPinDeclarations`](#getpindeclarations) `const` | Declare this node's input and output data pins. Override in subclasses to define pins. The editor reads these to generate visual pins, and the runtime uses them to allocate the RuntimeDataBlock. |
| `void` | [`GetPinDeclarations_Implementation`](#getpindeclarations_implementation-7) `virtual` `const` `inline` |  |
| `void` | [`SetRuntimeDataBlock`](#setruntimedatablock) `inline` | Set the runtime data block for this node. Called during camera instantiation from type assets. |
| `bool` | [`HasRuntimeDataBlock`](#hasruntimedatablock) `const` `inline` | Check if this node has a RuntimeDataBlock attached. |
| `void` | [`GatherAllPinDeclarations`](#gatherallpindeclarations) `const` | Gather ALL pin declarations: calls [GetPinDeclarations()](#getpindeclarations) (the virtual chain), then auto-appends pins for every Instanced subobject UPROPERTY on this node. |
| `void` | [`DeclareSubobjectPins`](#declaresubobjectpins) `const` | Generate pin declarations for an Instanced subobject's EditAnywhere properties. |
| `void` | [`ApplySubobjectPinValues`](#applysubobjectpinvalues)  | Apply resolved pin values to an Instanced subobject's properties. |
| `void` | [`ResolveAllInputPins`](#resolveallinputpins)  | Re-resolve every declared top-level input pin into its matching UPROPERTY field on this node. Called automatically by [TickNode()](#ticknode) before [OnTickNode()](#onticknode) when [ShouldAutoResolveInputPins()](#shouldautoresolveinputpins) returns true. |
| `T` | [`GetInputPinValue`](#getinputpinvalue) `const` | Read an input pin's resolved value. Checks wired → exposed → default. |
| `void` | [`SetOutputPinValue`](#setoutputpinvalue)  | Write an output pin's value to the RuntimeDataBlock. |
| `T` | [`GetInternalVariable`](#getinternalvariable) `const` | Read a camera-level internal variable. |
| `void` | [`SetInternalVariable`](#setinternalvariable)  | Write a camera-level internal variable. |
| `bool` | [`GetInputPinValueBool`](#getinputpinvaluebool) `const` |  |
| `int32` | [`GetInputPinValueInt32`](#getinputpinvalueint32) `const` |  |
| `float` | [`GetInputPinValueFloat`](#getinputpinvaluefloat) `const` |  |
| `double` | [`GetInputPinValueDouble`](#getinputpinvaluedouble) `const` |  |
| `FVector` | [`GetInputPinValueVector`](#getinputpinvaluevector) `const` |  |
| `FRotator` | [`GetInputPinValueRotator`](#getinputpinvaluerotator) `const` |  |
| `FTransform` | [`GetInputPinValueTransform`](#getinputpinvaluetransform) `const` |  |
| `AActor *` | [`GetInputPinValueActor`](#getinputpinvalueactor) `const` |  |
| `FName` | [`GetInputPinValueName`](#getinputpinvaluename) `const` |  |
| `void` | [`GetInputPinValueEnum`](#getinputpinvalueenum) `const` | Read an enum input pin's resolved value into a wildcard enum out parameter. The runtime data block stores enum slots as a normalized int64 (see GetPinTypeSize / WriteEnumInt64ToProperty). The Blueprint-facing property bound to OutValue may be FEnumProperty (underlying numeric width may be uint8/int32/int64) or FByteProperty (always uint8). We narrow-cast the int64 into the caller's property at execution time to keep the BP thunk symmetric with SetParameterBlockValue in ComposableCameraBlueprintLibrary. |
|  | [`DECLARE_FUNCTION`](#declare_function) `inline` |  |
| `void` | [`SetOutputPinValueBool`](#setoutputpinvaluebool)  |  |
| `void` | [`SetOutputPinValueInt32`](#setoutputpinvalueint32)  |  |
| `void` | [`SetOutputPinValueFloat`](#setoutputpinvaluefloat)  |  |
| `void` | [`SetOutputPinValueDouble`](#setoutputpinvaluedouble)  |  |
| `void` | [`SetOutputPinValueVector`](#setoutputpinvaluevector)  |  |
| `void` | [`SetOutputPinValueRotator`](#setoutputpinvaluerotator)  |  |
| `void` | [`SetOutputPinValueTransform`](#setoutputpinvaluetransform)  |  |
| `void` | [`SetOutputPinValueActor`](#setoutputpinvalueactor)  |  |
| `void` | [`SetOutputPinValueName`](#setoutputpinvaluename)  |  |
| `void` | [`SetOutputPinValueEnum`](#setoutputpinvalueenum)  | Write a wildcard enum value to an output pin. Mirrors GetInputPinValueEnum — reads the enum from the caller's property (FEnumProperty or FByteProperty) via the numeric-property API, normalizes to int64, and stores it in the data block slot. Callers on the consumer side read it back through the same int64 channel (see ResolveAllInputPins). |
|  | [`DECLARE_FUNCTION`](#declare_function-1) `inline` |  |
| `float` | [`GetInternalVariableFloat`](#getinternalvariablefloat) `const` |  |
| `FVector` | [`GetInternalVariableVector`](#getinternalvariablevector) `const` |  |
| `FName` | [`GetInternalVariableName`](#getinternalvariablename) `const` |  |
| `void` | [`GetInternalVariableEnum`](#getinternalvariableenum) `const` | Read an enum internal variable into a wildcard enum out parameter. Storage is a normalized int64; the thunk narrow-casts into the caller's property width. See GetInputPinValueEnum for the same pattern on the pin surface. |
|  | [`DECLARE_FUNCTION`](#declare_function-2) `inline` |  |
| `void` | [`SetInternalVariableFloat`](#setinternalvariablefloat)  |  |
| `void` | [`SetInternalVariableVector`](#setinternalvariablevector)  |  |
| `void` | [`SetInternalVariableName`](#setinternalvariablename)  |  |
| `void` | [`SetInternalVariableEnum`](#setinternalvariableenum)  | Write a wildcard enum value to an internal variable. Normalizes to int64 via the caller's FEnumProperty/FByteProperty and stores in the data block slot — the same representation every other enum consumer reads. |
|  | [`DECLARE_FUNCTION`](#declare_function-3) `inline` |  |
| `void` | [`OnPreTick`](#onpretick-1) `virtual` |  |
| `void` | [`OnPostTick`](#onposttick-1) `virtual` |  |
| `void` | [`DrawNodeDebug`](#drawnodedebug-4) `virtual` `const` `inline` | Called each frame when the `CCS.Debug.Viewport` CVar is enabled, for every node on the currently running camera. Override to draw world-space debug gizmos via `DrawDebugHelpers` (DrawDebugSphere, DrawDebugLine, etc.) that visualise this node's runtime state — e.g. a pivot sphere for PivotOffsetNode, a look-at line for LookAtNode, the collision trace for CollisionPushNode, a sampled spline path for SplineNode. |
| `void` | [`DrawNodeDebug2D`](#drawnodedebug2d) `virtual` `const` `inline` | 2D counterpart to DrawNodeDebug. Fires from a separate UDebugDrawService hook on the "Game" channel — which means it runs during PIE-possessed play (and standalone), NOT during F8 eject (editor viewport doesn't route through the game channel). That lines up with what 2D overlays are good for: screen-space debug that the player-eye perspective answers and an external view cannot (safe-zone rectangles, projected pivot markers, HUD-space gizmos). |

---

#### Initialize { #initialize-3 }

```cpp
void Initialize(AComposableCameraCameraBase * InOwningCamera, AComposableCameraPlayerCameraManager * InPlayerCameraManager)
```

---

#### TickNode { #ticknode }

```cpp
void TickNode(float DeltaTime, const FComposableCameraPose CurrentCameraPose, FComposableCameraPose & OutCameraPose)
```

---

#### GetOwningCameraTag { #getowningcameratag }

`const`

```cpp
FGameplayTag GetOwningCameraTag() const
```

---

#### GetOwningCamera { #getowningcamera }

`const` `inline`

```cpp
inline AComposableCameraCameraBase * GetOwningCamera() const
```

---

#### GetOwningPlayerCameraManager { #getowningplayercameramanager-1 }

`const` `inline`

```cpp
inline AComposableCameraPlayerCameraManager * GetOwningPlayerCameraManager() const
```

---

#### GetLevelSequenceCompatibility { #getlevelsequencecompatibility }

`const`

```cpp
EComposableCameraNodeLevelSequenceCompatibility GetLevelSequenceCompatibility() const
```

Declare how this node behaves when evaluated without a PCM (Level Sequence path). Default: Compatible. Override on nodes that need the viewport / player controller / HUD, or that spawn new cameras through the PCM. See the enum comment.

BlueprintNativeEvent so BP-authored camera nodes (subclasses of [UComposableCameraBlueprintCameraNode](../nodes/UComposableCameraBlueprintCameraNode.md#ucomposablecamerablueprintcameranode)) can declare their compatibility alongside native nodes. C++ overrides go on the _Implementation below; Blueprint subclasses override via a "Get Level Sequence Compatibility" BlueprintImplementableEvent node in their graph. External callers use the plain method name — the generated dispatcher routes to the BP override if present, else the _Implementation.

---

#### GetLevelSequenceCompatibility_Implementation { #getlevelsequencecompatibility_implementation }

`virtual` `const` `inline`

```cpp
virtual inline EComposableCameraNodeLevelSequenceCompatibility GetLevelSequenceCompatibility_Implementation() const
```

---

#### GetPatchCompatibility { #getpatchcompatibility }

`const`

```cpp
EComposableCameraNodePatchCompatibility GetPatchCompatibility() const
```

Declare how this node behaves when placed in a Camera Patch graph (PatchSystemProposal §11). Default: Compatible. Override on nodes that synthesize pose from scratch (Incompatible) or have surprising semantics when reading from an upstream pose (CompatibleWithCaveat).

BlueprintNativeEvent to mirror GetLevelSequenceCompatibility's idiom — BP-authored camera nodes (subclasses of [UComposableCameraBlueprintCameraNode](../nodes/UComposableCameraBlueprintCameraNode.md#ucomposablecamerablueprintcameranode)) can declare their own compatibility alongside native nodes. C++ overrides go on the _Implementation below; BP subclasses override via a "Get Patch
Compatibility" BlueprintImplementableEvent in their graph.

---

#### GetPatchCompatibility_Implementation { #getpatchcompatibility_implementation }

`virtual` `const` `inline`

```cpp
virtual inline EComposableCameraNodePatchCompatibility GetPatchCompatibility_Implementation() const
```

---

#### GetPinDeclarations { #getpindeclarations }

`const`

```cpp
void GetPinDeclarations(TArray< FComposableCameraNodePinDeclaration > & OutPins) const
```

Declare this node's input and output data pins. Override in subclasses to define pins. The editor reads these to generate visual pins, and the runtime uses them to allocate the RuntimeDataBlock.

Default implementation returns empty (no pins).

---

#### GetPinDeclarations_Implementation { #getpindeclarations_implementation-7 }

`virtual` `const` `inline`

```cpp
virtual inline void GetPinDeclarations_Implementation(TArray< FComposableCameraNodePinDeclaration > & OutPins) const
```

---

#### SetRuntimeDataBlock { #setruntimedatablock }

`inline`

```cpp
inline void SetRuntimeDataBlock(FComposableCameraRuntimeDataBlock * InDataBlock, int32 InNodeIndex)
```

Set the runtime data block for this node. Called during camera instantiation from type assets.

---

#### HasRuntimeDataBlock { #hasruntimedatablock }

`const` `inline`

```cpp
inline bool HasRuntimeDataBlock() const
```

Check if this node has a RuntimeDataBlock attached.

---

#### GatherAllPinDeclarations { #gatherallpindeclarations }

`const`

```cpp
void GatherAllPinDeclarations(TArray< FComposableCameraNodePinDeclaration > & OutPins) const
```

Gather ALL pin declarations: calls [GetPinDeclarations()](#getpindeclarations) (the virtual chain), then auto-appends pins for every Instanced subobject UPROPERTY on this node.

All external callers (editor, type-asset builder, runtime data-block allocator) should call this instead of [GetPinDeclarations()](#getpindeclarations) directly, so that subobject pins are included without per-node boilerplate.

---

#### DeclareSubobjectPins { #declaresubobjectpins }

`const`

```cpp
void DeclareSubobjectPins(FName SubobjectPropertyName, const UObject * Subobject, TArray< FComposableCameraNodePinDeclaration > & OutPins) const
```

Generate pin declarations for an Instanced subobject's EditAnywhere properties.

Iterates the subobject's UClass properties, maps each to an EComposableCameraPinType via TryMapPropertyToPinType, and emits one input pin declaration per mappable property with the compound name "SubobjectPropertyName.FieldName".

Properties tagged meta=(NoPinExposure) are skipped. Null subobjects are handled gracefully (no pins emitted).

Prefer [GatherAllPinDeclarations()](#gatherallpindeclarations) which calls this automatically for every Instanced property. Direct calls are only needed for unusual subobject relationships that reflection cannot discover (e.g. subobjects stored in containers).

---

#### ApplySubobjectPinValues { #applysubobjectpinvalues }

```cpp
void ApplySubobjectPinValues(FName SubobjectPropertyName, UObject * Subobject)
```

Apply resolved pin values to an Instanced subobject's properties.

For each mappable EditAnywhere property on the subobject, checks if the compound pin name has a resolved value in the RuntimeDataBlock (via TryResolveInputPin). If so, writes the value into the subobject's UPROPERTY. If not resolved, the subobject retains its authored (Instanced editor) value.

Safe to call when RuntimeDataBlock is null (no-op).

Prefer letting [Initialize()](#initialize-3) handle this automatically (it calls AutoApplySubobjectPinValues before OnInitialize). Direct calls are only needed for unusual subobject relationships.

---

#### ResolveAllInputPins { #resolveallinputpins }

```cpp
void ResolveAllInputPins()
```

Re-resolve every declared top-level input pin into its matching UPROPERTY field on this node. Called automatically by [TickNode()](#ticknode) before [OnTickNode()](#onticknode) when [ShouldAutoResolveInputPins()](#shouldautoresolveinputpins) returns true.

The binding between a pin and a UPROPERTY is by exact FName match against the name declared in [GetPinDeclarations()](#getpindeclarations). Each matched UPROPERTY must map cleanly to an EComposableCameraPinType (via TryMapPropertyToPinType) — if a pin has no backing UPROPERTY or the types don't align, the pin is skipped here and subclass code must use [GetInputPinValue<T>()](#getinputpinvalue) for it.

Subobject property pins ("Subobject.Field" compound names) are NOT touched by this method — they are handled once at [Initialize()](#initialize-3) via AutoApplySubobjectPinValues().

Performance: the per-class binding table is built once on first use and cached module-locally. Per-frame cost is a tight switch-dispatch loop with no reflection, one raw memory write per matched pin.

---

#### GetInputPinValue { #getinputpinvalue }

`const`

```cpp
template<typename T> T GetInputPinValue(FName PinName) const
```

Read an input pin's resolved value. Checks wired → exposed → default.

---

#### SetOutputPinValue { #setoutputpinvalue }

```cpp
template<typename T> void SetOutputPinValue(FName PinName, const T & Value)
```

Write an output pin's value to the RuntimeDataBlock.

---

#### GetInternalVariable { #getinternalvariable }

`const`

```cpp
template<typename T> T GetInternalVariable(FName VariableName) const
```

Read a camera-level internal variable.

---

#### SetInternalVariable { #setinternalvariable }

```cpp
template<typename T> void SetInternalVariable(FName VariableName, const T & Value)
```

Write a camera-level internal variable.

---

#### GetInputPinValueBool { #getinputpinvaluebool }

`const`

```cpp
bool GetInputPinValueBool(FName PinName) const
```

---

#### GetInputPinValueInt32 { #getinputpinvalueint32 }

`const`

```cpp
int32 GetInputPinValueInt32(FName PinName) const
```

---

#### GetInputPinValueFloat { #getinputpinvaluefloat }

`const`

```cpp
float GetInputPinValueFloat(FName PinName) const
```

---

#### GetInputPinValueDouble { #getinputpinvaluedouble }

`const`

```cpp
double GetInputPinValueDouble(FName PinName) const
```

---

#### GetInputPinValueVector { #getinputpinvaluevector }

`const`

```cpp
FVector GetInputPinValueVector(FName PinName) const
```

---

#### GetInputPinValueRotator { #getinputpinvaluerotator }

`const`

```cpp
FRotator GetInputPinValueRotator(FName PinName) const
```

---

#### GetInputPinValueTransform { #getinputpinvaluetransform }

`const`

```cpp
FTransform GetInputPinValueTransform(FName PinName) const
```

---

#### GetInputPinValueActor { #getinputpinvalueactor }

`const`

```cpp
AActor * GetInputPinValueActor(FName PinName) const
```

---

#### GetInputPinValueName { #getinputpinvaluename }

`const`

```cpp
FName GetInputPinValueName(FName PinName) const
```

---

#### GetInputPinValueEnum { #getinputpinvalueenum }

`const`

```cpp
void GetInputPinValueEnum(FName PinName, int32 & OutValue) const
```

Read an enum input pin's resolved value into a wildcard enum out parameter. The runtime data block stores enum slots as a normalized int64 (see GetPinTypeSize / WriteEnumInt64ToProperty). The Blueprint-facing property bound to OutValue may be FEnumProperty (underlying numeric width may be uint8/int32/int64) or FByteProperty (always uint8). We narrow-cast the int64 into the caller's property at execution time to keep the BP thunk symmetric with SetParameterBlockValue in ComposableCameraBlueprintLibrary.

---

#### DECLARE_FUNCTION { #declare_function }

`inline`

```cpp
inline DECLARE_FUNCTION(execGetInputPinValueEnum)
```

---

#### SetOutputPinValueBool { #setoutputpinvaluebool }

```cpp
void SetOutputPinValueBool(FName PinName, bool Value)
```

---

#### SetOutputPinValueInt32 { #setoutputpinvalueint32 }

```cpp
void SetOutputPinValueInt32(FName PinName, int32 Value)
```

---

#### SetOutputPinValueFloat { #setoutputpinvaluefloat }

```cpp
void SetOutputPinValueFloat(FName PinName, float Value)
```

---

#### SetOutputPinValueDouble { #setoutputpinvaluedouble }

```cpp
void SetOutputPinValueDouble(FName PinName, double Value)
```

---

#### SetOutputPinValueVector { #setoutputpinvaluevector }

```cpp
void SetOutputPinValueVector(FName PinName, FVector Value)
```

---

#### SetOutputPinValueRotator { #setoutputpinvaluerotator }

```cpp
void SetOutputPinValueRotator(FName PinName, FRotator Value)
```

---

#### SetOutputPinValueTransform { #setoutputpinvaluetransform }

```cpp
void SetOutputPinValueTransform(FName PinName, FTransform Value)
```

---

#### SetOutputPinValueActor { #setoutputpinvalueactor }

```cpp
void SetOutputPinValueActor(FName PinName, AActor * Value)
```

---

#### SetOutputPinValueName { #setoutputpinvaluename }

```cpp
void SetOutputPinValueName(FName PinName, FName Value)
```

---

#### SetOutputPinValueEnum { #setoutputpinvalueenum }

```cpp
void SetOutputPinValueEnum(FName PinName, const int32 & Value)
```

Write a wildcard enum value to an output pin. Mirrors GetInputPinValueEnum — reads the enum from the caller's property (FEnumProperty or FByteProperty) via the numeric-property API, normalizes to int64, and stores it in the data block slot. Callers on the consumer side read it back through the same int64 channel (see ResolveAllInputPins).

---

#### DECLARE_FUNCTION { #declare_function-1 }

`inline`

```cpp
inline DECLARE_FUNCTION(execSetOutputPinValueEnum)
```

---

#### GetInternalVariableFloat { #getinternalvariablefloat }

`const`

```cpp
float GetInternalVariableFloat(FName VariableName) const
```

---

#### GetInternalVariableVector { #getinternalvariablevector }

`const`

```cpp
FVector GetInternalVariableVector(FName VariableName) const
```

---

#### GetInternalVariableName { #getinternalvariablename }

`const`

```cpp
FName GetInternalVariableName(FName VariableName) const
```

---

#### GetInternalVariableEnum { #getinternalvariableenum }

`const`

```cpp
void GetInternalVariableEnum(FName VariableName, int32 & OutValue) const
```

Read an enum internal variable into a wildcard enum out parameter. Storage is a normalized int64; the thunk narrow-casts into the caller's property width. See GetInputPinValueEnum for the same pattern on the pin surface.

---

#### DECLARE_FUNCTION { #declare_function-2 }

`inline`

```cpp
inline DECLARE_FUNCTION(execGetInternalVariableEnum)
```

---

#### SetInternalVariableFloat { #setinternalvariablefloat }

```cpp
void SetInternalVariableFloat(FName VariableName, float Value)
```

---

#### SetInternalVariableVector { #setinternalvariablevector }

```cpp
void SetInternalVariableVector(FName VariableName, FVector Value)
```

---

#### SetInternalVariableName { #setinternalvariablename }

```cpp
void SetInternalVariableName(FName VariableName, FName Value)
```

---

#### SetInternalVariableEnum { #setinternalvariableenum }

```cpp
void SetInternalVariableEnum(FName VariableName, const int32 & Value)
```

Write a wildcard enum value to an internal variable. Normalizes to int64 via the caller's FEnumProperty/FByteProperty and stores in the data block slot — the same representation every other enum consumer reads.

---

#### DECLARE_FUNCTION { #declare_function-3 }

`inline`

```cpp
inline DECLARE_FUNCTION(execSetInternalVariableEnum)
```

---

#### OnPreTick { #onpretick-1 }

`virtual`

```cpp
virtual void OnPreTick(float DeltaTime, const FComposableCameraPose & CurrentCameraPose, FComposableCameraPose & OutCameraPose)
```

---

#### OnPostTick { #onposttick-1 }

`virtual`

```cpp
virtual void OnPostTick(float DeltaTime, const FComposableCameraPose & CurrentCameraPose, FComposableCameraPose & OutCameraPose)
```

---

#### DrawNodeDebug { #drawnodedebug-4 }

`virtual` `const` `inline`

```cpp
virtual inline void DrawNodeDebug(class UWorld * World, bool bViewerIsOutsideCamera) const
```

Called each frame when the `CCS.Debug.Viewport` CVar is enabled, for every node on the currently running camera. Override to draw world-space debug gizmos via `DrawDebugHelpers` (DrawDebugSphere, DrawDebugLine, etc.) that visualise this node's runtime state — e.g. a pivot sphere for PivotOffsetNode, a look-at line for LookAtNode, the collision trace for CollisionPushNode, a sampled spline path for SplineNode.

Access the owning camera via `OwningCamera` and current-frame pin values via the usual `GetInputPinValue<T>()` / member-read path — this hook fires AFTER TickNode, so pin-backed UPROPERTYs still hold the resolved values from the most recent evaluation.

`bViewerIsOutsideCamera` mirrors the ticker's frustum-draw flag: true when the viewer is observing the camera from outside (F8 eject, SIE, or `CCS.Debug.Viewport.AlwaysShow`), false when the player is looking through the camera. Most gizmos (pivot spheres at distant characters, lines to look-at targets, spline polylines far in the world) can ignore this and draw unconditionally. Gizmos that sit AT the camera's own position (e.g. `CollisionPushNode`'s self-collision sphere) should gate on this bool so they don't hermetically seal the player inside the wireframe during live gameplay.

Default implementation does nothing. Compiled out in shipping builds.

---

#### DrawNodeDebug2D { #drawnodedebug2d }

`virtual` `const` `inline`

```cpp
virtual inline void DrawNodeDebug2D(class UCanvas * Canvas, class APlayerController * PC) const
```

2D counterpart to DrawNodeDebug. Fires from a separate UDebugDrawService hook on the "Game" channel — which means it runs during PIE-possessed play (and standalone), NOT during F8 eject (editor viewport doesn't route through the game channel). That lines up with what 2D overlays are good for: screen-space debug that the player-eye perspective answers and an external view cannot (safe-zone rectangles, projected pivot markers, HUD-space gizmos).

Canvas provides the 2D surface; PC is the local player controller whose view is being rendered (for ProjectWorldToScreen and aspect ratio queries). Either may be null in edge cases — always check.

Default implementation does nothing. Compiled out in shipping builds.

### Protected Attributes

| Return | Name | Description |
|--------|------|-------------|
| `AComposableCameraCameraBase *` | [`OwningCamera`](#owningcamera)  |  |
| `AComposableCameraPlayerCameraManager *` | [`OwningPlayerCameraManager`](#owningplayercameramanager)  |  |
| `FComposableCameraRuntimeDataBlock *` | [`RuntimeDataBlock`](#runtimedatablock)  | Runtime data block for the pin system. Set when running from a camera type asset. |
| `int32` | [`RuntimeNodeIndex`](#runtimenodeindex)  | This node's index in the camera type asset's NodeTemplates array. |

---

#### OwningCamera { #owningcamera }

```cpp
AComposableCameraCameraBase * OwningCamera
```

---

#### OwningPlayerCameraManager { #owningplayercameramanager }

```cpp
AComposableCameraPlayerCameraManager * OwningPlayerCameraManager
```

---

#### RuntimeDataBlock { #runtimedatablock }

```cpp
FComposableCameraRuntimeDataBlock * RuntimeDataBlock = nullptr
```

Runtime data block for the pin system. Set when running from a camera type asset.

---

#### RuntimeNodeIndex { #runtimenodeindex }

```cpp
int32 RuntimeNodeIndex = INDEX_NONE
```

This node's index in the camera type asset's NodeTemplates array.

### Protected Methods

| Return | Name | Description |
|--------|------|-------------|
| `bool` | [`ShouldAutoResolveInputPins`](#shouldautoresolveinputpins) `virtual` `const` `inline` | Opt-out hook for the auto-resolve-before-tick behavior. Override and return false on nodes that manage their own pin reads (e.g. nodes whose UPROPERTYs must survive across frames or are written by external actors mid-tick). |
| `void` | [`OnInitialize`](#oninitialize)  | Per-activation one-shot initialization. Called exactly once per camera activation, after OwningCamera / OwningPlayerCameraManager / RuntimeDataBlock have all been wired. This is the hook for caching refs, instantiating internal objects, reading exposed parameters, and seeding any per-activation state the node needs before the first Tick. |
| `void` | [`OnInitialize_Implementation`](#oninitialize_implementation-5) `virtual` `inline` |  |
| `void` | [`OnFirstTickNode`](#onfirstticknode)  | Called exactly once on the first TickNode after activation, immediately after [ResolveAllInputPins()](#resolveallinputpins) and immediately before [OnTickNode()](#onticknode). |
| `void` | [`OnFirstTickNode_Implementation`](#onfirstticknode_implementation) `virtual` `inline` |  |
| `void` | [`OnTickNode`](#onticknode)  | Main node logic implemented here. This node can read/write pin values and/or CameraPose. |
| `void` | [`OnTickNode_Implementation`](#onticknode_implementation-7) `virtual` `inline` |  |

---

#### ShouldAutoResolveInputPins { #shouldautoresolveinputpins }

`virtual` `const` `inline`

```cpp
virtual inline bool ShouldAutoResolveInputPins() const
```

Opt-out hook for the auto-resolve-before-tick behavior. Override and return false on nodes that manage their own pin reads (e.g. nodes whose UPROPERTYs must survive across frames or are written by external actors mid-tick).

Default: true — any node with a pin + matching UPROPERTY gets the member refreshed before every OnTickNode call.

---

#### OnInitialize { #oninitialize }

```cpp
void OnInitialize()
```

Per-activation one-shot initialization. Called exactly once per camera activation, after OwningCamera / OwningPlayerCameraManager / RuntimeDataBlock have all been wired. This is the hook for caching refs, instantiating internal objects, reading exposed parameters, and seeding any per-activation state the node needs before the first Tick.

Nodes that need the outgoing camera's pose (what BeginPlayNode used to receive as CurrentCameraPose) should read it via OwningPlayerCameraManager->GetCurrentCameraPose() — this is the same value AActor::BeginPlay was passing in when it called BeginPlayCamera.

BlueprintNativeEvent: Blueprint subclasses can override "InitializeNode" to replace the C++ implementation. C++ subclasses override OnInitialize_Implementation and should call Super when chaining.

NOTE: Input pin values are NOT yet resolved when this is called. Do not read pin-backed UPROPERTYs here to seed per-frame state — use OnFirstTickNode instead, which runs after the first [ResolveAllInputPins()](#resolveallinputpins).

---

#### OnInitialize_Implementation { #oninitialize_implementation-5 }

`virtual` `inline`

```cpp
virtual inline void OnInitialize_Implementation()
```

---

#### OnFirstTickNode { #onfirstticknode }

```cpp
void OnFirstTickNode()
```

Called exactly once on the first TickNode after activation, immediately after [ResolveAllInputPins()](#resolveallinputpins) and immediately before [OnTickNode()](#onticknode).

This is the correct place to seed per-frame state that depends on live input pin values (e.g. initializing a "last position" tracker to the actual runtime position rather than the UPROPERTY default). By the time this fires, all pin-backed UPROPERTYs on this node already hold their resolved runtime values.

The flag is reset in [Initialize()](#initialize-3), so re-activating the camera triggers this hook again on the new first frame.

Default implementation is empty. C++ subclasses override OnFirstTickNode_Implementation. Blueprint subclasses override "FirstTickNode".

---

#### OnFirstTickNode_Implementation { #onfirstticknode_implementation }

`virtual` `inline`

```cpp
virtual inline void OnFirstTickNode_Implementation()
```

---

#### OnTickNode { #onticknode }

```cpp
void OnTickNode(float DeltaTime, const FComposableCameraPose & CurrentCameraPose, FComposableCameraPose & OutCameraPose)
```

Main node logic implemented here. This node can read/write pin values and/or CameraPose. 

**Parameters**

* `DeltaTime` Delta time for this frame. 

* `CurrentCameraPose` Current camera pose. 

* `OutCameraPose` Output camera pose for this node.

---

#### OnTickNode_Implementation { #onticknode_implementation-7 }

`virtual` `inline`

```cpp
virtual inline void OnTickNode_Implementation(float DeltaTime, const FComposableCameraPose & CurrentCameraPose, FComposableCameraPose & OutCameraPose)
```

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `bool` | [`bHasHadFirstTick`](#bhashadfirsttick)  | Set to true after the first TickNode call. Cleared by [Initialize()](#initialize-3) so re-activation re-triggers OnFirstTickNode on the new first frame. |

---

#### bHasHadFirstTick { #bhashadfirsttick }

```cpp
bool bHasHadFirstTick = false
```

Set to true after the first TickNode call. Cleared by [Initialize()](#initialize-3) so re-activation re-triggers OnFirstTickNode on the new first frame.

### Private Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`AutoDeclareSubobjectPins`](#autodeclaresubobjectpins) `const` | Auto-iterate all Instanced UPROPERTY fields and declare their child pins. |
| `void` | [`AutoApplySubobjectPinValues`](#autoapplysubobjectpinvalues)  | Auto-iterate all Instanced UPROPERTY fields and apply resolved pin values. |
| `const FComposableCameraNodePinBindingTable &` | [`GetOrBuildPinBindings`](#getorbuildpinbindings) `const` | Get or lazily build the pin binding table for this node's concrete UClass. Thread-safe (game-thread-only in practice, but guarded with a critical section so Blueprint recompile on the game thread cannot race with ResolveAllInputPins on the same frame). |
| `bool` | [`ReadBPEnumPropertyAsInt64`](#readbpenumpropertyasint64) `const` | Shared helper used by all enum CustomThunks to normalize a Blueprint-side enum property (FEnumProperty or FByteProperty) into the data block's canonical int64 representation. Returns false if the property is not an enum-backed numeric type. |
| `void` | [`WriteEnumInt64ToBPProperty`](#writeenumint64tobpproperty) `const` | Inverse of ReadBPEnumPropertyAsInt64: narrow-cast a normalized int64 into the caller's enum property (FEnumProperty underlying numeric width, or FByteProperty uint8). No-op on unknown kinds. Non-const because DECLARE_FUNCTION inline thunks need a matching this-pointer — the write itself is into the caller's memory, not the node. |

---

#### AutoDeclareSubobjectPins { #autodeclaresubobjectpins }

`const`

```cpp
void AutoDeclareSubobjectPins(TArray< FComposableCameraNodePinDeclaration > & OutPins) const
```

Auto-iterate all Instanced UPROPERTY fields and declare their child pins.

---

#### AutoApplySubobjectPinValues { #autoapplysubobjectpinvalues }

```cpp
void AutoApplySubobjectPinValues()
```

Auto-iterate all Instanced UPROPERTY fields and apply resolved pin values.

---

#### GetOrBuildPinBindings { #getorbuildpinbindings }

`const`

```cpp
const FComposableCameraNodePinBindingTable & GetOrBuildPinBindings() const
```

Get or lazily build the pin binding table for this node's concrete UClass. Thread-safe (game-thread-only in practice, but guarded with a critical section so Blueprint recompile on the game thread cannot race with ResolveAllInputPins on the same frame).

---

#### ReadBPEnumPropertyAsInt64 { #readbpenumpropertyasint64 }

`const`

```cpp
bool ReadBPEnumPropertyAsInt64(const FProperty * ValueProperty, const void * ValuePtr, int64 & OutValue) const
```

Shared helper used by all enum CustomThunks to normalize a Blueprint-side enum property (FEnumProperty or FByteProperty) into the data block's canonical int64 representation. Returns false if the property is not an enum-backed numeric type.

---

#### WriteEnumInt64ToBPProperty { #writeenumint64tobpproperty }

`const`

```cpp
void WriteEnumInt64ToBPProperty(const FProperty * OutValueProperty, void * OutValuePtr, int64 Value) const
```

Inverse of ReadBPEnumPropertyAsInt64: narrow-cast a normalized int64 into the caller's enum property (FEnumProperty underlying numeric width, or FByteProperty uint8). No-op on unknown kinds. Non-const because DECLARE_FUNCTION inline thunks need a matching this-pointer — the write itself is into the caller's memory, not the node.
