import requests
import json

api=r"https://servicodados.ibge.gov.br/api/v1/localidades/municipios/2507507"

resposta= requests.get(api)

if resposta.status_code == 200:
     dados = resposta.json()
     
else:
     print(f"{resposta.status_code}")

# for i in dados.values():
#      print(i)

with open("jampa.json", "w", encoding="utf-8") as f:
     f.write(json.dumps(dados, indent=4, ensure_ascii=False))
