# Base de données

## Couverture (mars 2026)
- 663 modèles, 6 catégories, ~46K+ observations dans `price_observations`
- 277/354 modèles originaux avec data eBay
- 203 modèles mobo + 149 PSU ajoutés

## Tables clés
- `component_market_stats` : `composite_price`, `lbc_median_price`, `lbc_sold_count`, `price_confidence`
- `hardware_models` : colonne `metadata` JSONB (GIN index) — socket/chipset/form_factor (mobo), wattage/certification/modular (PSU)
- `hardware_models` utilise `category_id` FK → toujours JOIN `hardware_categories`, jamais `WHERE category =`
- `listing_monitor` : colonne `current_price` (pas `price`)
- `user_inventory` : 24 cols, 7 indexes, 7 CHECK, 3 GENERATED (`profit_eur`, `profit_net_eur`, `hold_days`)
- `user_custom_transactions` : dépenses/revenus standalone
- `analysis_cache` (48h TTL, partagé par `ad_hash`) + `analysis_deep_cache` (perso, `ad_hash+user_id+level`)

## Règles pricing
- `ebay_active` **toujours exclu** des stats (prix demandés, pas transactions — gonfle médianes +40–65%)
- Source `ebay_active` en DB = `ebay_active` ; LBC monitor = `leboncoin` ; `source = 'lbc'` est **faux**
- Biais structurel résiduel +15–25% incompressible
- `composite_price` = LBC sold ×1.0 + eBay sold ×0.85 poids 0.8 ; ratio composite/median = 0.851 sur 328 modèles
- LBC sold proxy = `listing_monitor` annonces disparues (<30j listing age, <90j data age)
- `by_source` retourne toujours un dict `{source_name: count}`, jamais une liste

## Liens
- [[Stack technique]]
- [[Imports & conventions]]
- [[Estimator V3]]
