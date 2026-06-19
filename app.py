import streamlit as st
import joblib
import pandas as pd
import numpy as np

# ---- Load model and scaler ----
model = joblib.load("GradientBoosting_model.joblib")  # best model
scaler = joblib.load("scaler.joblib")         # if you scaled X

# ---- App Title ----
st.title("Retail Store Sales Prediction")
st.write("Predict sales / footfall based on product features")

# ---- User Input ----
st.sidebar.header("Enter Features:")

# Example features: price, discount, ad_spend, competitor_price, stock_level
price = st.sidebar.number_input("Price", min_value=0.0, value=50.0)
discount = st.sidebar.number_input("Discount", min_value=0.0, value=5.0)
ad_spend = st.sidebar.number_input("Ad Spend", min_value=0.0, value=2000.0)
competitor_price = st.sidebar.number_input("Competitor Price", min_value=0.0, value=55.0)
stock_level = st.sidebar.number_input("Stock Level", min_value=0.0, value=100.0)
weather_index = st.sidebar.number_input("Weather Index", min_value=0.0, value=0.5)
customer_sentiment = st.sidebar.number_input("Customer Sentiment", min_value=0.0, value=0.7)
return_rate = st.sidebar.number_input("Return Rate", min_value=0.0, value=0.05)
promotion_intensity = st.sidebar.number_input("Promotion Intensity", min_value=0.0, value=0.3)
footfall = st.sidebar.number_input("Footfall", min_value=0.0, value=100.0)

# ---- Prepare input for prediction ----
input_df = pd.DataFrame({
    "price": [price],
    "discount": [discount],
    "ad_spend": [ad_spend],
    "competitor_price": [competitor_price],
    "stock_level": [stock_level],
    "weather_index": [weather_index],
    "customer_sentiment": [customer_sentiment],
    "return_rate": [return_rate],
    "promotion_intensity": [promotion_intensity],
    "footfall": [footfall]
})

# Scale features if scaler was used
input_scaled = scaler.transform(input_df)

# ---- Prediction ----
if st.button("Predict"):
    prediction = model.predict(input_scaled)
    st.success(f"Predicted Sales / Volume: {prediction[0]:.2f}")
