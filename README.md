# VectOr-watch — IoT Behavioral Trust Analytics Platform

Intelligent. Adaptive. Explainable.
Real-time trust scoring for IoT devices that catches what rule-based systems miss.


# The Problem
   Traditional IoT security only catches obvious rule violations.  Modern attackers use low-and-slow attacks — gradually drifting a device's behavior over days or weeks, staying below every detection threshold while exfiltrating data the entire time. Existing systems see nothing wrong.

# What vector-watch Does
   Vector-watch continuously monitors IoT device network telemetry and assigns every device a dynamic Trust Score (0–100) using 4 detection layers running simultaneously:

   # Module What it does
   - 🔴 Hard Violation-- EngineInstantly flags  blacklisted IPs, unauthorized ports, threshold breaches
   - 🟠 Drift Detection-- EngineZ-score statistical analysis catches gradual behavioral drift over days
   - 🔵 ML Anomaly Module -- Isolation Forest model detects subtle multi-feature anomalies
   - 🟢 Trust Score Engine -- Combines all signals into a bounded 0–100 score with severity      classification

   Every score comes with a plain-language explanation — not just a number, but exactly why a device was flagged.

# Key Innovations

Explainability First - every decision is human-readable, for both analysts and non-technical stakeholders
Hybrid Detection — three independent layers mean no single point of failure
Anti-Poisoning Baseline Protection — baselines update only after human-gated confirmation, so attackers can't slowly train the system to accept malicious behavior
5 Severity Levels — Trusted / Low / Medium / High / Critical


🛠️ Tech Stack
- Layer Technologies Backend Python, FastAPI, PandasML EngineScikit-learn, Isolation Forest, Z-Score
- Statistics Frontend React.js, Recharts, Tailwind CSSDatabaseSQLite / PostgreSQL, Redis Deployment Docker, Edge-compatible

🏗️ Architecture
IoT Telemetry → Hard Violation Engine → Drift Detection → ML Anomaly Module → Trust Score Engine → Dashboard
Each module has a single responsibility — making the system modular, debuggable, and easy to extend.


# Install dependencies
pip install -r requirements.txt

# Run the backend
uvicorn main:app --reload

# Run the frontend
cd frontend && npm install && npm start

📊 Output Per Device (Every Cycle)

Trust Score (0–100)
Severity classification
Per-module penalty breakdown
Plain-language explanation of every risk signal


We don't just flag violations. We understand device behavior.

# DEVELOPERS~
TEAM CODEXX!!