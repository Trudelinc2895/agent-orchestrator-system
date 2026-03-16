# Exemple d'App Personnelle pour Contrôler le Système d'Agents

"""
Cette app simple démontre comment utiliser le système d'agents via des prompts.
Elle simule l'invocation du Master Orchestrator Agent pour des tâches complexes.

Dans VS Code avec Copilot, vous pouvez invoquer les agents directement :
- @Master Orchestrator Agent : Pour coordonner des tâches multi-domaines.
- @Agent Secret : Pour gérer des secrets sécurisés.
- @Unified Essential Agent : Pour des tâches polyvalentes.

Exemple d'utilisation :
1. Ouvrez une conversation Copilot.
2. Tapez : "@Master Orchestrator Agent Planifie un projet SaaS avec intégration Stripe."
3. L'agent analysera, priorisera, et assignera aux sous-agents appropriés.

Cette app peut être étendue pour intégrer des APIs ou des automatisations externes.
"""

def simulate_orchestrator_request(request):
    """
    Simule une requête au Master Orchestrator.
    En réalité, cela serait fait via Copilot ou une API.
    """
    print(f"Requête reçue : {request}")
    print("Analyse en cours...")
    print("Priorisation avec matrice Eisenhower...")
    print("Assignation aux agents : Agent SaaS, Agent Secret, Unified Essential")
    print("Exécution : Conception architecture, gestion secrets, automatisation.")
    print("Résultat : Projet planifié avec succès.")

if __name__ == "__main__":
    # Exemple d'utilisation
    request = "Créer une app SaaS avec paiement Stripe et analyse des données."
    simulate_orchestrator_request(request)

    print("\nPour une utilisation réelle, invoquez les agents dans Copilot.")
    print("Repo : https://github.com/Trudelinc2895/agent-orchestrator-system")