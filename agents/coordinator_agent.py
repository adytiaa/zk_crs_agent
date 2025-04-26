from crewai import Agent
from masumi_integration.masumi_client import submit_task

class CoordinatorAgent(Agent):
    def __init__(self):
        super().__init__(name="CoordinatorAgent")

    def handle_research_query(self, query):
        print(f"[Coordinator] Received query: {query}")
        
        task_payload = {
            "task_type": "statistical_analysis",
            "query": query
        }
        task_id = submit_task(task_payload)
        print(f"[Coordinator] Submitted task to Masumi. Task ID: {task_id}")

        return task_id
