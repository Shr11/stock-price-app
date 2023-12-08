import streamlit as st
import pandas as pd 
import sklearn as sk
from sklearn.ensemble import RandomForestClassifier

st.sidebar.text_input("Name")

st.write("""
         # Iris Flower Prediction App
         
         ***This app predicts the iris flower type***
         
         """)

st.sidebar.header("""User Input Parameters""")


def user_input_features():
    sepal_length = st.sidebar.slider('Sepal Length',4.1,7.9,5.6)
    sepal_width = st.sidebar.slider('Sepal Width',2.0,4.0,3.5)
    petal_width = st.sidebar.slider('Petal Width',0.10,2.10,1,6)
    petal_length = st.sidebar.slider('Petal Length',2.1,3.5,6.7)
    
    data = {
        'sepal_length': sepal_length,
        'sepal_width' : sepal_width,
        'petal_length': petal_length,
        'petal_width': petal_width
    }

    features = pd.DataFrame(data, index= [0])
    
    
    return features

df = user_input_features()

st.subheader('User Input Parameters')
st.write(df)