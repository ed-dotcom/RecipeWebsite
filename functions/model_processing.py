import pandas as pd
import scipy.sparse as sparse
import numpy as np

df_pickle = pd.read_pickle('data/ingr_map.pkl')
ingredients_clean = df_pickle[['id','replaced','count','raw_ingr']]

final_sparse = sparse.load_npz(r'data/sparse_final_df.npz')

def get_id(ingredient_str):
    # Transforms string input to pre-processed ID
    ingredient_id = ingredients_clean[ingredients_clean['raw_ingr'] ==ingredient_str]
    ingredient_id.reset_index(inplace=True)
    return ingredient_id.loc[0,'id']

def get_name(ingredient_id):
    # Transforms ID back to pre-processed string
    ingredient_name = ingredients_clean[ingredients_clean['id'] == ingredient_id]
    ingredient_name.reset_index(inplace=True)
    return ingredient_name.loc[0,'replaced']

def find_match(id_input,num_matches,min_ingredients):
    # Returns list of ingredient IDs and count of occurances
    recipe_indices = final_sparse[:,id_input] == 1
    numpy_arr = sparse.find(recipe_indices)
    test = np.unique(numpy_arr[0],return_counts=True)
    idx = test[0]
    test2 = idx[test[1] == max(test[1])]
    indices = (-final_sparse[test2,:].sum(axis=0).A1).argsort()[min_ingredients:num_matches+min_ingredients]
    return indices[len(id_input):]

def list_to_names(ingredient_id_list):
    # Takes in list of ingredient IDs and returns list of names
    list_ = []
    for id in ingredient_id_list:
        list_.append(get_name(id))
    return list_

def be_adventurous(id_input,adventure_criteria):
    list_ = []
    for id in id_input:
        counts = ingredients_clean.loc[ingredients_clean['id']==id]['count'].to_list()
        list_.append(counts[0])
    max_ingredients = round(max(list_) * 0.05)
    min_criteria = min([max([max_ingredients, 10]),adventure_criteria])
    return min_criteria

def output_func(input_ingredient, num_matches = 15, adventure = False, adventure_criteria = 15):
    '''Combines other functions into a workflow'''
    # input_ingredient = input_ingredient.split(',')
    num_matches += 1
    if type(input_ingredient) != list:
        input_ingredient = [input_ingredient]
    id_input = []

    for ingredient in input_ingredient:
        id_input.append(get_id(ingredient))
    min_ingredients = 0
    if adventure:
        min_ingredients = be_adventurous(id_input,adventure_criteria)
    id_list = find_match(id_input,num_matches,min_ingredients)
    names = list_to_names(id_list)
    return names
