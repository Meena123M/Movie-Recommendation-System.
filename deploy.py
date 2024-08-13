import streamlit as st
import pandas as pd
import pickle

st.title('Movie Recommendation System')

# movies_list=pickle.load(open('movies.pkl','rb'))

dic=pickle.load(open('df_dic.pkl','rb'))
movie=pd.DataFrame(dic)
similarity=pickle.load(open('similaity.pkl','rb'))



def movie_index(m):
  i=movie[movie['title']==m].index[0]
  distances=similarity[i]  
  movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6] 

  recommendation=[]  
  for i in movie_list:
      recommendation.append(movie.iloc[i[0]]['title'])

  return recommendation 

option = st.selectbox(
    "Pick your favoite one!",
   movie['title'].values
)
if st.button("Recommend", type="primary"):
   recommended_movies=movie_index(option)

   for i in recommended_movies:
      st.write(i)
   
   
 
