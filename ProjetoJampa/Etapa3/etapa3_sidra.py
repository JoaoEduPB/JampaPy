import pandas as pd
import geopandas as gpd

bairros = gpd.read_file("../Etapa2/bairros_jampa.geojson")
bairros["Area em Km²"] = bairros.to_crs(epsg=31985).area / (10**6)

tabela =pd.read_csv(
    r"/home/joao/JampaPy/ProjetoJampa/Etapa3/tabela_bairros_jampa.csv", 
    sep=";",
    header=None,
    names=["bairros_seco", "populacao"]
    )

tabela["NM_BAIRRO"] = tabela["bairros_seco"].str.split(" - ").str[0].str.strip()

tabela_limpa = tabela[["NM_BAIRRO", "populacao"]]

tabela_completa = bairros.merge(tabela_limpa, on="NM_BAIRRO")
tabela_completa["densidade"] = tabela_completa["populacao"] / tabela_completa["Area em Km²"]
tabela_completa["Area em Km²"] = tabela_completa["Area em Km²"].round(2)
tabela_completa["densidade"] = tabela_completa["densidade"].round(2)

tabela_completa.to_file("bairros_densidade_jampa.geojson" , driver="GeoJSON")

tabela_completa_ordernada = tabela_completa.sort_values(by="densidade", ascending=False)
# print(tabela_limpa.head(10))
# print(bairros[["NM_BAIRRO", "Area em Km²"]].head(10))
print(tabela_completa_ordernada[["NM_BAIRRO", "Area em Km²", "densidade"]].head(10))

