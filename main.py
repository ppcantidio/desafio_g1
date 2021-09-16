import requests
import re
import pandas as pd


req = requests.get('https://g1.globo.com')
html = req.text
cards = []

noticias = re.findall(r'"summary":"(.*?)","title":"(.*?)","url":"(.*?)"', html)

for noticia in noticias:
    card = {}
    card['Título'] = noticia[1]
    card['Subtítulo'] = noticia[0]
    card['Link'] = noticia[2]
    cards.append(card)

dataset = pd.DataFrame(cards)
print(dataset)
dataset.to_excel(r'data.xlsx', index=False)
