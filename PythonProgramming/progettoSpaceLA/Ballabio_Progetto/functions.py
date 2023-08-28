# File with Functions

# --- Libraries ------------------------------------
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from itertools import chain
import plotly.express as px

# --- Functions ------------------------------------

def scrapingByYear(year):

    # Effettua una richiesta alla pagina web
    url = 'https://en.wikipedia.org/wiki/' + str(year) + '_in_spaceflight'
    response = requests.get(url)

    # Analizza la risposta con Beautiful Soup
    soup = BeautifulSoup(response.text, 'lxml')

    # Trova la/e tabella/e dei lanci
    tables = soup.find_all('table', {'class': 'wikitable'})

    # Estrai l'intestazione della tabella (gli headers)
    headers = []
    for th in tables[0].find_all('th'):
        headers.append(th.text.strip())

    # lambda function to delete empty string from list
    headers = list(filter(lambda x: len(x) > 0, headers))
    # print(headers)
    # ['Date and time (UTC)', 'Rocket', 'Flight number', 'Launch site', 'LSP', 
    # 'Payload', 'Operator', 'Orbit', 'Function', 'Decay (UTC)', 'Outcome', 'Remarks']

    data = []

    for table in tables:
        # Estrai i dati della tabella # per ogni lancio
        for row in table.find_all('tr'): 
            # Se lo stile della riga è "background-color:#e9e4e4", non la considerare
            if row.get('style') != "background-color:#e9e4e4":
                rowData = []
                for td in row.find_all('td'):
                    text = td.text.strip()
                    # delete apice
                    if "[2]" in text:
                        text = text.replace("[2]","")
                    rowData.append(text)

                if len(rowData) > 1:
                    data.append(rowData)
    return data, headers


def fixDateFormat(df):

    # Put a space between month and time (if present)
    # ex. January20:14 -> January 20:14
    df['Date and time (UTC)'] = df['Date and time (UTC)'].str.replace(r'(\d{2}:\d{2})', r' \1', regex=True)