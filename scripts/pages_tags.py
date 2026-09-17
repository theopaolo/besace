"""Régénère la liste des étiquettes proposées par Pages CMS (.pages.yml) à partir des signets.

À lancer après avoir ajouté une étiquette dans un éditeur : Pages CMS ne propose que les valeurs listées.
"""
import glob
import re
from pathlib import Path

import yaml

tags = set()
for f in glob.glob("content/signets/*.md"):
    s = Path(f).read_text()
    if not s.startswith("---"):
        continue
    d = yaml.safe_load(s.split("---")[1]) or {}
    tags.update((d.get("taxonomies") or {}).get("tags") or [])

p = Path(".pages.yml")
s = p.read_text()
liste = "[" + ", ".join(sorted(tags)) + "]"
s, n = re.subn(r"(# étiquettes : scripts/pages_tags\.py\n\s*values: )\[.*?\]", lambda m: m.group(1) + liste, s, flags=re.S)
assert n == 1, "repère des étiquettes introuvable dans .pages.yml"
p.write_text(s)
print(f"{len(tags)} étiquettes")
