import requests
import json

url = r"https://servicodados.ibge.gov.br/api/v3/malhas/municipios/2507507?formato=application/vnd.geo+json"

resposta = requests.get(url)

if resposta.status_code == 200:
    print("OKAY!")
    dados = resposta.json()
    with open("etapa2jamp.geojson", "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4)
else:
    print(resposta.status_code)
