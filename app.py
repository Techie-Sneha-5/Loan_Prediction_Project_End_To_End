from flask import Flask,request,jsonify
import joblib
import os
import numpy as np
app=Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "Notebooks", "model.pkl")
model = joblib.load(MODEL_PATH)

@app.route("/")
def home():
    return "Loan Prediction API Running"
@app.route('/predict',methods=['GET','POST'])
def predict():
    data=request.get_json()
    features=data['features']
    input_data=np.array(features).reshape(1,-1)
    prediction=model.predict(input_data)
    return jsonify({
        "prediction":int(prediction[0])
    })
if __name__=="__main__":
    app.run(debug=True)

