import os
import openai
from openai import OpenAI
from dotenv import load_dotenv
import pandas as pd

# Load environment variables from the .env file
load_dotenv('chave.env')

chave_ = input("Coloque sua chave API_KEY:")

client = OpenAI(api_key= chave_)

prompt = [{
        "role":"user", 
        "content":f'Você é um analista de review deixada por um espectador do filme Paris, Texas . Você precisa me retornar 3 classificações, nas categorias chamadas Sentimento, Propensão e Aspecto. Suas classificações serão retornadas sem pontuações ou complementos, respeitando a capitalização utilizada, separadas por vírgula e espaço somente. Categoria Sentimento: Classifique o sentimento que passa a "Review a ser analisada" entre as classificações Detestei, Não gostei, Apático, Gostei, Amei. Categoria Propensão: Classifique a propensão de ver o filme novamente de alguém que escreveu a "Review a ser analisada" entre as classificações Veria Novamente, Não Veria Novamente. Categoria Aspecto: Classifique o assunto principal da "Review a ser analisada" escolhendo uma das seguintes categorias: Roteiro, Fotografia, Originalidade, Atuação, Emoção. Review a ser analisada: {comment}\nCategory:'
        }]

    response = client.chat.completions.create(
        model = 'gpt-3.5-turbo-0125',
        messages = prompt ,
        max_tokens = 600,
        temperature = 1
    )

    Resposta_do_chat = response.choices[0].message.content

    return Resposta_do_chat
