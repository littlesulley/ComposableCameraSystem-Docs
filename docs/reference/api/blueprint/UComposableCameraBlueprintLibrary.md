
# UComposableCameraBlueprintLibrary { #ucomposablecamerablueprintlibrary }

```cpp
#include <ComposableCameraBlueprintLibrary.h>
```

> **Inherits:** `UBlueprintFunctionLibrary`

Blueprint library.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`DECLARE_FUNCTION`](#declare_function) `inline` |  |

---

#### DECLARE_FUNCTION { #declare_function }

`inline`

```cpp
inline DECLARE_FUNCTION(execSetParameterBlockValue)
```

### Public Static Methods

| Return | Name | Description |
|--------|------|-------------|
| `AComposableCameraCameraBase *` | [`ActivateComposableCameraFromTypeAsset`](#activatecomposablecamerafromtypeasset) `static` | Activate a composable camera from a Camera Type Asset (data-driven workflow). <br/> |
| `AComposableCameraCameraBase *` | [`ActivateComposableCameraFromDataTable`](#activatecomposablecamerafromdatatable) `static` | Activate a composable camera from a DataTable row. |
| `void` | [`TerminateCurrentCamera`](#terminatecurrentcamera) `static` | Terminate the current camera — pops the active (top) context off the stack. The previous context resumes with an optional transition. Cannot pop the base context. |
| `void` | [`PopCameraContext`](#popcameracontext) `static` | Pop a specific camera context by name. If this is the active context, the previous context resumes with an optional transition. Cannot pop the base context if it is the last one remaining. |
| `int32` | [`GetCameraContextStackDepth`](#getcameracontextstackdepth) `static` | Get the current depth of the camera context stack. |
| `FName` | [`GetActiveContextName`](#getactivecontextname-1) `static` | Get the name of the currently active (top) context. |
| `void` | [`AddModifier`](#addmodifier-1) `static` | Add a modifier data asset. |
| `void` | [`RemoveModifier`](#removemodifier-1) `static` | Remove a modifier data asset. |
| `UComposableCameraActionBase *` | [`AddAction`](#addaction) `static` | Add a camera action. Multiple actions of the same class are not allowed. |
| `void` | [`ExpireAction`](#expireaction-1) `static` | Expire a camera action. |
| `AComposableCameraPlayerCameraManager *` | [`GetComposableCameraPlayerCameraManager`](#getcomposablecameraplayercameramanager) `static` | Get player camera manager and cast it to ComposableCameraPlayerCameraManager. Can be null if it's not the type. |
| `void` | [`SetParameterBlockValue`](#setparameterblockvalue) `static` | Custom thunk function for setting a single value in a ParameterBlock. Used internally by UK2Node_ActivateComposableCamera to fill the parameter block at compile time. |
| `FVector` | [`MakeLiteralVector`](#makeliteralvector) `static` |  |
| `FVector4` | [`MakeLiteralVector4`](#makeliteralvector4) `static` |  |
| `FVector2D` | [`MakeLiteralVector2D`](#makeliteralvector2d) `static` |  |
| `FRotator` | [`MakeLiteralRotator`](#makeliteralrotator) `static` |  |
| `FTransform` | [`MakeLiteralTransform`](#makeliteraltransform) `static` |  |

---

#### ActivateComposableCameraFromTypeAsset { #activatecomposablecamerafromtypeasset }

`static`

```cpp
static AComposableCameraCameraBase * ActivateComposableCameraFromTypeAsset(const UObject * WorldContextObject, int32 PlayerIndex, UComposableCameraTypeAsset * CameraTypeAsset, FName ContextName, UComposableCameraTransitionDataAsset * TransitionOverride, FComposableCameraParameterBlock Parameters, FComposableCameraActivateParams ActivationParams)
```

Activate a composable camera from a Camera Type Asset (data-driven workflow). <br/>
The type asset defines the node composition, exposed parameters, internal variables, and default transition. <br/>
 This function is hidden from the Blueprint palette because designers should author activation calls through UK2Node_ActivateComposableCamera instead — that K2 node generates a typed pin per exposed parameter and expands into this call at compile time. Exposing the raw [FComposableCameraParameterBlock](../structs/FComposableCameraParameterBlock.md#fcomposablecameraparameterblock) form in the BP menu would create a second, untyped, strictly worse workflow alongside the K2 node.

**Parameters**

* `WorldContextObject` World context object. <br/>

* `PlayerIndex` Player index (0 for single player). <br/>

* `CameraTypeAsset` The camera type data asset to instantiate. <br/>

* `ContextName` Optional context name. If valid, the camera activates in the specified context (auto-pushing if needed). If NAME_None, activates in the current active context. <br/>

* `TransitionOverride` Optional transition. If nullptr, the type asset's EnterTransition is used. <br/>

* `Parameters` Parameter block with exposed parameter values for this camera type. <br/>

* `ActivationParams` Parameters to define transient, lifetime, and pose preservation behavior. <br/>

**Returns**

The activated camera instance.

---

#### ActivateComposableCameraFromDataTable { #activatecomposablecamerafromdatatable }

`static`

```cpp
static AComposableCameraCameraBase * ActivateComposableCameraFromDataTable(const UObject * WorldContextObject, int32 PlayerIndex, UDataTable * DataTable, FName RowName)
```

Activate a composable camera from a DataTable row.

The row is expected to be of type [FComposableCameraParameterTableRow](../structs/FComposableCameraParameterTableRow.md#fcomposablecameraparametertablerow). The row's CameraType is sync-loaded and its Parameters.Values map is parsed via [FComposableCameraParameterBlock::ApplyStringValue](../structs/FComposableCameraParameterBlock.md#applystringvalue) using the type's exposed parameters. Parse failures are logged to LogComposableCameraSystem and fall back to the node pin's authored default so activation never refuses to proceed on a single bad cell; parameters with no valid source at all end up at the runtime data block's zero-initialized default.

This function is hidden from the Blueprint palette because designers should author DataTable-driven activation calls through UK2Node_ActivateComposableCameraFromDataTable instead — that K2 node provides a row-struct-filtered DataTable asset picker and a live row-name dropdown, and expands into this call at compile time.

**Parameters**

* `WorldContextObject` World context object. 

* `PlayerIndex` Player index (0 for single player). 

* `DataTable` DataTable asset containing the row. 

* `RowName` Name of the row to activate. The row's ActivationParams struct is used directly. 

**Returns**

The activated camera instance, or nullptr on failure.

---

#### TerminateCurrentCamera { #terminatecurrentcamera }

`static`

```cpp
static void TerminateCurrentCamera(const UObject * WorldContextObject, AComposableCameraPlayerCameraManager * PlayerCameraManager, UComposableCameraTransitionDataAsset * TransitionOverride, FComposableCameraActivateParams ActivationParams)
```

Terminate the current camera — pops the active (top) context off the stack. The previous context resumes with an optional transition. Cannot pop the base context. 

**Parameters**

* `WorldContextObject` World context object. <br/>

* `PlayerCameraManager` The player camera manager, must be a ComposableCameraPlayerCameraManager. <br/>

* `TransitionOverride` Optional transition. If nullptr, falls back to the resume camera's EnterTransition. <br/>

* `ActivationParams` Optional activation params for the resume camera.

---

#### PopCameraContext { #popcameracontext }

`static`

```cpp
static void PopCameraContext(const UObject * WorldContextObject, AComposableCameraPlayerCameraManager * PlayerCameraManager, FName ContextName, UComposableCameraTransitionDataAsset * TransitionOverride, FComposableCameraActivateParams ActivationParams)
```

Pop a specific camera context by name. If this is the active context, the previous context resumes with an optional transition. Cannot pop the base context if it is the last one remaining. 

**Parameters**

* `WorldContextObject` World context object. <br/>

* `PlayerCameraManager` The player camera manager, must be a ComposableCameraPlayerCameraManager. <br/>

* `ContextName` The name identifying which context to pop. <br/>

* `TransitionOverride` Optional transition. If nullptr, falls back to the resume camera's EnterTransition. <br/>

* `ActivationParams` Optional activation params for the resume camera.

---

#### GetCameraContextStackDepth { #getcameracontextstackdepth }

`static`

```cpp
static int32 GetCameraContextStackDepth(const UObject * WorldContextObject, AComposableCameraPlayerCameraManager * PlayerCameraManager)
```

Get the current depth of the camera context stack. 

**Parameters**

* `WorldContextObject` World context object. <br/>

* `PlayerCameraManager` The player camera manager, must be a ComposableCameraPlayerCameraManager. <br/>

**Returns**

The number of contexts on the stack (1 = base context only).

---

#### GetActiveContextName { #getactivecontextname-1 }

`static`

```cpp
static FName GetActiveContextName(const UObject * WorldContextObject, AComposableCameraPlayerCameraManager * PlayerCameraManager)
```

Get the name of the currently active (top) context. 

**Parameters**

* `WorldContextObject` World context object. <br/>

* `PlayerCameraManager` The player camera manager, must be a ComposableCameraPlayerCameraManager. <br/>

**Returns**

The active context's name.

---

#### AddModifier { #addmodifier-1 }

`static`

```cpp
static void AddModifier(const UObject * WorldContextObject, AComposableCameraPlayerCameraManager * PlayerCameraManager, UComposableCameraNodeModifierDataAsset * ModifierAsset)
```

Add a modifier data asset. 

**Parameters**

* `WorldContextObject` World context object. <br/>

* `PlayerCameraManager` The player camera manager, must be a ComposableCameraPlayerCameraManager. <br/>

* `ModifierAsset` Data asset for modifiers to add.

---

#### RemoveModifier { #removemodifier-1 }

`static`

```cpp
static void RemoveModifier(const UObject * WorldContextObject, AComposableCameraPlayerCameraManager * PlayerCameraManager, UComposableCameraNodeModifierDataAsset * ModifierAsset)
```

Remove a modifier data asset. 

**Parameters**

* `WorldContextObject` World context object. <br/>

* `PlayerCameraManager` The player camera manager, must be a ComposableCameraPlayerCameraManager. <br/>

* `ModifierAsset` Data asset for modifiers to remove.

---

#### AddAction { #addaction }

`static`

```cpp
static UComposableCameraActionBase * AddAction(const UObject * WorldContextObject, AComposableCameraPlayerCameraManager * PlayerCameraManager, TSubclassOf< UComposableCameraActionBase > ActionClass, bool bOnlyForCurrentCamera)
```

Add a camera action. Multiple actions of the same class are not allowed. 

**Parameters**

* `WorldContextObject` World context object. <br/>

* `PlayerCameraManager` The player camera manager, must be a ComposableCameraPlayerCameraManager. <br/>

* `ActionClass` The class of action you want to add. <br/>

* `bOnlyForCurrentCamera` If this action is only valid for current running camera. If true, the action will expire when the current camera is blended out.

---

#### ExpireAction { #expireaction-1 }

`static`

```cpp
static void ExpireAction(const UObject * WorldContextObject, AComposableCameraPlayerCameraManager * PlayerCameraManager, TSubclassOf< UComposableCameraActionBase > ActionClass)
```

Expire a camera action. 

**Parameters**

* `WorldContextObject` World context object. <br/>

* `PlayerCameraManager` The player camera manager, must be a ComposableCameraPlayerCameraManager. <br/>

* `ActionClass` The class of action you want to expire.

---

#### GetComposableCameraPlayerCameraManager { #getcomposablecameraplayercameramanager }

`static`

```cpp
static AComposableCameraPlayerCameraManager * GetComposableCameraPlayerCameraManager(const UObject * WorldContextObject, int Index)
```

Get player camera manager and cast it to ComposableCameraPlayerCameraManager. Can be null if it's not the type. 

**Parameters**

* `Index` Player index.

---

#### SetParameterBlockValue { #setparameterblockvalue }

`static`

```cpp
static void SetParameterBlockValue(FComposableCameraParameterBlock & ParameterBlock, FName ParameterName, const int32 & Value)
```

Custom thunk function for setting a single value in a ParameterBlock. Used internally by UK2Node_ActivateComposableCamera to fill the parameter block at compile time. 

**Parameters**

* `ParameterBlock` The parameter block to modify. 

* `ParameterName` The parameter name key. 

* `Value` The value to set (type-erased via CustomStructureParam).

---

#### MakeLiteralVector { #makeliteralvector }

`static`

```cpp
static FVector MakeLiteralVector(FVector Value)
```

---

#### MakeLiteralVector4 { #makeliteralvector4 }

`static`

```cpp
static FVector4 MakeLiteralVector4(FVector4 Value)
```

---

#### MakeLiteralVector2D { #makeliteralvector2d }

`static`

```cpp
static FVector2D MakeLiteralVector2D(FVector2D Value)
```

---

#### MakeLiteralRotator { #makeliteralrotator }

`static`

```cpp
static FRotator MakeLiteralRotator(FRotator Value)
```

---

#### MakeLiteralTransform { #makeliteraltransform }

`static`

```cpp
static FTransform MakeLiteralTransform(FTransform Value)
```
