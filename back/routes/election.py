
from datetime import datetime
from fastapi import APIRouter, HTTPException

from db.elections.get import get_election_by_date, get_elections


election = APIRouter(prefix="/election")

@election.get("/all")
async def get_all_elections():
    return await get_elections()

@election.get("/{date_str}")
async def get_election_on(date_str: str):
    try:
        day = datetime.strptime(date_str, "%Y-%m-%d");
    except:
        raise HTTPException(status_code=404, detail="Please use format Y-m-d for your date")
    return await get_election_by_date(day)
    