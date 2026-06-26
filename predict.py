import joblib
import os
import sys
import sklearn
import pandas as pd
print(sys.executable)
print(sklearn.__version__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "Notebooks", "model.pkl")

model = joblib.load(MODEL_PATH)

sample=pd.DataFrame({
    "Gender":[1],
    "Married":[0],
    "Dependents":[0],
    "Education":[0],
    "Self_Employed":[0],
    "ApplicantIncome":[6000],
    "CoapplicantIncome":[0],
    "LoanAmount":[141],
    "Loan_Amount_Term":[360],
    "Credit_History":[1],
    "Property_Area":[2]
})
prediction=model.predict(sample)
print(prediction)
