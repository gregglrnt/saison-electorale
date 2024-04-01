
import datetime
from prisma.models import Commune, Election
from ..main import prisma

#TODO: implement with filters
async def get_all_communes(page:int, withStation = False):
    count = await prisma.commune.count();
    all = await prisma.commune.find_many(take=20, skip=page*20, include={"closer_station": withStation})
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
    })
    
async def get_abstention_election(communeId: str, ballot: Election):
    res = await get_results_election(communeId, ballot)
    return {"abstention": res.abstention}
    
async def get_commune_by_text(text: str):
    res = await prisma.commune.find_many(where={
        "label": {
            "startswith": text,
            "mode": "insensitive"
        }
    }, take=20)
    return list(map(lambda r : {"label": r.label, "code": r.code}, res))

async def get_commune_and_scores(page:int, ballot: Election):
    count = await prisma.commune.count()
    openPolls = ballot.date.replace(hour=0, minute=0)
    closedPolls = ballot.date.replace(hour=23, minute=59)
    print(openPolls, closedPolls);
    res = await prisma.commune.find_many(take=500, skip=page*500, include={
        "closer_station": {
            "include": {
                "Meteo" : {
                    "where": {
                        "date": {
                            'lte': closedPolls,
                            'gte': openPolls
                            }
                        }
                    }
                }
            }, 'Results': {
                    "where": {
                        'ballotId': ballot.id    
                    }    
                },
        })
    return (count, res)

async def get_commune_results(code: str):
    return await prisma.commune.find_unique(where={"code": code}, include={
            "Results": {
                "include": {
                    "ballot": 
                        True}},
            "closer_station": {
                "include": {
                    "Meteo": True}}
            });