from mod_scraping import *
from mod_cleansing import *
from mod_openai import *
from mod_excel import *

pega_reviews()

reviews = cleansing('A2.csv')

respostas = [[gpt_classifica(review)] for review in reviews]

print(respostas)
