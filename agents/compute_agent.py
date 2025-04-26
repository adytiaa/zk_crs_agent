from crewai import Agent
from zk_circuits.proof_handler import generate_proof

class ComputeAgent(Agent):
    def __init__(self):
        super().__init__(name="ComputeAgent")

    def compute_and_prove(self, participant_data):
        print(f"[Compute] Processing data: {participant_data}")

        proof = generate_proof(participant_data)
        print(f"[Compute] Generated proof")

        return proof
