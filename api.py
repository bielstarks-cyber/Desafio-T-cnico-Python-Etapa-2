import requests

def conectarapi(valor):
    api_url = {}
    url = "https://botgames-employee-data-migration-vwsrh7tyda-uc.a.run.app/employees?id="
    url_completa = f"{url}{valor}"
    response = requests.get(url_completa, params=api_url)
    dados = response.json()

    return dados