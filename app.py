import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load Model
model = joblib.load("random_forest_model.pkl")

# Page Configuration
st.set_page_config(
    page_title="Healthcare Intelligence Platform",
    page_icon="🏥",
    layout="wide"
)

# Title
st.title("🏥 Healthcare Intelligence Platform")
st.subheader("Heart Disease Risk Prediction System")

st.markdown("---")

# Input Section
col1, col2 = st.columns(2)

with col1:

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=45
    )

    gender = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )

    sex = 0 if gender == "Female" else 1

    cp_option = st.selectbox(
        "Chest Pain Type",
        [
            "Typical Angina",
            "Atypical Angina",
            "Non-Anginal Pain",
            "Asymptomatic"
        ]
    )

    cp_mapping = {
        "Typical Angina": 0,
        "Atypical Angina": 1,
        "Non-Anginal Pain": 2,
        "Asymptomatic": 3
    }

    cp = cp_mapping[cp_option]

    trestbps = st.number_input(
        "Resting Blood Pressure (mm Hg)",
        min_value=80,
        max_value=250,
        value=120
    )

    chol = st.number_input(
        "Serum Cholesterol (mg/dl)",
        min_value=100,
        max_value=700,
        value=200
    )

    fbs_option = st.selectbox(
        "Fasting Blood Sugar > 120 mg/dl",
        ["No", "Yes"]
    )

    fbs = 0 if fbs_option == "No" else 1

with col2:

    restecg_option = st.selectbox(
        "Resting ECG Result",
        [
            "Normal",
            "ST-T Wave Abnormality",
            "Left Ventricular Hypertrophy"
        ]
    )

    restecg_mapping = {
        "Normal": 0,
        "ST-T Wave Abnormality": 1,
        "Left Ventricular Hypertrophy": 2
    }

    restecg = restecg_mapping[restecg_option]

    thalach = st.number_input(
        "Maximum Heart Rate Achieved",
        min_value=60,
        max_value=250,
        value=150
    )

    exang_option = st.selectbox(
        "Exercise Induced Angina",
        ["No", "Yes"]
    )

    exang = 0 if exang_option == "No" else 1

    oldpeak = st.number_input(
        "ST Depression (Oldpeak)",
        min_value=0.0,
        max_value=10.0,
        value=1.0,
        step=0.1
    )

    slope_option = st.selectbox(
        "Slope of Peak Exercise ST Segment",
        [
            "Upsloping",
            "Flat",
            "Downsloping"
        ]
    )

    slope_mapping = {
        "Upsloping": 0,
        "Flat": 1,
        "Downsloping": 2
    }

    slope = slope_mapping[slope_option]

    ca = st.selectbox(
        "Number of Major Vessels",
        [0, 1, 2, 3, 4]
    )

    thal_option = st.selectbox(
        "Thalassemia",
        [
            "Unknown",
            "Normal",
            "Fixed Defect",
            "Reversible Defect"
        ]
    )

    thal_mapping = {
        "Unknown": 0,
        "Normal": 1,
        "Fixed Defect": 2,
        "Reversible Defect": 3
    }

    thal = thal_mapping[thal_option]

# Prediction Button
if st.button("🔍 Predict Heart Disease Risk"):

    input_data = np.array([[
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

    prediction = model.predict(input_data)

    try:
        probability = model.predict_proba(input_data)

        # Class 0 = Disease
        risk_score = probability[0][0] * 100

    except:
        probability = None
        risk_score = None

    st.markdown("---")

    # Class 0 = Disease
    if prediction[0] == 0:

        st.error("⚠️ High Risk of Heart Disease")

        if risk_score is not None:
            st.metric(
                "Heart Disease Risk",
                f"{risk_score:.2f}%"
            )

    else:

        st.success("✅ Low Risk of Heart Disease")

        if risk_score is not None:
            st.metric(
                "Heart Disease Risk",
                f"{risk_score:.2f}%"
            )

    # Debug Output
    st.write("Prediction Value:", prediction[0])

    if probability is not None:
        st.write("Probability:", probability)

    st.markdown("### Patient Information Summary")

    summary = pd.DataFrame({
        "Parameter": [
            "Age",
            "Gender",
            "Chest Pain Type",
            "Blood Pressure",
            "Cholesterol",
            "Heart Rate",
            "Exercise Angina",
            "Thalassemia"
        ],
        "Value": [
            age,
            gender,
            cp_option,
            trestbps,
            chol,
            thalach,
            exang_option,
            thal_option
        ]
    })

    st.dataframe(summary, use_container_width=True)

st.markdown("---")
st.caption(
    "Healthcare Intelligence Platform | Heart Disease Prediction using Random Forest"
)
