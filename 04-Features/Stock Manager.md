# Stock Manager

✅ **DONE**

## Backend
- Table `user_inventory` : 24 cols, 7 indexes, 7 CHECK, 3 GENERATED (`profit_eur`, `profit_net_eur`, `hold_days`)
- `user_custom_transactions` pour dépenses/revenus standalone ; stat `real_profit_net` combine les deux
- 12 endpoints dans `routers/inventory.py` ; limites plan-gated
- Autocomplete via `GET /v1/models/autocomplete`

## Liens
- [[Base de données]]
- [[Imports & conventions]]
