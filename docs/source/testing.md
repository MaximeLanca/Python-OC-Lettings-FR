# Tests

Le projet utilise `pytest` avec `pytest-django`, configuré dans `setup.cfg`
(`DJANGO_SETTINGS_MODULE = oc_lettings_site.settings`).

## Organisation

- `oc_lettings_site/tests.py` : tests des gestionnaires d'erreurs 404/500.
- `letting/tests/tests_unit.py`, `letting/tests/tests_integration.py` :
  tests unitaires (modèles) et d'intégration (vues, résolution d'URL) de
  l'application `letting`.
- `profiles/tests/tests_unit.py`, `profiles/tests/tests_integration.py` :
  équivalent pour l'application `profiles`.

## Lancer les tests

```bash
pytest
```

## Couverture de code

Le pipeline CI/CD exige une couverture minimale de **80 %** :

```bash
coverage run -m pytest
coverage report --fail-under=80
coverage html   # génère htmlcov/index.html
```

## Linting

```bash
flake8
```

Configuration : longueur de ligne maximale 99 caractères, dossiers
`migrations` et `venv` exclus (voir `setup.cfg`).
