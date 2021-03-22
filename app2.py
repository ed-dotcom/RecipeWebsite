import streamlit as st
import pandas as pd
import numpy as np

def app():
        
    st.title('Não encontrou o que desejava? Tente fazer a busca na opção Ingredientes desconhecidos.')

    st.text_input('Digite seu ingrediente')