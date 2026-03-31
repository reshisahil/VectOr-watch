from trust_score import calculate_trust_score
from explain import generate_explanation

def core_engine(arif_output, saffwan_output):

    hard_penalty = arif_output["hard_penalty"]
    drift_penalty = arif_output["drift_penalty"]
    reasons = arif_output["reasons"]

    ml_penalty = saffwan_output["ml_penalty"]

    # calculate trust
    trust_score = calculate_trust_score(
        hard_penalty, drift_penalty, ml_penalty
    )

    # generate explanation
    result = generate_explanation(
        trust_score, reasons, ml_penalty
    )

    return result