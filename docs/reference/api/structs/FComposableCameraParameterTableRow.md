
# FComposableCameraParameterTableRow { #fcomposablecameraparametertablerow }

```cpp
#include <ComposableCameraParameterTableRow.h>
```

> **Inherits:** `FTableRowBase`

DataTable row describing a camera-type activation. One row = one callable "camera preset": the camera type to activate, the context to activate into, an optional transition override, pose preservation, and the serialized values for each exposed parameter on that type.

Parameter values are stored as strings inside [FComposableCameraExposedParameterValues](FComposableCameraExposedParameterValues.md#fcomposablecameraexposedparametervalues) (see the rationale above that struct for why there's a wrapper). At activation time, each entry is parsed by [FComposableCameraParameterBlock::ApplyStringValue](FComposableCameraParameterBlock.md#applystringvalue) using the type info from the selected CameraType's GetExposedParameters(). This keeps the row schema fixed (one USTRUCT for the whole DataTable) while still allowing each row to carry whatever parameter set its selected camera type happens to declare.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TSoftObjectPtr< UComposableCameraTypeAsset >` | [`CameraType`](#cameratype)  | The camera type this row activates. Soft-referenced so DataTable assets don't force-load every camera type in the project at boot. |
| `FName` | [`ContextName`](#contextname-3)  | Context to activate into. If NAME_None, the active context is used. |
| `TSoftObjectPtr< UComposableCameraTransitionDataAsset >` | [`TransitionOverride`](#transitionoverride)  | Optional transition override. If null, the type asset's default transition is used. |
| `FComposableCameraActivateParams` | [`ActivationParams`](#activationparams)  | Activation parameters forwarded to the context stack when this row is used. Contains pose preservation, initial transform, transient settings, etc. — identical to the struct exposed on the K2 node. |
| `FComposableCameraExposedParameterValues` | [`Parameters`](#parameters)  | Per-parameter values for this row's CameraType. The wrapper struct exists so the editor can hang an IPropertyTypeCustomization off it — customizations do not fire at the root of FStructureDetailsView, only on child struct properties. |

---

#### CameraType { #cameratype }

```cpp
TSoftObjectPtr< UComposableCameraTypeAsset > CameraType
```

The camera type this row activates. Soft-referenced so DataTable assets don't force-load every camera type in the project at boot.

---

#### ContextName { #contextname-3 }

```cpp
FName ContextName
```

Context to activate into. If NAME_None, the active context is used.

---

#### TransitionOverride { #transitionoverride }

```cpp
TSoftObjectPtr< UComposableCameraTransitionDataAsset > TransitionOverride
```

Optional transition override. If null, the type asset's default transition is used.

---

#### ActivationParams { #activationparams }

```cpp
FComposableCameraActivateParams ActivationParams
```

Activation parameters forwarded to the context stack when this row is used. Contains pose preservation, initial transform, transient settings, etc. — identical to the struct exposed on the K2 node.

---

#### Parameters { #parameters }

```cpp
FComposableCameraExposedParameterValues Parameters
```

Per-parameter values for this row's CameraType. The wrapper struct exists so the editor can hang an IPropertyTypeCustomization off it — customizations do not fire at the root of FStructureDetailsView, only on child struct properties.
