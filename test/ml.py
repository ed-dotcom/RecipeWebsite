import joblib

def kmeans():
  kmeans = joblib.load('../models/kmeans.joblib')
  return kmeans

