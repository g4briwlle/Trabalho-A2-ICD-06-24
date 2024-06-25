""" Geração de Insights Usando a API da OpenAI """

import os
import openai
from openai import OpenAI

def gpt_classifica(comment):

    chave_1 = 'sk-proj-k7GLrgLcR00pS2dZE'
    chave_2 = '8BaT3BlbkFJQ8i6oF94z2L9m9NpcMAW'

    client = OpenAI(api_key= chave_1+chave_2)
    
    prompt = [{
        "role":"user", 
        "content":f'Você é um analista de review deixada por um espectador do filme Paris, Texas . Você precisa me retornar 3 classificações, nas categorias chamadas Sentimento, Propensão e Aspecto. Suas classificações serão retornadas sem pontuações ou complementos, respeitando a capitalização utilizada, separadas por vírgula e espaço somente, no modelo Classificação1, Classificação2, Classificação3. Categoria Sentimento: Classifique o sentimento que passa a "Review a ser analisada" entre as classificações Detestei, Não gostei, Apático, Gostei, Amei. Categoria Propensão: Classifique a propensão de ver o filme novamente de alguém que escreveu a "Review a ser analisada" entre as classificações Veria Novamente, Não Veria Novamente. Categoria Aspecto: Classifique o assunto principal da "Review a ser analisada" escolhendo uma das seguintes categorias: Roteiro, Fotografia, Originalidade, Atuação, Emoção. Review a ser analisada: {comment}\nCategory:'
        }]

    response = client.chat.completions.create(
        model = 'gpt-3.5-turbo-0125',
        messages = prompt ,
        max_tokens = 600,
        temperature = 1
    )

    Resposta_do_chat = response.choices[0].message.content

    return Resposta_do_chat

