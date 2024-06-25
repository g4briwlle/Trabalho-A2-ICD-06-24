import os
import openai
from openai import OpenAI
from dotenv import load_dotenv
import pandas as pd

# Load environment variables from the .env file
load_dotenv('chave.env')

chave_ = input("Coloque sua chave API_KEY:")

client = OpenAI(api_key= chave_)

dataset = pd.read_csv("A2.csv")

# primeiro insight

datavalues = dataset.values

lista_comentarios = []
for x in range(0, 226):
    lista_comentarios.append(datavalues[x][1:])

def classifica_sentimento(comment):
    prompt = [{
        "role":"user", 
        "content":f"classifique o sentimento da seguinte review sobre um filme específico: {comment} escolhendo uma das seguintes categorias: Detestei, Não gostei, Apático, Gostei, Amei",
        }]

    response = client.chat.completions.create(
        # engine="text-davinci-003",
        model = 'gpt-3.5-turbo-0125',
        messages = prompt,
        max_tokens = 600,
        temperature = 1
    )

    Resposta_do_chat = response.choices[0].message.content

    return Resposta_do_chat

sentimentos = []

for comentario in lista_comentarios:
    print("ok")
    sentimentos.append(classifica_sentimento(comentario))

print(sentimentos)

# segundo insight

def classifica_categorias(comment):
    prompt = [{
        "role": "user",
        "content": f"Classifique o assunto principal do comentário a seguir: {comment} escolhendo uma das seguintes categorias: roteiro, fotografia, originalidade, atuação, emoção"
    }]
    
    response = client.chat.completions.create(
        model='gpt-3.5-turbo-0125',
        messages=prompt,
        max_tokens=600,
        temperature=1
    )
    
    Resposta_do_chat = response.choices[0].message.content
    
    return Resposta_do_chat.strip()

categorias = []

for comentario in lista_comentarios:
    categorias.append(classifica_categorias(comentario))

print(categorias)

# terceiro insight

def classifica_propensao(comment):
    prompt = [{
        "role": "user",
        "content": f"Classifique a propensão de alguém que escreveu o seguinte comentário sobre um filme: {comment} escolhendo uma das seguintes categorias: veria novamente, não veria novamente"
    }]
    
    response = client.chat.completions.create(
        model='gpt-3.5-turbo-0125',
        messages=prompt,
        max_tokens=600,
        temperature=1
    )
    
    Resposta_do_chat = response.choices[0].message.content
    
    return Resposta_do_chat.strip()

propensoes = []

for comentario in lista_comentarios:
    propensoes.append(classifica_propensao(comentario))

print(propensoes)
