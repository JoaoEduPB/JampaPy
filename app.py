import streamlit as st
import pandas as pd
import geopandas as gpd
import folium
from streamlit_folium import st_folium
import plotly.express as px

st.set_page_config(
    page_title="Dashboard CVLI João Pessoa",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Painel Interativo de Segurança Pública -João Pessoa / PB")
st.markdown("Análise espacial e estatítica de taxa de CVLI por 10.000 habitantes nos 64 bairros da capital")

@st.cache_data
def carreagr_dados():
    df = pd.read_csv("ProjetoJampa/Etapa5/tabela_final_jampa.csv", sep=";")
    gdf = gpd.read_file("ProjetoJampa/Etapa2/bairros_jampa.geojson")
    gdf = gdf[["NM_BAIRRO", "geometry"]].merge(df, on="NM_BAIRRO")
    return df, gdf

df , gdf = carreagr_dados()

st.sidebar.header("🔍 Filtros de Pesquisa")
taxa_max = float(df["TAXA_10K"].max())

faixa_taxa = st.sidebar.slider(
    "Filtrar por Faixa de Taxa (por 10k hab):",
    min_value=0.0,
    max_value=taxa_max,
    value=(0.0, taxa_max)
)

df_filtrado = df[(df["TAXA_10K"] >= faixa_taxa[0]) & (df["TAXA_10K"] <= faixa_taxa[1])]
gdf_filtrado = gdf[gdf["NM_BAIRRO"].isin(df_filtrado["NM_BAIRRO"])]

col1, col2, col3, col4 = st.columns(4)
col1.metric("Bairros Exibidos", len(df_filtrado))
col2.metric("Total de Ocorrências", int(df_filtrado["ocorrencias"].sum()))
col3.metric("População Coberta", f"{int(df_filtrado['populacao'].sum()):,}".replace(",", "."))
col4.metric("Média da Taxa/10k", f"{df_filtrado['TAXA_10K'].mean():.2f}")

st.markdown("---")

col_mapa, col_grafico = st.columns([1.2, 1])

with col_mapa:
    st.subheader("🗺️ Mapa Coroplético")
    
    mapa = folium.Map(
        location=[-7.115, -34.863],
        zoom_start=11,
        tiles="https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer/tile/{z}/{y}/{x}",
        attr="Tiles &copy; Esri"
    )

    faixas_cores = [0, 1, 2, 4, 8, 20, 100]

    folium.Choropleth(
        geo_data=gdf_filtrado,
        name="choropleth",
        data=gdf_filtrado,
        columns=["NM_BAIRRO", "TAXA_10K"],
        key_on="feature.properties.NM_BAIRRO",
        fill_color="YlOrRd",
        fill_opacity=0.7,
        line_opacity=0.4,
        bins=faixas_cores,
        legend_name="Taxa por 10k hab."
    ).add_to(mapa)

    tooltip = folium.features.GeoJsonTooltip(
        fields=["NM_BAIRRO", "populacao", "ocorrencias", "TAXA_10K"],
        aliases=["Bairro:", "População:", "Ocorrências:", "Taxa/10k:"],
        localize=True,
        sticky=True
    )

    folium.GeoJson(
        gdf_filtrado,
        style_function=lambda x: {'fillColor': '#00000000', 'color': '#000000', 'weight': 0.5},
        highlight_function=lambda x: {'fillColor': '#000000', 'color': '#000000', 'fillOpacity': 0.2, 'weight': 1.5},
        tooltip=tooltip
    ).add_to(mapa)

    # Renderiza o mapa Folium dentro do Streamlit
    st_folium(mapa, width=580, height=480)

with col_grafico:
    st.subheader("📊 Top Bairros por Taxa de CVLI")
    top_n = st.slider("Selecione o tamanho do Ranking:", 5, 20, 10)
    
    df_top = df_filtrado.sort_values(by="TAXA_10K", ascending=False).head(top_n)
    
    fig = px.bar(
        df_top,
        x="TAXA_10K",
        y="NM_BAIRRO",
        orientation="h",
        text="TAXA_10K",
        color="TAXA_10K",
        color_continuous_scale="Reds",
        labels={"TAXA_10K": "Taxa / 10k hab", "NM_BAIRRO": "Bairro"}
    )
    fig.update_layout(yaxis=dict(autorange="reversed"), showlegend=False, height=430)
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# 6. Tabela Interativa de Dados
st.subheader("📋 Tabela Completa de Dados")
st.dataframe(
    df_filtrado.sort_values("TAXA_10K", ascending=False)[["NM_BAIRRO", "populacao", "ocorrencias", "TAXA_10K"]],
    use_container_width=True
)