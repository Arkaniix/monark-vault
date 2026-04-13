# Monark Lens

Extension Chrome (Manifest V3, Shadow DOM, TypeScript/Vite) — v1.7.37+

## Détection variantes
- `findVariantName()` + système alias préfixé (5 241 alias, 203KB)
- Regex GPU toujours en safety net (override alias + non-GPU)
- `extractGpuModel` : 5 patterns dont fallback sans préfixe ("1080ti")
- `normalize()` : collapse suffixes GPU (ti/xtx/super) et préfixes (gtx/rtx/rx)
- 99% détection sur 2 119 titres réels

## Signal & cache
- Signal stocké au cache hit ; UPSERT sur `(ad_hash, user_id)` avec tracking `previous_price`
- Backend : `analysis_cache` (48h TTL, partagé par `ad_hash`) + `analysis_deep_cache` (perso, `ad_hash+user_id+level`)

## Leboncoin DOM fallback
- h1 pour titre, code postal→région via `normalizeRegionFromDept`
- URL path pour categoryId, `criteria_item_condition` pour "Pour pièces"
- `__NEXT_DATA__` ne contient plus les données annonce

## Liens
- [[Estimator V3]]
- [[Sui generis]]
- [[Anti-ban & Proxies]]
