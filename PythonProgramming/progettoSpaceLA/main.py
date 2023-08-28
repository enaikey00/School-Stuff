
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from itertools import chain
import plotly.express as px

from functions import *

year = input("Which year in spaceflight? Year: ")

data, headers = scrapingByYear(year)

# unisce ogni tre liste in un'unica lista
merged_data = [list(chain(*data[i:i + 2])) for i in range(0, len(data), 2)]
# rimuove le liste che hanno più o meno di 11 elementi (sono altre tables)
filtered_data = [lst for lst in merged_data if len(lst) == 11]
data = filtered_data

# crea un DataFrame con i dati
df = pd.DataFrame(data, columns = headers[:-1])

# fix date format
fixDateFormat(df)

# salva su excel per visualizzare i dati
df.to_excel("output.xlsx")


# --- Analisi Dati con Pandas ------------------------

# Print dtypes
print(df.dtypes)

print("\n--- Total Launches ---")
totalLaunches = len(df.index)
print(totalLaunches)

# --- Analisi dei NaN --------------------------------
print("\n--- NaN Overview ---")
# Blank spaces are NaN
df = df.replace(r'^\s*$', np.nan, regex=True)

# Print total NaN count
nanTotal = df.isnull().sum().sum()
print("Total: ", nanTotal)
print("% of Records: ", round(nanTotal/(df.shape[0]*df.shape[1]), 2),"%" )

# Print NaN by column
print(pd.isnull(df).sum()[pd.isnull(df).sum() > 0])

print(df.info()) # or head

print("\n--- Function Overview ---")
functionCount = df['Function'].value_counts()
filtered_functionCount = functionCount[functionCount >= 5]
print(filtered_functionCount.to_string())

print("\n--- Orbit Overview ---")
orbitCount = df['Orbit'].value_counts()
filtered_orbitCount = orbitCount[orbitCount >= 5]
print(filtered_orbitCount.to_string())




# --- Grafico a barre Function -----------------------------
colors = ['blue', 'red', 'green', 'yellow', 'purple']  # Definisci una lista di colori
colors = colors * (len(filtered_functionCount) // len(colors)) + colors[:len(filtered_functionCount) % len(colors)]  # Ripeti e taglia la lista per adattarla ai tuoi dati


fig = px.bar(x=filtered_functionCount.index, 
             y=filtered_functionCount.values,
             color=colors,
             labels={'x':'Function', 'y':'Count'},
             title='Function of the Launches')
fig.show()

# --- Grafico a torta NaN -----------------------------
# Calcola la somma dei valori NaN per ogni colonna
nan_counts = pd.isnull(df).sum()
# Filtra le colonne con più di 0 valori NaN
nan_counts = nan_counts[nan_counts > 0]

# Crea un grafico a torta
fig = px.pie(names=nan_counts.index, 
             values=nan_counts.values, 
             title='NaN counts in each column')
fig.show()


# Grafico a Torta Outcome ----------------------------
# Conta il numero di ciascun valore unico nella colonna 'Outcome'
outcome_counts = df['Outcome'].value_counts()

# rafico a torta
fig = px.pie(names=outcome_counts.index, 
             values=outcome_counts.values, 
             title='Outcomes of space launches')
fig.show()

"""
UPGRADE possibili: 
l'utente può inserire un range di anni
        nota: come gestire una lista di df o come unire più df, conservando l'informazione sull'anno (ex.una nuova colonna)
fare funzione per racchiudere i grafici
colab
"""