import streamlit as st
import pandas as pd
import plotly.express as px
import pacote

kmeans = kmeans()

data = pd.read_csv('data/pca.csv')

fig = px.scatter(x=data[0], y=data[1], color=kmeans.labels_, hover_name=data.index)
st.plotly_chart(fig)


fig2 = px.scatter_3d(x=data[0], y=data[1], z=data[2],color=kmeans.labels_, hover_name=data.index)
st.plotly_chart(fig2)
