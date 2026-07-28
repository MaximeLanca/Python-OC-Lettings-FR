# Déploiement

## Docker

Le `Dockerfile` construit une image basée sur `python:3.11-slim` :

1. Installation des dépendances via `uv` à partir de `requirements.txt`.
2. Copie du code source.
3. `python manage.py collectstatic --noinput`.
4. Au démarrage : `python manage.py migrate` puis lancement de Gunicorn sur
   le port `8000`.

```bash
docker build -t python-oc-lettings-fr .
docker run -p 8000:8000 --env-file .env python-oc-lettings-fr
```

## Intégration continue (CI)

Le workflow GitHub Actions `.github/workflows/ci-cd.yml` se déclenche sur
chaque `push`, quelle que soit la branche, et exécute le job `test` :

1. Installation de Python 3.11 et des dépendances (via `uv`).
2. Linting (`flake8`).
3. Tests avec couverture (`coverage run -m pytest`), échec si la couverture
   est inférieure à 80 %.

## Déploiement continu (CD)

Uniquement sur la branche `main`, après succès du job `test` :

1. **`build`** : connexion à Docker Hub et publication de l'image
   (`iguanna/python-oc-lettings-fr:latest` et `:<sha du commit>`).
2. **`deploy`** : déclenchement du déploiement sur **Render** via un
   webhook (`RENDER_DEPLOY_HOOK_URL`).

### Secrets GitHub Actions requis

| Secret | Usage |
|---|---|
| `SECRET_KEY` | Clé secrète Django pour les tests |
| `DOCKERHUB_USERNAME` / `DOCKERHUB_TOKEN` | Authentification Docker Hub |
| `RENDER_DEPLOY_HOOK_URL` | Webhook de déploiement Render |

## Suivi des erreurs (Sentry)

En production, définir la variable d'environnement `SENTRY_SDK` avec le DSN
du projet Sentry pour activer le suivi des erreurs et des traces de
performance (voir `config/sentry.py`).
