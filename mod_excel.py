""" Transferência das reviews para Excel """
import pandas as pd
from mod_openai import *
from mod_cleansing import *

reviews = cleansing('A2.csv')
respostas = [gpt_classifica(review) for review in reviews]

sentimento = []
propensao = []
aspecto = []

for i in range(len(respostas)):
    sentimento.append(respostas[i].split(",")[0])
    propensao.append(respostas[i].split(",")[1])
    aspecto.append(respostas[i].split(",")[2])

data = {
    'Sentimento': sentimento,
    'Propensão': propensao,
    'Aspecto': aspecto
}

df = pd.DataFrame(data)

df.to_csv('reviews_tratadas.csv', index=False)
