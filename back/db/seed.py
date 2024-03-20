import asyncio
from prisma import Prisma
from seed.meteo import seed_meteo
from seed.communes import seed_communes
from seed.elections import seed_election_1


async def main() -> None:
    db = Prisma(auto_register=True)
    await db.connect()
    await seed_meteo()
    await seed_communes()
    await seed_election_1()
    await db.disconnect()

if __name__ == '__main__':
    asyncio.run(main())