# streamlit run app.py

import streamlit as st
import util

# Load model and artifacts
util.load_saved_artifacts()

# Web App Title
st.set_page_config(page_title="Bangalore Home Price Predictor", layout="centered")
st.title("🏠 Bangalore Home Price Prediction App")

# Sidebar Inputs
st.sidebar.header("Input Features")

locations = util.get_location_names()
selected_location = st.sidebar.selectbox("Select Location", locations)
sqft = st.sidebar.number_input("Total Square Feet", min_value=100.0, step=50.0)
bath = st.sidebar.slider("Number of Bathrooms", 1, 10, 2)
bhk = st.sidebar.slider("Number of BHK", 1, 10, 2)

# Predict Button
if st.sidebar.button("Predict Price"):
    predicted_price = util.get_estimated_price(selected_location, sqft, bhk, bath)
    st.success(f"🏡 Estimated Price: ₹ {predicted_price:,.2f} Lakhs")

# Footer
st.markdown("---")
st.markdown("Developed by [Aman] 💻")
