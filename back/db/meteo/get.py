
from datetime import datetime

from lib.meteo import get_weather_status
from ..main import prisma

async def get_meteo_by_station_by_day(stationId: int, date: str):
    openPolls = datetime.strptime(date, "%Y-%m-%d").replace(hour=0, minute=0)
    closedPolls = datetime.strptime(date, "%Y-%m-%d").replace(hour=23, minute=59)
    weather = await prisma.meteo.find_many(where={
        "AND": [
            {'stationId': stationId},
            {'date': {
                'lte': closedPolls,
                'gte': openPolls,
            }}
        ]
    })
    return list(map(lambda x: {** dict(x), 'status': get_weather_status(x)}, weather))