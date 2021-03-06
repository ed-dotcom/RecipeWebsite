import streamlit as st
import pandas as pd
import requests
from functions.model_processing import *
# from functions.plot import *
import plotly.express as px
import joblib

##### MISSING: change background (png)
CSS = """
h1 {
    color: red;
}
body {
    background-image: url(https://headwayadp.org.au/wp-content/uploads/2019/11/cooking.jpg);
    background-size: cover;
}
"""

##### MISSING: transfer to API_request.py
def get_combination(ingredients, num_matches, adventure, adventure_criteria):
    ingredients_join = ','.join(ingredients)
    url = 'https://ingredients-playground-api-bfr4ogevkq-uc.a.run.app/find_combination'
    params = {
        'input_ingredient': ingredients,
        'num_matches': num_matches,
        'adventure' : adventure,
        'adventure_criteria': adventure_criteria
    }
    response = requests.get(url, params=params)
    print(response.status_code)
    if response.status_code != 200:
        return False
    return response.json()

##### MISSING: transfer to API_request.py
def get_similar(ingredient):
    url = f'https://ingredients-playground-api-bfr4ogevkq-uc.a.run.app/most_similar/{ingredient}'
    response = requests.get(url)
    print(response.status_code)
    if response.status_code != 200:
        return False
    return response.json()


def kmeans():
  kmeans = joblib.load('models/kmeans.joblib')
  return kmeans

def display_charts():
  kmean = kmeans()

  data = pd.read_csv('data/pca.csv')
  fig = px.scatter(x=data['0'], y=data['1'], color=kmean.labels_, hover_name=data['Unnamed: 0'])
  fig2 = px.scatter_3d(x=data['0'], y=data['1'], z=data['2'],color=kmean.labels_, hover_name=data['Unnamed: 0'])

  return fig, fig2


##### MISSING: transform in permanent CSS injection (remove checkbox)
# if st.sidebar.checkbox('Inject CSS'):
#     st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)

@st.cache
def get_unique_ingredientes():
    return pd.read_csv('data/ordered_keys.csv')
ORDERED_KEYS = get_unique_ingredientes()

# Sidebar
st.sidebar.title('Navigation')
##### MISSING: put about before, then set playgroung to default
navigation = st.sidebar.radio('Pages',['Playground', 'About'])
##### MISSING: add a horizontal bar, something to separate navigation from parameters

if navigation == 'Playground':
    st.sidebar.subheader('')
    ##### MISSING: deal with ingredients with '
    ingredients = st.sidebar.multiselect('', ORDERED_KEYS['replaced'].unique())
    st.title('Food playground')
    # instructions and info to appear while user has not added any input
    if not ingredients:
        st.subheader('Dont tell the kids you are playing with food!')
        ##### MISSING: add instructions
        st.write('Instructions on how to use')

    num_matches = st.sidebar.slider('How many suggestions?', 0, 35, 15)

    if st.sidebar.checkbox('Most popular combinations', value = True):
        if ingredients:
            st.subheader('The most popular combinations are:')
            response_json = get_combination(ingredients, num_matches, adventure=False, adventure_criteria=0)
            if response_json != False:
                response_str = response_json['Recommendations']
                response_str = ', '.join(response_str)
                st.write(response_str)
            else:
                # loading .csv inside else so the page does not need to load if API is ok
                @st.cache
                def get_unique_ingredientes():
                    return pd.read_csv('data/ordered_keys.csv')
                ORDERED_KEYS = get_unique_ingredientes()
                @st.cache
                def get_pickle():
                    return pd.read_pickle('../ingredient_matching/data/ingr_map.pkl')
                df_pickle = get_pickle()
                @st.cache
                def get_ingredients_clean(df_pickle):
                    return df_pickle[['id','replaced','count','raw_ingr']]
                ingredients_clean = get_ingredients_clean(df_pickle)
                @st.cache
                def get_sparse():
                    return sparse.load_npz(r'../ingredient_matching/data/sparse_final_df.npz')
                final_sparse = get_sparse()
                ##### MISSING: maybe filter out results like water, salt, etc
                names = output_func(ingredients, num_matches)
                names_str = f'{names}'.replace('\'','')
                names_str = names_str.replace('[','')
                names_str = names_str.replace(']','')
                st.write(names_str)

    if st.sidebar.checkbox('Adventurous combinations'):
        if ingredients:
            adventure_criteria = st.sidebar.slider('How adventurous are you?', 0, 35, 15)
            st.subheader('Our bold suggestions are:')
            response_json = get_combination(ingredients, num_matches, adventure=True, adventure_criteria=adventure_criteria)
            if response_json != False:
                response_str = response_json['Recommendations']
                response_str = ', '.join(response_str)
                st.write(response_str)
            else:
                # carregar os .csv
                @st.cache
                def get_unique_ingredientes():
                    return pd.read_csv('data/ordered_keys.csv')
                ORDERED_KEYS = get_unique_ingredientes()
                @st.cache
                def get_pickle():
                    return pd.read_pickle('../ingredient_matching/data/ingr_map.pkl')
                df_pickle = get_pickle()
                @st.cache
                def get_ingredients_clean(df_pickle):
                    return df_pickle[['id','replaced','count','raw_ingr']]
                ingredients_clean = get_ingredients_clean(df_pickle)
                @st.cache
                def get_sparse():
                    return sparse.load_npz(r'../ingredient_matching/data/sparse_final_df.npz')
                final_sparse = get_sparse()
                ##### MISSING: maybe filter out results like water, salt, etc
                names = output_func(ingredients, num_matches, adventure = True, adventure_criteria = adventure_criteria)
                names_str = f'{names}'.replace('\'','')
                names_str = names_str.replace('[','')
                names_str = names_str.replace(']','')
                st.write(names_str)

    if st.sidebar.checkbox('Similar ingredients'):
        if ingredients:
            for ingredient in ingredients:
                st.subheader(f'Most similar to {ingredient}')
                response_json = get_similar(ingredient)
                if response_json != False:
                    ##### MISSING: maybe filter out results like water, salt,etc
                    response = response_json['most_similar'][1:]
                    for item in response:
                        st.write(item[0],round(float(item[1]),2)*100, '%')
                    # response_str = ', '.join(response_str)
                    # st.write(response_str)
                    df = pd.DataFrame.from_dict(response_json)
                else:
                    st.write('In development')



if navigation == 'About':
    ##### MISSING: write projetc presentation
    st.write('This project uses the dataset provided at https://www.kaggle.com/shuyangli94/food-com-recipes-and-user-interactions?select=PP_recipes.csv')
    st.write('The Food Playground is a tool that suggests flavor harmonizations and possible substitutions between over 8,000 ingredients, based on recipes in whic they appear together.')
    st.write('Two models are the basis for the tools available at the playground: one is based on simple statistical inference, by computing the co-occurance of all items in a 178.000 receipes dataset. Another model uses natural language processing and k-means clustering to train a Machine Learning model that created 30 clusters of similar ingredients.')
    fig, fig2 = display_charts()
    st.subheader('Ingredients clustering')
    st.plotly_chart(fig)
    st.subheader('Ingredients clustering 3D')
    st.plotly_chart(fig2)



########### coisas a resolver: banana + tomate o c??digo quebra; ingredientes com aspas quebram tb