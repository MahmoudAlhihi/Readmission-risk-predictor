import streamlit as st
import requests

API_URL = "http://51.20.53.90:8000/predict"

st.set_page_config(page_title="Readmission Risk Predictor", page_icon="🏥")
st.title("Readmission Risk Predictor")
st.write("Enter patient details to predict the risk of readmission within 30 days.")
st.subheader("Patient Information")

number_inpatient = st.number_input("Number of Inpatient visits", min_value=0, value=2, step=1)
discharge_disposition_id = st.number_input("Discharge Disposition ID", min_value=0, value=1, step=1)
number_emergency = st.number_input("Number of emergency visits", min_value=0, value=0, step=1)
number_diagnoses = st.number_input("Number of diagnoses", min_value=0, value=8, step=1)

diabetesMed = st.selectbox("Diabetes Medication", options=["Yes", "No"])
insulin = st.selectbox("Insulin", options=["Yes", "No"])
diag1_group_circulatory = st.selectbox("Circulatory Diagnosis", options=["Yes", "No"])
payer_code_MC = st.selectbox("Payer Code MC", options=["Yes", "No"])
medical_specialty_InternalMedicine = st.selectbox("Internal Medicine Specialty", options=["Yes", "No"])

if st.button("Predict Readmission Risk"):
    payload = {
        "features": {
            "number_inpatient": number_inpatient,
            "discharge_disposition_id": discharge_disposition_id,
            "number_emergency": number_emergency,
            "number_diagnoses": number_diagnoses,
            "diabetesMed": 1 if diabetesMed == "Yes" else 0,
            "insulin": 1 if insulin == "Yes" else 0,
            "diag1_group_circulatory": 1 if diag1_group_circulatory == "Yes" else 0,
            "payer_code_MC": 1 if payer_code_MC == "Yes" else 0,
            "medical_specialty_InternalMedicine": 1 if medical_specialty_InternalMedicine == "Yes" else 0
        }
    }

    try :
        response = requests.post(API_URL, json=payload, timeout=10)
        response.raise_for_status()
        result = response.json()

        probability = result["readmission_probability"]
        prediction = result["prediction"]
        threshold = result["threshold"]

        st.subheader("Prediction Result")
        st.metric(label="Readmission Probability", value=f"{probability:.2f}")
        st.write(f"**Threshold:** {threshold:.2f}")

        if prediction == 1:
            st.error("High Risk of Readmission")
        else:
            st.success("Low Risk of Readmission")
    except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to the API: {e}")
    