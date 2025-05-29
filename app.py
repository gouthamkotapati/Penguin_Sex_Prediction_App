import streamlit as st
import pickle
import numpy as np

with open("pen_model.pkl", "rb") as file:
    tree = pickle.load(file)

st.title("🐧 Penguin Sex Predictor")
st.write("Enter the penguin's physical characteristics to predict whether it's **MALE** or **FEMALE**.")

species = st.selectbox("Species", ["Adelie", "Gentoo", "Chinstrap"])
island = st.selectbox("Island", ["Biscoe", "Dream", "Torgersen"])
culmen_length = st.number_input("Culmen Length (mm)", min_value=30.0, max_value=60.0, step=0.1)
culmen_depth = st.number_input("Culmen Depth (mm)", min_value=13.0, max_value=21.0, step=0.1)
flipper_length = st.number_input("Flipper Length (mm)", min_value=170, max_value=240, step=1)
body_mass = st.number_input("Body Mass (g)", min_value=2500, max_value=6500, step=10)

# Prediction logic
if st.button("Predict"):
    features = np.array([[species,island,culmen_length,culmen_depth,flipper_length,body_mass]])
    prediction = tree.predict(features)
    result = "MALE" if prediction[0] == 1 else "FEMALE"
    st.success(f"The model predicts: **{result}**")


