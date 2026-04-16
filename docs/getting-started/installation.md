# Installation

This page covers getting the plugin files into your project. Enabling it and pointing your project at the new player camera manager is covered in [Enabling the Plugin](enabling-plugin.md).

## Requirements

| Requirement                    | Notes                                                                                                                                                      |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Unreal Engine **5.6** or above | The plugin tracks 5.6 or above and has not been back-ported.                                                                                               |
| A **C++ project**              | Blueprint-only projects cannot compile source plugins. If your project is Blueprint-only, convert it first via *File → New C++ Class* (any class will do). |
| Build toolchain                | Visual Studio 2022 on Windows, or Rider + the matching toolchain. UE's standard build setup applies.                                                       |
| Git (optional)                 | If you plan to customize and track the plugin as a submodule.                                                                                              |

Supported platforms are **Win64, Android, Linux, and LinuxArm64**, matching the `PlatformAllowList` declared in the `.uplugin` file. macOS, iOS, and consoles are not currently supported.

## Plugin dependencies

The plugin depends on three engine plugins that are bundled with UE 5.6:

- `EngineCameras` — Epic's built-in camera framework; used for a handful of shared base types.
- `EnhancedInput` — the default input system.
- `ActorSequence` — used by a couple of shipped nodes for in-camera sequence playback.

Each of these is shipped with the engine, so you do not need to install anything separately. They will be auto-enabled as transitive dependencies when ComposableCameraSystem itself is enabled.

## Installing the plugin

Choose **one** of the two options below.

### Option A — download and drop in

1. Download the plugin source from the [GitHub repository](https://github.com/littlesulley/ComposableCameraSystem) (either a release zip or a `git clone`).
2. Extract it so that you have a folder named `ComposableCameraSystem` containing `ComposableCameraSystem.uplugin`.
3. Copy that folder into your project's `Plugins/` directory. If `Plugins/` doesn't exist next to your `.uproject`, create it. The final path should be:

    ```
    <YourProject>/
    ├─ <YourProject>.uproject
    ├─ Source/
    └─ Plugins/
       └─ ComposableCameraSystem/
          ├─ ComposableCameraSystem.uplugin
          ├─ Source/
          └─ ...
    ```

### Option B — Git submodule

If your project is a Git repository and you want to stay up-to-date with the plugin's `dev-v1` branch:

```bash
cd <YourProject>
git submodule add -b dev-v1 https://github.com/littlesulley/ComposableCameraSystem.git Plugins/ComposableCameraSystem
git submodule update --init --recursive
```

Pulling new changes later is then `git submodule update --remote --merge`.

## Regenerating project files

After dropping the plugin in, tell UE to pick it up:

1. Close Visual Studio / Rider if it's open.
2. Right-click your project's `.uproject` in File Explorer (Windows) and choose **Generate Visual Studio project files**. On Linux, run `GenerateProjectFiles.sh` from your engine source, or use your IDE's equivalent.
3. Open the regenerated `.sln` / `.uproject` in your IDE.

You should now see a **ComposableCameraSystem** folder under `Games → <YourProject> → Plugins` in the Solution Explorer, with the three modules:

- `ComposableCameraSystem` (Runtime)
- `ComposableCameraSystemEditor` (Editor)
- `ComposableCameraSystemUncookedOnly` (UncookedOnly)

## First build

Build the **Development Editor** configuration for the `Win64` (or your platform) target. The first build compiles the plugin alongside your project and can take several minutes. Subsequent incremental builds are fast.

If the build fails, the most common causes are:

- **Engine version mismatch** — the plugin targets UE 5.6. Check that your project's `EngineAssociation` in the `.uproject` is `5.6`.
- **Compiler mismatch** — Windows builds need the UE-blessed VS 2022 workload installed (see Epic's [Setting Up Visual Studio](https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-visual-studio-development-environment-for-cplusplus-projects-in-unreal-engine) guide).
- **Missing transitive dependencies** — if you've customized your project to disable `EngineCameras`, `EnhancedInput`, or `ActorSequence`, re-enable them.

If the build succeeds, launch the editor and continue with [Enabling the Plugin](enabling-plugin.md).
