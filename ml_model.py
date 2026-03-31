from sklearn.ensemble import IsolationForest

def train_model(data):
    model = IsolationForest(contamination=0.1, random_state=42)
    model.fit(data)
    return model

def get_ml_penalty(model, record):
    score = model.decision_function([record])[0]

    if score < -0.2:
        return 20
    elif score < 0:
        return 10
    else:
        return 0