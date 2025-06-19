import numpy as np
from sklearn.linear_model import LogisticRegression
import hashlib
import uuid

class HospitalAgent:
    def __init__(self, hospital_id, seed):
        self.hospital_id = hospital_id
        self.X, self.y = self.generate_data(seed)

    def generate_data(self, seed):
        np.random.seed(seed)
        X = np.random.randn(100, 10)
        y = (np.sum(X[:, :3], axis=1) + np.random.randn(100)) > 0
        return X, y.astype(int)

    def train_model(self):
        model = LogisticRegression()
        model.fit(self.X, self.y)
        return model.coef_, model.intercept_

    def generate_zkp(self, coef):
        return {
            "hospital_id": self.hospital_id,
            "proof": hashlib.sha256(coef.tobytes()).hexdigest(),
            "timestamp": str(uuid.uuid4())
        }
