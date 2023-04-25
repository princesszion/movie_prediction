# import streamlit as st
# #st.set_page_config(layout="wide")
#
# st.set_page_config(
#      layout="wide",
#      initial_sidebar_state="expanded",
# )
# import pandas as pd
# import numpy as np
# from prediction import predict_data
# st.title("Movie Classification System")
# st.markdown("Toy model to play to classify Movies into \
# Flop movie, Average movie, Hit movie")
#
# st.header("Movie Characteristics")
# col1, col2, col3, col4 = st.columns((1,1,1,1))
# with col1:
#     num_voted_users = st.number_input('Insert number of voted users')
#     num_user_for_reviews = st.number_input('Insert number of users for review')
#     duration = st.number_input('Insert movie Duration')
# with col2:
#     movie_facebook_likes = st.number_input('Insert number of facebook likes for movie')
#     gross = st.number_input('Insert gross revenue of movie')
#     genres = st.number_input('Insert genre of the movie')
#
# with col3:
#     actor_1_facebook_likes = st.number_input('Insert actor 1 facebook likes')
#     actor_2_facebook_likes = st.number_input('Insert actor 2 facebook likes')
#     actor_3_facebook_likes = st.number_input('Insert  actor 3 facebook likes ')
#
# with col4:
#     director_facebook_likes = st.number_input('Insert movie director facebook likes')
#     actor_3_name = st.number_input('Insert actor 3 name')
#     budget = st.number_input('Insert movie total budget')
#     title_year = st.number_input('Insert movie release year')
#
#
# if st.button("Predict type of Movie"):
#     in_data = [duration, director_facebook_likes, actor_3_facebook_likes,
#     actor_1_facebook_likes,gross, genres, num_voted_users,
#     actor_3_name, num_user_for_reviews,budget,title_year,
#        actor_2_facebook_likes, movie_facebook_likes]
#     result = predict_data([in_data])
#     st.text(result[0])

import streamlit as st
st.set_page_config(
     layout="wide",
     initial_sidebar_state="expanded",
)
import pandas as pd
import numpy as np
from prediction import predict_data

# Set background color and font style
st.markdown("""
<style>
body {
    background-color: #F9F9F9;
    font-family: 'Helvetica', sans-serif;
}
</style>
""", unsafe_allow_html=True)

# Set header and subheader
st.write("""
# Movie Classification System
Toy model to play to classify Movies into Flop movie, Average movie, Hit movie
""")


def app():
    st.title("App Page")

    # Add link to go to Test page
    st.markdown("[Go to Test Page](http://localhost:8501/test)")
# Create sidebar with movie characteristics inputs
st.sidebar.header('Movie Characteristics')
app()
# num_critic_for_reviews = st.sidebar.number_input('Number of critic for reviews', value=0)
duration = st.sidebar.number_input('Duration of the movie', value=0)
director_facebook_likes = st.sidebar.number_input('Movie director Facebook likes', value=0)
actor_3_facebook_likes = st.sidebar.number_input('Actor 3 Facebook likes', value=0)
actor_1_facebook_likes = st.sidebar.number_input('Actor 1 Facebook likes', value=0)
gross = st.sidebar.number_input('Gross revenue of movie', value=0)
#genres = st.sidebar.selectbox('Genre of the movie', ['Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music', 'Musical', 'Mystery', 'News', 'Reality-TV', 'Romance', 'Sci-Fi', 'Short', 'Sport', 'Talk-Show', 'Thriller', 'War', 'Western'])
genre_options ={
    'Action':1,
    'Animation':2,
    'Adventure':3,
    'Family':4,
    'Horror':5,
    'History':6,
    'Mystery':7,
    'Romance':8,
    'Documentary':9,
    'Fantasy':10,
    'Comedy':11,
    'Biography':12,
    'Crime':13,
    'Drama':14,
    'Science Fiction':15,
    'Politics':16,
    'Thriller':17,
}
genres_value = st.sidebar.selectbox('Genre of the movie',options=list(genre_options.keys()),index = 0)
genres = genre_options.get(genres_value)
num_voted_users = st.sidebar.number_input('Number of people who voted for the movie', value=0)
#cast_total_facebook_likes = st.sidebar.number_input('Total facebook like for the movie', value=0)
num_user_for_reviews = st.sidebar.number_input('Number of users who gave a review', value=0)
facenumber_in_poster = st.sidebar.number_input('Number of actors featured in the movie in the movie poster', value=0)
budget = st.sidebar.number_input('Budget of the movie in Dollars', value=0)
content_rating = st.sidebar.number_input('Content rating pf the movie', value=0)
title_year = st.sidebar.number_input('The year in which the movie is released', value=0)
actor_2_facebook_likes = st.sidebar.number_input('Actor 2 Facebook likes', value=0)
aspect_ratio = st.sidebar.number_input('Aspect ratio the movie was made in', value=0)
movie_facebook_likes = st.sidebar.number_input('Total number of facebook likes for the movie', value=0)

# actor_3_name = st.sidebar.text_input('Actor 3 name')
#popularity = st.sidebar.number_input('Popularity of movie', value=0)
#vote_count = st.sidebar.number_input('Movie release year', value=0)

# Create prediction button
if st.sidebar.button("Predict type of movie"):
    in_data = [duration, director_facebook_likes, actor_3_facebook_likes,
    actor_1_facebook_likes,gross, genres, num_voted_users,
    facenumber_in_poster, num_user_for_reviews,content_rating,budget,title_year,
    actor_2_facebook_likes, aspect_ratio,movie_facebook_likes]
    result = predict_data([in_data])
    st.write(f"**The predicted type of movie is:** {result[0]}")

# Set footer text
st.markdown("""
***
Created by [Your Name](https://www.yourwebsite.com/)
""")

