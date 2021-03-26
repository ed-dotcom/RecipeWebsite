import pandas as pd
import plotly.express as px
import joblib

def kmeans():
  kmeans = joblib.load('../models/kmeans.joblib')
  return kmeans

def display_charts():
  kmean = kmeans()

  data = pd.read_csv('../data/pca.csv')
  fig = px.scatter(x=data['0'], y=data['1'], color=kmean.labels_, hover_name=data['Unnamed: 0'])
  fig2 = px.scatter_3d(x=data['0'], y=data['1'], z=data['2'],color=kmean.labels_, hover_name=data['Unnamed: 0'])

  return fig, fig2
