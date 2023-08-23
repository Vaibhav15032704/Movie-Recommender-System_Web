import streamlit as st
import pickle

def recomend(movie,dataFrame):
    movie_index = dataFrame[dataFrame['title'] == movie].index[0]

    distances = similarity[movie_index]
    movies_list2 = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]


    recomended_movies = []
    for i in movies_list2:
        recomended_movies.append(dataFrame.iloc[i[0]].title)
    return recomended_movies

movies_list1 = pickle.load(open('movies.pkl','rb'))
movies_list = movies_list1['title'].values


similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movies Recomender System')

option = st.selectbox(
    'How would you like to be contacted?',
movies_list
)

if st.button('Recomend'):
    recommendations = recomend(option,movies_list1)
    for i in recommendations:
        st.write(i)
