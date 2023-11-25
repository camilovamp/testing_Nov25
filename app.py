import streamlit as st
import pandas as pd
import plotly.express as px

#reading the file, dropping unneded column
df=pd.read_csv('cars_workshop.csv')
df = df.drop(df.columns[0], axis=1)
#---------------------------------------------


#creating header with checkbox
st.header('Market of used cars.Original data')
st.write("""
##### Filter the data below to see the ads by manufacturer
""")