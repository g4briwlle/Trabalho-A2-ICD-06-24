""" Geração de Insights Usando a API da OpenAI """

from openai import OpenAI

with open("chave_tarefa_0506.txt", "r") as arquivo:
    chave = arquivo.read()

OpenAI.api_key = chave.strip()

client = OpenAI(api_key = chave)
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
