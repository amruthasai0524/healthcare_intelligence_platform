# 🏥 Healthcare Intelligence Platform
### Heart Disease Prediction using Statistics, Machine Learning, Deep Learning, SQL, Power BI & Streamlit

---

## 📌 Project Overview

The Healthcare Intelligence Platform is an end-to-end healthcare analytics and disease prediction system developed to identify patients at risk of heart disease using clinical data.

This project combines:

- Data Analysis
- Statistical Testing
- SQL Database Integration
- Machine Learning
- Deep Learning
- Power BI Dashboarding
- Streamlit Deployment

to create a complete healthcare intelligence solution.

---

## 🎯 Business Objective

Heart disease is one of the leading causes of mortality worldwide. Early prediction can help healthcare professionals make informed decisions and improve patient outcomes.

The primary objectives of this project are:

- Analyze patient clinical records
- Identify key risk factors associated with heart disease
- Build predictive models for disease classification
- Create interactive dashboards for healthcare insights
- Deploy a real-time prediction application

---

# 📂 Project Structure

```text
Healthcare-Intelligence-Platform/
│
├── data/
│   └── heart_disease_data.csv
│
├── notebooks/
│   ├── 01_EDA.ipynb
│   ├── 02_Statistical_Analysis.ipynb
│   ├── 03_SQL_Integration.ipynb
│   ├── 04_Machine_Learning.ipynb
│   └── 05_Deep_Learning.ipynb
│
├── dashboard/
│   └── Heart_Disease_Dashboard.pbix
│
├── SQL/
│   └── healthcare_queries.sql
│
├── app.py
├── random_forest_model.pkl
├── scaler.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🛠️ Technology Stack

## Programming Language

- Python

## Data Analysis

- Pandas
- NumPy

## Data Visualization

- Matplotlib
- Seaborn

## Statistical Analysis

- T-Test
- Chi-Square Test
- ANOVA

## Database

- MySQL

## Machine Learning

- Logistic Regression
- Random Forest Classifier

## Deep Learning

- TensorFlow
- Keras
- Artificial Neural Networks (ANN)

## Dashboarding

- Power BI

## Deployment

- Streamlit

---

# 📊 Dataset Information

The dataset contains clinical attributes of patients used to predict heart disease occurrence.

### Features

| Feature | Description |
|----------|------------|
| age | Age of Patient |
| sex | Gender |
| cp | Chest Pain Type |
| trestbps | Resting Blood Pressure |
| chol | Cholesterol |
| fbs | Fasting Blood Sugar |
| restecg | Resting ECG Results |
| thalach | Maximum Heart Rate |
| exang | Exercise Induced Angina |
| oldpeak | ST Depression |
| slope | Slope of Peak Exercise ST Segment |
| ca | Number of Major Vessels |
| thal | Thalassemia |
| target | Heart Disease Presence |

---

# 🔍 Phase 1: Exploratory Data Analysis (EDA)

### Activities Performed

- Data Loading
- Data Cleaning
- Missing Value Analysis
- Duplicate Record Check
- Outlier Detection
- Feature Distribution Analysis
- Correlation Analysis

### Insights

- Heart disease occurrence varies significantly across chest pain categories.
- Cholesterol and age show notable variation among patients.
- Certain clinical variables exhibit stronger correlations with disease status.

---

# 📈 Phase 2: Statistical Analysis

Statistical hypothesis testing was conducted to validate relationships between clinical features and heart disease occurrence.

## 1️⃣ Independent T-Test

**Objective**

Compare cholesterol levels between patients with and without heart disease.

### Results

| Metric | Value |
|----------|----------|
| T Statistic | -2.1025 |
| P Value | 0.0359 |

### Conclusion

A statistically significant difference exists in cholesterol levels between the two groups.

---

## 2️⃣ Chi-Square Test

**Objective**

Determine whether gender is associated with heart disease occurrence.

### Results

| Metric | Value |
|----------|----------|
| Chi Square Statistic | 46.6239 |
| P Value | 8.60e-12 |

### Conclusion

Gender has a statistically significant association with heart disease occurrence.

---

## 3️⃣ ANOVA Test

**Objective**

Compare age distributions across chest pain categories.

### Results

| Metric | Value |
|----------|----------|
| F Statistic | 6.8134 |
| P Value | 0.00016 |

### Conclusion

At least one chest pain category differs significantly in average age.

---

# 🗄️ Phase 3: SQL Integration

MySQL was integrated to manage healthcare records and perform analytical queries.

### Implemented Operations

- Database Creation
- Table Creation
- Data Import
- Data Retrieval
- Aggregate Analysis
- Risk Factor Analysis

### Sample Queries

- Average Cholesterol by Disease Status
- Average Age by Gender
- Heart Disease Distribution
- Maximum Heart Rate Analysis

---

# 🤖 Phase 4: Machine Learning

Several machine learning models were developed and evaluated.

## Logistic Regression

### Accuracy

```text
84.43%
```

### Purpose

Baseline classification model for disease prediction.

---

## Random Forest Classifier

### Accuracy

```text
98.36%
```

### Purpose

Ensemble learning model for improved predictive performance.

### Top Features

| Feature | Importance |
|----------|----------|
| cp | 0.1346 |
| thal | 0.1205 |
| thalach | 0.1111 |
| ca | 0.1106 |
| oldpeak | 0.1100 |

---

# 🧠 Phase 5: Deep Learning

An Artificial Neural Network (ANN) was developed using TensorFlow and Keras.

### ANN Performance

```text
Accuracy: 91.80%
```

### Architecture

- Input Layer
- Hidden Layer 1 (ReLU)
- Hidden Layer 2 (ReLU)
- Output Layer (Sigmoid)

---

# 📊 Phase 6: Power BI Dashboard

An interactive Power BI dashboard was designed for healthcare analytics.

## Dashboard Pages

### Executive Summary

- Total Patients
- Average Age
- Average Cholesterol
- Disease Distribution

### Clinical Risk Analysis

- Cholesterol Analysis
- Blood Pressure Analysis
- Chest Pain Analysis
- Heart Rate Analysis

### Machine Learning Insights

- Model Accuracy Comparison
- Feature Importance Analysis

---

# 🚀 Phase 7: Streamlit Deployment

A web application was developed using Streamlit to provide real-time heart disease prediction.

### Features

- User-friendly interface
- Clinical data input
- Real-time prediction
- Instant risk assessment

### Run Application

```bash
streamlit run app.py
```

---

# 📋 Model Performance Comparison

| Model | Accuracy |
|---------|---------|
| Logistic Regression | 84.43% |
| ANN | 91.80% |
| Random Forest | 98.36% |

### Best Performing Model

🏆 Random Forest Classifier

---

# 🎯 Key Achievements

✅ Performed comprehensive healthcare data analysis

✅ Conducted statistical hypothesis testing

✅ Integrated MySQL database operations

✅ Developed Machine Learning models

✅ Implemented Deep Learning using ANN

✅ Built interactive Power BI dashboards

✅ Deployed a real-time Streamlit application

✅ Achieved 98.36% prediction accuracy

---

# 🔮 Future Enhancements

- Integration with Electronic Health Records (EHR)
- Cloud Deployment (AWS/Azure)
- Explainable AI (SHAP)
- Advanced Deep Learning Architectures
- Real-Time Data Streaming

---

# 👩‍💻 Author

### Amrutha Reddy

**Aspiring Data Scientist | Healthcare Analytics Enthusiast | Machine Learning Practitioner**

GitHub: https://github.com/amruthasai0524

---
