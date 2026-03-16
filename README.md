# Agent Orchestrator System

Système d'agents IA modulaire, versionnable et réutilisable dans tous tes projets.

## Objectif

Ce dépôt fournit une base **stable à long terme** pour :

- orchestrer plusieurs agents spécialisés ;
- brancher ton IA maison sur un point d'entrée unique ;
- réutiliser la même stack d'agents dans plusieurs projets ;
- maintenir une gouvernance propre (versions, conventions, évolutions).

## Architecture

- `master-orchestrator.agent.md` : routeur principal et coordination multi-agents.
- `unified-essential.agent.md` : agent polyvalent (fallback opérationnel).
- Agents spécialisés : analytics, legal, marketing, secrets, SaaS, outils.
- `schema-systeme.agent.md` : vue conceptuelle globale.
- `example-app.py` : exemple concret de point de départ utilisable partout.

## Installation (VS Code / Copilot)

1. Clone ce dépôt.
2. Copie les fichiers `*.agent.md` dans ton dossier de prompts utilisateur VS Code.
3. Redémarre VS Code.
4. Vérifie que les agents apparaissent dans la liste des agents custom.

Chemin Windows courant :

`C:\Users\<ton-user>\AppData\Roaming\Code - Insiders\User\prompts`

## Utilisation rapide

Exemples d'invocation :

- `@Master Orchestrator Agent Lance un plan SaaS complet avec roadmap et priorités.`
- `@Unified Essential Agent Structure ce projet en MVP puis itérations.`
- `@Agent Secret Propose une stratégie sécurisée de rotation des secrets.`

## Intégration avec ton IA maison

Approche recommandée :

1. Ton IA maison envoie une intention (`task`, `context`, `constraints`).
2. Le **Master Orchestrator** choisit le bon agent.
3. Résultat normalisé renvoyé (plan, actions, risques, next steps).

Tu peux utiliser `example-app.py` comme socle pour ton routeur local.

## Durabilité long terme

- Convention de nommage stricte des agents.
- Documentation d'exploitation dans `OPERATIONS.md`.
- Gouvernance et standards dans `AGENTS.md`.
- Versionnement via changelog (`CHANGELOG.md`).

## Licence

Usage personnel et privé (modifiable selon ton besoin).
