
# FComposableCameraOcclusionMaterialOverride { #fcomposablecameraocclusionmaterialoverride }

```cpp
#include <ComposableCameraOcclusionFadeNode.h>
```

Per-primitive record of materials replaced while the primitive is in the faded set. Stored as a USTRUCT on the node so GC keeps the original-materials array alive until we restore it, which avoids a dangling-pointer risk the moment a mesh's only remaining reference to its original material is this record.

OverrideMaterials is kept in lockstep with OriginalMaterials for symmetry and debug inspection — it also pins the MID we created from the user's OcclusionMaterial, so that reloading / hot-reloading the source material doesn't immediately invalidate our swap.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TWeakObjectPtr< UPrimitiveComponent >` | [`Component`](#component)  | The primitive whose material slots we swapped. Weak ref so actor destruction (e.g. NPC pooled away) cleans itself up — we prune stale entries each tick. |
| `TArray< TObjectPtr< UMaterialInterface > >` | [`OriginalMaterials`](#originalmaterials)  | Original UMaterialInterface per element index, captured at swap time. |
| `TArray< TObjectPtr< UMaterialInterface > >` | [`OverrideMaterials`](#overridematerials)  | MIDs we created from the occlusion material per element index. Recorded so the node holds a hard GC reference to them for the lifetime of the override. |

---

#### Component { #component }

```cpp
TWeakObjectPtr< UPrimitiveComponent > Component
```

The primitive whose material slots we swapped. Weak ref so actor destruction (e.g. NPC pooled away) cleans itself up — we prune stale entries each tick.

---

#### OriginalMaterials { #originalmaterials }

```cpp
TArray< TObjectPtr< UMaterialInterface > > OriginalMaterials
```

Original UMaterialInterface per element index, captured at swap time.

---

#### OverrideMaterials { #overridematerials }

```cpp
TArray< TObjectPtr< UMaterialInterface > > OverrideMaterials
```

MIDs we created from the occlusion material per element index. Recorded so the node holds a hard GC reference to them for the lifetime of the override.
