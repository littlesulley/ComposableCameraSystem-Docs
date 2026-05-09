"""
MkDocs hook: convert Obsidian wiki-link images to standard Markdown.

  ![[assets/images/Pasted image 20260416132656.png]]
  →  ![Pasted image 20260416132656](assets/images/Pasted image 20260416132656.png)

Also handles optional alt-text / resize syntax:
  ![[image.png|alt text]]  →  ![alt text](image.png)
  ![[image.png|300]]       →  ![image](image.png){width=300}
"""

import re
from pathlib import PurePosixPath
from urllib.parse import urljoin

_OBSIDIAN_IMG = re.compile(
    r'!\[\['           # opening ![[
    r'([^\]|]+)'       # group 1: file path (everything up to ] or |)
    r'(?:\|([^\]]*))?' # group 2: optional alt / size after |
    r'\]\]'            # closing ]]
)


def _replace(m: re.Match) -> str:
    path = m.group(1).strip()
    modifier = (m.group(2) or '').strip()

    # Derive a default alt from the filename (minus extension)
    stem = PurePosixPath(path).stem
    attr = ''

    if modifier.isdigit():
        # ![[img.png|300]] → resize
        alt = stem
        attr = '{width=%s}' % modifier
    elif modifier:
        alt = modifier
    else:
        alt = stem

    result = '![%s](%s)' % (alt, path)
    if attr:
        result += attr
    return result


def on_page_markdown(markdown: str, **kwargs) -> str:
    return _OBSIDIAN_IMG.sub(_replace, markdown)


def on_page_context(context, page, config, nav, **kwargs):
    # mkdocs-shadcn 0.10.6 derives this from page.file.src_path, which is
    # OS-specific and emits MkDocs 1.6 URL warnings on Windows. src_uri is the
    # URL-safe form of the same path.
    try:
        from shadcn.plugins.mixins.order import NUMBER_PREFIX
    except Exception:
        return context

    src_uri = NUMBER_PREFIX.sub(lambda m: m.group(1), page.file.src_uri)
    context["raw_markdown_url"] = urljoin(config.site_url or "/", src_uri)
    return context
