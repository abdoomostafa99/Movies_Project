import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(layout="wide")

movies = pd.read_csv('movies.csv')

interest = st.selectbox('Select a column to filter by:',
    ['genre','director','actor_1','actor_2'])

colmn1 , colmn2 = st.columns(2)
with colmn1:

    st.title(f'top 10 popular {interest}')
    top_10 = movies[interest].value_counts().nlargest(10).reset_index()
    top_10.columns = [interest , 'count']
    st.plotly_chart(px.bar(top_10 , x=interest , y='count',color=interest, text_auto = 'True'))

with colmn2:
    st.title(f'buttom 10 popular {interest}')
    below_10 = movies[interest].value_counts().nsmallest(10).reset_index()
    below_10.columns = [interest , 'count']
    st.plotly_chart(px.bar(below_10 , x=interest , y='count',color=interest, text_auto = 'True'))