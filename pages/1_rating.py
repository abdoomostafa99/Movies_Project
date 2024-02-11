import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(layout="wide")
movies = pd.read_csv('movies.csv')

st.title('About Rating')

max_rate = movies['rating'].max()
min_rate = movies['rating'].min()

col1, col2 = st.columns(2)

card1 = col1.container(border=1)
card1.metric(label = f'Max Rating Movies' , value = movies['rating'].max())

card2 = col2.container(border=1)
card2.metric(label = f'Min Rating Movies' , value = movies['rating'].min())

st.divider()

x = st.selectbox('Select a film you need know details:',
    movies['movie_name'])

y = movies[movies['movie_name'] == x].groupby('movie_name')[['rating','runtime']].sum().reset_index()
st.markdown(y.to_markdown(index=False))

st.divider()

st.title('Number Of Rating')
st.plotly_chart(px.histogram(movies , x = 'rating' , color='rating',title='number of rating'))
st.divider()

rate_above_9 = movies['rating'] > 9
rate_above_9 = movies[rate_above_9][['movie_name','rating']]

rate_below_9 = movies['rating'] == 8.1
rate_below_9 = movies[rate_below_9][['movie_name','rating']]

co1, co2 = st.columns(2)

with co1:
    st.title('Movies with rating (above 9)')
    st.plotly_chart(px.bar(rate_above_9 , x = 'movie_name' , y = 'rating' , color='movie_name', text_auto = 'True'))
with co2:
    st.title('Movies with min rating (8.1)')
    st.plotly_chart(px.bar(rate_below_9 , x = 'movie_name' , y = 'rating' , color='movie_name', text_auto = 'True'))

st.divider()
rating = st.slider('Pick a rate', 8.1 , 9.3 , step = 0.1)
slide = movies[movies['rating'] == rating]['movie_name']
st.markdown(slide.to_markdown(index = False))
