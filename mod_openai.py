""" Geração de Insights Usando a API da OpenAI """

from openai import OpenAI


client = OpenAI(api_key="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")

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

