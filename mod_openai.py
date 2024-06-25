""" Geração de Insights Usando a API da OpenAI """

import os
import openai
from openai import OpenAI
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = openai_api_key
client = OpenAI(api_key="OPENAI_API_KEY")

dataset = pd.read_csv("A2.csv")
datavalues = dataset.values

lista_comentarios = []
for x in range(0, 226):
    lista_comentarios.append(datavalues[x][1:])

def classifica_sentimento(comment):
    prompt = [{
        "role":"user", 
        "content":f"classifique o sentimento da seguinte review sobre um filme específico: {comment}\nCategory:"        
        }]

    response = openai.completions.create(
        engine="text-davinci-003",
        model = 'gpt-3.5-turbo-0125',
        choices=["Detestei", "Não gostei", "Apático", "Gostei", "Amei"],
        messages = prompt ,
        max_tokens = 600,
        temperature = 1
    )

    Resposta_do_chat = response.choices[0].message.content

    return Resposta_do_chat

sentimentos = []

for comentario in lista_comentarios:
    sentimentos.append(classifica_sentimento(comentario))

print(sentimentos)
