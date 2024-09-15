from client import Client
from functions import current_conditions,get_coordinates,air_quality_tile
from pathlib import Path
import os
import leafmap.foliumap as leafmap
import folium

GOOGLE_MAPS_API_KEY = your_api
# set up client
client = Client(key=GOOGLE_MAPS_API_KEY)
# a location in Los Angeles, CA
location = "santorini"
location = get_coordinates(location)

# a JSON response
print(location)
current_conditions_data = current_conditions(
  client,
  location,
  include_health_suggestion=True,
  include_additional_pollutant_info=True
)

zoom = 7
tiles = air_quality_tile(
    client,
    location,
    pollutant="UAQI_INDIGO_PERSIAN",
    zoom=zoom,
    get_adjoining_tiles=False)




lat = location["latitude"]
lon = location["longitude"]

map = leafmap.Map(location=[lat, lon], tiles="OpenStreetMap", zoom_start=zoom)

for tile in tiles:
  latmin, latmax, lonmin, lonmax = tile["bounds"]
  AQ_image = tile["image"]
  folium.raster_layers.ImageOverlay(
    image=AQ_image,
    bounds=[[latmin, lonmin], [latmax, lonmax]],
    opacity=0.7
  ).add_to(map)

location = "mykonos"
location = get_coordinates(location)

zoom = 7
tiles = air_quality_tile(
    client,
    location,
    pollutant="UAQI_INDIGO_PERSIAN",
    zoom=zoom,
    get_adjoining_tiles=False)


lat = location["latitude"]
lon = location["longitude"]

for tile in tiles:
  latmin, latmax, lonmin, lonmax = tile["bounds"]
  AQ_image = tile["image"]
  folium.raster_layers.ImageOverlay(
    image=AQ_image,
    bounds=[[latmin, lonmin], [latmax, lonmax]],
    opacity=0.7
  ).add_to(map)

location = "athens"
location = get_coordinates(location)

zoom = 7
tiles = air_quality_tile(
    client,
    location,
    pollutant="UAQI_INDIGO_PERSIAN",
    zoom=zoom,
    get_adjoining_tiles=False)


lat = location["latitude"]
lon = location["longitude"]

for tile in tiles:
  latmin, latmax, lonmin, lonmax = tile["bounds"]
  AQ_image = tile["image"]
  folium.raster_layers.ImageOverlay(
    image=AQ_image,
    bounds=[[latmin, lonmin], [latmax, lonmax]],
    opacity=0.7
  ).add_to(map)

output_path = "kyklades_air_quality_map.html"
map.save(output_path)
print(f"Map saved to {output_path}")
