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

## License

The documentation content is authored by Sulley (littlesulley). License TBD.
