""" Geração de Insights Usando a API da OpenAI """

import os
import openai
from openai import OpenAI
from dotenv import load_dotenv
import pandas as pd

"""
load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')

openai.api_key = openai_api_key

dataset = pd.read_excel("A2.xlsx")
"""
"""
def converte_comentarios_em_nota():
    lista_notas = []

    prompt = [{"role": "user", "content": f""]

    response = client.chat.completions.create(
        messages=prompt,
        model="gpt-3.5-turbo-0125",
        max_tokens=200,
        temperature=1
    )


    lista_notas.append[] = 

    return response

"""
"""
def insights(lista):
    

>>>>>>> 484a7cc5aabdf687716554d8cfc3a25bc26a18ae
"""