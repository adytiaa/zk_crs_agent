from crewai import Agent
from zk_circuits.proof_handler import verify_proof

class ValidationAgent(Agent):
    def __init__(self):
        super().__init__(name="ValidationAgent")

    def validate_proof(self, proof):
        print(f"[Validation] Verifying proof...")

        valid = verify_proof(proof)
        if valid:
            print(f"[Validation] Proof is valid ✅")
        else:
            print(f"[Validation] Proof is INVALID ❌")
        
        return valid
