import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('pen_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Title
st.title("Penguin Sex Prediction App")
st.write("Predict whether a penguin is male or female based on its measurements.")

# User inputs
culmen_length = st.number_input("Culmen Length (mm)", min_value=30.0, max_value=60.0, value=45.0)
culmen_depth = st.number_input("Culmen Depth (mm)", min_value=13.0, max_value=22.0, value=17.0)
flipper_length = st.number_input("Flipper Length (mm)", min_value=170, max_value=240, value=200)
body_mass = st.number_input("Body Mass (g)", min_value=2500, max_value=6500, value=4000)

island = st.selectbox("Island", options=["Biscoe", "Dream", "Torgersen"])
species = st.selectbox("Species", options=["Adelie", "Gentoo", "Chinstrap"])

# Map string input to numerical values (as per preprocessing)
island_map = {"Biscoe": 0, "Dream": 1, "Torgersen": 2}
species_map = {"Adelie": 0, "Gentoo": 1, "Chinstrap": 2}

island_val = island_map[island]
species_val = species_map[species]

# Prediction
if st.button("Predict Sex"):
    input_data = np.array([[culmen_length, culmen_depth, flipper_length, body_mass, island_val, species_val]])
    prediction = model.predict(input_data)[0]
    result = "MALE" if prediction == 0 else "FEMALE"
    st.success(f"The predicted sex of the penguin is: **{result}**")
