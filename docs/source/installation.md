# Installation et développement local

## Prérequis

- Compte GitHub avec accès en lecture au dépôt
- Git
- Python 3.11 ou supérieur
- SQLite3 CLI (optionnel, pour inspecter la base locale)

## Cloner le dépôt

```bash
git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git
cd Python-OC-Lettings-FR
```

## Créer l'environnement virtuel

```bash
python -m venv venv
source venv/bin/activate       # macOS / Linux
# .\venv\Scripts\Activate.ps1  # Windows PowerShell
```

## Installer les dépendances

```bash
pip install -r requirements.txt
```

## Variables d'environnement

L'application lit sa configuration depuis l'environnement (via
`python-dotenv`, fichier `.env` à la racine) :

| Variable | Description |
|---|---|
| `SECRET_KEY` | Clé secrète Django, obligatoire |
| `ALLOWED_HOSTS` | Liste d'hôtes autorisés, séparés par des virgules |
| `DATABASE_URL` | URL de connexion à la base (PostgreSQL en production) ; si absente, une base SQLite locale (`oc-lettings-site.sqlite3`) est utilisée |
| `SENTRY_SDK` | DSN Sentry pour le suivi d'erreurs (optionnel) |

## Lancer le site

```bash
python manage.py runserver
```

Puis ouvrir [http://localhost:8000](http://localhost:8000). Le site doit
afficher plusieurs profils et locations.

## Linting

```bash
flake8
```

## Tests unitaires et d'intégration

```bash
pytest
```

Avec couverture de code (le pipeline CI exige au moins 80 % de couverture) :

```bash
coverage run -m pytest
coverage report --fail-under=80
```

## Panel d'administration

Aller sur [http://localhost:8000/admin](http://localhost:8000/admin) et se
connecter avec les identifiants de test fournis par le jeu de données
(`fixtures.json`).
