import streamlit as st
from skops.io import load
import pandas as pd

st.title("House Price Prediction App")

# load the model
model = load("model/model.skops")

# use input fields to get user input
area = st.number_input("Put Area of land")
bedrooms = st.number_input("Put number of bedrooms")
age = st.number_input("Put Age of house")

user_data= pd.DataFrame({
    'Area_sqft': [area],
    'Bedrooms': [bedrooms],
    'Age_years': [age]
})

# predict the price
if st.button("Predict Price"):
    if area == 0.00 or bedrooms == 0.00 or age == 0.00:
        st.write("Please fill in all fields.")
    else:
        prediction = model.predict(user_data)
        st.write(f"The predicted house price is {prediction[0]}")