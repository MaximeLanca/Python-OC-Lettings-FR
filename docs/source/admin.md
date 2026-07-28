# Panel d'administration

Le panel d'administration Django est disponible sur `/admin/`.

Les modèles suivants y sont enregistrés :

- `letting.Letting`
- `letting.Address`
- `profiles.Profile`

L'enregistrement se fait simplement via `admin.site.register(...)` dans
`letting/admin.py` et `profiles/admin.py` (pas de classe `ModelAdmin`
personnalisée à ce jour).

## Créer un superutilisateur

```bash
python manage.py createsuperuser
```
