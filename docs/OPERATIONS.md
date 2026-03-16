# OPERATIONS (Long terme)

## Objectif

Assurer un fonctionnement stable et durable du système d'agents à travers tous tes projets.

## Stratégie de déploiement multi-projets

### Option A (recommandée) : dépôt source unique

1. Ce dépôt reste la source de vérité.
2. Chaque projet consomme les fichiers `*.agent.md` via copie contrôlée.
3. Mise à jour par version (tag/release interne).

### Option B : sous-module Git

- Ajouter ce dépôt comme sous-module dans chaque projet.
- Permet de pinner une version stable par projet.

## Politique de version

- Patch: correction de texte, bug mineur d'instruction.
- Minor: ajout d'un agent ou capacité rétrocompatible.
- Major: changement de comportement pouvant casser un workflow existant.

## Procédure de release

1. Mettre à jour `CHANGELOG.md`.
2. Vérifier les agents (frontmatter + sections minimales).
3. Tagger la version (`vX.Y.Z`).
4. Diffuser la version dans les projets consommateurs.

## Observabilité opérationnelle

- Tenir un journal des incidents (instruction ambiguë, mauvais routage).
- Documenter cause racine + correction.
- Ajouter des exemples de prompts validés.

## Bonnes pratiques IA maison

- Utiliser le Master Orchestrator comme seule porte d'entrée.
- Normaliser les entrées/sorties :
  - Entrée : `objectif`, `contexte`, `contraintes`.
  - Sortie : `plan`, `actions`, `risques`, `prochaines étapes`.
- Garder un fallback vers `Unified Essential Agent` en cas d'échec de routage.
