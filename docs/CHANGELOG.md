# Changelog

## v1.2.0 - 2026-03-18

### Added
- 4 nouveaux agents spécialisés:
	- `agent-devops.agent.md`
	- `agent-billing-ops.agent.md`
	- `agent-customer-success.agent.md`
	- `agent-product-growth.agent.md`
- `docs/SYSTEM-GLOBAL-SUMMARY.md` (inventaire global, état d'avancement, readiness prod).
- `.github/workflows/validate-agents.yml` (validation CI des fichiers agents).

### Changed
- `agents/README.md` enrichi avec les nouveaux agents spécialisés.
- `README.md` mis à jour (architecture, arborescence, CI).
- `architecture/schema-systeme.agent.md` aligné avec la nouvelle couche Go-To-Market & Delivery.
- `agents/core/master-orchestrator.agent.md` mis à jour avec les nouveaux agents supervisés.
- `examples/example-app.py` amélioré pour router vers DevOps/Billing Ops/Customer Success.
- `.gitignore` renforcé pour mieux couvrir les secrets, artefacts cloud/terraform et credentials.

## v1.1.0 - 2026-03-16

### Added
- `AGENTS.md` (gouvernance et conventions).
- `OPERATIONS.md` (guide d'exploitation long terme).
- README complet orienté usage multi-projets.

### Changed
- `BOT.agent.md` remplacé par une version exploitable (plus de placeholder).
- `Mind.agent.md` remplacé par une version exploitable (plus de placeholder/commande parasite).

### Fixed
- Suppression des artefacts de fin de fichier dans `essential-tools.agent.md`.
- Suppression des artefacts de fin de fichier dans `saas-architecture.agent.md`.

## v1.0.0 - 2026-03-16

### Added
- Base initiale des agents (`*.agent.md`).
- `example-app.py` comme exemple de point de départ.
