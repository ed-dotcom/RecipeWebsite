import streamlit as st
import pandas as pd
import app1
import requests 
from Modulo.chamadaAPI import fetch_ingredients_infos
from functions.model_processing import *
from functions.w2v import word2vec
from scipy import sparse
import joblib


@st.cache
def get_unique_ingredientes():
    return pd.read_csv('data/ordered_keys.csv', compression='infer', storage_options=None)
ORDERED_KEYS = get_unique_ingredientes()
@st.cache
def get_pickle():
    return pd.read_pickle('../ingredient_matching/data/ingr_map.pkl', compression='infer',storage_options=None)
df_pickle = get_pickle()
@st.cache
def get_ingredients_clean(df_pickle):
    return df_pickle[['id','replaced','count','raw_ingr']]
ingredients_clean = get_ingredients_clean(df_pickle)
@st.cache
def get_word2vec():
    return joblib.load('models/word2vec.joblib')
similar_results = get_word2vec()

@st.cache
def get_sparse():
    return sparse.load_npz(r'../ingredient_matching/data/sparse_final_df.npz')
final_sparse = get_sparse()

def output_func(input_ingredient, num_matches = 15, adventure = False, adventure_criteria = 15):
            '''Combines other functions into a workflow'''
            # input_ingredient = input_ingredient.split(',')
            num_matches += 1
            if type(input_ingredient) != list:
                input_ingredient = [input_ingredient]
            id_input = []

            for ingredient in input_ingredient:
                id_input.append(get_id(ingredient))
            min_ingredients = 0
            if adventure:
                min_ingredients = be_adventurous(id_input,adventure_criteria)
            id_list = find_match(id_input,num_matches,min_ingredients)
            names = list_to_names(id_list)
            return names

navigation = st.sidebar.radio('Navigation',['Playground', 'Tech'])
if navigation == 'Playground':
    # About paragraph here
    st.write('Playground goes here')

    ingredients = st.sidebar.multiselect('Selecione seu ingrediente', ORDERED_KEYS['replaced'].unique())
    for i in ingredients:
        print(i)
        ### get only ingredient name
        st.write(ORDERED_KEYS[ORDERED_KEYS['replaced']==i][['replaced','id']])

    if st.sidebar.checkbox('Melhores combinações'):
        st.subheader('Suas melhores combinações são:')
        num_matches = st.slider('Quantas sugestões?', 0, 35, 15)
        # st.write(“I'm “, age, 'years old')
        names = output_func(ingredients, num_matches)
        st.write(names)
    
    if st.sidebar.checkbox('Surprise Function'):
        st.subheader('surprise:')
        num_matches = st.slider('Quantas sugestões?', 0, 35, 15)
        adventure_criteria = st.slider('How adventurous are you?', 0, 35, 15)
        names = output_func(ingredients, num_matches, adventure = True, adventure_criteria = adventure_criteria,)
        st.write(names)

    if st.sidebar.checkbox('Similar ingredients'):
        st.subheader('Similar:')    
        similar = word2vec(ingredients)
    # .. other resources
if navigation == 'Tech':
    st.write('Technical stuff here')
    # add vitor's chart



#1chamar API Marilia *****
#fetch_ingredients_infos(input, "Marilia", id=True)
#2chamar API Gean ****
#fetch_ingredients_infos(input, "Gean", id=True)
#3chamar API Zucher ****
#fetch_ingredients_infos(input, "Zucher", id=True)

