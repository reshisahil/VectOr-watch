def check_hard_rules(data):
    penalty = 0
    reasons = []

    # Rule 1: Unauthorized Port
    if data["port_used"] not in [80, 443]:
        penalty += 20
        reasons.append("Unauthorized port")

    # Rule 2: Too Many Failed Connections
    if data["failed_connections"] > 10:
        penalty += 15
        reasons.append("Too many failed connections")

    return penalty, reasons