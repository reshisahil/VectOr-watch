import pandas as pd
from hard_rules import check_hard_rules
from drift import detect_drift


def detection_engine(data):
    hard_penalty, hard_reasons = check_hard_rules(data)
    drift_penalty, drift_reason = detect_drift(data)

    reasons = list(hard_reasons)

    if drift_penalty > 0:
        reasons.append(drift_reason)

    return {
        "device_id": data["device_id"],
        "hard_penalty": hard_penalty,
        "drift_penalty": drift_penalty,
        "reasons": reasons
    }


# READ CSV
df = pd.read_csv("devices.csv")

print("\n=== IoT Device Security Analysis ===")

# LOOP THROUGH DEVICES
for _, row in df.iterrows():
    device = row.to_dict()

    result = detection_engine(device)

    total_penalty = result["hard_penalty"] + result["drift_penalty"]

    # Risk logic
    if total_penalty > 40:
        risk = "HIGH"
    elif total_penalty > 20:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    # OUTPUT (IMPORTANT LINE FIXED)
    print("\nDevice ID:", result["device_id"])
    print("Hard Penalty:", result["hard_penalty"])
    print("Drift Penalty:", result["drift_penalty"])
    print("Total Penalty:", total_penalty)
    print("Risk Level:", risk)
    print("Reasons:", result["reasons"])