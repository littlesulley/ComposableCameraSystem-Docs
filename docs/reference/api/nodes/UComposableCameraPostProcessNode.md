
# UComposableCameraPostProcessNode { #ucomposablecamerapostprocessnode }

```cpp
#include <ComposableCameraPostProcessNode.h>
```

> **Inherits:** [`UComposableCameraCameraNodeBase`](../uobjects-other/UComposableCameraCameraNodeBase.md#ucomposablecameracameranodebase)

Node that applies post-process settings to the camera pose.

Works like a PostProcessVolume but scoped to a single camera type. Only properties whose bOverride_* flag is true take effect; all others pass through from the camera component's baseline or from earlier nodes.

The settings are applied once per tick via FPostProcessUtils::OverridePostProcessSettings onto OutCameraPose.PostProcessSettings. Multiple PostProcess nodes in the same camera stack compose in execution order (later nodes override earlier ones for the same bOverride_* property).

No pins are declared — FPostProcessSettings is configured entirely through the Details panel, matching the PostProcessVolume workflow [UE](#ue) artists are already familiar with.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FPostProcessSettings` | [`PostProcessSettings`](#postprocesssettings-1)  | Post-process settings to apply. Toggle individual bOverride_* flags to control which properties this node contributes. Properties with their override flag off are left untouched. |

---

#### PostProcessSettings { #postprocesssettings-1 }

```cpp
FPostProcessSettings PostProcessSettings
```

Post-process settings to apply. Toggle individual bOverride_* flags to control which properties this node contributes. Properties with their override flag off are left untouched.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`OnTickNode_Implementation`](#onticknode_implementation-8) `virtual` |  |

---

#### OnTickNode_Implementation { #onticknode_implementation-8 }

`virtual`

```cpp
virtual void OnTickNode_Implementation(float DeltaTime, const FComposableCameraPose & CurrentCameraPose, FComposableCameraPose & OutCameraPose)
```
