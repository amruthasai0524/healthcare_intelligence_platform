import streamlit as st
import numpy as np
import joblib

model = joblib.load("random_forest_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("Heart Disease Prediction System")

age = st.number_input("Age", 20, 100)

sex = st.selectbox("Sex", [0,1])

cp = st.selectbox("Chest Pain Type", [0,1,2,3])

trestbps = st.number_input("Resting Blood Pressure")

chol = st.number_input("Cholesterol")

fbs = st.selectbox("Fasting Blood Sugar", [0,1])

restecg = st.selectbox("Rest ECG", [0,1,2])

thalach = st.number_input("Maximum Heart Rate")

exang = st.selectbox("Exercise Induced Angina", [0,1])

oldpeak = st.number_input("Old Peak")

slope = st.selectbox("Slope", [0,1,2])

ca = st.selectbox("Number of Vessels", [0,1,2,3,4])

thal = st.selectbox("Thal", [0,1,2,3])

if st.button("Predict"):

    patient_data = np.array([[

        age,
        sex,
        cp,
        trestbps,
        chol,
        fbs,
        restecg,
        thalach,
        exang,
        oldpeak,
        slope,
        ca,
        thal

    ]])

    patient_data = scaler.transform(patient_data)

    prediction = model.predict(patient_data)

    if prediction[0] == 1:

        st.error("High Risk of Heart Disease")

    else:

        st.success("Low Risk of Heart Disease")