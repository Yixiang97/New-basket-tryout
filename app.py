from flask import Flask, render_template, request, jsonify
import json
import pandas as pd
import os
from datetime import datetime

app = Flask(__name__)

# === ROUTES ===

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/personnel")
def get_personnel():
    with open("data/personnel.json", "r") as file:
        personnel_data = json.load(file)
    return jsonify(personnel_data)

@app.route("/submit-leave", methods=["POST"])
def submit_leave():
    data = request.get_json()
    new_entry = {
        "Name": data["name"],
        "Start Date": data["start"],
        "End Date": data["end"],
        "Reason": data["reason"],
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    file_path = "data/leave_log.xlsx"

    # Load or create Excel
    if os.path.exists(file_path):
        df = pd.read_excel(file_path)
        df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
    else:
        df = pd.DataFrame([new_entry])

    df.to_excel(file_path, index=False)
    return jsonify({"message": "Leave submitted successfully!"})

if __name__ == "__main__":
    app.run(debug=True)

