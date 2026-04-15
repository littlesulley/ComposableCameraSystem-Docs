
# FComposableCameraPinKey { #fcomposablecamerapinkey }

```cpp
#include <ComposableCameraNodePinTypes.h>
```

Key identifying a specific pin on a specific node instance. Used as a map key in the RuntimeDataBlock for offset lookups.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `int32` | [`NodeIndex`](#nodeindex)  |  |
| `FName` | [`PinName`](#pinname)  |  |

---

#### NodeIndex { #nodeindex }

```cpp
int32 NodeIndex = INDEX_NONE
```

---

#### PinName { #pinname }

```cpp
FName PinName
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `bool` | [`operator==`](#operator-6) `const` `inline` |  |

---

#### operator== { #operator-6 }

`const` `inline`

```cpp
inline bool operator==(const FComposableCameraPinKey & Other) const
```
