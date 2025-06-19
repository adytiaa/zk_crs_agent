import numpy as np
import hashlib
import uuid

class AggregatorAgent:
    def __init__(self, agent_id="aggregator-001"):
        self.agent_id = agent_id

    def federated_average(self, model_params):
        coefs = np.mean([m[0] for m in model_params], axis=0)
        intercepts = np.mean([m[1] for m in model_params], axis=0)
        return coefs, intercepts

    def hash_model(self, coef):
        return hashlib.sha256(coef.tobytes()).hexdigest()

    def generate_log(self, model_hash, zkp_proofs):
        return {
            "agent_id": self.agent_id,
            "model_hash": model_hash,
            "zkp_proofs": zkp_proofs,
            "verification_status": "pending",
            "audit_id": str(uuid.uuid4())
        }
