''' Módulo de Scraping '''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd

# Instituindo headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
}

# Referenciando o website do filme selecionado
url = 'https://www.imdb.com/title/tt0087884/reviews/?ref_=ttrt_ql_2'

# Iniciando o driver para carregar todas as reviews da página
driver = webdriver.Chrome()
driver.get(url)

# Lista que receberá os comentários
ratings = []

# A maior problemática enfrentada fora a dificuldade em lidar com as aplicações de JavaScript.

# Nesse caso, os botões "Load More" impediam a leitura completa das reviews

# Solução: Loop para continuamente clicar no botão Load More, até que esse não exista mais
while True:
    try:
        # Replace ".ipl-load-more__button" with the appropriate CSS selector for the "Load More" button
        load_more_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".ipl-load-more__button"))
        )
        load_more_button.click()
        # Wait for the new reviews to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".lister-item-content"))
        )
    except Exception as e:
        print(f"Exception occurred: {e}")
        break

# Organiza o html com BeautifulSoup
soup = BeautifulSoup(driver.page_source, "html.parser")

# Encontra os elementos das reviews no html organizado
cells = soup.find_all('div', class_='lister-item-content')

# Extrai as avaliações
for cell in cells:
    review_text_div = cell.find('div', class_="text show-more__control")
    if review_text_div:
        rating = review_text_div.text.strip()
        ratings.append(rating)

# Cria um dataframe a partir das avaliações extraídas
dataset = pd.DataFrame({'Rating': ratings})

# Retorna e imprime o dataset
print(dataset)

# Encerra o webdriver
driver.quit()

# Passa o dataset para o arquivo A2.xlsx
dataset.to_excel("A2.xlsx")
df = pd.read_excel("A2.xlsx")
