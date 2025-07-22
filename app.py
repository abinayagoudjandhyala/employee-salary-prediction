import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("salary_model.pkl")

st.set_page_config(page_title="Salary Prediction", layout="centered")
st.title("💼 Employee Salary Prediction")

st.markdown("Enter employee details below to predict their salary:")

# Input fields
gender = st.selectbox("Gender", options=["Male", "Female"])
dept_id = st.number_input("Department ID (1-20)", min_value=1, max_value=20, value=5)
perf_score = st.slider("Performance Score ID (1 = Needs Improvement, 4 = Exceeds)", 1, 4, 3)
satisfaction = st.slider("Employee Satisfaction (1-5)", 1, 5, 3)
projects = st.slider("Special Projects Count", 0, 10, 0)
absences = st.slider("Absences", 0, 30, 0)

# Convert gender to numeric
gender_id = 1 if gender == "Male" else 0

# Create input DataFrame
input_df = pd.DataFrame({
    "GenderID": [gender_id],
    "DeptID": [dept_id],
    "PerfScoreID": [perf_score],
    "EmpSatisfaction": [satisfaction],
    "SpecialProjectsCount": [projects],
    "Absences": [absences]
})

# Predict
if st.button("Predict Salary 💰"):
    prediction = model.predict(input_df)[0]
    st.success(f"Estimated Salary: **${prediction:,.2f}**")
