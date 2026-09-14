# Glane

Glane est une bibliothèque collective de liens au format Markdown. Chaque signet comprend une URL, une catégorie, des étiquettes (tags) et une brève description de son utilité.

Le site est accessible à l'adresse : [glane.ludique.dev](https://glane.ludique.dev).

Une partie des signets provient de la [veille tech d'Anaïs Sparesotto](https://github.com/anais0210/veille-tech).

### Ajouter ou modifier un signet

Ouvrez \[app.pagescms.org\](https://app.pagescms.org) dans votre navigateur. Connectez-vous avec votre compte GitHub. Choisissez le dépôt \*glane\*.

Le formulaire indique les champs obligatoires. Vos modifications sont sauvegardées directement dans le dépôt, et le site est mis à jour en moins d’une minute.

**Dans un éditeur :**

1. Vérifiez que l’URL n’existe pas déjà dans `content/signets/`.
2. Copiez le fichier `modeles/signet.md` dans `content/signets/` et renommez-le, par exemple `mon-outil.md`.
3. Remplissez les métadonnées et ajoutez une ou deux phrases pour décrire l’utilité du lien. Ne répétez pas le titre ou l’URL, car le site les affiche déjà.
4. Envoyez vos modifications sur la branche `main`.

Les catégories et les pages de tags sont créées automatiquement à partir des métadonnées.

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
- Catégorie : `developpement`, `design` ou `ressources`, en premier. Ajoutez `francophone` en second si la ressource est en français : `category: [ressources, francophone]`. Pour créer une catégorie, ajoutez-la dans `config.toml` (`[extra.categories]`) et dans `.pages.yml`.
- Tags courts, en minuscules, sans accents.
- Lien vers une autre fiche : `[Pagefind](@/signets/pagefind.md)`, avec le nom lisible comme texte du lien. Zola vérifie que la cible existe.

### Site

Le site est généré par [Zola](https://www.getzola.org/).

- [Guide d'intallation](https://www.getzola.org/documentation/getting-started/installation/)

#### Commandes principales :

**Lance un server local**

```bash
zola start
```

**Build le suite**

```bash
zola build
```

Pour plus d’informations, se référer à la documentation de Zola.
