# Estimator V3

Endpoint : `GET /v1/estimator/evaluate`

## Fichiers
- `schemas/estimator_v3.py`
- `services/estimator_components.py`
- `services/estimator_engine.py`

## Philosophie verdict
- Raisonne comme un **revendeur**, pas un consommateur
- Toujours négocier, jamais attendre
- LOWBALL remplace WAIT ; seuil AVOID <15 (pas <30)
- Verdicts action : Foncer / Tenter au culot / Passer
- Tier 1 data block inséré avant Tier 2/3

## Pricing
- Voir [[Base de données]] pour les règles composite_price / ebay_active

## Liens
- [[Base de données]]
- [[Monark Lens]]
- [[Imports & conventions]]
