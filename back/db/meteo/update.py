from typing import List
from prisma.models import Commune, Station
from geopy.distance import distance

def convert_coordinates(txt: str):
    return tuple(map(lambda x: float(x), txt.split(",")))

def get_closer_station(coord: tuple, other: List[Station]):
    try : 
        closer_station = other[0]
        station_distance = float('inf')
        for station in other:
            location = convert_coordinates(station.coordinates)
            dist = distance(coord, location).kilometers
            if(dist < station_distance):
                closer_station = station
                station_distance = dist
        return closer_station
    except: 
        print("Could not find a closer station")

async def get_nearby_stations(coord):
    lon = int(coord[0])
    lat = int(coord[1])
    res = await Station.prisma().find_many(where={
        'OR': [
            {'coordinates': {
                'startswith': str(lon)
            }}, 
            {'coordinates': {
                'contains': ", " + str(lat)
            }}
        ]
    })
    return res
    
        

async def link_station_to_communes(commune: Commune):
    has_station = await Station.prisma().find_first(where={
        "zip":commune.zip
    })
    if(has_station):
        await Commune.prisma().update({"closer_station": {"connect": {"id": has_station.id}}}, where={"code": commune.code})
        return
    
    coord = convert_coordinates(commune.centroid)

    closer_stations = await get_nearby_stations(coord)
    
    res = get_closer_station(coord, closer_stations)
    
    if(res):
        await Commune.prisma().update({"closer_station": {"connect": {"id": res.id}}}, where={"code": commune.code})
    else:
        print(f"Commune {commune.code} could not be linked to station")
        
async def seed_stations_to_communes():
    coms = await Commune.prisma().find_many()
    for c in coms:
        await link_station_to_communes(c)