
# AComposableCameraImpulseBox { #acomposablecameraimpulsebox }

```cpp
#include <ComposableCameraImpulseBox.h>
```

> **Inherits:** `AActor`, [`IComposableCameraImpulseShapeInterface`](../interfaces/IComposableCameraImpulseShapeInterface.md#icomposablecameraimpulseshapeinterface)

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `EComposableCameraImpulseBoxDistanceType` | [`DistanceType`](#distancetype)  |  |
| `FRuntimeFloatCurve` | [`ForceCurve`](#forcecurve)  |  |

---

#### DistanceType { #distancetype }

```cpp
EComposableCameraImpulseBoxDistanceType DistanceType {  }
```

---

#### ForceCurve { #forcecurve }

```cpp
FRuntimeFloatCurve ForceCurve
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`AComposableCameraImpulseBox`](#acomposablecameraimpulsebox-1)  |  |
| `FVector` | [`GetForce`](#getforce) `virtual` |  |
| `FVector` | [`GetOrigin`](#getorigin) `virtual` |  |
| `AActor *` | [`GetSelf`](#getself) `virtual` `inline` |  |
| `FVector` | [`GetOrigin`](#getorigin-1)  |  |

---

#### AComposableCameraImpulseBox { #acomposablecameraimpulsebox-1 }

```cpp
AComposableCameraImpulseBox()
```

---

#### GetForce { #getforce }

`virtual`

```cpp
virtual FVector GetForce(const FVector & CameraPosition)
```

---

#### GetOrigin { #getorigin }

`virtual`

```cpp
virtual FVector GetOrigin()
```

---

#### GetSelf { #getself }

`virtual` `inline`

```cpp
virtual inline AActor * GetSelf()
```

---

#### GetOrigin { #getorigin-1 }

```cpp
FVector GetOrigin(const FVector & CameraPosition)
```

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TObjectPtr< UBoxComponent >` | [`BoxComponent`](#boxcomponent)  |  |

---

#### BoxComponent { #boxcomponent }

```cpp
TObjectPtr< UBoxComponent > BoxComponent
```
