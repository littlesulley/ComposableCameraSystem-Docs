
# AComposableCameraImpulseSphere { #acomposablecameraimpulsesphere }

```cpp
#include <ComposableCameraImpulseSphere.h>
```

> **Inherits:** `AActor`, [`IComposableCameraImpulseShapeInterface`](../interfaces/IComposableCameraImpulseShapeInterface.md#icomposablecameraimpulseshapeinterface)

This actor can be placed into levels or spawned dynamically to provide an impulse mechanism for cameras. <br/>
When camera enters the sphere, it will receive consistent impulse force initiated by this sphere. <br/>
The force direction is from the sphere origin to the camera position.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `float` | [`Radius`](#radius-1)  |  |
| `FRuntimeFloatCurve` | [`ForceCurve`](#forcecurve-1)  |  |

---

#### Radius { #radius-1 }

```cpp
float Radius { 100.f }
```

---

#### ForceCurve { #forcecurve-1 }

```cpp
FRuntimeFloatCurve ForceCurve
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`AComposableCameraImpulseSphere`](#acomposablecameraimpulsesphere-1)  |  |
| `FVector` | [`GetForce`](#getforce-1) `virtual` |  |
| `FVector` | [`GetOrigin`](#getorigin-2) `virtual` |  |
| `AActor *` | [`GetSelf`](#getself-1) `virtual` `inline` |  |

---

#### AComposableCameraImpulseSphere { #acomposablecameraimpulsesphere-1 }

```cpp
AComposableCameraImpulseSphere()
```

---

#### GetForce { #getforce-1 }

`virtual`

```cpp
virtual FVector GetForce(const FVector & CameraPosition)
```

---

#### GetOrigin { #getorigin-2 }

`virtual`

```cpp
virtual FVector GetOrigin()
```

---

#### GetSelf { #getself-1 }

`virtual` `inline`

```cpp
virtual inline AActor * GetSelf()
```

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TObjectPtr< USphereComponent >` | [`SphereComponent`](#spherecomponent)  |  |

---

#### SphereComponent { #spherecomponent }

```cpp
TObjectPtr< USphereComponent > SphereComponent
```
