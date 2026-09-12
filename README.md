# Glane

Glane est une bibliothèque collective de liens au format Markdown. Chaque signet comprend une URL, une catégorie, des étiquettes (tags) et une brève description de son utilité.

Le site est accessible à l'adresse : [glane.ludique.dev](https://glane.ludique.dev).

### Ajouter ou modifier un signet

Deux façons, au choix.

**Dans le navigateur** : ouvrez [app.pagescms.org](https://app.pagescms.org), connectez-vous avec GitHub, choisissez le dépôt `glane`. Le formulaire impose les champs et enregistre directement dans le dépôt. Le site se reconstruit tout seul en une minute.

**Dans un éditeur** (Obsidian, VS Code, autre) :

1. Vérifiez que l'URL n'existe pas déjà dans `content/signets/`.
2. Copiez `modeles/signet.md` dans `content/signets/` sous un nom comme `mon-outil.md`.
3. Remplissez les métadonnées et expliquez en une ou deux phrases pourquoi conserver ce lien.
4. Pour une image, déposez-la dans `content/images/` et insérez-la avec `![Description](/images/mon-outil.webp)`.
5. Poussez sur `main`.

L'index par catégorie et les pages de tags sont générés à partir des métadonnées, il n'y a rien d'autre à mettre à jour.

### Conventions

- Un signet par fichier, frontmatter YAML :

  ```yaml
  ---
  title: "Nom"
  extra:
    url: https://example.org/
  taxonomies:
    category: [developpement]
    tags: [markdown, site-statique]
  ---
  ```

- Nom de fichier en minuscules, sans accents, avec des tirets.
- Catégorie : `developpement`, `design` ou `ressources`. Pour en ajouter une, ajoutez-la aussi dans `.pages.yml`.
- Tags courts, en minuscules, sans accents.
- Lien vers une autre fiche : `[pagefind](@/signets/pagefind.md)`. Zola vérifie que la cible existe.

### Site

Le site est généré par [Zola](https://www.getzola.org/), un binaire sans dépendances. En local :

```sh
brew install zola
zola serve
```

Le déploiement sur GitHub Pages est fait par `.github/workflows/pages.yml` à chaque push sur `main`.
