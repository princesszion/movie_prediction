import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
from PIL import Image
from prediction import predict_data
#Create header

st.write("<h1 style='color: skyblue; text-align: center;'>PREDICT<span style='color:black'>.IT</span></h1>", unsafe_allow_html=True)
# st.write(""" from insights to foresights - Predict""")
st.write("<h4 style='color: black;'>Great tool to predict a movie’s success</h4>", unsafe_allow_html=True)
# st.write("By shedding light on the elements that contribute to a movie's success, we help you to make predict the success of your movie. Don’t miss out on the chance to make informed decisions about which movies to produce and invest in.")

#image
#image = "https://www.analyticsinsight.net/wp-content/uploads/2022/01/10-Movies-on-artificial-intelligence-that-Engineers-geek-out-on.jpg"
image = "https://cdni.iconscout.com/illustration/premium/thumb/artificial-intelligence-3454686-2918395.png"
# st.image(image)

col1, col2 = st.columns(2)
# Adding the content to the first column
with col1:
    st.write("By shedding light on the elements that contribute to a movie's success, we help you to make predict the success of your movie.")
    st.write("All you have to do is to:")
    st.markdown("- Provide relevant information in the form and press the button to submit")

    st.markdown('''
    <style>
    [data-testid="stMarkdownContainer"] ul{
        padding-left:10px;
    }
    </style>
    ''', unsafe_allow_html=True)

with col2:
    st.image(image)
st.text(" ")
st.text(" ")
st.markdown(
    """
    <style>
    .page-button {
        background-color: none;
        padding: 0.5rem 2rem;
        border-radius: 0.5rem;
        border: 2px solid #82CBED;
        cursor: pointer;

    }
    </style>
    """
    , unsafe_allow_html=True
)

st.markdown(
    "<a href='https://docs.google.com/document/d/17TKULd_pSmUXFowtu_QxTwh1W8-UyTSF1sF-ccNbfi0/edit' class='page-button' target='_blank' style ='margin-left: 260px; text-decoration: none; color:#000000; '>Learn more</a>",
    unsafe_allow_html=True)
#Bring in the data
data = pd.read_csv('movie_metadataFinal.csv')
st.text(" ")
st.text(" ")
st.text(" ")
st.text(" ")
st.text(" ")
# st.text(" ")
# st.text(" ")
st.write("<h3 style='color: skyblue;'>THE DATA BEING USED:</h3>", unsafe_allow_html=True)

data

#Create and name sidebar
st.markdown(
    """
    <style>
    .css-1aumxhk {
    background-color: #011839;
    background-image: none;
    color: #ffffff
}
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.header('FILL IN YOUR INFORMATION')

# st.sidebar.write("""#### Choose your SG bias""")
def user_input_features():
    duration = st.sidebar.number_input('Duration of the movie(in minutes)', value=0)
    director_facebook_likes = st.sidebar.number_input('Movie director Facebook likes', value=0)
    actor_3_facebook_likes = st.sidebar.number_input('Actor 3 Facebook likes', value=0)
    actor_1_facebook_likes = st.sidebar.number_input('Actor 1 Facebook likes', value=0)
    gross = st.sidebar.number_input('Gross revenue of movie', value=0)
    # genres = st.sidebar.selectbox('Genre of the movie', ['Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music', 'Musical', 'Mystery', 'News', 'Reality-TV', 'Romance', 'Sci-Fi', 'Short', 'Sport', 'Talk-Show', 'Thriller', 'War', 'Western'])
    genre_options = {
        'Action': 1,
        'Animation': 2,
        'Adventure': 3,
        'Family': 4,
        'Horror': 5,
        'History': 6,
        'Mystery': 7,
        'Romance': 8,
        'Documentary': 9,
        'Fantasy': 10,
        'Comedy': 11,
        'Biography': 12,
        'Crime': 13,
        'Drama': 14,
        'Science Fiction': 15,
        'Politics': 16,
        'Thriller': 17,
    }
    genres_value = st.sidebar.selectbox('Genre of the movie', options=list(genre_options.keys()), index=0)
    genres = genre_options.get(genres_value)
    num_voted_users = st.sidebar.number_input('Number of people who voted for the movie', value=0)
    #cast_total_facebook_likes = st.sidebar.number_input('Total facebook like for the movie', value=0)
    num_user_for_reviews = st.sidebar.number_input('Number of users who gave a review', value=0)
    facenumber_in_poster = st.sidebar.number_input('Number of actors featured in the movie in the movie poster',
                                                   value=0)
    budget = st.sidebar.number_input('Budget of the movie in Dollars', value=0)
    content_rating = st.sidebar.number_input('Content rating of the movie', value=0)
    title_year = st.sidebar.number_input('The year in which the movie will be  released', value=0)
    actor_2_facebook_likes = st.sidebar.number_input('Actor 2 Facebook likes', value=0)
    aspect_ratio = st.sidebar.number_input('Aspect ratio the movie was made in', value=0)
    movie_facebook_likes = st.sidebar.number_input('Total number of facebook likes for the movie', value=0)

    if st.sidebar.button("Predict type of movie"):
        user_data = [duration, director_facebook_likes, actor_3_facebook_likes,
                   actor_1_facebook_likes, gross, genres, num_voted_users,
                   facenumber_in_poster, num_user_for_reviews, content_rating, budget, title_year,
                   actor_2_facebook_likes, aspect_ratio, movie_facebook_likes]
        result = predict_data([user_data])

        # Create a Pandas DataFrame to store the inputs
        display_data = {'Variable 1': [duration],
                     'Variable 2': [director_facebook_likes],
                     'Variable 3': [actor_3_facebook_likes],
                     'Variable 4': [actor_1_facebook_likes],
                     'Variable 5': [gross],
                     'Variable 6': [genres],
                     'Variable 7': [num_voted_users],
                     'Variable 8': [num_user_for_reviews],
                     'Variable 9': [facenumber_in_poster],
                     'Variable 10': [budget],
                     'Variable 11': [content_rating],
                     'Variable 12': [title_year],
                     'Variable 13': [actor_2_facebook_likes],
                     'Variable 14': [aspect_ratio],
                     'Variable 15': [movie_facebook_likes]}

        # Convert the user data to a Pandas DataFrame
        features = pd.DataFrame(display_data)
        # for i in range(0,10):
        #     st.text("")

        st.write("<h3 style='color: skyblue;'>YOUR CHOSEN VALUES:</h3>", unsafe_allow_html=True)
        st.write(features)
        st.write("<h3 style='color: skyblue;'>YOUR PREDICTION OUTPUT:</h3>", unsafe_allow_html=True)

        st.write(f"**Your movie will be:** {result[0]}")
df_user = user_input_features()
