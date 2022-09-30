import folium
import pandas

data=pandas.read_csv("Volcanoes.txt")
lat=list(data["Latitude"])
log=list(data["Longitude"])
brief=list(data["Location"])
Elevat=list(data["Elevation"])
color=["red","blue"]
def color_as(elevation):
    if elevation < 1000:
        return 'green'
    elif elevation < 2000:
        return 'orange'
    else:
        return 'red'
    

map=folium.Map(location=[17.3213, 82.0407 ],zoom_start=5,tiles="Stamen Terrain")
fgp=folium.FeatureGroup(name="Population")
fgv=folium.FeatureGroup(name="Volacanoes")
fgv.add_child(folium.CircleMarker(location=[17.3213, 82.0407],radius=6,popup="Peddi Reddi Sri Vijayakiran",
    fill_color="blue",color='red',fill_opacity = 0.7))
for lt, lg ,br,el in zip(lat,log,brief,Elevat):
    fgv.add_child(folium.CircleMarker(location=[lt,lg],radius=6,popup=br+"Loc",
    fill_color=color_as(el),color='grey',fill_opacity = 0.7))
fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
                            style_function=lambda x:{'fillColor':'yellow' if x['properties']['POP2005']<10000000
                            else 'red'}))
map.add_child(fgp)
map.add_child(fgv)
map.add_child(folium.LayerControl())
map.save("Map1.html")

