import streamlit as st
import pandas as pd
import app1
import requests 
from Modulo.chamadaAPI import fetch_ingredients_infos


@st.cache
def get_unique_ingredientes():
    return pd.read_csv('data/ordered_keys.csv', compression='infer', storage_options=None)
ORDERED_KEYS = get_unique_ingredientes()

navigation = st.sidebar.radio('Navigation',['About','Playground'])
if navigation == 'About':
    st.write('About page here')
    ### code of the about page
if navigation == 'Playground':
    st.write('Playground goes here')

    Ingredientes = st.sidebar.multiselect('Selecione seu ingrediente', ORDERED_KEYS['replaced'].unique())
    for i in Ingredientes:
        print(i)
        st.write(ORDERED_KEYS[ORDERED_KEYS['replaced']==i][['replaced','id']])

    if st.sidebar.checkbox('Melhores combinações'):
        st.subheader('Suas melhores combinações são:')
        st.write('Best ingredientes match')
    if st.sidebar.checkbox('Ingredientes mais utilizados'):
        st.subheader('Seus ingredienntes mais utilizados são:')
        st.write('Sal')
    if st.sidebar.checkbox('Ingredientes menos utilizados'):
        st.subheader('Seus ingredienntes menos utilizados são:')
        st.write('Chuchu')


st.sidebar.title('Mais informações:')


#1chamar API Marilia *****
#fetch_ingredients_infos(input, "Marilia", id=True)
#2chamar API Gean ****
#fetch_ingredients_infos(input, "Gean", id=True)
#3chamar API Zucher ****
#fetch_ingredients_infos(input, "Zucher", id=True)

