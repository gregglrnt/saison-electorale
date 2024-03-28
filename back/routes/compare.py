from datetime import datetime
import json
from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder

from db.communes.get import get_abstention_election, get_all_communes, get_commune_and_scores, get_results_election
from db.elections.get import get_election_by_date
from db.meteo.get import get_meteo_by_station_by_day
from utils.meteo import get_weather_status


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
    election = await get_election_by_date(day)
    if(election == None):
        raise HTTPException(status_code=404, details=f"No election on {day}")
    
    (count, results) = await get_commune_and_scores(page=page, ballot=election)
    
    all = []
    
    for res in results:
        try:
            abs = res.Results[0].abstention
        except: 
            abs = None
        try: 
            meteo = res.closer_station.Meteo[0]
        except: 
            meteo = None
        all.append({
            "commune": res.label,
            "code": res.code,
            "centroid": res.centroid,
            "geojson": res.geojson,
            "abstention": abs,
            "weather_status": get_weather_status(meteo),
            "weather": meteo
        })
    
    return {"page": page, "total_pages": round(count / 500), "date": election.date, "communes": all};
