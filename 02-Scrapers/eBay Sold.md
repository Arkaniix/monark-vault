# eBay Sold

Scrape des résultats eBay "Sold" pour données de prix transactionnels.

## Points clés
- Pages de résultats suffisent — pas besoin de fetch les listings individuels
- `ebay_active` **toujours exclu** des stats (voir [[Base de données]])
- `total_price` inclut les frais de port → biais structurel
- Coefficient : eBay sold ×0.85, poids 0.8

## Liens
- [[Timers systemd]]
- [[Base de données]]
- [[Anti-ban & Proxies]]
