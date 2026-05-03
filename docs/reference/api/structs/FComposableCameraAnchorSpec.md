
# FComposableCameraAnchorSpec { #fcomposablecameraanchorspec }

```cpp
#include <ComposableCameraShot.h>
```

Resolves a single world-space anchor point from various sources. Reused by `[FShotPlacement::PlacementAnchor](FShotPlacement.md#placementanchor)`, `[FShotAim::AimAnchor](FShotAim.md#aimanchor)`, and `[FShotFocus::FocusAnchor](FShotFocus.md#focusanchor)` — three different roles, one shape.

Three modes:

* SingleTarget: anchor = one target's pivot

* WeightedWorldCentroid: anchor = weighted centroid of N targets

* FixedWorldPosition: anchor = an explicit world point

Properties are BlueprintReadOnly per spec §1.4.

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `EShotAnchorMode` | [`Mode`](#mode-3)  |  |
| `int32` | [`TargetIndex`](#targetindex)  | Index into the owning Shot's Targets array. Used iff Mode == SingleTarget. Validated >= 0 && < Targets.Num() at solve time. |
| `TArray< FComposableCameraAnchorTargetWeight >` | [`WeightedTargets`](#weightedtargets)  | Per-target weights for WeightedWorldCentroid mode. |
| `FVector` | [`WorldPosition`](#worldposition)  | Explicit world-space point, used iff Mode == FixedWorldPosition. |

---

#### Mode { #mode-3 }

```cpp
EShotAnchorMode Mode = 
```

---

#### TargetIndex { #targetindex }

```cpp
int32 TargetIndex = 0
```

Index into the owning Shot's Targets array. Used iff Mode == SingleTarget. Validated >= 0 && < Targets.Num() at solve time.

---

#### WeightedTargets { #weightedtargets }

```cpp
TArray< FComposableCameraAnchorTargetWeight > WeightedTargets
```

Per-target weights for WeightedWorldCentroid mode.

---

#### WorldPosition { #worldposition }

```cpp
FVector WorldPosition = FVector::ZeroVector
```

Explicit world-space point, used iff Mode == FixedWorldPosition.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `bool` | [`ResolveWorldPosition`](#resolveworldposition) `const` | Resolves to a single world point given the Shot's full target list. Returns false (OutPos unchanged) when: SingleTarget — TargetIndex out of range OR Actor null WeightedCentroid — no entry has Weight > 0 AND a valid Actor FixedWorldPosition — never (always returns true) |

---

#### ResolveWorldPosition { #resolveworldposition }

`const`

```cpp
bool ResolveWorldPosition(TConstArrayView< FComposableCameraShotTarget > Targets, FVector & OutPos) const
```

Resolves to a single world point given the Shot's full target list. Returns false (OutPos unchanged) when: SingleTarget — TargetIndex out of range OR Actor null WeightedCentroid — no entry has Weight > 0 AND a valid Actor FixedWorldPosition — never (always returns true)
