# ComposableCameraSystem — Documentation

Source for the public documentation site at **https://composable-camera-system.readthedocs.io**.

This repository is the authoring source: Markdown files under `docs/`, MkDocs config in `mkdocs.yml`, Read the Docs build config in `.readthedocs.yaml`. Read the Docs pulls from `main` on every push and rebuilds the site automatically.

## Stack

- **[MkDocs](https://www.mkdocs.org/)** — static site generator
- **[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)** — theme
- **[Read the Docs](https://readthedocs.org/)** — build + hosting
- **KaTeX** — math rendering
- **Mermaid** — diagrams (via `pymdownx.superfences`)

## Local preview

```bash
python -m venv .venv
source .venv/bin/activate    # .venv\Scripts\activate on Windows
pip install -r requirements.txt
mkdocs serve
```

Then open http://localhost:8000.

## Authoring conventions

- Use standard Markdown — no wikilinks, no Obsidian-embedded-file syntax.
- Images go under `docs/assets/images/` and are referenced relatively.
- Math: inline `$x$`, display `$$ ... $$`.
- Mermaid diagrams live inside ` ```mermaid ` code fences.
- Cross-references use relative links to `.md` files, e.g. `[Context Stack](../concepts/context-stack.md)`.

## Obsidian setup for contributors

Open this folder as an Obsidian vault and configure:

- *Settings → Files & Links → Use [[Wikilinks]]* — **off**
- *New link format* — **Relative path to file**
- *Default location for new attachments* — **In subfolder under current folder** → `assets/images`

That's it. Anything you write will render identically in MkDocs.

## Auto-generated C++ API reference

`docs/reference/api/` is generated from the plugin's C++ headers. It is **committed to this repo** (not generated on RTD), so the checked-in state is what ships. Regenerate whenever the plugin's public headers change:

1. Clone the plugin (public) and check out the branch you want to document:
   ```bash
   git clone --depth 1 --branch dev-v1 \
     https://github.com/littlesulley/ComposableCameraSystem.git plugin-src
   ```
2. Run Doxygen against the plugin headers:
   ```bash
   cd plugin-src && doxygen ../Doxyfile   # Doxyfile is in this repo's root
   ```
   Output: `plugin-src/doxygen-out/xml/` (~230 XML files).
3. Run moxygen to produce a single monolithic Markdown file:
   ```bash
   moxygen --anchors --output api.md plugin-src/doxygen-out/xml
   ```
4. Run the splitter to emit per-class pages and a categorized index:
   ```bash
   python3 tools/split_api.py          # reads api.md, writes docs/reference/api/
   ```
5. Rebuild the nav fragment under Reference → C++ API Reference in `mkdocs.yml`:
   ```bash
   python3 tools/build_api_nav.py      # prints the YAML fragment; paste into mkdocs.yml
   ```
6. Commit the regenerated `docs/reference/api/` tree and updated `mkdocs.yml`.

The Doxygen config (`Doxyfile`) and the two Python tools (`tools/split_api.py`, `tools/build_api_nav.py`) are tracked here. Moxygen is installed via `npm install -g moxygen`.

## License

The documentation content is authored by Sulley (littlesulley). License TBD.
