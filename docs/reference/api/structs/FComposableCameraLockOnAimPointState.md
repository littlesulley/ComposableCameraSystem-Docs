# FComposableCameraLockOnAimPointState { #fcomposablecameralockonaimpointstate }

```cpp
#include <ComposableCameraLockOnAimPoint.h>
```

Runtime state for `ComposableCameraSystem::ComputeLockOnAimPoint`.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `bool` | [`bInModify`](#binmodify) | True while the follow/aim pair is inside the correction radius. |
| `bool` | [`bHasCurrentAddition`](#bhascurrentaddition) | True while a correction offset is active or blending out. |
| `FVector` | [`CurrentAddition`](#currentaddition) | Current correction offset added to the raw aim point. |
| `bool` | [`bIsBlendingOut`](#bisblendingout) | True while the previous correction offset is fading back to zero. |
| `float` | [`BlendOutElapsedTime`](#blendoutelapsedtime) | Elapsed blend-out time in seconds. |
| `FVector` | [`BlendOutStartAddition`](#blendoutstartaddition) | Correction offset captured when blend-out began. |

---

#### bInModify { #binmodify }

```cpp
bool bInModify = false
```

True while the follow/aim pair is inside the correction radius.

---

#### bHasCurrentAddition { #bhascurrentaddition }

```cpp
bool bHasCurrentAddition = false
```

True while a correction offset is active or blending out.

---

#### CurrentAddition { #currentaddition }

```cpp
FVector CurrentAddition = FVector::ZeroVector
```

Current correction offset added to the raw aim point.

---

#### bIsBlendingOut { #bisblendingout }

```cpp
bool bIsBlendingOut = false
```

True while the previous correction offset is fading back to zero.

---

#### BlendOutElapsedTime { #blendoutelapsedtime }

```cpp
float BlendOutElapsedTime = 0.f
```

Elapsed blend-out time in seconds.

---

#### BlendOutStartAddition { #blendoutstartaddition }

```cpp
FVector BlendOutStartAddition = FVector::ZeroVector
```

Correction offset captured when blend-out began.
