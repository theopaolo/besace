# Glane

Glane est une bibliothèque collective de liens au format Markdown. Chaque signet comprend une URL, une catégorie, des étiquettes (tags) et une brève description de son utilité.

Le site est accessible à l’adresse : [glane.ludique.dev](https://glane.ludique.dev).

Pour explorer le contenu, ouvrez l’index.

---

### Lire et rechercher

- **Dans Obsidian** : ouvrez le dossier `contenu/` comme coffre existant.

- **Dans VS Code** : installez l’extension Foam, puis ouvrez le dossier `contenu/`.

- **Dans un autre éditeur** : ouvrez directement les fichiers `.md`. Les liens de l’index utilisent la syntaxe Markdown standard.

Utilisez la recherche d’Obsidian ou la recherche globale de VS Code pour retrouver un titre, une URL, un tag ou une phrase. Les liens sous la forme `[[nom-du-fichier]]` permettent de naviguer entre les notes dans Obsidian et Foam.

---

### Ajouter un signet

1. Vérifiez que l’URL n’existe pas déjà dans `contenu/signets/` pour éviter les doublons.

2. Copiez le modèle dans `contenu/signets/` sous un nom comme `mon-outil.md`.

3. Remplissez les métadonnées et expliquez en une ou deux phrases pourquoi conserver ce lien.

4. Ajoutez, si pertinent, un lien vers une autre fiche avec `[[nom-du-fichier]]`.

5. Intégrez la fiche à l’index, sous sa catégorie.

6. Pour une image facultative, déposez un fichier dans `contenu/images/`, puis insérez-le dans la fiche avec `![Description de l’aperçu](../images/mon-outil.webp)`.

---

### Conventions

- **Un signet par fichier** : le frontmatter YAML doit contenir `title`, `url`, `category`, `tags`.

- **Nom de fichier unique** : en minuscules, sans accents, avec des tirets.

- **Catégorie principale** : choisissez parmi _développement_, _design_ ou _ressources_. Si aucune ne convient, ajoutez-en une nouvelle à la liste et à l’index.

- **Tags** : courts, en minuscules et sans accents.

- **Liens** :
- Utilisez des wikilinks simples pour les fichiers internes : `[[eleventy]]`.

- Employez des liens Markdown classiques pour les URL externes et les images.
