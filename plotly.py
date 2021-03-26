import plotly.express as px
from kmeans import kmeans
import streamlit as st
import pandas as pd


def display_charts():
    kmean = kmeans()

    data = pd.read_csv('data/pca.csv')

    fig = px.scatter(x=data[0], y=data[1], color=kmeans.labels_, hover_name=data.index)

    fig2 = px.scatter_3d(x=data[0], y=data[1], z=data[2],color=kmeans.labels_, hover_name=data.index)
    return fig, fig2

kmeans = kmeans()
print(kmeans.labels_)