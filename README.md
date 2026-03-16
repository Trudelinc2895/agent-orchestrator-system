# Agent Orchestrator System

Système d'agents IA modulaire, versionnable et réutilisable dans tous tes projets.

## Objectif

Ce dépôt fournit une base **stable à long terme** pour :

- orchestrer plusieurs agents spécialisés ;
- brancher ton IA maison sur un point d'entrée unique ;
- réutiliser la même stack d'agents dans plusieurs projets ;
- maintenir une gouvernance propre (versions, conventions, évolutions).

## Architecture

- `agents/core/` : orchestrateur + agents centraux.
- `agents/specialized/` : agents métiers (analytics, legal, marketing, secret).
- `agents/saas/` : agents orientés architecture SaaS.
- `agents/tools/` : agents opérationnels/outils.
- `architecture/` : schéma système global.
- `examples/` : point de départ utilisable partout.
- `docs/` : gouvernance, opérations, changelog.

## Arborescence

`README.md`
`agents/core/*.agent.md`
`agents/specialized/*.agent.md`
`agents/saas/*.agent.md`
`agents/tools/*.agent.md`
`architecture/schema-systeme.agent.md`
`examples/example-app.py`
`docs/AGENTS.md`
`docs/OPERATIONS.md`
`docs/CHANGELOG.md`

## Installation (VS Code / Copilot)

1. Clone ce dépôt.
2. Copie tous les fichiers `*.agent.md` depuis `agents/**` et `architecture/` dans ton dossier de prompts utilisateur VS Code.
3. Redémarre VS Code.
4. Vérifie que les agents apparaissent dans la liste des agents custom.

Chemin Windows courant :

`C:\Users\<ton-user>\AppData\Roaming\Code - Insiders\User\prompts`

## Utilisation rapide

Exemples d'invocation :

- `@Master Orchestrator Agent Lance un plan SaaS complet avec roadmap et priorités.`
- `@Unified Essential Agent Structure ce projet en MVP puis itérations.`
- `@Agent Secret Propose une stratégie sécurisée de rotation des secrets.`
- @agent

## Intégration avec ton IA maison

Approche recommandée :

1. Ton IA maison envoie une intention (`task`, `context`, `constraints`).
2. Le **Master Orchestrator** choisit le bon agent.
3. Résultat normalisé renvoyé (plan, actions, risques, next steps).

Tu peux utiliser `examples/example-app.py` comme socle pour ton routeur local.

## Durabilité long terme

- Convention de nommage stricte des agents.
- Documentation d'exploitation dans `docs/OPERATIONS.md`.
- Gouvernance et standards dans `docs/AGENTS.md`.
- Versionnement via changelog (`docs/CHANGELOG.md`).

## Licence

Usage personnel et privé (modifiable selon ton besoin).
