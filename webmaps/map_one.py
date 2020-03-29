import folium
import pandas

data_frame = pandas.read_csv("volcanos.csv")
lat = list(data_frame["LAT"])
lon = list(data_frame["LON"])

map = folium.Map(location=[38.58, -99.09],
                 zoom_start=10, tiles='cartodbpositron')

feature_group = folium.FeatureGroup(name="Map")

for lt, lg in zip(lat, lon):
    feature_group.add_child(folium.Marker(location=[lt, lg],
                                          icon=folium.Icon(color='green')))

map.add_child(feature_group)
map.save('Map1.html')
