import datetime
from ..main import prisma

async def get_election(election_type: str, round: 1 | 2):
    return await prisma.election.find_first(where={
            "type": election_type.upper(),
            "round": round,
        })
    
async def get_election_by_date(date: datetime):
    return await prisma.election.find_first(where={
        "date": date
    })
    
async def get_elections():
    return await prisma.election.find_many()