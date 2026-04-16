# Changelog

Reverse-chronological log of documentation updates. Each entry corresponds to a batch of plugin changes that the auto-updater skill (`ccs-docs-updater`) processed.

Entries are written automatically; feel free to edit them if you want to reword or add context.

## 2026-04-16 — plugin `775fc66..2810fd5`

**Plugin commits** ([compare](https://github.com/littlesulley/ComposableCameraSystem/compare/775fc660c1a132c4549daa774d137f631926c4be...2810fd5eac84f7ca98d8adb0bd05de0a7a18445d))

- `2810fd5` Optimize pins; add more nodes; support complex camera pose parameters; add FName and Enum pin support.

**C++ API pages regenerated:** 39 classes changed (5 added, 32 modified, 2 removed).

- Added: `UComposableCameraFilmbackNode`, `UComposableCameraLensNode`, `UComposableCameraOrthographicNode`, `FComposableCameraNodePinBinding`, `FComposableCameraNodePinBindingTable`.
- Removed: `UComposableCameraComputeRandomOffsetNode`, `UComposableCameraFixedPoseNode` (headers deleted upstream).

**Prose drafts added:** none — `docs/reference/nodes.md` already contains hand-authored entries for all three new nodes (`LensNode`, `FilmbackNode`, `OrthographicNode`), so no auto-drafted stubs were appended.

**Flagged for review:**

- `docs/reference/nodes.md` still contains prose sections for `FixedPoseNode` (line 16) and `ComputeRandomOffsetNode` (line 177) whose underlying headers were deleted in this commit range. Either confirm the nodes still exist under a different name or remove/update those prose entries.
- New `FComposableCameraNodePinBinding` / `FComposableCameraNodePinBindingTable` structs appeared alongside the "FName and Enum pin support" commit. Consider whether pin-binding authoring deserves a short section in `docs/user-guide/authoring-camera-types.md`.

---


## 2026-04-15 — initial baseline at plugin `775fc66`

Documentation site and auto-update pipeline established. The C++ API reference under `reference/api/` reflects plugin `dev-v1` at commit `775fc66` ("Refactor everything with AI."). Subsequent changes will appear above this entry.
