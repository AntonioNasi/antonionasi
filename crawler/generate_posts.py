import json
from pathlib import Path
import re
import unicodedata

BASE_DIR = Path(__file__).resolve().parent.parent

arquivo = BASE_DIR / "_data" / "eventos.json"

posts = BASE_DIR / "_eventos"

posts.mkdir(
    parents=True,
    exist_ok=True
)

with open(
    arquivo,
    encoding="utf8"
) as f:

    eventos = json.load(f)


def slugify(text):

    text = unicodedata.normalize(
        "NFKD",
        text
    ).encode(
        "ascii",
        "ignore"
    ).decode()

    text=text.lower()

    text=re.sub(
        r'["\':;,.!?()]',
        '',
        text
    )

    text=re.sub(
        r'[^a-z0-9\s-]',
        '',
        text
    )

    text=re.sub(
        r'\s+',
        '-',
        text
    )

    text=re.sub(
        '-+',
        '-',
        text
    )

    return text.strip("-")


for e in eventos:

    slug=slugify(
        e["title"]
    )

    filename=(
        f'{e["date"]}-{slug}.md'
    )

    titulo=e["title"].replace(
        '"',
        "'"
    )

    content=f"""---
layout: post
title: '{titulo}'
date: {e["date"]}
image: {e["image"]}
crawler: true
---

{e["excerpt"]}

[Acessar evento]({e["url"]})
"""

    with open(
        posts/filename,
        "w",
        encoding="utf8"
    ) as f:

        f.write(content)

print("Posts gerados")