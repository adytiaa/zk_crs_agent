from kodosumi import Agent, AgentContext, AgentConfig
from agents.hospital_agent import HospitalAgent
from agents.aggregator_agent import AggregatorAgent
from utils.model import evaluate_federated_model
import json


class ClinicalFLAgent(Agent):
    def __init__(self):
        super().__init__()

    async def on_run(self, ctx: AgentContext):
        hospitals = [HospitalAgent(hid, seed) for hid, seed in enumerate([1, 2, 3])]
        local_models, zkp_proofs = [], []

        for hospital in hospitals:
            coef, intercept = hospital.train_model()
            local_models.append((coef, intercept))
            zkp_proofs.append(hospital.generate_zkp(coef))

        aggregator = AggregatorAgent()
        fed_coef, fed_intercept = aggregator.federated_average(local_models)
        fed_model_hash = aggregator.hash_model(fed_coef)

        audit_log = aggregator.generate_log(fed_model_hash, zkp_proofs)
        accuracy = evaluate_federated_model(fed_coef, fed_intercept)

        ctx.logger.info("Federated model test accuracy: %.4f", accuracy)
        ctx.logger.info("Kodosumi-compatible audit log:\n%s", json.dumps(audit_log, indent=2))


if __name__ == "__main__":
    config = AgentConfig(id="clinical-fl-agent")
    agent = ClinicalFLAgent()
    agent.run(config)
