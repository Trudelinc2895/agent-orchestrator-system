"""Point de départ universel pour piloter ton système d'agents.

Usage :
    python example-app.py "Créer une roadmap SaaS avec priorités"
"""

from dataclasses import dataclass
import sys


@dataclass
class AgentDecision:
    agent: str
    reason: str


def route_intent(intent: str) -> AgentDecision:
    text = intent.lower()

    if any(
        k in text
        for k in [
            "deploy",
            "ci/cd",
            "production",
            "incident",
            "observabilité",
        ]
    ):
        return AgentDecision(
            "@Agent DevOps",
            "Demande liée à la production, au déploiement ou à la fiabilité.",
        )

    if any(
        k in text
        for k in [
            "abonnement",
            "billing",
            "facturation",
            "refund",
            "dunning",
        ]
    ):
        return AgentDecision(
            "@Agent Billing Ops",
            "Demande liée aux opérations de facturation et abonnements.",
        )

    if any(
        k in text
        for k in [
            "onboarding",
            "support",
            "rétention",
            "churn",
            "csat",
        ]
    ):
        return AgentDecision(
            "@Agent Customer Success",
            "Demande liée à l'adoption et à la réussite client.",
        )

    if any(
        k in text for k in ["secret", "token", "api key", "mot de passe"]
    ):
        return AgentDecision(
            "@Agent Secret",
            "Demande liée aux secrets/sécurité.",
        )

    if any(
        k in text for k in ["saas", "tenant", "architecture", "scalabilité"]
    ):
        return AgentDecision("@SaaS", "Demande liée à l'architecture SaaS.")

    if any(k in text for k in ["marketing", "acquisition", "conversion"]):
        return AgentDecision(
            "@Agent Marketing",
            "Demande marketing/monétisation.",
        )

    return AgentDecision(
        "@Master Orchestrator Agent",
        "Demande multi-domaine ou générale, routée vers l'orchestrateur.",
    )


def build_prompt(intent: str) -> str:
    decision = route_intent(intent)
    return (
        f"{decision.agent} {intent}\n\n"
        f"[Raison de routage: {decision.reason}]\n"
        "Réponds avec: Résumé, Plan d'action, Risques, Prochaine étape."
    )


def main() -> None:
    intent = " ".join(sys.argv[1:]).strip() or (
        "Planifie mon prochain sprint projet IA maison."
    )
    prompt = build_prompt(intent)

    print("=== Prompt prêt à coller dans Copilot ===")
    print(prompt)
    print(
        "\nAstuce: ce fichier peut être copié dans n'importe quel "
        "projet comme routeur local minimal."
    )


if __name__ == "__main__":
    main()
