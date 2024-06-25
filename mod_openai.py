""" Geração de Insights Usando a API da OpenAI """

import os
import openai
from openai import OpenAI
from dotenv import load_dotenv
import pandas as pd


dataset = pd.read_csv("A2.csv")
print(dataset)

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = openai_api_key

