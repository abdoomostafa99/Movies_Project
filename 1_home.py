import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(layout="wide")

movies = pd.read_csv('movies.csv')

st.title('Movies Analysis')
st.image('https://wallpapers.com/images/hd/the-avengers-superhero-movie-eeotwqkmypkvalg9.webp')

st.markdown('''
* Welcome to the Movie  Analysis project!\n
* This project is focused on analyzing and visualizing data on a dataset related to movies.\n
* The goal is to gain insights into various aspects of the movie industry, such as box office performance, genre trends, and audience preferences
''')

movies.dropna(inplace=True)
st.subheader('Sample Dataset')
if st.checkbox('Show Dataset'):
    st.dataframe(movies.head(5))
