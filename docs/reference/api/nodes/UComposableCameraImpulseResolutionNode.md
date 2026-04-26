
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
| `UComposableCameraInterpolatorBase *` | [`Interpolator`](#interpolator-4)  |  |

---

#### VelocityDamping { #velocitydamping }

```cpp
float VelocityDamping { 1.f }
```

---

#### Interpolator { #interpolator-4 }

```cpp
UComposableCameraInterpolatorBase * Interpolator
```

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`UComposableCameraImpulseResolutionNode`](#ucomposablecameraimpulseresolutionnode-1) `inline` |  |
| `void` | [`OnInitialize_Implementation`](#oninitialize_implementation-16) `virtual` |  |
| `void` | [`OnTickNode_Implementation`](#onticknode_implementation-24) `virtual` |  |
| `void` | [`BeginDestroy`](#begindestroy-2) `virtual` |  |
| `void` | [`GetPinDeclarations_Implementation`](#getpindeclarations_implementation-22) `virtual` `const` |  |
| `void` | [`AddImpulseShape`](#addimpulseshape) `inline` |  |
| `void` | [`RemoveImpulseShape`](#removeimpulseshape) `inline` |  |

---

#### UComposableCameraImpulseResolutionNode { #ucomposablecameraimpulseresolutionnode-1 }

`inline`

```cpp
inline UComposableCameraImpulseResolutionNode()
```

---

#### OnInitialize_Implementation { #oninitialize_implementation-16 }

`virtual`

```cpp
virtual void OnInitialize_Implementation()
```

---

#### OnTickNode_Implementation { #onticknode_implementation-24 }

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

#### GetPinDeclarations_Implementation { #getpindeclarations_implementation-22 }

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
| `TUniquePtr< TCameraInterpolator< TValueTypeWrapper< FVector > > >` | [`Interpolator_T`](#interpolator_t-3)  |  |

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

#### Interpolator_T { #interpolator_t-3 }

```cpp
TUniquePtr< TCameraInterpolator< TValueTypeWrapper< FVector > > > Interpolator_T
```
