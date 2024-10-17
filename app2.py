import streamlit as st
import os 
import numpy as np
import pandas as pd
from mlProject.pipeline.prediction import PredictionPipeline

st.title("Wine Quality Prediction using Modular Coding")

def train():
  os.system("python main.py")
  return "Training Successful!"

check=0

@st.cache
def load_data():
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
    data = pd.read_csv(url, sep=';')
    return data

data = load_data()

# Split the data into features and target
X = data.drop("quality", axis=1)

#st.sidebar("Train the model!")
if st.sidebar.button("Train!"):
  status=train()
  st.sidebar.write(status)
  check=1


# Streamlit app
st.title("Wine Quality Prediction App")
st.write("This app predicts the quality of wine based on various features.")

# Sidebar for user input
st.sidebar.header("Input Features")
fixed_acidity = st.sidebar.slider("Fixed Acidity", float(X["fixed acidity"].min()), float(X["fixed acidity"].max()), float(X["fixed acidity"].mean()))
volatile_acidity = st.sidebar.slider("Volatile Acidity", float(X["volatile acidity"].min()), float(X["volatile acidity"].max()), float(X["volatile acidity"].mean()))
citric_acid = st.sidebar.slider("Citric Acid", float(X["citric acid"].min()), float(X["citric acid"].max()), float(X["citric acid"].mean()))
residual_sugar = st.sidebar.slider("Residual Sugar", float(X["residual sugar"].min()), float(X["residual sugar"].max()), float(X["residual sugar"].mean()))
chlorides = st.sidebar.slider("Chlorides", float(X["chlorides"].min()), float(X["chlorides"].max()), float(X["chlorides"].mean()))
free_sulfur_dioxide = st.sidebar.slider("Free Sulfur Dioxide", float(X["free sulfur dioxide"].min()), float(X["free sulfur dioxide"].max()), float(X["free sulfur dioxide"].mean()))
total_sulfur_dioxide = st.sidebar.slider("Total Sulfur Dioxide", float(X["total sulfur dioxide"].min()), float(X["total sulfur dioxide"].max()), float(X["total sulfur dioxide"].mean()))
density = st.sidebar.slider("Density", float(X["density"].min()), float(X["density"].max()), float(X["density"].mean()))
pH = st.sidebar.slider("pH", float(X["pH"].min()), float(X["pH"].max()), float(X["pH"].mean()))
sulphates = st.sidebar.slider("Sulphates", float(X["sulphates"].min()), float(X["sulphates"].max()), float(X["sulphates"].mean()))
alcohol = st.sidebar.slider("Alcohol", float(X["alcohol"].min()), float(X["alcohol"].max()), float(X["alcohol"].mean()))

# Collect user input into a feature array
data = [fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alcohol]
data = np.array(data).reshape(1, 11)

# Make prediction
if st.button("Predict Quality"):
    obj = PredictionPipeline()
    predict = obj.predict(data)
    st.success(round(predict[0], 2))


      
  

