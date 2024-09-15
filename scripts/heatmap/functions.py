import requests
from tile import TileHelper
import numpy as np

def get_coordinates(location):
    geocoding_url = f'https://maps.googleapis.com/maps/api/geocode/json'
    response = requests.get(geocoding_url, params={'address': location, 'key': "AIzaSyDZtmn2wbMUjS3SaEsXwnTc5q_N1rZZBTs"})
    geocoding_data = response.json()

    if geocoding_data['status'] == 'OK':
        lat_lng = geocoding_data['results'][0]['geometry']['location']
        return {
            "latitude": lat_lng['lat'],
            "longitude": lat_lng['lng']
        }#lat_lng['lat'], lat_lng['lng']
    else:
        print("Geocoding API request failed:", geocoding_data['status'])
        return None, None



def current_conditions(
    client,
    location,
    include_local_AQI=True,
    include_health_suggestion=False,
    include_all_pollutants=True,
    include_additional_pollutant_info=False,
    include_dominent_pollutant_conc=True,
    language=None,
):
    """
    See documentation for this API here
    https://developers.google.com/maps/documentation/air-quality/reference/rest/v1/currentConditions/lookup
    """
    params = {}

    if isinstance(location, dict):
        params["location"] = location
    else:
        raise ValueError(
            "Location argument must be a dictionary containing latitude and longitude"
        )

    extra_computations = []
    if include_local_AQI:
        extra_computations.append("LOCAL_AQI")

    if include_health_suggestion:
        extra_computations.append("HEALTH_RECOMMENDATIONS")

    if include_additional_pollutant_info:
        extra_computations.append("POLLUTANT_ADDITIONAL_INFO")

    if include_all_pollutants:
        extra_computations.append("POLLUTANT_CONCENTRATION")

    if include_dominent_pollutant_conc:
        extra_computations.append("DOMINANT_POLLUTANT_CONCENTRATION")

    if language:
        params["language"] = language

    params["extraComputations"] = extra_computations

    return client.request_post("/v1/currentConditions:lookup", params)


def air_quality_tile(
    client,
    location,
    pollutant="UAQI_INDIGO_PERSIAN",
    zoom=4,
    get_adjoining_tiles = True

):

  # see https://developers.google.com/maps/documentation/air-quality/reference/rest/v1/mapTypes.heatmapTiles/lookupHeatmapTile

  assert pollutant in [
      "UAQI_INDIGO_PERSIAN",
      "UAQI_RED_GREEN",
      "PM25_INDIGO_PERSIAN",
      "GBR_DEFRA",
      "DEU_UBA",
      "CAN_EC",
      "FRA_ATMO",
      "US_AQI"
  ]

  # contains useful methods for dealing the tile coordinates
  helper = TileHelper()

  # get the tile that the location is in
  world_coordinate, pixel_coord, tile_coord = helper.location_to_tile_xy(location,zoom_level=zoom)

  # get the bounding box of the tile
  bounding_box = helper.tile_to_bounding_box(tx=tile_coord[0],ty=tile_coord[1],zoom_level=zoom)

  if get_adjoining_tiles:
    nearest_corner, nearest_corner_direction = helper.find_nearest_corner(location, bounding_box)
    adjoining_tiles = helper.get_ajoining_tiles(tile_coord[0],tile_coord[1],nearest_corner_direction)
  else:
    adjoining_tiles = []

  tiles = []
  #get all the adjoining tiles, plus the one in question
  for tile in adjoining_tiles + [tile_coord]:

    bounding_box = helper.tile_to_bounding_box(tx=tile[0],ty=tile[1],zoom_level=zoom)
    image_response = client.request_get(
        "/v1/mapTypes/" + pollutant + "/heatmapTiles/" + str(zoom) + '/' + str(tile[0]) + '/' + str(tile[1])
    )

    # convert the PIL image to numpy
    try:
      image_response = np.array(image_response)
    except:
      image_response = None

    tiles.append({
        "bounds":bounding_box,
        "image":image_response
    })

  return tiles