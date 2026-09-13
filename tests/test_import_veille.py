import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from import_veille import slugify, to_markdown

assert slugify("Explorateur d'Accessibilité") == "explorateur-d-accessibilite"
assert slugify("Les-Tilleuls.coop") == "les-tilleuls-coop"

fiche = to_markdown({
    "name": 'Hack"n Speak',
    "url": "https://example.org/é",
    "type": "podcast",
    "themes": ["cybersecurite", "ia"],
    "lang": "FR",
})
assert 'title: "Hack\\"n Speak"' in fiche
assert "tags: [podcast, cybersecurite, ia]" in fiche
assert fiche.endswith("---\n\n\n")
print("ok")
