#!/usr/bin/env python3
"""
generate_codebase_map.py
Scan ~/monark_api/app/, extract internal imports, generate Obsidian notes
in 08-Codebase/ with [[wikilinks]] for graph view.
Idempotent — chaque run écrase 08-Codebase/ entièrement.
"""

import os
import re
import shutil
from pathlib import Path
from collections import defaultdict

# ── Config ─────────────────────────────────────────────────────────────────
APP_DIR     = Path.home() / "monark_api" / "app"
VAULT_DIR   = Path.home() / "monark-vault"
OUTPUT_DIR  = VAULT_DIR / "08-Codebase"
DASHBOARD   = VAULT_DIR / "00-Dashboard.md"

SKIP_DIRS = {"__pycache__", "venv", ".git"}

CATEGORY_ORDER = [
    "routers", "services", "models", "schemas",
    "scrapers", "scripts", "core", "db",
]

# ── Helpers ─────────────────────────────────────────────────────────────────

def module_key(rel_path: Path) -> str:
    """app/routers/inventory.py  →  'app.routers.inventory'"""
    return "app." + ".".join(rel_path.with_suffix("").parts)


def note_name(module: str) -> str:
    """
    'app.routers.inventory'  →  'routers - inventory'
    'app.main'               →  'main'
    """
    parts = module.split(".")[1:]   # drop leading 'app'
    return " - ".join(parts) if len(parts) > 1 else parts[0]


def has_logic(path: Path) -> bool:
    """True if __init__.py contains any non-blank, non-comment line."""
    for line in path.read_text(errors="ignore").splitlines():
        stripped = line.strip()
        if stripped and not stripped.startswith("#"):
            return True
    return False


def extract_internal_imports(path: Path) -> set:
    """Return all app.* module references found in the file."""
    content = path.read_text(errors="ignore")
    found = set()
    for m in re.finditer(r"from\s+(app(?:\.\w+)+)\s+import", content):
        found.add(m.group(1))
    for m in re.finditer(r"^import\s+(app(?:\.\w+)+)", content, re.MULTILINE):
        found.add(m.group(1))
    return found


def collect_modules() -> dict:
    """Return {module_key: abs_path} for all relevant .py files."""
    modules = {}
    for root, dirs, files in os.walk(APP_DIR):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        root_path = Path(root)
        for fname in sorted(files):
            if not fname.endswith(".py"):
                continue
            fpath = root_path / fname
            if fname == "__init__.py" and not has_logic(fpath):
                continue
            key = module_key(fpath.relative_to(APP_DIR))
            modules[key] = fpath
    return modules

# ── Main ────────────────────────────────────────────────────────────────────

def main():
    modules = collect_modules()
    print(f"✓ {len(modules)} modules trouvés")

    # Build dependency graph
    imports_of  = {}
    imported_by = defaultdict(set)

    for key, path in modules.items():
        raw = extract_internal_imports(path)
        resolved = {ref for ref in raw if ref != key}
        imports_of[key] = resolved
        for dep in resolved:
            imported_by[dep].add(key)

    # Clear + recreate output dir
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True)

    # Generate one note per module
    for key, path in modules.items():
        nn         = note_name(key)
        rel_app    = path.relative_to(APP_DIR)
        rel_source = path.relative_to(Path.home() / "monark_api")

        # Imports section
        deps = sorted(imports_of.get(key, set()))
        if deps:
            import_lines = []
            for d in deps:
                if d in modules:
                    import_lines.append(f"- [[{note_name(d)}]]")
                else:
                    import_lines.append(f"- `{d}` *(package)*")
            imports_block = "\n".join(import_lines)
        else:
            imports_block = "*Aucun import interne*"

        # Imported-by section
        rev = sorted(r for r in imported_by.get(key, set()) if r in modules)
        rev_block = (
            "\n".join(f"- [[{note_name(r)}]]" for r in rev)
            if rev
            else "*Aucun module interne ne l'importe*"
        )

        content = f"""# {rel_app}

> Auto-généré par `generate_codebase_map.py`

## Imports internes
{imports_block}

## Importé par
{rev_block}

## Fichier source
`{rel_source}`
"""
        (OUTPUT_DIR / f"{nn}.md").write_text(content, encoding="utf-8")

    print(f"✓ {len(modules)} notes générées dans {OUTPUT_DIR}/")

    # Generate index
    cats = defaultdict(list)
    for key in sorted(modules):
        parts = key.split(".")
        cat = parts[1] if len(parts) >= 3 else "other"
        cats[cat].append(key)

    lines = [
        "# 📁 Index Codebase",
        "",
        "> Auto-généré — ne pas éditer manuellement",
        "",
    ]
    for cat in CATEGORY_ORDER:
        if cat not in cats:
            continue
        lines.append(f"## {cat.capitalize()}")
        for key in cats[cat]:
            lines.append(f"- [[{note_name(key)}]]")
        lines.append("")
    for cat, keys in sorted(cats.items()):
        if cat in CATEGORY_ORDER:
            continue
        lines.append(f"## {cat.capitalize()}")
        for key in keys:
            lines.append(f"- [[{note_name(key)}]]")
        lines.append("")

    (OUTPUT_DIR / "_Index Codebase.md").write_text("\n".join(lines), encoding="utf-8")
    print("✓ _Index Codebase.md généré")

    # Update 00-Dashboard.md (idempotent)
    dashboard = DASHBOARD.read_text(encoding="utf-8")
    if "### Codebase" not in dashboard:
        codebase_block = "\n### Codebase\n- [[_Index Codebase]]\n"
        # Insert before the first horizontal rule (end of nav section)
        dashboard = dashboard.replace("\n---\n", codebase_block + "\n---\n", 1)
        DASHBOARD.write_text(dashboard, encoding="utf-8")
        print("✓ 00-Dashboard.md mis à jour")
    else:
        print("  (Dashboard déjà à jour — section Codebase présente)")


if __name__ == "__main__":
    main()
