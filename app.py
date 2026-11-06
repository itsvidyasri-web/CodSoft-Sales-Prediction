import streamlit as st
import pickle
import pandas as pd

# Load trained model
with open("sales_model.pkl", "rb") as file:
    model = pickle.load(file)

# Website title
st.title("Sales Prediction Using Machine Learning")

st.write("Enter your advertising expenses to predict sales.")

# User inputs
tv = st.number_input("TV Advertising", min_value=0.0)
radio = st.number_input("Radio Advertising", min_value=0.0)
newspaper = st.number_input("Newspaper Advertising", min_value=0.0)

# Prediction button
if st.button("Predict Sales"):

    input_data = pd.DataFrame(
        [[tv, radio, newspaper]],
        columns=["TV", "Radio", "Newspaper"]
    )

    prediction = model.predict(input_data)

    st.success(f"Predicted Sales: {prediction[0]:.2f}")