
# UComposableCameraModifierManager { #ucomposablecameramodifiermanager }

```cpp
#include <ComposableCameraModifierManager.h>
```

> **Inherits:** `UObject`

An actor managing all camera modifiers.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`AddModifier`](#addmodifier)  |  |
| `void` | [`RemoveModifier`](#removemodifier)  |  |
| `FComposableCameraModifierData &` | [`GetModifierData`](#getmodifierdata) `inline` |  |

---

#### AddModifier { #addmodifier }

```cpp
void AddModifier(UComposableCameraNodeModifierDataAsset * ModifierAsset)
```

---

#### RemoveModifier { #removemodifier }

```cpp
void RemoveModifier(UComposableCameraNodeModifierDataAsset * ModifierAsset)
```

---

#### GetModifierData { #getmodifierdata }

`inline`

```cpp
inline FComposableCameraModifierData & GetModifierData()
```

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FComposableCameraModifierData` | [`ModifierData`](#modifierdata)  |  |

---

#### ModifierData { #modifierdata }

```cpp
FComposableCameraModifierData ModifierData
```
