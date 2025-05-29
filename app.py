import streamlit as st
import numpy as np
import pickle
import os

# App title
st.title("🐧 Penguin Sex Predictor")
st.write("Enter the penguin's physical characteristics to predict whether it's **MALE** or **FEMALE**.")

# Load the model safely
model_path = "pen_model.pkl"
if not os.path.exists(model_path):
    st.error("Model file not found. Please ensure 'pen_model.pkl' is in the same folder as this app.")
    st.stop()

try:
    with open(model_path, "rb") as f:
        model = pickle.load(f)
except Exception as e:
    st.error(f"Error loading the model: {e}")
    st.stop()

# Input fields
species = st.selectbox("Species", ["Adelie", "Gentoo", "Chinstrap"])
island = st.selectbox("Island", ["Biscoe", "Dream", "Torgersen"])
culmen_length = st.number_input("Culmen Length (mm)", min_value=30.0, max_value=60.0, step=0.1)
culmen_depth = st.number_input("Culmen Depth (mm)", min_value=13.0, max_value=21.0, step=0.1)
flipper_length = st.number_input("Flipper Length (mm)", min_value=170, max_value=240, step=1)
body_mass = st.number_input("Body Mass (g)", min_value=2500, max_value=6500, step=10)

# Encoding inputs
species_encoded = {"Adelie": 0, "Gentoo": 1, "Chinstrap": 2}[species]
island_encoded = {"Biscoe": 0, "Dream": 1, "Torgersen": 2}[island]

# Prediction
if st.button("Predict"):
    input_data = np.array([[species_encoded, island_encoded, culmen_length, culmen_depth, flipper_length, body_mass]])
    prediction = model.predict(input_data)[0]
    sex = "MALE" if prediction == 0 else "FEMALE"
    st.success(f"Predicted Sex: **{sex}**")
