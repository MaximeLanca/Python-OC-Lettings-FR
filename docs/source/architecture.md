# Architecture

## Arborescence du projet

```text
Python-OC-Lettings-FR/
├── oc_lettings_site/   # Application racine : settings, urls, page d'accueil, erreurs 404/500
├── letting/            # Application "locations" : modèles Address et Letting
├── profiles/           # Application "profils" : modèle Profile (extension de User)
├── config/
│   └── sentry.py       # Initialisation du SDK Sentry
├── static/              # CSS, JS, images, fonts
├── docs/                # Documentation Sphinx (ce site)
├── manage.py
├── main.py
├── Dockerfile
├── requirements.txt
└── .github/workflows/ci-cd.yml
```

## Applications Django

Chaque application suit la structure standard Django : `models.py`,
`views.py`, `urls.py`, `admin.py`, `apps.py`, `migrations/`, `templates/`,
et un dossier `tests/`.

```{mermaid}
flowchart LR
    User[Navigateur] --> Root[oc_lettings_site.urls]
    Root -->|/| Index[oc_lettings_site.views.index]
    Root -->|/lettings/*| Letting[letting.urls]
    Root -->|/profiles/*| Profiles[profiles.urls]
    Root -->|/admin/*| Admin[django.contrib.admin]
    Letting --> LettingModel[(Letting / Address)]
    Profiles --> ProfileModel[(Profile → User)]
```

> Si le diagramme ci-dessus ne s'affiche pas, l'extension Mermaid n'est pas
> activée dans la configuration Sphinx ; le flux reste décrit textuellement
> dans [Routes](urls.md).

## Journalisation

Chaque application (`letting`, `profiles`, `oc_lettings_site`) possède son
propre logger, configuré dans `oc_lettings_site/settings.py` (niveau `INFO`,
sortie console). Les accès aux pages et les erreurs 404/500 sont journalisés.

## Suivi des erreurs

`config/sentry.py` initialise Sentry si la variable d'environnement
`SENTRY_SDK` (DSN) est définie. Le taux d'échantillonnage des traces est de
100 % (`traces_sample_rate=1.0`).
