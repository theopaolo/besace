"""Importe un export CSV Raindrop (et en option un export CSV Notion) en fiches signet.

Usage : python3 scripts/import_raindrop.py raindrop.csv [notion.csv]

Une fiche par URL dans content/signets/. Le dossier Raindrop donne la catégorie
(table DOSSIERS), sinon la première étiquette connue (table ETIQUETTES), sinon
"ressources". Le dossier est aussi gardé en étiquette. Les étiquettes Notion
s'ajoutent à celles de Raindrop pour une même URL, et les URL présentes
seulement dans Notion donnent une fiche minimale. L'extrait Raindrop devient
le premier paragraphe, la note personnelle le post-it, la couverture l'image.
Les fiches déjà présentes ne sont pas réécrites.
"""
import csv
import re
import sys
import unicodedata
from pathlib import Path
from urllib.error import URLError
from urllib.parse import urlparse

import fetch_images

SIGNETS = Path(__file__).resolve().parents[1] / "content/signets"

DOSSIERS = {
    "Graphisme": "design", "Studios, ateliers, agences": "design", "Artist": "design",
    "Photography": "design", "Art cntmpr": "design", "Coloque": "design", "Articles": "design",
    "AspireInspire": "design",
    "Web": "developpement", "Web-toys": "developpement", "micro-SaaS": "developpement",
    "micro-tool": "developpement", "appRessource": "developpement", "creative coding": "developpement",
    "Web publication": "developpement", "Technology": "developpement",
    "Logiciel Convivial": "societe", "Numérique de controle": "societe", "Cooperer": "societe",
    "Ecologie anthropocene": "societe",
    "SoundUI": "son", "📻 RadioWebsite": "son",
    "Game related": "jeu",
}
# ponytail: pour les dossiers fourre-tout (all, Bookmarks, Unsorted), la première
# étiquette connue tranche. À affiner à la main sur les fiches mal classées.
ETIQUETTES = {
    "design": "design", "graphiste": "design", "studio": "design", "portfolio": "design",
    "site-inspiration": "design", "typo": "design", "typographie": "design", "art": "design",
    "photography": "design", "inspiration": "design",
    "webtool": "developpement", "coding": "developpement", "tool": "developpement",
    "library": "developpement", "framework": "developpement", "javascript": "developpement",
    "ecoweb": "developpement", "tech": "developpement", "ai": "developpement", "a11y": "developpement",
    "audio": "son", "radio": "son", "webradio": "son", "music": "son", "instrument": "son", "podcast": "son",
    "game": "jeu", "playdate": "jeu", "game-theory": "jeu", "gamedev": "jeu",
    "coop": "societe", "smallweb": "societe", "eco": "societe",
}
FOURRE_TOUT = {"all", "Bookmarks", "Unsorted", ""}


def slugify(text):
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def etiquettes(texte):
    """"siteInspiration, Note app;AI" -> ["site-inspiration", "note-app", "ai"]"""
    return [slugify(re.sub(r"(?<=[a-z])(?=[A-Z])", "-", t)) for t in re.split(r"[,;]", texte) if t.strip()]


def propre(text):
    """Raindrop laisse passer des caractères de contrôle, que YAML refuse."""
    return re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]", "", text).strip()


def court(texte, n=280):
    """Coupe l'extrait à la dernière fin de phrase avant n caractères, sinon au dernier mot."""
    if len(texte) <= n:
        return texte
    m = re.match(r"(.{0,%d}[.!?])(?=\s|$)" % (n - 1), texte)
    return m.group(1) if m else texte[:n].rsplit(" ", 1)[0] + "…"


def titre(s):
    return re.split(r"\s+\|\s*", s["title"])[0].strip() or urlparse(s["url"]).netloc.removeprefix("www.")


def yaml_str(text):
    return '"' + text.replace("\\", "\\\\").replace('"', '\\"') + '"'


def cle(url):
    return url.strip().rstrip("/")


