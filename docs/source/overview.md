# Vue d'ensemble

**Python-OC-Lettings-FR** est le site web d'Orange County Lettings, une
application web Django qui présente :

- des **locations** (*lettings*) : une adresse et un titre d'annonce ;
- des **profils** utilisateurs : un compte Django `User` étendu avec une
  ville favorite.

## Stack technique

| Composant | Rôle |
|---|---|
| Django 5.2 | Framework web principal |
| SQLite (local) / PostgreSQL (production) | Base de données, via `dj-database-url` |
| Gunicorn | Serveur WSGI en production |
| WhiteNoise | Service des fichiers statiques en production |
| Sentry | Suivi des erreurs applicatives |
| Docker | Conteneurisation de l'application |
| GitHub Actions | Intégration et déploiement continus (CI/CD) |
| Render | Hébergement de l'application déployée |

## Applications Django du projet

Le projet est structuré en trois applications Django :

- `oc_lettings_site` : application racine (page d'accueil, pages d'erreur
  404/500, configuration globale) ;
- `letting` : gestion des locations (`Letting`, `Address`) ;
- `profiles` : gestion des profils utilisateurs (`Profile`).

Voir [Applications](apps.md) pour le détail de chaque application et
[Routes](urls.md) pour la liste des URLs exposées.
