# Décisions techniques

Journal des décisions structurantes du projet.

## Principes
- Etienne délègue les décisions seuils/calculs à Claude, garde le contrôle sur la philosophie produit
- Diagnostic-first avec stops de validation avant implémentation
- Corrections domaine quand la logique Claude ne matche pas le comportement revendeur réel

## Décisions actées
- `ebay_active` exclu des stats définitivement
- LOWBALL remplace WAIT dans l'estimator
- LLM jamais dans l'API publique (coût tokens) — uniquement Deal Hunter perso
- `curl_cffi` > Playwright pour le scraping
- Pas de stockage données brutes annonces ([[Sui generis]])

## Liens
- [[Estimator V3]]
- [[Sui generis]]
- [[Base de données]]
