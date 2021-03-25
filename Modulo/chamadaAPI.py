import requests


def fetch_ingredients_infos(ingredient, Criador, id=False):
    """
    #fazer comparacao no dataset entre id do ingrediente 
    """
    url = f"https://apigroup/{Criador}/{ingredient}"
    response = requests.get(url)
    if response.status_code != 200:
        return ''
    data = response.json()
    return data
