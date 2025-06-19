import numpy as np
from sklearn.linear_model import LogisticRegression
from agents.hospital_agent import HospitalAgent
from sklearn.metrics import accuracy_score

def evaluate_federated_model(fed_coef, fed_intercept):
    model = LogisticRegression()
    model.coef_ = fed_coef
    model.intercept_ = fed_intercept
    model.classes_ = np.array([0, 1])
    X_test, y_test = HospitalAgent("test", 99).generate_data(99)
    y_pred = model.predict(X_test)
    return accuracy_score(y_test, y_pred)
