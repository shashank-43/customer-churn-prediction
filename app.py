# GENDER: 1 = Female, 0 = Male
# CHURN: 1 = Yes, 0 = No

import streamlit as st
import joblib
import numpy as np

# Load the trained model and scaler
scaler = joblib.load("scaler.pkl")
model = joblib.load("model.pkl")

# Application title
st.title("Customer Churn Prediction App")

st.divider()

st.write("Enter the customer details below and click the Predict button to get a churn prediction.")

st.divider()

# User inputs
age = st.number_input("Enter Age", min_value=10, max_value=100, value=30)

tenure = st.number_input("Enter Tenure", min_value=0, max_value=130, value=10)

monthly_charge = st.number_input("Enter Monthly Charge", min_value=30, max_value=150)

gender = st.selectbox("Select Gender", ["Male", "Female"])

st.divider()

# Prediction button
predict_button = st.button("Predict")

if predict_button:

    gender_selected = 1 if gender == "Female" else 0

    X = [age, gender_selected, tenure, monthly_charge]

    X_array = np.array(X).reshape(1, -1)

    X_scaled = scaler.transform(X_array)

    prediction = model.predict(X_scaled)[0]

    predicted = "Churn" if prediction == 1 else "Not Churn"

    st.success(f"Prediction: {predicted}")

else:
    st.info("Please enter the customer details and click the Predict button.")