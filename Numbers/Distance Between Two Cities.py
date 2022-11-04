"""
Calculates the distance between two cities and allows the user to specify a unit of distance.
This program may require finding coordinates for the cities like latitude and longitude
"""
import math

import geocoder

cityA = geocoder.arcgis(input('Type the first City: '))
print(cityA.json['address'])
cityB = geocoder.arcgis(input('Type the second City: '))
print(cityB.json['address'])
latA = cityA.json['lat']
latB = cityB.json['lat']
lonA = cityA.json['lng']
lonB = cityB.json['lng']


def get_distance(latA, latB, lonA, lonB):
    # use haversine forumla
    earth_rad = 6371.0
    dlat = math.radians(latB - latA)
    dlon = math.radians(lonB - lonA)
    a = math.sin(dlat / 2) * math.sin(dlat / 2) + \
        math.cos(math.radians(latA)) * math.cos(math.radians(latB)) * \
        math.sin(dlon / 2) * math.sin(dlon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return earth_rad * c


dist = get_distance(latA, latB, lonA, lonB)
print(f'{dist:4.2f} km, {dist * 0.621371192:4.2f} miles')
