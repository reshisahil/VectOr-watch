def detect_drift(data):
    current = data["packets_per_min"]
    baseline = data["baseline"]

    # Safety check (important)
    if baseline == 0:
        return 0, "No baseline data"

    drift = ((current - baseline) / baseline) * 100

    if drift > 50:
        return 25, "High traffic spike"
    elif drift > 30:
        return 20, "Moderate drift"
    else:
        return 0, "Normal"