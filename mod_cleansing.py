""" Limpeza dos dados e organização em lista """

import pandas as pd

def cleansing(a):
    
    # Leitura do arquivo Excel especificado pelo argumento 'a'
    reviews = pd.read_csv(a)

    # Transformar cada linha em uma lista de strings e depois em uma lista única
    lista_de_reviews = reviews.apply(lambda row: ' '.join(map(str, row)), axis=1).tolist()
    reviews_limpa = []

    for i in range(len(lista_de_reviews)):
        
        # Substituir todas as ocorrências de "\'" por "'"
        review = lista_de_reviews[i].replace("\'", "'")
        
        # Converter a string da review em uma lista de caracteres
        review = list(review)
    
        # Encontrar o índice do primeiro espaço (' ')
        b = review.index(' ')
    
        # Adcionar à lista reviews_limpa o conteúdo da review a partir da sua numeração, separada do texto por um espaço
        reviews_limpa.append(''.join(review[(b+1):]))
    return reviews_limpa
