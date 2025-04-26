from agents.coordinator_agent import CoordinatorAgent

if __name__ == "__main__":
    coordinator = CoordinatorAgent()
    query = "Is average improvement > 20%?"
    result = coordinator.handle_query(query)
    print(f"Final validated result: {result}")