#!/bin/bash
# auto_update_vault.sh — régénère la carte codebase et push vers GitHub
set -e

cd ~/monark-vault
python3 generate_codebase_map.py
git add .
git diff --cached --quiet || git commit -m "Auto-update codebase map $(date +%Y-%m-%d_%H:%M)"
git push origin main
