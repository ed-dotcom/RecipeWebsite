import streamlit as st
import pandas as pd
import app1


ORDERED_KEYS = pd.read_csv('data/ordered_keys.csv')

#PAGES= {
#   'Faça uma busca por ingredientes': app1,
#   'Digite seu ingrediente desconhecido':app2,
#
#}

#st.sidebar.title('Menu')
#selection = st.sidebar.radio('Ir para ',list(PAGES.keys()))
#page = PAGES[selection]
#page.app()
ORDERED_KEYS = pd.read_csv('data/ordered_keys.csv')

@st.cache
def get_combination_percentage():
    return pd.read_csv('data/combination_percentage_01.csv', compression='infer', storage_options=None)
COMBINATION_PERCENTAGE = get_combination_percentage()

def get_combinations(search_word, range_start, range_end):
    word_index = ORDERED_KEYS[ORDERED_KEYS['replaced'] == search_word[0]].index[0]
    ingredient_row = COMBINATION_PERCENTAGE.iloc[word_index,:].T.sort_values(ascending=False)
    top_results = []
    for position in range(range_start,range_end):
        ingr_id = int(ingredient_row.index[position])
        name = ORDERED_KEYS['replaced'].iloc[ingr_id]
        top_results.append(name)
    return top_results


def print_combinations(selectByuser):

    for i in selectByuser:
        print(i)
        st.write(ORDERED_KEYS[ORDERED_KEYS['replaced']==i][['replaced', 'id']])
    

def app():
    
    st.title('Aproveite para desfrutar de uma das maiores base de Dados de ingredientes.Faça uma busca com os ingredientes que deseja.')
        
    selectByuser = st.multiselect('Escolha uma das funcionalidades:', 
            ORDERED_KEYS['replaced'].unique())
    
    
    st.write('Top results', get_combinations(selectByuser,1,21))


Ingredientes = st.sidebar.multiselect('Selecione seu ingrediente', ORDERED_KEYS['replaced'].unique())
recipes = st.sidebar.multiselect('Selecione a combinacao', ORDERED_KEYS['replaced'].unique())
new_df = get_combinations(search_word, range_start, range_end)
st.write(new_df) 





