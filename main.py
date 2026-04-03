from hard_rules import check_hard_rules
from drift import detect_drift
from ml_model import train_model, get_ml_penalty
from trust_score import calculate_trust_score
from explain import generate_explanation
import pandas as pd


# Train ML model once
data = pd.DataFrame([
    [100, 2],
    [105, 3],
    [98, 1]
])

model = train_model(data)


def full_pipeline(input_data):

    # 🔹 ARIF PART
    hard_penalty, hard_reasons = check_hard_rules(input_data)
    drift_penalty, drift_reason = detect_drift(input_data)

    reasons = hard_reasons
    if drift_penalty > 0:
        reasons.append(drift_reason)

    # 🔹 SAFFWAN PART (ML)
    record = [
        input_data["packets_per_min"],
        input_data["failed_connections"]
    ]

    ml_penalty = get_ml_penalty(model, record)

    # 🔹 YOUR PART
    trust_score = calculate_trust_score(
        hard_penalty, drift_penalty, ml_penalty
    )

    result = generate_explanation(
        trust_score, reasons, ml_penalty
    )

    return result