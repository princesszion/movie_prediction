import streamlit as st
import pandas as pd
import numpy as np
from prediction import predict_data
st.title("Movie Classification System")
st.markdown("Toy model to play to classify Movies into \
Flop movie, Average movie, Hit movie")

st.header("Movie Characteristics")
col1, col2 = st.columns(2)
with col1:
    num_voted_users = st.number_input('Insert number of voted users')
    num_critic_for_reviews = st.number_input('Insert critic reviews')
    num_user_for_reviews = st.number_input('Insert number of users for review')
    duration = st.number_input('Insert movie Duration')
    movie_facebook_likes = st.number_input('Insert number of facebook likes for movie')
    gross = st.number_input('Insert gross revenue of movie')
    cast_total_facebook_likes = st.number_input('Insert number of facebook likes for casts')
with col2:
    actor_2_facebook_likes = st.number_input('Insert actor 2 facebook likes')
    actor_1_facebook_likes = st.number_input('Insert actor 1 facebook likes')
    genres = st.number_input('Insert genre of the movie')
    actor_3_facebook_likes = st.number_input('Insert  actor 3 facebook likes ')
    content_rating = st.number_input('Insert movie content rating')
    director_facebook_likes = st.number_input('Insert movie director facebook likes')
    language = st.number_input('Insert language of the movie')



if st.button("Predict type of Movie"):
    in_data = [num_voted_users, num_critic_for_reviews, num_user_for_reviews,duration,movie_facebook_likes,gross,director_facebook_likes,language,cast_total_facebook_likes,actor_2_facebook_likes,actor_1_facebook_likes,genres,actor_3_facebook_likes,content_rating]
    result = predict_data([in_data])
    st.text(result[0])