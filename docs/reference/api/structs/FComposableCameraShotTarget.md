
# FComposableCameraShotTarget { #fcomposablecamerashottarget }

```cpp
#include <ComposableCameraShotTarget.h>
```

Per-Actor data within a single [FComposableCameraShot](FComposableCameraShot.md#fcomposablecamerashot). Targets are PURELY world-space objects: identity (Actor + Bone + Offset via the embedded `[FComposableCameraTargetInfo](FComposableCameraTargetInfo.md#fcomposablecameratargetinfo)`) plus an optional bounding box used by the FOV bounds-fit solve. Targets do NOT carry screen-space composition data — that lives on the Shot's Placement / Aim layers (see Docs/ShotBasedKeyframing.md §3 for the layered data model).

V1.x (pre-refactor): `DesiredScreenPosition`, `ScreenPositionWeight`, `Method` (Rotate / Translate) lived here. V2 deletes those fields — screen-position constraints come from `[FShotPlacement::ScreenPosition](FShotPlacement.md#screenposition-1)` (where the placement anchor lands, realized via lateral camera translation) and `[FShotAim::ScreenPosition](FShotAim.md#screenposition)` (where the aim anchor lands, realized via camera rotation). Method is no longer per-target: Placement is always Translate (changes Position), Aim is always Rotate (changes Rotation). This kills the old V1.x cross-layer coupling.

Properties are BlueprintReadOnly per the Shot system's "no runtime BP
API for mutating Shot data" principle (spec §1.4).

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `FComposableCameraTargetInfo` | [`Target`](#target)  | Identity + pivot resolution. Drives the world point this target contributes to all solver passes. |
| `EShotTargetBoundsShape` | [`BoundsShape`](#boundsshape)  |  |
| `FVector` | [`ManualBoundsExtent`](#manualboundsextent)  | Half-extent in world units; used iff BoundsShape == ManualExtent. |
| `EBoundsCachePolicy` | [`BoundsCachePolicy`](#boundscachepolicy)  | Cache refresh policy when BoundsShape == AutoFromComponentBounds. See EBoundsCachePolicy and spec §3.3.1. |
| `int32` | [`BoundsRefreshIntervalFrames`](#boundsrefreshintervalframes)  | Refresh interval in frames when BoundsCachePolicy == Periodic. |
| `FVector` | [`CachedAutoBoundsExtent`](#cachedautoboundsextent)  | Snapshot of Actor->GetComponentsBoundingBox().GetExtent() — populated via [RefreshAutoBoundsCache()](#refreshautoboundscache). Never read directly by user code; go through [GetEffectiveBoundsExtent()](#geteffectiveboundsextent) which dispatches on BoundsShape. |
| `TWeakObjectPtr< class UPrimitiveComponent >` | [`CachedBoundsMeshComponent`](#cachedboundsmeshcomponent)  | Cached weak ref to the actor's first SkeletalMesh / StaticMesh component used by `RefreshAutoBoundsCache`. Polish P.1 — without this, `Live`-policy refreshes call `Actor->FindComponentByClass<...>()` per tick per target (`O(actor.Components.Num())` linear walk), which accumulates measurably on character actors with 30+ components in a 4-target Shot at 60fps. With the cache, `Live` reduces to a weak-ptr validity check + a `Bounds.GetBox()` read; only invalidation (actor swap, component destroyed) re-runs `FindComponentByClass`. |
| `float` | [`BoundsContributionWeight`](#boundscontributionweight)  | Importance weight of this target's bounds in the FOV bounds-fit solve. Drives the BlackEye-style "perceptual union box" sizing in spec §4.5: high-weight targets dominate the resulting box, low-weight ones contribute proportionally less. 0 = target has bounds but doesn't drive FOV. Clamped [0, 1] — only ratios matter in the perceptual-box math, the [0, 1] convention keeps Details-panel intent readable. |

---

#### Target { #target }

```cpp
FComposableCameraTargetInfo Target
```

Identity + pivot resolution. Drives the world point this target contributes to all solver passes.

---

#### BoundsShape { #boundsshape }

```cpp
EShotTargetBoundsShape BoundsShape = 
```

---

#### ManualBoundsExtent { #manualboundsextent }

```cpp
FVector ManualBoundsExtent = FVector(50.f)
```

Half-extent in world units; used iff BoundsShape == ManualExtent.

---

#### BoundsCachePolicy { #boundscachepolicy }

```cpp
EBoundsCachePolicy BoundsCachePolicy = 
```

Cache refresh policy when BoundsShape == AutoFromComponentBounds. See EBoundsCachePolicy and spec §3.3.1.

---

#### BoundsRefreshIntervalFrames { #boundsrefreshintervalframes }

```cpp
int32 BoundsRefreshIntervalFrames = 30
```

Refresh interval in frames when BoundsCachePolicy == Periodic.

---

#### CachedAutoBoundsExtent { #cachedautoboundsextent }

```cpp
FVector CachedAutoBoundsExtent = FVector::ZeroVector
```

Snapshot of Actor->GetComponentsBoundingBox().GetExtent() — populated via [RefreshAutoBoundsCache()](#refreshautoboundscache). Never read directly by user code; go through [GetEffectiveBoundsExtent()](#geteffectiveboundsextent) which dispatches on BoundsShape.

Marked Transient: the cache is rebuilt at Shot activation and is never serialized.

---

#### CachedBoundsMeshComponent { #cachedboundsmeshcomponent }

```cpp
TWeakObjectPtr< class UPrimitiveComponent > CachedBoundsMeshComponent
```

Cached weak ref to the actor's first SkeletalMesh / StaticMesh component used by `RefreshAutoBoundsCache`. Polish P.1 — without this, `Live`-policy refreshes call `Actor->FindComponentByClass<...>()` per tick per target (`O(actor.Components.Num())` linear walk), which accumulates measurably on character actors with 30+ components in a 4-target Shot at 60fps. With the cache, `Live` reduces to a weak-ptr validity check + a `Bounds.GetBox()` read; only invalidation (actor swap, component destroyed) re-runs `FindComponentByClass`.

Stored as `TWeakObjectPtr<UPrimitiveComponent>` (the common base of SkelMesh + StaticMesh) so the same field handles either class. Mutable so the const-method `GetEffectiveBoundsExtent` could still do a read-side validity check if needed; current callers only mutate via `RefreshAutoBoundsCache` (already non-const). Transient so the cache doesn't persist across save/load — actors must re-resolve on first tick after load.

---

#### BoundsContributionWeight { #boundscontributionweight }

```cpp
float BoundsContributionWeight = 1.f
```

Importance weight of this target's bounds in the FOV bounds-fit solve. Drives the BlackEye-style "perceptual union box" sizing in spec §4.5: high-weight targets dominate the resulting box, low-weight ones contribute proportionally less. 0 = target has bounds but doesn't drive FOV. Clamped [0, 1] — only ratios matter in the perceptual-box math, the [0, 1] convention keeps Details-panel intent readable.

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`RefreshAutoBoundsCache`](#refreshautoboundscache)  | Refreshes CachedAutoBoundsExtent from Actor's component bounds. No-op when BoundsShape != AutoFromComponentBounds OR Target.Actor is null. Call from: (a) Shot Editor on Actor pick / BoundsShape toggle; (b) Runtime when the Shot becomes active in LS; (c) Periodic / Live tick if the policy demands. |
| `FVector` | [`GetEffectiveBoundsExtent`](#geteffectiveboundsextent) `const` | Returns the effective bounds half-extent based on BoundsShape: None → FVector::ZeroVector (target ignored by FOV solve) ManualExtent → ManualBoundsExtent AutoFromComponentBounds → CachedAutoBoundsExtent (zero if cache cold — degrades silently to "no bounds") |

---

#### RefreshAutoBoundsCache { #refreshautoboundscache }

```cpp
void RefreshAutoBoundsCache()
```

Refreshes CachedAutoBoundsExtent from Actor's component bounds. No-op when BoundsShape != AutoFromComponentBounds OR Target.Actor is null. Call from: (a) Shot Editor on Actor pick / BoundsShape toggle; (b) Runtime when the Shot becomes active in LS; (c) Periodic / Live tick if the policy demands.

Walks the actor's component hierarchy via GetComponentsBoundingBox (O(component count)) — never call from per-frame code unless the cache policy is Live.

---

#### GetEffectiveBoundsExtent { #geteffectiveboundsextent }

`const`

```cpp
FVector GetEffectiveBoundsExtent() const
```

Returns the effective bounds half-extent based on BoundsShape: None → FVector::ZeroVector (target ignored by FOV solve) ManualExtent → ManualBoundsExtent AutoFromComponentBounds → CachedAutoBoundsExtent (zero if cache cold — degrades silently to "no bounds")
