
from prisma.models import Commune, Election
from ..main import prisma

#TODO: implement with filters
async def get_all_communes(page:int):
    count = await prisma.commune.count();
    all = await prisma.commune.find_many(take=20, skip=page*20)
    return (count, all)

async def get_commune(code: str):
    commune = await prisma.commune.find_unique(where={
        "code": code,
    }, include={"closer_station": True})
    if(commune == None):
        raise Exception("Not exists")
    return commune
    
    
async def get_results_election(communeId: str, ballot: Election):
    return await prisma.results.find_unique(where={
        "ballotId_communeId": {
            "ballotId": ballot.id,
            "communeId": communeId,
        }
    }, include={
        "ballot": True
    })