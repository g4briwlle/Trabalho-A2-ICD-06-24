""" Extração e preparação dos Dados """

import requests



# testando se é possível a raspagem de dados
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
}

url = "https://www.reclameaqui.com.br/empresa/secretaria-estadual-de-educacao-rj/"

response = requests.get(url, headers=headers)

print(response.status_code)

