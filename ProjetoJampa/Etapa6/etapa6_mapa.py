import folium
import pandas as pd
import geopandas as gpd

gdf = gpd.read_file("../Etapa3/bairros_densidade_jampa.geojson")
df = pd.read_csv("../Etapa5/tabela_final_jampa.csv", sep=";")

gdf = gdf[["NM_BAIRRO", "geometry"]].merge(df, on="NM_BAIRRO")

mapa = folium.Map(
    location=[-7.115, -34.863], zoom_start=12, 
    tiles="https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer/tile/{z}/{y}/{x}",
    attr="Tiles &copy; Esri"
    )

#Desenhar contornos dos bairros
faixas_cores = [0, 1, 2, 4, 8, 20, 100]

folium.Choropleth(
    geo_data=gdf,
    name="choropleth",
    data=gdf,
    columns=["NM_BAIRRO", "TAXA_10K"],
    key_on="feature.properties.NM_BAIRRO",
    fill_color= "YlOrRd",
    fill_opacity=0.7,
    line_opacity=0.4,
    bins=faixas_cores,
    legend_name="Taxa de CVLI por 10.000 Habitantes"
    
).add_to(mapa)

tooltip = folium.features.GeoJsonTooltip(
    fields=["NM_BAIRRO", "populacao", "ocorrencias", "TAXA_10K"],
    aliases=["Bairro:", "População:", "Ocorrências:", "Taxa/10k:"],
    localize=True,
    sticky=True
)

folium.GeoJson(
    gdf,
    style_function=lambda x: {'fillColor': '#00000000', 'color': '#000000', 'weight': 0.5},
    highlight_function=lambda x: {'fillColor': '#000000', 'color': '#000000', 'fillOpacity': 0.2, 'weight': 1.5},
    tooltip=tooltip
).add_to(mapa)

mapa.save("mapa_jampa.html")