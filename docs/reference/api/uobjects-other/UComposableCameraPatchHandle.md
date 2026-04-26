
# UComposableCameraPatchHandle { #ucomposablecamerapatchhandle }

```cpp
#include <ComposableCameraPatchHandle.h>
```

> **Inherits:** `UObject`

Caller-facing opaque handle to an active Patch.

Held weakly: when the underlying instance is removed (expired, context popped, Director destroyed), the handle's getters return defaulted values and IsActive returns false. Callers do not need to null-check the handle on every getter.

Construction is internal to [UComposableCameraPatchManager](UComposableCameraPatchManager.md#ucomposablecamerapatchmanager) — callers receive the handle from AddPatch and pass it to ExpirePatch / the BP getters.

GC lifetime caveat: the handle UObject itself has only a weak back-reference from the instance, so callers MUST keep the handle alive through their own strong reference. Blueprint usage is automatic — BP variables hold strong refs. C++ usage requires storing the handle in a UPROPERTY (or other GC-tracked location) on the owning class; a raw local pointer that goes out of scope will be collected, after which Manual-channel ExpirePatch becomes impossible (Duration / Condition channels still expire normally).

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`BindInstance`](#bindinstance)  | Internal binding — set by PatchManager::AddPatch immediately after handle construction. |
| `UComposableCameraPatchInstance *` | [`GetInstance`](#getinstance) `const` |  |
| `bool` | [`IsActive`](#isactive) `const` |  |
| `EComposableCameraPatchPhase` | [`GetPhase`](#getphase) `const` |  |
| `float` | [`GetAlpha`](#getalpha) `const` |  |
| `float` | [`GetElapsedTime`](#getelapsedtime-1) `const` |  |

---

#### BindInstance { #bindinstance }

```cpp
void BindInstance(UComposableCameraPatchInstance * InInstance)
```

Internal binding — set by PatchManager::AddPatch immediately after handle construction.

---

#### GetInstance { #getinstance }

`const`

```cpp
UComposableCameraPatchInstance * GetInstance() const
```

---

#### IsActive { #isactive }

`const`

```cpp
bool IsActive() const
```

---

#### GetPhase { #getphase }

`const`

```cpp
EComposableCameraPatchPhase GetPhase() const
```

---

#### GetAlpha { #getalpha }

`const`

```cpp
float GetAlpha() const
```

---

#### GetElapsedTime { #getelapsedtime-1 }

`const`

```cpp
float GetElapsedTime() const
```

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TWeakObjectPtr< UComposableCameraPatchInstance >` | [`Instance`](#instance)  |  |

---

#### Instance { #instance }

```cpp
TWeakObjectPtr< UComposableCameraPatchInstance > Instance
```
