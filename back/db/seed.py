import asyncio
import csv
import os
from prisma import Prisma
from prisma.models import Meteo

meteo_path = "../../data/meteo"

csv_files = [file for file in os.listdir(meteo_path) if file.endswith(".csv")]

columns = [0, 1, 6, 7, 9, 14, 35, 38, 59, 64, 73, 74]

def set_float_or_null(value : str) -> float | None:
    try:
        return float(value)
    except:
        return None


async def extract_data_from_meteo(csv_file):
    with open(csv_file, "r") as file:
        csvreader = csv.reader(file, delimiter=";")
        # data = list(csvreader)
        # header = data[0]
        # data = data[1:]
        # print("Values in", [header[pos] for pos in columns])
        next(csvreader)
        for _ in range(10):
            row = next(csvreader)
            values = [row[pos] for pos in columns]
            print(values)
            await Meteo.prisma().create(
                data={
                    'stationId': values[0],
                    'date': values[1],
                    'wind_speed': set_float_or_null(values[2]),
                    'temperature_kelvin': set_float_or_null(values[3]),
                    'humidity': set_float_or_null(values[4]),
                    'cloudiness': set_float_or_null(values[5]),
                    'ice_height': set_float_or_null(values[6]),
                    'rain': set_float_or_null(values[7]),
                    'coordinates': values[8],
                    'temperature_celsius': set_float_or_null(values[9]),
                    'commune': values[10],
                    'zip': values[11]
                }
            )
    

async def main() -> None:
    db = Prisma(auto_register=True)
    await db.connect()
    #await extract_data_from_meteo(os.path.join(meteo_path, csv_files[0]))
    await db.disconnect()

if __name__ == '__main__':
    asyncio.run(main())