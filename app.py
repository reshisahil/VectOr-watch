from flask import Flask, render_template, request
import pandas as pd
from ml_model import train_model, get_ml_penalty

app = Flask(__name__)

# Training data
data = pd.DataFrame([
    [100, 2],
    [105, 3],
    [98, 1]
])

model = train_model(data)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        packets = int(request.form["packets"])
        failed = int(request.form["failed"])

        record = [packets, failed]
        ml_penalty = get_ml_penalty(model, record)

        # logic
        if ml_penalty == 0:
            message = "Device behavior is normal"
            status = "Safe ✅"
            color = "green"
        elif ml_penalty <= 10:
            message = "Slight unusual activity detected"
            status = "Suspicious ⚠️"
            color = "orange"
        else:
            message = "High anomaly detected - possible threat"
            status = "Anomaly Detected 🚨"
            color = "red"

        result = {
            "ml_penalty": ml_penalty,
            "message": message,
            "status": status,
            "color": color,
            "packets": packets,
            "failed": failed
        }

    # 🔥 IMPORTANT: ALWAYS return result (even if None)
    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)