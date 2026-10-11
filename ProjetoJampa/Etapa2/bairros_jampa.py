import geopandas as gpd

gpf = gpd.read_file(r"PB_bairros_CD2022.gpkg")

cd_mun_jp = "2507507"
df_jampa = gpf[gpf['CD_MUN'] == cd_mun_jp]

df_jampa.to_file("bairros_jampa.geojson", driver="GeoJSON")

df_jampa["Area em Km²"] = df_jampa.to_crs(epsg=31985).area / (10**6)
df_jampa_ordenado = df_jampa.sort_values(by="Area em Km²", ascending=False)
print(df_jampa_ordenado[["NM_BAIRRO", "Area em Km²"]].head(10))

# print(df_jampa.columns)