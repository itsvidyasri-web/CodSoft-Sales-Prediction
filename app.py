
import streamlit as st
import pickle
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Sales Prediction Dashboard",
    page_icon="📊",
    layout="wide"
)

# Load trained model
with open("sales_model.pkl", "rb") as file:
    model = pickle.load(file)

# Custom styling
st.markdown("""
<style>
.main {
    background-color: #f5f7fb;
}
h1 {
    color: #17365d;
}
div.stButton > button {
    background-color: #17365d;
    color: white;
    border-radius: 10px;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

# Dashboard heading
st.title("Sales Prediction Dashboard")
st.caption("Machine Learning Based Sales Forecasting")

st.divider()

# Sidebar
st.sidebar.header("Advertising Budget")
st.sidebar.write("Enter your advertising expenses.")

tv = st.sidebar.slider(
    "TV Advertising",
    0, 300, 150
)

radio = st.sidebar.slider(
    "Radio Advertising",
    0, 50, 25
)

newspaper = st.sidebar.slider(
    "Newspaper Advertising",
    0, 120, 30
)

# Main dashboard
st.subheader("Advertising Overview")

col1, col2, col3 = st.columns(3)

col1.metric("TV Budget", f"{tv}")
col2.metric("Radio Budget", f"{radio}")
col3.metric("Newspaper Budget", f"{newspaper}")

total_budget = tv + radio + newspaper

st.metric("Total Advertising Budget", f"{total_budget}")

st.divider()

# Prediction
st.subheader("Sales Forecast")

if st.button("Predict Sales"):

    input_data = pd.DataFrame(
        [[tv, radio, newspaper]],
        columns=["TV", "Radio", "Newspaper"]
    )

    prediction = model.predict(input_data)[0]

    st.success("Prediction completed successfully!")

    st.metric(
        "Predicted Sales",
        f"{prediction:.2f}"
    )

    st.subheader("Advertising Budget Breakdown")

    chart_data = pd.DataFrame({
        "Platform": ["TV", "Radio", "Newspaper"],
        "Budget": [tv, radio, newspaper]
    })

    st.bar_chart(
        chart_data,
        x="Platform",
        y="Budget"
    )

st.divider()

st.subheader("About This Project")

st.write("""
This application uses a Linear Regression Machine Learning model
to predict sales based on TV, Radio and Newspaper advertising expenses.

Developed as part of the CodSoft Data Science Internship.
""")
