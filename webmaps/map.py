import folium
import pandas

data_frame = pandas.read_csv("volcanos.csv")
lat = list(data_frame["LAT"])
lon = list(data_frame["LON"])
elevation = list(data_frame["ELEV"])
names = list(data_frame["NAME"])

map = folium.Map(location=[38.58, -99.09],
                 zoom_start=4, tiles='cartodbdark_matter')

feature_group = folium.FeatureGroup(name="Map")


def color(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


for lt, lg, elev, name in zip(lat, lon, elevation, names):
    feature_group.add_child(folium.Marker(location=[lt, lg],
                                          popup=[name, elev],
                                          icon=folium.Icon(color(elev))))

geo = open('world.geojson', 'r', encoding='utf-8-sig').read()
feature_group.add_child(folium.GeoJson(data=geo))

map.add_child(feature_group)
map.save('index.html')
