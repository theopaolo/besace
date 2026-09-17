# Besace

Besace est ma bibliothèque personnelle de liens au format Markdown, sur le même moteur que [Glane](https://github.com/theopaolo/glane). Les fiches viennent de Raindrop et de Notion, puis s'enrichissent à la main. Chaque signet comprend une URL, une catégorie, des étiquettes (tags) et une brève description de son utilité.

Le site est accessible à l'adresse : [besace.ludique.dev](https://besace.ludique.dev).

Une partie des signets provient de la [veille tech d'Anaïs Sparesotto](https://github.com/anais0210/veille-tech).

### Ajouter ou modifier un signet

Ouvrez \[app.pagescms.org\](https://app.pagescms.org) dans votre navigateur. Connectez-vous avec votre compte GitHub. Choisissez le dépôt *besace*.

Le formulaire indique les champs obligatoires. Vos modifications sont sauvegardées directement dans le dépôt, et le site est mis à jour en moins d’une minute.

**Dans un éditeur :**

1. Vérifiez que l’URL n’existe pas déjà dans `content/signets/`.
2. Copiez le fichier `modeles/signet.md` dans `content/signets/` et renommez-le, par exemple `mon-outil.md`.
3. Remplissez les métadonnées et ajoutez une ou deux phrases pour décrire l’utilité du lien. Ne répétez pas le titre ou l’URL, car le site les affiche déjà.
4. Envoyez vos modifications sur la branche `main`.

Les catégories et les pages de tags sont créées automatiquement à partir des métadonnées. Les grands dossiers de la vue d’accueil sont définis dans `config.toml` (`[[extra.dossiers]]`) par listes d’étiquettes et de catégories ; un signet sans correspondance va « En vrac ».

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
- Tags courts, en minuscules, sans accents. Pages CMS ne propose que les étiquettes listées dans `.pages.yml` : après en avoir créé une dans un éditeur, lancez `python3 scripts/pages_tags.py` pour mettre la liste à jour.
- `extra.dossiers: [slug]` place un signet dans un grand dossier en plus de ceux déduits de ses étiquettes (slugs dans `config.toml`).
- Lien vers une autre fiche : `[Pagefind](@/signets/pagefind.md)`, avec le nom lisible comme texte du lien. Zola vérifie que la cible existe.

### Porter le design vers Glane

Le design se fait ici d'abord. Glane le reprend avec la commande décrite dans son README (`git archive` depuis ce dépôt, sans les signets).

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
