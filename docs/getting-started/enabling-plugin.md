# Enabling the Plugin

At this point you should have the plugin compiled into your project from [Installation](installation.md). This page turns it on and wires your project up to actually use it.

## 1. Enable the plugin in Project Settings

1. Open the editor.
2. Go to **Edit → Plugins**.
3. In the search box, type `ComposableCameraSystem`.
4. Tick the **Enabled** checkbox next to the plugin.
5. Click **Restart Now** when prompted.

After the restart, verify that the plugin is live by looking at **Edit → Plugins → Installed → Other**; you should see `ComposableCameraSystem` marked as enabled, along with its three transitive dependencies (`EngineCameras`, `EnhancedInput`, `ActorSequence`) which are auto-enabled by UE.

## 2. Swap in the Composable Camera Player Camera Manager

ComposableCameraSystem runs through a custom subclass of `APlayerCameraManager` called `AComposableCameraPlayerCameraManager`. Any PlayerController that should use the new camera system needs to be pointed at it.

The recommended way is to set it **on your default PlayerController class**, so every player in your project picks it up automatically.

### If you're using a Blueprint PlayerController

1. Open your project's PlayerController Blueprint (often `BP_PlayerController` or similar — check **Project Settings → Maps & Modes → Default Modes → Selected GameMode → Player Controller Class**).
2. In the Class Defaults, find the **Camera** category.
3. Set **Player Camera Manager Class** to `ComposableCameraPlayerCameraManager`.
4. Compile and save.

### If you're using a C++ PlayerController

In the constructor of your PlayerController:

```cpp
#include "ComposableCameraPlayerCameraManager.h"

AMyPlayerController::AMyPlayerController()
{
    PlayerCameraManagerClass = AComposableCameraPlayerCameraManager::StaticClass();
}
```

Make sure the file that includes this lists `ComposableCameraSystem` in its module `.Build.cs`:

```csharp
PublicDependencyModuleNames.AddRange(new[]
{
    "Core", "CoreUObject", "Engine", "InputCore",
    "ComposableCameraSystem",
});
```

### If you haven't customized the PlayerController at all

You'll need a custom one for this setup. The quickest path is to create a small Blueprint subclass of `PlayerController`, set its **Player Camera Manager Class** as above, and then in **Project Settings → Maps & Modes**, set **Default Modes → Selected GameMode → Player Controller Class** (or your game mode's Player Controller Class) to your new Blueprint.

## 3. Verify in PIE

1. Open any level in your project.
2. Press **Play** (Alt+P or the toolbar's Play button) to enter Play-In-Editor.
3. Open the console (backtick `` ` ``) and type:

    ```
    showdebug composablecamera
    ```

    You should see an on-screen debug overlay showing the active camera context stack, the current camera, and the current evaluation tree.

If the overlay doesn't appear:

- **Nothing at all on screen** — the `showdebug` command is typo-sensitive. Make sure you typed `composablecamera` with no spaces.
- **Debug says "No Composable Camera PCM"** — your PlayerController is still using the default `APlayerCameraManager`. Re-check step 2 and confirm that the PlayerController you set the class on is actually the one your GameMode spawns.
- **Editor crashes or fails to PIE** — check the output log for `LogComposableCameraSystem` errors. The most common cause is a missing transitive engine plugin dependency; re-enable `EngineCameras`, `EnhancedInput`, and `ActorSequence`.

## What's happening under the hood

`AComposableCameraPlayerCameraManager` replaces the default per-frame camera update logic with a pipeline that owns:

- a **Context Stack** (gameplay / cutscene / UI-style modes),
- a **Director** per context, and
- an **Evaluation Tree** per director that blends cameras and nodes into the final pose each frame.

You don't interact with those directly yet — activating a camera (the next page) handles the plumbing. For the full picture see [Concepts](../user-guide/concepts/index.md).

Once the debug overlay is printing, you're ready to [author your first camera](your-first-camera.md).
