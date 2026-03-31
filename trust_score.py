def calculate_trust_score(hard_penalty, drift_penalty, ml_penalty):
    # cap each penalty (important for fairness)
    hard_penalty = min(hard_penalty, 30)
    drift_penalty = min(drift_penalty, 30)
    ml_penalty = min(ml_penalty, 30)

    total_penalty = hard_penalty + drift_penalty + ml_penalty

    trust_score = max(0, 100 - total_penalty)

    return trust_score