def lire(raindrop, notion):
    signets = {}
    for x in csv.DictReader(open(raindrop, encoding="utf-8-sig")):
        signets[cle(x["url"])] = {
            "title": propre(x["title"]), "url": x["url"].strip(), "folder": x["folder"],
            "tags": etiquettes(x["tags"]), "excerpt": court(" ".join(propre(x["excerpt"]).split())),
            "note": propre(x["note"]), "cover": x["cover"].strip(), "date": x["created"][:10],
        }
    if notion:
        for x in csv.DictReader(open(notion, encoding="utf-8-sig")):
            if not x["URL"].startswith("http"):
                continue
            s = signets.setdefault(cle(x["URL"]), {
                "title": propre(x["Name"]), "url": x["URL"].strip(), "folder": "", "tags": [],
                "excerpt": "", "note": "", "cover": "", "date": "",
            })
            s["tags"] += [t for t in etiquettes(x["tags"]) if t not in s["tags"]]
    return signets.values()


def categorie(s):
    if s["folder"] in DOSSIERS:
        return DOSSIERS[s["folder"]]
    return next((ETIQUETTES[t] for t in s["tags"] if t in ETIQUETTES), "ressources")


def image(slug, url):
    deja = next(fetch_images.IMAGES.glob(f"{slug}.*"), None)
    if deja:
        return f"/images/{deja.name}"
    try:
        _, data = fetch_images.get(url, 5_000_000)
    except (URLError, TimeoutError, ValueError, OSError) as e:
        print(f"  couverture ignorée : {e}")
        return ""
    ext = fetch_images.extension(data)
    if not ext:
        return ""
    fetch_images.IMAGES.mkdir(exist_ok=True)
    chemin = fetch_images.IMAGES / f"{slug}.{ext}"
    chemin.write_bytes(data)
    fetch_images.reduire(chemin)
    return f"/images/{slug}.{ext}"


def to_markdown(s, slug):
    tags = s["tags"] + ([slugify(s["folder"])] if s["folder"] not in FOURRE_TOUT else [])
    corps = "\n\n".join(p for p in (s["excerpt"], s["note"]) if p)
    img = image(slug, s["cover"]) if s["cover"] else ""
    return (
        "---\n"
        f"title: {yaml_str(titre(s))}\n"
        + (f"date: {s['date']}\n" if s["date"] else "")
        + "extra:\n"
        + (f"  image: {yaml_str(img)}\n" if img else "")
        + f"  url: {yaml_str(s['url'])}\n"
        "taxonomies:\n"
        f"  category: [{categorie(s)}]\n"
        f"  tags: [{', '.join(dict.fromkeys(tags))}]\n"
        "---\n\n"
        f"{corps}\n"
    )


def main(raindrop, notion=None):
    written = skipped = 0
    pris = {"index", *(p.stem for p in SIGNETS.glob("*.md"))}  # index.md est réservé par Zola
    urls = {cle(m[1]) for p in SIGNETS.glob("*.md") if (m := re.search(r'^  url: "(.*?)"$', p.read_text(), re.M))}
    for s in lire(raindrop, notion):
        if cle(s["url"]) in urls:  # déjà importé lors d'une passe précédente
            skipped += 1
            continue
        domaine = urlparse(s["url"]).netloc.removeprefix("www.")
        slug = slugify(titre(s)) or slugify(domaine)  # titre sans caractère latin
        if slug in pris:  # titres génériques (home, about) : le domaine départage
            slug = slugify(f"{domaine} {slug}")
        if slug in pris:
            skipped += 1
            print(f"existe déjà, ignoré : {slug}")
            continue
        pris.add(slug)
        (SIGNETS / f"{slug}.md").write_text(to_markdown(s, slug))
        written += 1
    print(f"{written} fiches écrites, {skipped} ignorées")


if __name__ == "__main__":
    if len(sys.argv) not in (2, 3):
        sys.exit(__doc__)
    main(*sys.argv[1:])
