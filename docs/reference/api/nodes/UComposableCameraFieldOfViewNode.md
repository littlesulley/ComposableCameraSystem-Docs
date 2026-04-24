
# UComposableCameraFieldOfViewNode { #ucomposablecamerafieldofviewnode }

```cpp
#include <ComposableCameraFieldOfViewNode.h>
```

> **Inherits:** [`UComposableCameraCameraNodeBase`](../uobjects-other/UComposableCameraCameraNodeBase.md#ucomposablecameracameranodebase)

Node for adjusting field of view. This FOV is directly set to the CameraPose each frame.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `float` | [`FieldOfView`](#fieldofview-1)  |  |
| `bool` | [`bDynamicFov`](#bdynamicfov)  |  |
| `float` | [`MinFoV`](#minfov)  |  |
| `float` | [`MaxFoV`](#maxfov)  |  |
| `float` | [`FoVDamping`](#fovdamping)  |  |
| `float` | [`DesiredTargetViewportSize`](#desiredtargetviewportsize)  |  |
| `TArray< TObjectPtr< AActor > >` | [`ActorsForDynamicFoV`](#actorsfordynamicfov)  |  |

---

#### FieldOfView { #fieldofview-1 }

```cpp
float FieldOfView { 79.f }
```

---

#### bDynamicFov { #bdynamicfov }

```cpp
bool bDynamicFov { false }
```

---

#### MinFoV { #minfov }

```cpp
float MinFoV { 30.f }
```

---

#### MaxFoV { #maxfov }

```cpp
float MaxFoV { 120.f }
```

---

#### FoVDamping { #fovdamping }

```cpp
float FoVDamping { 0.5f }
```

---

#### DesiredTargetViewportSize { #desiredtargetviewportsize }

```cpp
float DesiredTargetViewportSize { 40.f }
```

---

#### ActorsForDynamicFoV { #actorsfordynamicfov }

```cpp
TArray< TObjectPtr< AActor > > ActorsForDynamicFoV
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`OnTickNode_Implementation`](#onticknode_implementation-8) `virtual` |  |
| `void` | [`GetPinDeclarations_Implementation`](#getpindeclarations_implementation-8) `virtual` `const` |  |

---

#### OnTickNode_Implementation { #onticknode_implementation-8 }

`virtual`

```cpp
virtual void OnTickNode_Implementation(float DeltaTime, const FComposableCameraPose & CurrentCameraPose, FComposableCameraPose & OutCameraPose)
```

---

#### GetPinDeclarations_Implementation { #getpindeclarations_implementation-8 }

`virtual` `const`

```cpp
virtual void GetPinDeclarations_Implementation(TArray< FComposableCameraNodePinDeclaration > & OutPins) const
```
