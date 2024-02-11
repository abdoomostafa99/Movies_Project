import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(layout="wide")

movies = pd.read_csv('movies.csv')


interest = st.selectbox('Select a column to filter by:',
    ['runtime','votes','metascore','gross_collection'])
    
c1 , c2 = st.columns(2)
with c1:

    st.title(f'top 10 {interest} movies')
    dfnew = movies[['movie_name',interest]].nlargest(10 , interest)
    st.plotly_chart(px.bar(dfnew , x = 'movie_name' , y = interest , color='movie_name' , text_auto = 'True'))

with c2:
    st.title(f'buttom 10 {interest} movies')
    dfnew1 = movies[['movie_name',interest]].nsmallest(10 , interest)
    st.plotly_chart(px.bar(dfnew1 , x = 'movie_name' , y = interest , color='movie_name', text_auto = 'True'))

