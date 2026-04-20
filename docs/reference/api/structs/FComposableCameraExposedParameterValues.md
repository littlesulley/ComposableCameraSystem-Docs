
# FComposableCameraExposedParameterValues { #fcomposablecameraexposedparametervalues }

```cpp
#include <ComposableCameraParameterTableRow.h>
```

Bag of serialized per-parameter values, keyed by the exposed parameter's FName. Exists as a dedicated USTRUCT (rather than a naked TMap field on the row) so the editor module can register an IPropertyTypeCustomization for it.

WHY THIS WRAPPER EXISTS: [UE](#ue)'s FStructureDetailsView — the panel used by the DataTable editor to edit a row — does NOT invoke IPropertyTypeCustomization at the ROOT struct level. It only applies customizations to child struct properties. If we customized [FComposableCameraParameterTableRow](FComposableCameraParameterTableRow.md#fcomposablecameraparametertablerow) directly, the customization would never fire for DataTable row editing. Wrapping the parameter map in this sub-struct gives us a child property that the details view will route through our customization, and from there we walk up to the parent row to find the sibling CameraType.

At runtime, code reads Row.Parameters.Values directly — this struct exists purely to give the editor a customization hook.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TMap< FName, FString >` | [`Values`](#values-1)  | Serialized per-parameter values keyed by the exposed parameter's FName. |

---

#### Values { #values-1 }

```cpp
TMap< FName, FString > Values
```

Serialized per-parameter values keyed by the exposed parameter's FName.

Not authored directly in the DataTable editor — the property-type customization generates a widget per parameter based on the parent row's selected CameraType and round-trips values through [FComposableCameraParameterBlock::ApplyStringValue](FComposableCameraParameterBlock.md#applystringvalue) at activation time. Entries whose keys no longer correspond to any exposed parameter on the current CameraType are auto-removed by the customization.
