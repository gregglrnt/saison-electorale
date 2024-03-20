
import csv
import os
from prisma.models import Meteo, Station

csv_files = [file for file in os.listdir("../../data/meteo") if file.endswith(".csv")]

columns = [0, 1, 6, 7, 9, 14, 35, 38, 59, 64, 73, 74]

def set_float_or_null(value : str) -> float | None:
    try:
        return float(value)
    except:
        return None

async def create_meteo_station(id: str, coordinates: str, commune: str, zip: str) -> Station:
    station = await Station.prisma().find_unique(where={
        "id":id
    })
    if(station == None):
        station = await Station.prisma().create(data={
            "coordinates": coordinates,
            "commune": commune,
            "zip": zip,
            "id": id,
        })
    return station
    

async def add_meteo_record(row: list[str]):
    try:
        station = await create_meteo_station(row[0], row[8], row[10], row[11])
        await Meteo.prisma().create(data={
            "date": row[1],
            'wind_speed': set_float_or_null(row[2]),
            'temperature_kelvin': set_float_or_null(row[3]),
            'humidity': set_float_or_null(row[4]),
            'cloudiness': set_float_or_null(row[5]),
            'ice_height': set_float_or_null(row[6]),
            'rain': set_float_or_null(row[7]),
            'temperature_celsius': set_float_or_null(row[9]),
            "station": {
                "connect": {
                    "id": station.id
                }
            }
        })
    except: 
        print("fail", row[1], station.id)
    

async def seed_meteo():
    for csv_file in csv_files:
        path = os.path.join("../../data/meteo", csv_file)
        print(csv_file)
        with open(path, "r") as file:
            csvreader = csv.reader(file, delimiter=";")
            next(csvreader)
            for _ in range(10):
                row = next(csvreader)
                values = [row[pos] for pos in columns]
                await add_meteo_record(values)