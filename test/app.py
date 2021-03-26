import streamlit as st
from plot import display_charts


fig, fig2 = display_charts()
st.plotly_chart(fig)
st.plotly_chart(fig2)
