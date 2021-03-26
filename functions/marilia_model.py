import pandas as pd
import numpy as np

combination_percentage = pd.read_csv('data/combination_percentage.csv')
ordered_keys = pd.read_csv('data/ordered_keys.csv')

# gets most popular combinations with one ingredient
def most_popular(search_word):
    word_index = ordered_keys[ordered_keys['replaced'] == search_word].index[0]
    ingredient_row = combination_percentage.iloc[word_index:word_index+1,:].T.sort_values(by=word_index, ascending=False)
    top_results = []
    for index in range(1,20): # alter here to get percentage of results
        ingr_id = ingredient_row.T.columns[index]
        name = ordered_keys['replaced'].iloc[int(ingr_id)]
        top_results.append(name)
    return top_results

# gets surprising combinations with one ingredient, considering only the third top tier
def surprise(search_word):
    word_index = ordered_keys[ordered_keys['replaced'] == search_word].index[0]
    ingredient_row = combination_percentage.iloc[word_index:word_index+1,:].T.sort_values(by=word_index, ascending=False)
    size_results = ingredient_row[ingredient_row[word_index] != 0].shape[0]
    random_toptier = []
    for index in np.random.randint(0,int(size_results/3),20):
        ingr_id = ingredient_row.T.columns[index]
        name = ordered_keys['replaced'].iloc[int(ingr_id)]
        random_toptier.append(name)

    return random_toptier