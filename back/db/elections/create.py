from datetime import datetime
from prisma.models import Election, Results

async def create_or_get_election(filename: str):
        [date_str, election] = filename.removesuffix(".csv").split("_")
        date = datetime.strptime(date_str, "%Y-%m-%d")
        [election_type, election_round] = election.split("-")
        election = await create_election(date, int(election_round), election_type.upper())
        return election.id

async def create_election(date: datetime, election_round: int, election_type: str) -> Election:
    election = await Election.prisma().find_first(where={
        "date": date
    })
    
    if(election == None):
        election = await Election.prisma().create(data={
            "date": date,
            "round": election_round,
            "type": election_type
        })
        
    return election
    
async def create_result(code: str, abs: float, voters: float, invalid: float, election: int):
    try:
        await Results.prisma().create(data = {
            "commune": {
                "connect": {
                    "code": code
                }
            },
            "abstention": abs,
            "voters": voters,
            "invalidVotes": invalid,
            "ballot": {
                "connect": {
                    "id": election
                }
            }
        })
    except Exception as e:
        print("erreur", e, election)