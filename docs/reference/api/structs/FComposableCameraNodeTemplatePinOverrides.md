
# FComposableCameraNodeTemplatePinOverrides { #fcomposablecameranodetemplatepinoverrides }

```cpp
#include <ComposableCameraNodePinTypes.h>
```

Per-node-template container for pin overrides, forming a parallel array to [UComposableCameraTypeAsset::NodeTemplates](../data-assets/UComposableCameraTypeAsset.md#nodetemplates). Each entry holds the sparse list of overrides for the corresponding node instance. A wrapper struct (rather than TArray<TArray<…>>) is used because Unreal's reflection does not support nested TArray properties directly.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TArray< FComposableCameraPinOverride >` | [`Overrides`](#overrides)  | Sparse list of pin overrides for this node instance. Pins without an entry here use their C++ declaration defaults (bAsPin = Decl.bDefaultAsPin, DefaultValueString from the class). |

---

#### Overrides { #overrides }

```cpp
TArray< FComposableCameraPinOverride > Overrides
```

Sparse list of pin overrides for this node instance. Pins without an entry here use their C++ declaration defaults (bAsPin = Decl.bDefaultAsPin, DefaultValueString from the class).
