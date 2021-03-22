import streamlit as st

import app1
import app2

PAGES= {
    'Faça uma busca por ingredientes': app1,
    'Digite seu ingrediente desconhecido':app2,

}

st.sidebar.title('Menu')
selection = st.sidebar.radio('Ir para ',list(PAGES.keys()))
page = PAGES[selection]
page.app()