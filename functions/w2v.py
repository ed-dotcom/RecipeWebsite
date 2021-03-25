import joblib
import pandas as pd

def word2vec(ingredient):

  word2vec = joblib.load('models/word2vec.joblib')
  try:
    ms = word2vec.wv.most_similar(ingredient)
  except:
    ms = {'ERROR': f'We are sorry but the word "{ingredient}" is not in vocabulary... try eating something else! :)'}
  return ms
