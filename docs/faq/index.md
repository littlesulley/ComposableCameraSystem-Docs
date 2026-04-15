# FAQ

Answers to questions that come up often enough to deserve a single canonical place. If your question isn't here, check the matching concept or reference page first — most "why does it behave like X" answers live there.

## Installation and project setup

### Do I need a C++ project?

Yes. `ComposableCameraSystem` is a source plugin — it compiles as part of your project, not the engine. A Blueprint-only project can't compile source plugins. The simplest migration is **File → New C++ Class** (any trivial class) in your existing Blueprint project — UE regenerates the project as a C++ project automatically.

### Which engine versions does it support?

UE 5.6 only. The plugin uses APIs that don't exist in 5.5 and earlier, and no backport is planned.

### Which platforms?

**Win64, Android, Linux, LinuxArm64** are supported. macOS, iOS, and consoles have not been tested. If you hit a platform-specific build break, open an issue with the error output.

### How do I switch the PCM?

Set the `PlayerCameraManagerClass` on your `APlayerController` subclass (or its Blueprint equivalent) to `AComposableCameraPlayerCameraManager`. The full walkthrough is in [Enabling the Plugin](../getting-started/enabling-plugin.md).

### `Activate Composable Camera` has no parameter pins. Where did they go?

The K2 node introspects the selected type asset and builds pins for each exposed parameter. If the pins are missing:

- **No type asset selected yet** — select one.
- **Type asset has no parameters authored** — open it in the graph editor and add some in the Parameters panel.
- **Parameters changed after the K2 node was placed** — right-click the node, **Refresh Node**.

## Behavior and semantics

### Why did my camera snap instead of blend?

For a blend to fire, the five-tier resolution chain has to yield a non-null transition. Most common causes of an unintended snap:

1. **First activation after PIE start** — if nothing supplies a transition, the first camera of a PIE session hard-cuts in. This is by design.
2. **Caller-supplied `TransitionOverride` = null** — an explicit null caller override still wins tier 1 and short-circuits the rest.
3. **Target camera has no `EnterTransition`** and the source has no `ExitTransition` and no transition-table entry matches the pair — tier 5 is reached and there's no transition to run.

