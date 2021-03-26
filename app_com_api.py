import streamlit as st
import pandas as pd
import requests 
from plotly import display_charts

CSS = """
h1 {
    color: red;
}
body {
    background-image: url(https://headwayadp.org.au/wp-content/uploads/2019/11/cooking.jpg);
    background-size: cover;
}
"""

if st.sidebar.checkbox('Inject CSS'):
    st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)

@st.cache
def get_unique_ingredientes():
    return pd.read_csv('data/ordered_keys.csv', compression='infer', storage_options=None)
ORDERED_KEYS = get_unique_ingredientes()


navigation = st.sidebar.radio('Navigation',['Playground', 'Tech'])
if navigation == 'Playground':
    # About paragraph here
    st.title('Food playground')

    ingredients = st.sidebar.multiselect('Selecione seu ingrediente', ORDERED_KEYS['replaced'].unique())
    for i in ingredients:
        print(i)
        ### get only ingredient name
        # st.write(ORDERED_KEYS[ORDERED_KEYS['replaced']==i][['replaced','id']])
    
    ### code to appear while user has not added input
    if not ingredients:
        st.subheader('Dont tell the kids you are playing with food!')
        st.write('Instructions on how to use')

    num_matches = st.sidebar.slider('Quantas sugestões?', 0, 35, 15)
### se a API falhar, manter uma condicional que carregue o df

    # if st.sidebar.checkbox('Melhores combinações', value = True):
    #     if ingredients:
    #         st.subheader('Suas melhores combinações são:')
    #         names = output_func(ingredients, num_matches)
    #         names_str = f'{names}'.replace('\'','')
    #         names_str = names_str.replace('[','')
    #         names_str = names_str.replace(']','')
    #         st.write(names_str)
    
    # if st.sidebar.checkbox('Surprise Function'):
    #     if ingredients:
    #         st.subheader('surprise:')
    #         adventure_criteria = st.sidebar.slider('How adventurous are you?', 0, 35, 15)
    #         names = output_func(ingredients, num_matches, adventure = True, adventure_criteria = adventure_criteria,)
    #         names_str = f'{names}'.replace('\'','')
    #         names_str = names_str.replace('[','')
    #         names_str = names_str.replace(']','')
    #         st.write(names_str)

    # if st.sidebar.checkbox('Similar ingredients'):
    #     if ingredients:
    #         st.subheader('Similar:')    

if navigation == 'Tech':
    st.write('This project uses the dataset provided at https://www.kaggle.com/shuyangli94/food-com-recipes-and-user-interactions?select=PP_recipes.csv')
    st.write('The Food Playground is a tool that suggests flavor harmonizations and possible substitutions between over 8,000 ingredients, based on recipes in whic they appear together.')
    st.write('Two models are the basis for the tools available at the playground: one is based on simple statistical inference, by computing the co-occurance of all items in a 178.000 receipes dataset. Another model uses natural language processing and k-means clustering to train a Machine Learning model that created 30 clusters of similar ingredients.')
    fig, fig2 = display_charts()
    st.plotly_chart(fig)
    st.plotly_chart(fig2)



#1chamar API Marilia *****
#fetch_ingredients_infos(input, "Marilia", id=True)
#2chamar API Gean ****
#fetch_ingredients_infos(input, "Gean", id=True)
#3chamar API Zucher ****
#fetch_ingredients_infos(input, "Zucher", id=True)

# url = 'http://localhost:8000/most_popular'
# params = {
#     'input_ingredient': ingredients,
#     'num_matches': num_matches
# }
# response = requests.get(url, params=params)
# response.json()
# #=> {wait: 64}


# url = 'http://localhost:8000/adventurous'
# params = {
#     'input_ingredient': ingredients,
#     'num_matches': num_matches,
#     'adventure' = True,
#     'adventure_criteria': num_matches
# }
# response = requests.get(url, params=params)
# response.json()
# #=> {wait: 64}



# url = 'http://localhost:8000/most_similar'
# params = {
#     'input_ingredient': ingredients,
# }
# response = requests.get(url, params=params)
# response.json()
# #=> {wait: 64}
