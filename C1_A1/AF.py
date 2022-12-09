import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.tiobe.com/tiobe-index/'

url = "https://pokemondb.net/pokedex/all"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

rows = soup.find('table', attrs={"id":"pokedex"}).find('tbody').find_all('tr')

rows[0].find_all('td')[1].get_text()
rows[0].find_all('td')[2].get_text()

names = []
types = []
total = []
hp = []
attacks = []
defense = []
sp_attacks = []
sp_def = []
sppeds = []

for row in rows:
    names.append(row.find_all('td')[1].get_text())
    types.append(row.find_all('td')[2].get_text())
    total.append(row.find_all('td')[3].get_text())
    hp.append(row.find_all('td')[4].get_text())
    attacks.append(row.find_all('td')[5].get_text())
    defense.append(row.find_all('td')[6].get_text())
    sp_attacks.append(row.find_all('td')[7].get_text())
    sp_def.append(row.find_all('td')[8].get_text())
    sppeds.append(row.find_all('td')[9].get_text())

df = pd.DataFrame({
    "types":types,
    "total":total,
    "hp":hp,
    "attack":attacks,
    "def":defense,
    "sp attack":sp_attacks,
    "sp def":sp_def,
    "spped":sppeds
})

df.to_csv('tablas.csv')