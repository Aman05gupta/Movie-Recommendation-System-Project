import streamlit as st
import pickle
import pandas as pd
import requests
def fetch_poster(id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8ad413a63f5b7fa1a2175555f9519cfa&language=en-US'.format(id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse=True, key=lambda x: x[1])[1:6]

    recommend_movies = []
    recommend_movies_posters = []
    for i in movie_list:
        id = movies.iloc[i[0]].id

        recommend_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommend_movies_posters.append(fetch_poster(id))



    return recommend_movies, recommend_movies_posters

movie_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movie_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox('How would ou like to be contacted?', movies['title'].values)

if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])


