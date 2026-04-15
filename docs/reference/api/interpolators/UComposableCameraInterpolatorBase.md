
# UComposableCameraInterpolatorBase { #ucomposablecamerainterpolatorbase }

```cpp
#include <ComposableCameraInterpolatorBase.h>
```

> **Inherits:** `UObject`
> **Subclassed by:** [`UComposableCameraIIRInterpolator`](UComposableCameraIIRInterpolator.md#ucomposablecameraiirinterpolator), [`UComposableCameraSimpleSpringInterpolator`](UComposableCameraSimpleSpringInterpolator.md#ucomposablecamerasimplespringinterpolator), [`UComposableCameraSpringDamperInterpolator`](UComposableCameraSpringDamperInterpolator.md#ucomposablecameraspringdamperinterpolator)

Base interpolator.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `TUniquePtr< TCameraInterpolator< TValueTypeWrapper< double > > >` | [`BuildDoubleInterpolator`](#builddoubleinterpolator) `virtual` `const` `inline` |  |
| `TUniquePtr< TCameraInterpolator< TValueTypeWrapper< FVector2d > > >` | [`BuildVector2dInterpolator`](#buildvector2dinterpolator) `virtual` `const` `inline` |  |
| `TUniquePtr< TCameraInterpolator< TValueTypeWrapper< FVector3d > > >` | [`BuildVector3dInterpolator`](#buildvector3dinterpolator) `virtual` `const` `inline` |  |
| `TUniquePtr< TCameraInterpolator< TValueTypeWrapper< FQuat > > >` | [`BuildQuatInterpolator`](#buildquatinterpolator) `virtual` `const` `inline` |  |
| `TUniquePtr< TCameraInterpolator< TValueTypeWrapper< FRotator > > >` | [`BuildRotatorInterpolator`](#buildrotatorinterpolator) `virtual` `const` `inline` |  |

---

#### BuildDoubleInterpolator { #builddoubleinterpolator }

`virtual` `const` `inline`

```cpp
virtual inline TUniquePtr< TCameraInterpolator< TValueTypeWrapper< double > > > BuildDoubleInterpolator() const
```

---

#### BuildVector2dInterpolator { #buildvector2dinterpolator }

`virtual` `const` `inline`

```cpp
virtual inline TUniquePtr< TCameraInterpolator< TValueTypeWrapper< FVector2d > > > BuildVector2dInterpolator() const
```

---

#### BuildVector3dInterpolator { #buildvector3dinterpolator }

`virtual` `const` `inline`

```cpp
virtual inline TUniquePtr< TCameraInterpolator< TValueTypeWrapper< FVector3d > > > BuildVector3dInterpolator() const
```

---

#### BuildQuatInterpolator { #buildquatinterpolator }

`virtual` `const` `inline`

```cpp
virtual inline TUniquePtr< TCameraInterpolator< TValueTypeWrapper< FQuat > > > BuildQuatInterpolator() const
```

---

#### BuildRotatorInterpolator { #buildrotatorinterpolator }

`virtual` `const` `inline`

```cpp
virtual inline TUniquePtr< TCameraInterpolator< TValueTypeWrapper< FRotator > > > BuildRotatorInterpolator() const
```
