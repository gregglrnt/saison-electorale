from datetime import datetime
from fastapi import APIRouter, HTTPException

from db.communes.get import get_all_communes, get_results_election
from db.elections.get import get_election_by_date
from db.meteo.get import get_meteo_by_station_by_day


compare = APIRouter(
    prefix="/compare"
)

@compare.get("/all/{date_str}")
async def get_all_data_from_date(date_str: str, page: int = 0):
    try: 
        day = datetime.strptime(date_str, "%Y-%m-%d")
    except: 
        raise HTTPException(status_code=404, detail="You should use date format Y-m-d")
    
    #get all communes with stations
    (count, communes) = await get_all_communes(page, withStation=True)
    election = await get_election_by_date(day)
    if(election == None):
        raise HTTPException(status_code=404, details=f"No election on {day}")
    
    res = []
    
    for commune in communes:
        weather = await get_meteo_by_station_by_day(commune.closer_station.id, date=day)
        results = await get_results_election(commune.code, election)
        
        res.append({
            "commune": commune.code,
            "label": commune.label,
            "weather": weather,
            "results": results,
        })
    
    return {
        "election": election,
        "page": page,
        "total_items": count,
        "communes": res,
    }
        
        
    
    #get meteo per day for all communes
    
    #get ballots from communes for specific day
        
    
    #return only 
        

## batch all meteo records by election
## and return
