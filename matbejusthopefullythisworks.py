import pandas as pd
import folium
import certifi

location = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_week.csv"
earthquake_locations = pd.read_csv(location)
earthquake_locations = earthquake_locations[["latitude", "longitude", "mag"]]

mapp = folium.Map(location=[earthquake_locations.latitude.mean(), earthquake_locations.longitude.mean()])

for location_info in earthquake_locations.iterrows():
    folium.Marker([location_info["latitude"], location_info["longitude"]], popup=location_info["mag"]).add_to(mapp)

mapp.save(hopefullythisworks.html)