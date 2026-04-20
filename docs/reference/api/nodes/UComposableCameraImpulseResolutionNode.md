
# UComposableCameraImpulseResolutionNode { #ucomposablecameraimpulseresolutionnode }

```cpp
#include <ComposableCameraImpulseResolutionNode.h>
```

> **Inherits:** [`UComposableCameraCameraNodeBase`](../uobjects-other/UComposableCameraCameraNodeBase.md#ucomposablecameracameranodebase)

Node for resolving impulse shapes including impulse box and impulse sphere.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `float` | [`VelocityDamping`](#velocitydamping)  |  |
| `UComposableCameraInterpolatorBase *` | [`Interpolator`](#interpolator-3)  |  |

---

#### VelocityDamping { #velocitydamping }

```cpp
float VelocityDamping { 1.f }
```

---

#### Interpolator { #interpolator-3 }

```cpp
UComposableCameraInterpolatorBase * Interpolator
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`OnInitialize_Implementation`](#oninitialize_implementation-10) `virtual` |  |
| `void` | [`OnTickNode_Implementation`](#onticknode_implementation-18) `virtual` |  |
| `void` | [`BeginDestroy`](#begindestroy-2) `virtual` |  |
| `void` | [`GetPinDeclarations_Implementation`](#getpindeclarations_implementation-16) `virtual` `const` |  |
| `void` | [`AddImpulseShape`](#addimpulseshape) `inline` |  |
| `void` | [`RemoveImpulseShape`](#removeimpulseshape) `inline` |  |

---

#### OnInitialize_Implementation { #oninitialize_implementation-10 }

`virtual`

```cpp
virtual void OnInitialize_Implementation()
```

---

#### OnTickNode_Implementation { #onticknode_implementation-18 }

`virtual`

```cpp
virtual void OnTickNode_Implementation(float DeltaTime, const FComposableCameraPose & CurrentCameraPose, FComposableCameraPose & OutCameraPose)
```

---

#### BeginDestroy { #begindestroy-2 }

`virtual`

```cpp
virtual void BeginDestroy()
```

---

#### GetPinDeclarations_Implementation { #getpindeclarations_implementation-16 }

`virtual` `const`

```cpp
virtual void GetPinDeclarations_Implementation(TArray< FComposableCameraNodePinDeclaration > & OutPins) const
```

---

#### AddImpulseShape { #addimpulseshape }

`inline`

```cpp
inline void AddImpulseShape(AActor * Shape)
```

---

#### RemoveImpulseShape { #removeimpulseshape }

`inline`

```cpp
inline void RemoveImpulseShape(AActor * Shape)
```

### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `TObjectPtr< USphereComponent >` | [`Sphere`](#sphere)  |  |
| `TArray< TScriptInterface< IComposableCameraImpulseShapeInterface > >` | [`ImpulseShapes`](#impulseshapes)  |  |
| `FVector` | [`OldVelocity`](#oldvelocity)  |  |
| `TUniquePtr< TCameraInterpolator< TValueTypeWrapper< FVector > > >` | [`Interpolator_T`](#interpolator_t-1)  |  |

---

#### Sphere { #sphere }

```cpp
TObjectPtr< USphereComponent > Sphere
```

---

#### ImpulseShapes { #impulseshapes }

```cpp
TArray< TScriptInterface< IComposableCameraImpulseShapeInterface > > ImpulseShapes
```

---

#### OldVelocity { #oldvelocity }

```cpp
FVector OldVelocity { FVector::ZeroVector }
```

---

#### Interpolator_T { #interpolator_t-1 }

```cpp
TUniquePtr< TCameraInterpolator< TValueTypeWrapper< FVector > > > Interpolator_T
```
