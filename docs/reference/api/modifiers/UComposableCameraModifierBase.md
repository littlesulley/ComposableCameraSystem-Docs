
# UComposableCameraModifierBase { #ucomposablecameramodifierbase }

```cpp
#include <ComposableCameraModifierBase.h>
```

> **Inherits:** `UObject`

An abstract modifier that provides interfaces for customizing node properties. Modifiers can only be applied to non-transient cameras.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TSubclassOf< UComposableCameraCameraNodeBase >` | [`NodeClass`](#nodeclass)  |  |

---

#### NodeClass { #nodeclass }

```cpp
TSubclassOf< UComposableCameraCameraNodeBase > NodeClass
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`ApplyModifier`](#applymodifier)  |  |

---

#### ApplyModifier { #applymodifier }

```cpp
void ApplyModifier(UComposableCameraCameraNodeBase * Node)
```
