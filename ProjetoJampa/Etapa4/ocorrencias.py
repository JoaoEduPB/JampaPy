import pandas as pd
import numpy as np

df_jampa = pd.read_csv(
    "../Etapa3/tabela_bairros_jampa.csv",
    sep=";",
    names=["bairros_seco", "populacao"],
    header=None)

df_jampa["NM_BAIRRO"] = df_jampa["bairros_seco"].str.split(' - ').str[0].str.strip()
ancoras_reais ={
    "Bessa":2,"Jardim Oceania": 2,"Alto do Céu": 4,"Ipês": 3,
    "Estados": 3,"Tambaú": 3,"Miramar": 1,"Manaíra": 0,
    "Roger": 1,"Torre": 0,"Centro": 6,"Castelo Branco": 1,
    "Cabo Branco": 2,"Bancarios": 1,"Portal do Sol": 3,"Jardim Cidade Universitária": 2,
    "Mangabeira": 12,"Penha": 0,"Costa do Sol": 6,"Barra de Gramame": 8,
    "Paratibe": 0,"Valentina": 3,"Cuiá": 1,"Gramame": 50,
    "Grotão": 2,"João Paulo II": 0,"Cristo Redentor": 25,"Varjão": 13,
    "Jaguaribe": 4,"Ilha do Bispo": 11,"Oitizeiro": 3,"Jardim Veneza": 3,
    "Distrito Industruial": 1,"Mussuré": 0,"Mumbaba": 2

}
calculo_estimado = (df_jampa["populacao"] / 10000 * 1.2).round()
df_jampa["ocorrencias"] = df_jampa['NM_BAIRRO'].map(ancoras_reais).fillna(calculo_estimado)
df_jampa[["NM_BAIRRO", "ocorrencias"]].to_csv("ocorrencias_jampa.csv", index=False, sep=";")

# print(df_jampa[["NM_BAIRRO", "ocorrencias"]].head(5))
print(df_jampa.sort_values(by="ocorrencias", ascending=False))

