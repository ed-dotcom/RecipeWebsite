import streamlit as st
import pandas as pd
import numpy as np

RECIPES = pd.read_csv('data/combination_percentage_01.csv', compression='infer', storage_options=None)
#print(RECIPES['replaced'].unique())

def get_combinations(search_word):
    ordered_keys = pd.read_csv('data/ordered_keys.csv')
    word_index = ordered_keys[ordered_keys['replaced'] == search_word].index[0]
    ingredient_row = combination_percentage.iloc[word_index:word_index+1,:].T.sort_values(by=word_index, ascending=False)
    top_results = []
    for index in range(1,20):
        ingr_id = ingredient_row.T.columns[index]
        name = ordered_keys['replaced'].iloc[ingr_id]
        top_results.append(name)
    return top_results

def app():
    
    st.title('Aproveite para desfrutar de uma das maiores base de Dados de ingredientes.Faça uma busca com os ingredientes que deseja.')
        
    selectByuser = st.multiselect('Escolha uma das funcionalidades:', 
                RECIPES['replaced'].unique())
    print_combinations(selectByuser)

def print_combinations(selectByuser):

    for i in selectByuser:
        print(i)
        st.write(RECIPES[RECIPES['replaced']==i][['replaced', 'id']])
    print(selectByuser)