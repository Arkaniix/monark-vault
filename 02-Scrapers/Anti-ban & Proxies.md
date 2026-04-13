# Anti-ban & Proxies

## Stack scraping
- `curl_cffi` avec `impersonate="chrome131"` → bypass Datadome, 0 blocks
- Playwright **non nécessaire**

## Webshare
- Proxies résidentiels rotatifs : `proxies_fr.txt` (5 672 IPs FR), $3.50/GB
- Rotating endpoint couvre DE/ES/FR/IT/US
- Bandwidth actuel : ~4.1 GB/jour → cible 1.5 GB/jour (O1 sampling LBC + O2 session Vinted partagée)

## Anti-ban
- UA rotation, headers Sec-Fetch-*, délais 8–18s, refresh session toutes les 20–35 requêtes

## Abandonnés
- Idealo (Akamai Bot Manager), CDiscount (Baleen JS), Bright Data ($215, mauvais ROI)

## Diagnostics
- `DiagnosticCollector` dans `BaseScraper`
- Flags : FETCH_FAILED, ZERO_RESULTS, ZERO_MATCHED, LOW_MATCH_RATE, SOFT_BLOCK, RESULTS_NOT_MATCHED, MAINSTREAM_NOT_FOUND

## Liens
- [[Timers systemd]]
- [[Monitor Vinted]]
- [[Stack technique]]
