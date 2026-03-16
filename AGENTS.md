# AGENTS Governance

Ce fichier définit les règles d'évolution du système d'agents.

## 1) Convention de nommage

- Format fichier : `kebab-case.agent.md`
- Le champ `name` doit être unique.
- Le champ `description` doit tenir en 1 phrase claire.

## 2) Contrat minimum d'un agent

Chaque agent doit contenir :

1. Frontmatter YAML valide (`name`, `description`).
2. Section `Rôle`.
3. Section `Quand utiliser`.
4. Section `Limites / Sécurité`.
5. Section `Sortie attendue` (format de réponse).

## 3) Règles de sécurité

- Jamais de secrets en clair dans les fichiers.
- Toujours demander autorisation explicite avant action sensible.
- Préférer variables d'environnement ou coffre-fort.

## 4) Règles de stabilité

- Toute modification d'agent impactant le comportement doit être notée dans `CHANGELOG.md`.
- Éviter les changements cassants ; si nécessaire, documenter une migration.
- Garder des instructions simples, testables et non ambiguës.

## 5) Hiérarchie recommandée

- 1 orchestrateur principal.
- 1 agent polyvalent (fallback).
- N agents spécialisés par domaine.

## 6) Checklist PR/commit

- [ ] Frontmatter valide.
- [ ] Aucun placeholder restant.
- [ ] Aucun artefact (`</content>`, texte parasite, etc.).
- [ ] Description et usage cohérents.
- [ ] Changelog mis à jour.
