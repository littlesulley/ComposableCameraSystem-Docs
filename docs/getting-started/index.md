---
title: Getting Started
---

# Getting Started

This section walks you through the three steps from a fresh UE 5.6 project to a working ComposableCameraSystem camera:

1. **[Installation](installation.md)** — drop the plugin into your project and regenerate project files.
2. **[Enabling the Plugin](enabling-plugin.md)** — switch your project's player camera manager over to `AComposableCameraPlayerCameraManager` and verify the setup in PIE.
3. **[Your First Camera](your-first-camera.md)** — create a camera type asset, wire a small follow + look-at rig in the graph editor, and activate it from a Blueprint.

## Before you begin

ComposableCameraSystem is a **source plugin** — you compile it as part of your project, not the engine. That means:

- Your project must be a **C++ project** (Blueprint-only projects cannot compile source plugins).
- You need a working **Visual Studio 2022** (Windows), **Xcode** (macOS), or **Rider** + toolchain setup, matching Epic's standard UE 5.6 build environment.
- Supported platforms: **Win64, Android, Linux, LinuxArm64**. The plugin has not been tested on macOS, iOS, or consoles.

!!! warning "Version status"
    The plugin is currently at **version 0.1** and is flagged `IsExperimentalVersion`. APIs, asset formats, and the graph editor schema may change without notice. Expect to rebuild caches and re-save assets between updates.

## What you'll have at the end

A project whose active camera is driven by a data asset you authored in the graph editor, and a Blueprint node you can call to activate it. From there the rest of the docs — the **User Guide**, **Tutorials**, and **Extending** sections — build on this foundation.
