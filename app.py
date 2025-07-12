import numpy as np
import streamlit as st
import pickle

model = pickle.load(open('PricePredictor.pkl','rb'))
st.title("House Price Prediction")

car = float(st.text_input("Enter No. of cars: ", "0"))
landsize = float(st.text_input("Enter landsize: ", "134"))
building = float(st.text_input("Enter building size: ", "134"))
yearbuilt = float(st.text_input("Enter year built: ", "1890"))



featureInput = np.array([[car,landsize,building,yearbuilt]])

price = model.predict(featureInput)

st.write(f'Hello, *World!* :sunglasses: . House Price : {price} ')
