# # Titanic Survival Prediction REST API

This project is part of my internship tasks.

## Description
A REST API that predicts Titanic survival using a Random Forest classifier.

## How to Run Locally
1. Install dependencies:
   pip install flask scikit-learn joblib numpy



2. Start the API:
python api_app.py

Copy-paste this command into another Command Prompt window:



curl -X POST http://127.0.0.1:5000/predict ^
-H "Content-Type: application/json" ^
-d "{\"Pclass\":3,\"Sex\":1,\"Age\":25,\"SibSp\":0,\"Parch\":0,\"Fare\":7.25,\"Embarked\":2}"

Press Enter

Output
{"prediction":"Did Not Survive"}
