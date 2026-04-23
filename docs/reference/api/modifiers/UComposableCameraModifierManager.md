
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
| `const FComposableCameraModifierData &` | [`GetModifierData`](#getmodifierdata-1) `const` `inline` | Const overload for read-only access (debug tooling / inspectors). Returns the same struct by const reference — callers can iterate the ModifierData / EffectiveModifiers maps but cannot mutate them. |

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

---

#### GetModifierData { #getmodifierdata-1 }

`const` `inline`

```cpp
inline const FComposableCameraModifierData & GetModifierData() const
```

Const overload for read-only access (debug tooling / inspectors). Returns the same struct by const reference — callers can iterate the ModifierData / EffectiveModifiers maps but cannot mutate them.

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FComposableCameraModifierData` | [`ModifierData`](#modifierdata)  |  |

---

#### ModifierData { #modifierdata }

```cpp
FComposableCameraModifierData ModifierData
```
