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
