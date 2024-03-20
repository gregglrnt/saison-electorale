
from datetime import datetime
from fastapi import APIRouter, HTTPException
from db.elections.get import get_election, get_election_by_date
from db.communes.get import get_all_communes, get_commune, get_results_election
from db.meteo.get import get_meteo_by_station_by_day


router = APIRouter(
    prefix="/commune"
)

@router.get("/all")
async def get_communes(page : int = 0):
    [count, items] = await get_all_communes(page)
    return {
        "page": page, 
        "total": count,
        "items": items
    }

@router.get("/{code}/meteo/{date_str}")
async def get_self_meteo_date(code: str, date_str: str):
    #date must be Y-m-d
    try: 
        datetime.strptime(date_str, "%Y-%m-%d")
    except:
        raise HTTPException(status_code=404, detail=f"Date should be in format Y-m-d")
    try: 
        commune = await get_commune(code)
    except:
        raise HTTPException(status_code=404, detail= f"Commune {code} does not exists !")
    
    print(commune)
    
    meteo = await get_meteo_by_station_by_day(date=date_str, stationId=commune.closer_station.id) 
    
    return {
        "commune": commune.label,
        "meteo": meteo
    }
    
@router.get("/{code}/election/{election}/{round}")
async def get_results_by_election(code: str, election: str, round: int = 1):
    try:
        election = await get_election(election, round)
        print(election)
        return await get_results_election(code, election)
    except Exception as e:
        print(e)

@router.get("/{code}/election/{date}")
async def get_results_by_date(code: str, date: str):
    try:
        day = datetime.strptime(date, "%Y-%m-%d")
    except:
        raise HTTPException(status_code=404, detail="You should use date format Y-m-d")
    try:
        election = await get_election_by_date(day)
        return await get_results_election(code, election)
    except Exception as e:
        print(e)