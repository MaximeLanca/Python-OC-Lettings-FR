# Routes

## Routes racines

| URL | Vue | Description |
|---|---|---|
| `/` | `oc_lettings_site.views.index` | Page d'accueil |
| `/lettings/` | inclut `letting.urls` | Locations |
| `/profiles/` | inclut `profiles.urls` | Profils |
| `/admin/` | `django.contrib.admin` | Panel d'administration |

Gestionnaires d'erreurs personnalisés : `handler404` →
`oc_lettings_site.views.page_not_found`, `handler500` →
`oc_lettings_site.views.server_error`.

## `letting` (préfixe `/lettings/`)

| URL | Nom de la route | Vue |
|---|---|---|
| `/lettings/` | `letting:index` | Liste de toutes les locations |
| `/lettings/<letting_id>/` | `letting:letting` | Détail d'une location (404 si absente) |

## `profiles` (préfixe `/profiles/`)

| URL | Nom de la route | Vue |
|---|---|---|
| `/profiles/` | `profile:index` | Liste de tous les profils |
| `/profiles/<username>/` | `profile:profile` | Détail d'un profil (404 si absent) |
