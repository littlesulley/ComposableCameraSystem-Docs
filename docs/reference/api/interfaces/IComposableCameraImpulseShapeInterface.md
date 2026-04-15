
# IComposableCameraImpulseShapeInterface { #icomposablecameraimpulseshapeinterface }

```cpp
#include <ComposableCameraImpulseShapeInterface.h>
```

> **Subclassed by:** [`AComposableCameraImpulseBox`](../actors/AComposableCameraImpulseBox.md#acomposablecameraimpulsebox), [`AComposableCameraImpulseSphere`](../actors/AComposableCameraImpulseSphere.md#acomposablecameraimpulsesphere)

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `FVector` | [`GetForce`](#getforce-2)  |  |
| `FVector` | [`GetOrigin`](#getorigin-3)  |  |
| `AActor *` | [`GetSelf`](#getself-2)  |  |
| `void` | [`BindToOnComponentBeginOverlap`](#bindtooncomponentbeginoverlap) `virtual` `inline` |  |
| `void` | [`BindToOnComponentEndOverlap`](#bindtooncomponentendoverlap) `virtual` `inline` |  |

---

#### GetForce { #getforce-2 }

```cpp
FVector GetForce(const FVector & CameraPosition)
```

---

#### GetOrigin { #getorigin-3 }

```cpp
FVector GetOrigin()
```

---

#### GetSelf { #getself-2 }

```cpp
AActor * GetSelf()
```

---

#### BindToOnComponentBeginOverlap { #bindtooncomponentbeginoverlap }

`virtual` `inline`

```cpp
virtual inline void BindToOnComponentBeginOverlap(UPrimitiveComponent * OverlappedComponent, AActor * OtherActor, UPrimitiveComponent * OtherComp, int32 OtherBodyIndex, bool bFromSweep, const FHitResult & SweepResult)
```

---

#### BindToOnComponentEndOverlap { #bindtooncomponentendoverlap }

`virtual` `inline`

```cpp
virtual inline void BindToOnComponentEndOverlap(UPrimitiveComponent * OverlappedComponent, AActor * OtherActor, UPrimitiveComponent * OtherComp, int32 OtherBodyIndex)
```
