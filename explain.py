def generate_explanation(trust_score, reasons, ml_penalty):
    if trust_score > 70:
        severity = "Low Risk"
    elif trust_score > 40:
        severity = "Medium Risk"
    else:
        severity = "High Risk"

    # AI-style explanation
    if ml_penalty > 10:
        reasons.append("AI detected hidden anomaly")

    explanation = " + ".join(reasons)

    return {
        "trust_score": trust_score,
        "severity": severity,
        "explanation": explanation
    }