from flask import Flask, request, jsonify, render_template
import pandas as pd
import joblib
import os

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)

# مسیر مدل
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "model.pkl")

# بارگذاری مدل
model = joblib.load(MODEL_PATH)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    sample = pd.DataFrame([{
        "engine": float(data["engine"]),
        "cylandr": int(data["cylandr"]),
        "fuelcity": float(data["fuelcity"]),
        "fuelwy": float(data["fuelwy"]),
        "fuelcomb": float(data["fuelcomb"])
    }])

    prediction = model.predict(sample)

    return jsonify({
        "co2": round(float(prediction[0]), 2)
    })


if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )