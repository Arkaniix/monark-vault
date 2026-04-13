# Repair Guide

Backend ✅ DONE — Frontend ⏳ pending

## Tables
- `repair_symptoms` (37 symptômes, GPU/CPU/RAM/SSD/mobo/PSU)
- `repair_guides` (JSONB)
- `repair_deep_cache` (unique sur `model_id+symptom_id+md5(context)`)
- `repair_history`

## Endpoints
- `GET /v1/repair/symptoms` — liste
- `GET /v1/repair/guide/{slug}` — gratuit
- `POST /v1/repair/deep-diagnostic` — 5cr, Claude Haiku 4.5, cache 30j
- `GET /v1/repair/history`
- `POST /v1/repair/history/{id}/outcome`

## Seed
- `scripts/seed_repair_guides.py` — 37/37 guides statiques générés

## Pending
- LLM endpoint Part 2
- Prompt Lovable frontend

## Liens
- [[Imports & conventions]]
- [[Lovable workflow]]
