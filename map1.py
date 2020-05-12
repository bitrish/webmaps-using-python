import folium
import pandas
data=pandas.read_csv("volcano2.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])
def color_producer(elevation):
    if elevation <1000:
        return 'green'
    else:
        return 'blue'

map=folium.Map(location=[-23,56],zoom_start=6,tiles="Stamen Terrain")
fg1=folium.FeatureGroup(name="Volcano")
for lt,ln,el in zip(lat,lon,elev):
    fg1.add_child(folium.CircleMarker(location=[lt,ln],radius=6,popup=str(el),fill_color=color_producer(el),color='grey',fill_opacity=0.6))
    fg2=folium.FeatureGroup(name="population")
fg2.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
style_function =lambda x: {'fillColor':'red' if x['properties']['POP2005']<2000000 else 'green'}))

map.add_child(fg1)
map.add_child(fg2)
map.add_child(folium.LayerControl())
map.save("map3.html")
