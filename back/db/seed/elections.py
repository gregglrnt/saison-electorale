import csv
import os

from data.formats import Format, format_2012_leg, format_2012_pres
from elections.create import create_from_csv, create_result
data_path = "../../data/scrutins"


async def seed_election_basic(path: str, format: Format):
    csv_files = [file for file in os.listdir(data_path + path) if file.endswith(".csv")]
    for file_name in csv_files:
        election = await create_from_csv(file_name)
        csv_file = os.path.join(data_path + path, file_name)
        with open(csv_file, "r") as file:
            csv_reader = csv.reader(file, delimiter=",")
            next(csv_reader)
            for _ in range(500): 
                row = next(csv_reader)
                code= row[format["dep_code"]].zfill(2) + row[format["com_code"]].zfill(3)
                await create_result(code=code, abs=float(row[format["abst"]]), voters=float(row[format["voters"]]), invalid=float(row[format["invalid"]]), election=election)

        

async def seed_election_1():
    await seed_election_basic("/pres_2012", format_2012_pres)
        
async def seed_election_2():
    await seed_election_basic("/leg_2012", format_2012_leg)
    
async def seed_election_all():
    await seed_election_1()
    await seed_election_2()
    print("success!")