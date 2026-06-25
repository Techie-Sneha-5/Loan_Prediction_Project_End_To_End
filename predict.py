import joblib
import sys
import sklearn
import pandas as pd
print(sys.executable)
print(sklearn.__version__)
model=joblib.load(r"C:\Users\Sneha\Desktop\Loan_Prediction_Project\Notebooks\model.pkl")
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
