from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load("titanic_model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(force=True)

    # Extract features from JSON
    pclass = int(data["Pclass"])
    sex = int(data["Sex"])
    age = float(data["Age"])
    sibsp = int(data["SibSp"])
    parch = int(data["Parch"])
    fare = float(data["Fare"])
    embarked = int(data["Embarked"])

    # Prepare input for prediction
    features = np.array([[pclass, sex, age, sibsp, parch, fare, embarked]])
    prediction = model.predict(features)[0]
    result = "Survived" if prediction == 1 else "Did Not Survive"

    # Return as JSON
    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(debug=True)
