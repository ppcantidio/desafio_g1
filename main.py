import requests
import re
import json

req = requests.get('https://g1.globo.com')
html = req.text
cards = []

noticias = re.findall(r'"summary":"(.*?)","title":"(.*?)","url":"(.*?)"', html)

for noticia in noticias:
    card = {}
    card['Titulo'] = noticia[1]
    card['Subtitulo'] = noticia[0]
    card['Link'] = noticia[2]
    cards.append(card)

json_object = json.dumps(cards, ensure_ascii=False)
print(json_object)