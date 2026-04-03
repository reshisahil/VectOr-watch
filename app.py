from flask import Flask, render_template, request
from main import full_pipeline

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        packets = int(request.form["packets"])
        failed = int(request.form["failed"])

        input_data = {
            "device_id": "cam_01",
            "packets_per_min": packets,
            "baseline": 100,
            "port_used": 443,
            "failed_connections": failed
        }

        result = full_pipeline(input_data)

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)