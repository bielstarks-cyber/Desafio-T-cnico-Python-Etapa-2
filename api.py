import os

import requests

def conectarapi(valor):
    api_url = {}
    user_url_api = os.getenv('USER_URL_API')
    url = user_url_api
    url_completa = f"{url}{valor}"
    response = requests.get(url_completa, params=api_url)
    dados = response.json()

    return dados