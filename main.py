from mod_scraping import *
from mod_cleansing import *
from mod_openai import *
from mod_excel import *

pega_reviews()

reviews = cleansing('A2.xlsx')

insights(reviews)




