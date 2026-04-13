# Imports & conventions

## Chemins critiques
- `app.core.security` (PAS `app.core.auth`)
- `app.db.session` (PAS `app.core.database`)

## Hardware model matching
- **GPU** : suffixes TI SUPER/TI/SUPER/XTX/XT/GRE → strict match obligatoire
- **CPU** : suffixes X3D/KS/KF/K/G/F/X → strict match
- **RAM** : normalisation GB↔Go / TB↔To + suppression parenthèses pour sites FR
- **Motherboard** : fabricant + chipset_ref + distinction stricte B650 vs B650M
- **PSU** : fabricant + ref + wattage
- `hardware_models` a des doublons avec/sans préfixe fabricant et suffixes bruit type "(Navi 31)"

## Fichiers backend clés
- Estimator V3 : `schemas/estimator_v3.py`, `services/estimator_components.py`, `services/estimator_engine.py`
- Admin routers : `admin_cron.py`, `admin_observatory.py`, `admin_dashboard.py`, `admin_catalog.py`
- `listing_filters.py` v6 : patterns mobo/psu, 33/33 tests ; port JS pas mis à jour (API gère le filtrage)
- Crédits : déduction via `credit_logs` (pas `credits_balance`)

## Liens
- [[Base de données]]
- [[Stack technique]]
