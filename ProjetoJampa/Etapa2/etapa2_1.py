import geopandas as gpd

gdf = gpd.read_file("etapa2jamp.geojson")

gdf_utm = gdf.to_crs(epsg=31985)

area_km = gdf_utm.area / (10**6)

print(f"Area de João Pessoa em KM²: {area_km.iloc[0]:.2f}")