import dotenv
import requests
import os

dotenv.load_dotenv() # CARREGA VARIÁVEIS DO .env

NASA_API_KEY = os.getenv("NASA_API_KEY") # PEGA A CHAVE DA API DO

BASE_URL = "https://api.nasa.gov/planetary/apod" # URL BASE DA API

'''PARÂMETROS
DATE - yyyy-mm-dd
start_date - yyyy-mm-dd
end_date - yyyy-mm-dd
count - número de imagens aleatórias
api_key - chave da API'''
r = requests.get(BASE_URL, params={'api_key': NASA_API_KEY} )
# o PARAMS serve para digitar o "?" que indica que vai parÂmetro
data = r.json()# DICIONÁRIO JAVASCRIPT
title = data.get('title', 'Sem título')
description = data.get('explanation', 'Sem descrição')
image = data.get('hdurl', 'Sem imagem')

print(title, description, image)
