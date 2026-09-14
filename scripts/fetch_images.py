"""Récupère l'image OpenGraph de chaque signet pour décorer la grille.

Usage : python3 scripts/fetch_images.py [content/signets/un-signet.md ...]

Sans argument, traite toutes les fiches. Une fiche qui a déjà `extra.image`
est ignorée, on peut donc relancer le script après chaque ajout. L'image est
enregistrée dans content/images/<slug>.<ext> et son chemin écrit dans le
frontmatter. Les images moches se suppriment à la main, avec la ligne
`image:` de la fiche.
"""
import re
import shutil
import subprocess
import sys
from pathlib import Path
from urllib.error import URLError
from urllib.parse import quote, urljoin
from urllib.request import Request, urlopen

RACINE = Path(__file__).resolve().parents[1]
SIGNETS = RACINE / "content/signets"
IMAGES = RACINE / "content/images"
UA = "Mozilla/5.0 (compatible; besace/1.0; +https://besace.ludique.dev)"


def extension(data):
    """D'après les octets, le Content-Type ment parfois."""
    if data[:3] == b"\xff\xd8\xff":
        return "jpg"
    if data[:4] == b"\x89PNG":
        return "png"
    if data[:4] == b"RIFF" and data[8:12] == b"WEBP":
        return "webp"
    if data[:4] == b"GIF8":
        return "gif"
    return None

META = re.compile(
    r'<meta[^>]+(?:property|name)=["\'](?:og:image|twitter:image)(?::url)?["\'][^>]*?content=["\']([^"\']+)|'
    r'<meta[^>]+content=["\']([^"\']+)["\'][^>]*?(?:property|name)=["\'](?:og:image|twitter:image)(?::url)?["\']',
    re.I,
)


def get(url, limit):
    url = quote(url, safe=":/?&=#%+@")  # les URL avec accents
    with urlopen(Request(url, headers={"User-Agent": UA}), timeout=10) as r:
        return r.headers.get_content_type(), r.read(limit)


def image_de(url):
    ctype, html = get(url, 500_000)
    m = META.search(html.decode("utf-8", "replace"))
    if not m:
        return None
    src = urljoin(url, m.group(1) or m.group(2))
    _, data = get(src, 5_000_000)
    return extension(data), data


LARGEUR_MAX = 1200  # l'image la plus grande servie est l'og:image en 1200 px


def reduire(chemin):
    """Ramène l'image à 1200 px de large avec sips (macOS), sinon la laisse telle quelle."""
    if shutil.which("sips"):
        subprocess.run(["sips", "-Z", str(LARGEUR_MAX), str(chemin)], capture_output=True)


def traiter(fiche):
    texte = fiche.read_text()
    if re.search(r"^  image:", texte, re.M):
        return "déjà"
    m = re.search(r"^  url:\s*[\"']?(https?://[^\s\"']+)", texte, re.M)
    if not m:
        return "sans url"
    try:
        trouve = image_de(m.group(1))
    except (URLError, TimeoutError, ValueError, OSError) as e:
        return f"erreur : {e}"
    if not trouve:
        return "pas d'image"
    if not trouve[0]:
        return "format non géré"
    ext, data = trouve
    IMAGES.mkdir(exist_ok=True)
    chemin = IMAGES / f"{fiche.stem}.{ext}"
    chemin.write_bytes(data)
    reduire(chemin)
    fiche.write_text(re.sub(r"^extra:\n", f'extra:\n  image: "/images/{fiche.stem}.{ext}"\n', texte, count=1, flags=re.M))
    return f"ok ({len(data) // 1024} Ko)"


if __name__ == "__main__":
    fiches = [Path(p) for p in sys.argv[1:]] or sorted(SIGNETS.glob("*.md"))
    for fiche in fiches:
        if fiche.name == "_index.md":
            continue
        print(f"{fiche.stem}: {traiter(fiche)}")
