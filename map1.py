import folium
import pandas#pandas are used for storing csv or any other type of files effectively
data=pandas.read_csv("volcano2.txt")#read_csv or read_json is used for reading data present in the respective files
lat=list(data["LAT"])#used to store data in lat variable as list type
lon=list(data["LON"])
elev=list(data["ELEV"])
def color_producer(elevation):#function returns color depending on the elevation for each volcano
    if elevation <1000:
        return 'green'
    else:
        return 'blue'

map=folium.Map(location=[-23,56],zoom_start=6,tiles="Stamen Terrain")#map method is used to create a base layer of map 
fg1=folium.FeatureGroup(name="Volcano")
for lt,ln,el in zip(lat,lon,elev):#this loop is used for adding circle marker for each of your volcano which shows elevation on hover
    fg1.add_child(folium.CircleMarker(location=[lt,ln],radius=6,popup=str(el),fill_color=color_producer(el),color='grey',fill_opacity=0.6))#fill color is udes to fill color inside the  circle and color is uded to color the outer radius of thr circle
    
fg2=folium.FeatureGroup(name="population")#CircleMarker AND Marker are method inside the folium library
fg2.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
style_function =lambda x: {'fillColor':'red' if x['properties']['POP2005']<2000000 else 'green'}))

map.add_child(fg1)#it is used to add the feature grop fg1 in your map
map.add_child(fg2)
map.add_child(folium.LayerControl())#it is udes to add a function of showing your map with or without any layer
map.save("map3.html")#after creating and adding it is used to save our file with a name given by the user
