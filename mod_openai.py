""" Geração de Insights Usando a API da OpenAI """

import os
import openai
from openai import OpenAI
from dotenv import load_dotenv
import pandas as pd

client = OpenAI(api_key="")

dataset = pd.read_csv("A2.csv")
print(dataset)

"""
def converte_comentarios_em_nota(comentario):

    prompt = [{
        "role": "user",
        "content": "Resuma "
            }]

    response = client.chat.completions.create(
        messages=prompt,
        model="gpt-3.5-turbo-0125",
        max_tokens=200,
        temperature=1
    )

    Resposta_do_chat = response.choices[0].message.content

def insights(lista):
"""
