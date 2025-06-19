import streamlit as st
import joblib

# Load trained model
model = joblib.load('home_price_model.pkl')

# UI
st.title("Home Price Prediction App")

# Input from user
sqft = st.number_input("Enter area in square feet:", min_value=100, step=50)

# Prediction
if st.button("Predict Price"):
    prediction = model.predict([[sqft]])
    st.success(f"Predicted Price: ₹ {prediction[0]:,.2f}")