import asyncio
from main import prisma
from seed.meteo import seed_meteo
from seed.communes import add_geojson, seed_communes
from seed.elections import seed_election_all
from meteo.update import seed_stations_to_communes

async def main() -> None:
    await prisma.connect()
    await seed_meteo()
    await seed_communes()
    await seed_election_all()
    await seed_stations_to_communes()
    await prisma.disconnect()

if __name__ == '__main__':
    asyncio.run(main())