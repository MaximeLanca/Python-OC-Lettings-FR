# Base de données

## Local

En développement local, sans `DATABASE_URL` défini, Django utilise SQLite via
le fichier `oc-lettings-site.sqlite3` à la racine du projet.

```bash
sqlite3 oc-lettings-site.sqlite3
.tables
pragma table_info(letting_letting);
.quit
```

## Production

En production, `DATABASE_URL` (parsé par `dj-database-url`) pointe vers une
base PostgreSQL.

## Migrations

```bash
python manage.py migrate
```

Chaque application possède ses propres migrations dans `<app>/migrations/`.
Notamment, `oc_lettings_site` et `letting`/`profiles` contiennent des
migrations de type "copy data", utilisées lors de la restructuration du
projet en applications séparées.

## Jeu de données

Le fichier `fixtures.json` à la racine contient des données de test
(profils, locations, adresses) chargeables via :

```bash
python manage.py loaddata fixtures.json
```
