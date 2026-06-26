import streamlit as st
import requests
st.title("Loan Prediction System")
st.write("Enter Applicant Details: ")
Gender=st.selectbox("Gender(0=Female,1=Male)",[0,1])
Married=st.selectbox("Married(0=No,1=Yes)",[0,1])
Dependents=st.selectbox("Dependents(0= 0 Dependents,1= 1 Dependent,2= 2 Dependents,3= 3+ Dependents)",[0,1,2,3])
Education=st.selectbox("Education(0=Graduate,1=Not Graduate)",[0,1])
Self_Employed=st.selectbox("Self_Employed(0=No,1=Yes)",[0,1])
ApplicantIncome=st.number_input("ApplicantIncome",step=1)
CoapplicantIncome=st.number_input("CoapplicantIncome",step=1)
LoanAmount=st.number_input("LoanAmount",step=1)
Loan_Amount_Term=st.number_input("Loan_Amount_Term",step=1)
Credit_History=st.selectbox("Credit_History(0=Bad,1=Good)",[0,1])
Property_Area=st.selectbox("Property_Area(0=Rural,1=Semiurban,2=Urban)",[0,1,2])




if st.button("Predict Loan Status"):
    features=[Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area]

    try:
        response=requests.post("https://loan-prediction-project-end-to-end.onrender.com/predict",json={"features":features},timeout=30)
        st.write("Status Code:",response.status_code)
        st.write("Response Text:",response.text)
        result=response.json()
        st.write("RAW RESPONSE: ",result)       
        
        if result["prediction"]==1:
            st.success("Loan Approved!!!")
        elif result["prediction"]==0:
            st.error("Loan Rejected")
        else:
            st.error("ERROR")

    except Exception as e:
        st.error(f"Error: {e}")    
        