Set `EnterTransition` on the target type asset to an `InertializedTransition` as a safe default. See [Transitions & Blending](../user-guide/transitions-and-blending.md#five-tier-resolution-chain-in-practice).

### Why did my stacked modifiers not combine their effects?

They target the same `NodeClass`. Only one modifier wins per `(camera, node class)` — whichever group has higher `Priority`. There is no stacking. If you need additive effects, either fold the logic into a single modifier, or split the targets across different node classes. See [Modifiers → Priority](../reference/modifiers.md#priority-one-group-wins-per-camera-node-class).

### My modifier isn't applying to the camera.

Three usual culprits:

- **The camera is transient.** Transient cameras skip modifier resolution entirely. Clear `bIsTransient` on the activation params.
- **Tag mismatch.** The group's `CameraTags` and the camera's tag set must share at least one tag (`HasAny` semantics). If the group has non-empty tags and the camera has an empty tag set, the group won't apply.
- **Priority lost to another group.** Another active group targeting the same node class has a higher `Priority`.

### I popped a context but nothing blended — the cutscene just disappeared.

Check `ExitTransition` on the cutscene's type asset. If it's null *and* nothing else in the resolution chain supplies a transition, the pop hard-cuts back. The `EnterTransition` on the *resumed* camera is the tier-4 fallback; set it if you don't want to author per-cutscene exit transitions.

### My camera tracks the target one frame behind.

That's the intended behavior when a node reads an actor position and another node uses it downstream — the read happens once per frame, the write is per frame. If the lag is visible, you're probably reading the actor at an evaluation point *after* the actor's own tick, causing a one-frame hitch. Two fixes:

- **Use the context parameter pattern** — pass the actor in as a context parameter rather than reading it fresh in a node. The PCM resolves the reference before evaluation begins.
- **Adjust tick prerequisites** — set the character's tick group to `TG_PrePhysics` and the PCM's camera eval to `TG_PostUpdateWork` so the camera always sees the final post-movement position.

## Performance

### How expensive is each camera?

The per-camera cost is dominated by the node chain. With the shipped ~8-node third-person composition, one camera evaluates in ~5–15 µs on a modern desktop CPU. A blend between two cameras roughly doubles that because both trees evaluate. The `CollisionPushNode` is usually the single most expensive shipped node — its trace/sphere-sweep dominates.

Measure on your target hardware with Unreal Insights; don't rely on desktop numbers for mobile budgets.

### Why is my node allocating in the hot path?

You probably violated the [hot-path rule](../extending/custom-nodes.md#the-hot-path-rule-repeated-because-it-matters). Common offenders:

- `FString::Printf` inside `OnTickNode_Implementation`.
- `TArray::Add` on a result buffer every frame — preallocate and use `SetNumUninitialized()` instead.
- `NewObject` inside tick — cache the subobject in `OnInitialize`.
- Implicit `FString` construction from `UE_LOG` at `Verbose` level (the format string is still built even when the log category is disabled). Gate verbose logs behind `if (UE_LOG_ACTIVE(LogComposableCameraSystem, Verbose))` explicitly.

### Blueprint nodes are slow, right?

`BlueprintCameraNode` ticks through the BP VM — in aggregate, several times slower than an equivalent C++ node. For prototyping or one-off gameplay-specific logic on a single camera, it's fine. For shipping production code that runs on many cameras every frame, port it to a C++ node. The [Custom Nodes](../extending/custom-nodes.md) recipe is the cheapest way to migrate.

## Editor

### My node's default value in the Details panel appears twice.

You have a pin declaration whose name doesn't exactly match its `UPROPERTY` `FName` — including the `b` prefix on bools. The editor renders both the reflection-driven row and the plain-text fallback row. Fix by aligning the names exactly, or remove the manual pin declaration and let reflection drive it.

### The graph editor's palette doesn't show my new node.

Check:

- The class is under `Source/ComposableCameraSystem/Public/Nodes/` (or your project's equivalent `Public/Nodes/`). The editor walks the class hierarchy; misplaced classes are invisible.
- The class derives from `UComposableCameraCameraNodeBase` (not `UObject`).
- You've done a full editor restart since the class was added — new `UCLASS`es aren't picked up by Live Coding.
- The class isn't marked `Abstract`.

### Right-click on a pin says "Refresh", but my pins don't change.

For K2 nodes (like `Activate Composable Camera`), **Refresh Node** re-runs pin generation against the currently-selected type asset. If the type asset's parameters haven't changed, refresh is a no-op. If you expected a refresh to pick up a schema change, save the type asset first — some schemas only propagate on save.

## Extending

### Where do new nodes live?

`Source/ComposableCameraSystem/Public/Nodes/` + `Source/ComposableCameraSystem/Private/Nodes/`. For transitions it's `Transitions/`, for modifiers it's `Modifiers/`. Don't add them to `Core/` or `Utils/` — the editor's discovery walks the canonical subfolders. See [Extending](../extending/index.md) for the full placement table.

### Can I add a node in my project module without modifying the plugin?

Yes. The reflection-driven discovery doesn't care which module the class lives in — as long as it derives from `UComposableCameraCameraNodeBase` and lives in a module that depends on `ComposableCameraSystem`, the editor finds it. Use the same `Public/Nodes` / `Private/Nodes` layout inside your project module.

### How do I ship a set of project-specific cameras without polluting the plugin?

Keep all project-specific types (type assets, subclassed nodes, modifier data assets) in your project Content folder and a project-level module. The plugin folder stays clean and upgradeable. Only touch the plugin when you're contributing back a genuinely-reusable feature.

### Can I write a node in Blueprint?

Yes — use `BlueprintCameraNode`, which provides a Blueprint-implementable `OnTickNode`. See the caveat in the Performance section above: it's fine for prototypes and one-off gameplay logic, not for production code on the hot path.

### What about a custom transition in Blueprint?

Not currently supported. Transitions must be C++. The four-phase lifecycle, `InitParams` plumbing, and pose-math helpers aren't exposed to BP in a way that would let you author a useful transition from the graph. Author in C++ and expose the parameters via `UPROPERTY(EditAnywhere)` — authors will see them in the instanced-subobject picker.

## Troubleshooting

### "No camera is active" overlay, but I called `ActivateComposableCamera`.

- The `BeginPlay` wiring fires before the follow target exists — delay activation until the target spawns.
- The `GameMode` isn't using `AComposableCameraPlayerCameraManager`. Revisit [Enabling the Plugin](../getting-started/enabling-plugin.md).
- A custom `PlayerController` overrides the PCM class elsewhere. Grep for `PlayerCameraManagerClass = ...`.
- The K2 node never ran — drop a print-string on its exec output to confirm.

### `showdebug composablecamera` shows garbage in the overlay (NaN positions, missing fields).

Something in the node chain produced a bad pose and a downstream node propagated it. Step through the chain by adding a `FixedPoseNode` between each pair and checking which swap "fixes" the output — the node *before* the bad output is the culprit. File an issue with the composition if it's a shipped node.

### My C++ modifier fails to apply — `Cast<MyNodeClass>(Node)` returns null.

The modifier's `NodeClass` is set to the wrong class, or was never set. Remember: `NodeClass` is a **Class Default Object**-level configuration, not a per-instance edit. Open the modifier class (not an instance), set `NodeClass` in its Details, recompile. The plugin intentionally marks it `EditDefaultsOnly, NoEditInline` to discourage per-instance edits that silently break the manager's indexing.

## Anything else

If none of the above covers your question, the short versions of the three reference spots:

- **Concept question** → one of the five pages under [User Guide → Concepts](../user-guide/concepts/index.md).
- **"What does X do?"** → [Reference](../reference/index.md) — the nodes / transitions / modifiers catalogs, or the auto-generated [C++ API](../reference/api/index.md).
- **"How do I build X?"** → [Tutorials](../tutorials/index.md).

For anything genuinely missing, open an issue on the [GitHub repository](https://github.com/littlesulley/ComposableCameraSystem-Docs/issues).
