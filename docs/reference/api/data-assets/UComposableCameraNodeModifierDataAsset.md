
# UComposableCameraNodeModifierDataAsset { #ucomposablecameranodemodifierdataasset }

```cpp
#include <ComposableCameraModifierDataAsset.h>
```

> **Inherits:** `UDataAsset`

Data asset for node modifiers. A node modifier can modify any parameters of any node type at runtime. <br/>
All modifiers are defined using blueprints by the users. Modifiers can only be applied to non-transient cameras.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TArray< UComposableCameraModifierBase * >` | [`Modifiers`](#modifiers-1)  |  |
| `UComposableCameraTransitionBase *` | [`OverrideEnterTransition`](#overrideentertransition)  |  |
| `UComposableCameraTransitionBase *` | [`OverrideExitTransition`](#overrideexittransition)  |  |
| `FGameplayTagContainer` | [`CameraTags`](#cameratags)  |  |
| `int32` | [`Priority`](#priority)  |  |

---

#### Modifiers { #modifiers-1 }

```cpp
TArray< UComposableCameraModifierBase * > Modifiers
```

---

#### OverrideEnterTransition { #overrideentertransition }

```cpp
UComposableCameraTransitionBase * OverrideEnterTransition
```

---

#### OverrideExitTransition { #overrideexittransition }

```cpp
UComposableCameraTransitionBase * OverrideExitTransition
```

---

#### CameraTags { #cameratags }

```cpp
FGameplayTagContainer CameraTags
```

---

#### Priority { #priority }

```cpp
int32 Priority { 0 }
```
