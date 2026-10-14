import pandas as pd
# import geopandas as gpd

ocorrencias = pd.read_csv(
    "../Etapa4/ocorrencias_jampa.csv",
    sep=";",  
)

pop_bairros = pd.read_csv(
    "../Etapa3/tabela_bairros_jampa.csv",
    sep=";",
    header=None,
    names=["bairros", "populacao"]
)

pop_bairros["NM_BAIRRO"] = pop_bairros["bairros"].str.split(" - ").str[0].str.strip()

censo = pop_bairros.merge(ocorrencias, on="NM_BAIRRO")
censo["TAXA_10K"] = ((censo["ocorrencias"] / censo["populacao"]) * 10000).round(2)

# print(censo[["NM_BAIRRO", "populacao", "ocorrencias", "TAXA_10K"]].sort_values(by="TAXA_10K", ascending=False).head(5))
colunas_finais = ["NM_BAIRRO", "populacao", "ocorrencias", "TAXA_10K"]
censo.sort_values(by="TAXA_10K", ascending=False)[colunas_finais].to_csv(
    "tabela_final_jampa.csv", index=False, sep=";"
    )
