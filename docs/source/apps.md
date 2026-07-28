# Applications

## `oc_lettings_site`

Application racine : page d'accueil, gestion des erreurs 404/500, et
configuration globale du projet (`settings.py`, `urls.py`).

```{eval-rst}
.. automodule:: oc_lettings_site.views
   :members:

.. automodule:: oc_lettings_site.models
   :members:
```

## `letting`

Gère les locations immobilières.

Modèles :

- **`Address`** : numéro, rue, ville, état (2 lettres), code postal, code
  pays ISO (3 lettres).
- **`Letting`** : titre de l'annonce, lié en `OneToOne` à une `Address`.

```{eval-rst}
.. automodule:: letting.models
   :members:

.. automodule:: letting.views
   :members:
```

## `profiles`

Étend le modèle `User` de Django avec un profil.

- **`Profile`** : lié en `OneToOne` à un `User`, avec un champ optionnel
  `favorite_city`.

```{eval-rst}
.. automodule:: profiles.models
   :members:

.. automodule:: profiles.views
   :members:
```

:::{note}
La génération automatique de la documentation ci-dessus dépend de
`sphinx.ext.autodoc` et nécessite que le projet Django puisse être importé au
moment du build (voir `docs/source/conf.py`). Si le build échoue à importer
Django, ces sections apparaissent vides mais le reste de la documentation
reste disponible.
:::
