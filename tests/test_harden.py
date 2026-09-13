import shutil
import subprocess
import tempfile
from pathlib import Path


root = Path(__file__).resolve().parents[1]
with tempfile.TemporaryDirectory(prefix="glane-harden-", dir="/tmp") as directory:
    site = Path(directory).resolve()
    for name in ("templates", "static"):
        shutil.copytree(root / name, site / name)
    shutil.copy(root / "config.toml", site)
    (site / "content/signets").mkdir(parents=True)
    shutil.copy(root / "content/_index.md", site / "content")
    shutil.copy(root / "content/signets/_index.md", site / "content/signets")
    (site / "content/images").mkdir()
    shutil.copy(root / "content/images/fond.jpg", site / "content/images")

    def build():
        subprocess.run(["zola", "build", "--force"], cwd=site, check=True)
        return (site / "public/index.html").read_text()

    empty = build()
    assert "Aucun signet pour le moment" in empty
    assert "Ajouter le premier signet" in empty
    assert "Page introuvable" in (site / "public/404.html").read_text()

    for name, fields in {
        "missing": "",
        "unsafe": 'extra:\n  url: "javascript:alert(1)"\n',
        "valid": 'extra:\n  url: "https://example.org/?a=1&b=2"\ntaxonomies:\n  category: [design]\n  tags: [developpement]\n',
    }.items():
        (site / f"content/signets/{name}.md").write_text(
            f'---\ntitle: "{name} 中文 مرحبا 👋"\n{fields}---\n\nTexte de la fiche.\n'
        )
    populated = build()
    assert 'id="filtres-tags"' in populated
    assert '<h2 class="fiche-titre' in populated
    assert '<p class="fiche-onglet">' in populated
    assert "pastille" not in populated
    assert 'href="https://app.pagescms.org"' in populated
    assert "Sans catégorie" in populated
    assert "missing 中文 مرحبا 👋" in populated
    assert "unsafe 中文 مرحبا 👋" in populated
    assert populated.count("Lien indisponible") == 2
    for path in (site / "public").rglob("*.html"):
        html = path.read_text()
        assert 'href="javascript:' not in html, path
        assert 'href="#contenu"' in html, path
    assert "Lien indisponible." in (site / "public/signets/missing/index.html").read_text()
    valid = (site / "public/signets/valid/index.html").read_text()
    assert 'href="https://example.org/?a=1&amp;b=2"' in valid
    category = (site / "public/category/design/index.html").read_text()
    assert '<h2 class="fiche-titre' in category
    tags = (site / "public/tags/index.html").read_text()
    assert "developpement" in tags and "Développement" not in tags

print("Hardening checks passed.")
