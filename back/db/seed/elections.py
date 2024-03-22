import csv
import os

from data.formats import Format, format_2012_leg, format_2012_pres, format_2021_dep, format_2021_reg, format_2015, format_2014_muni, format_2014_euro, format_2017, format_2022, format_2015_reg, format_2022_leg1
from elections.create import create_from_csv, create_result
data_path = "../../data/scrutins"

def tofloat(txt: str):
    if(isinstance(txt, str)):
        txt = txt.replace(",", ".")
    return float(txt)
    

async def seed_election(path: str, format: Format, separator=","):
    csv_files = [file for file in os.listdir(data_path + path) if file.endswith(".csv")]
    for file_name in csv_files:
        electionId = await create_from_csv(file_name)
        csv_file = os.path.join(data_path + path, file_name)
        with open(csv_file, "r") as file:
            csv_reader = csv.reader(file, delimiter=separator)
            next(csv_reader)
            for _ in range(500): 
                row = next(csv_reader)
                code= row[format["dep_code"]].zfill(2) + row[format["com_code"]].zfill(3)
                if isinstance(format["invalid"], list):
                    invalid = 0
                    for i in format["invalid"]:
                        invalid += tofloat(row[i])
                else:
                    invalid = row[format["invalid"]]
                await create_result(code=code, abs=tofloat(row[format["abst"]]), voters=tofloat(row[format["voters"]]), invalid=tofloat(invalid), election=electionId)
 

    
async def seed_election_all():
    print("seeding elections and results.... ")
    all_formats = [('/dep_2021', format_2021_dep, ","),
            ('/euro_2014', format_2014_euro, ","),
            ('/format_2015', format_2015, ","),
            ('/format_2017', format_2017, ","),
            ('/format_2022', format_2022, ","), 
            ('/leg_2012', format_2012_leg, ","),
            ('/muni_2014', format_2014_muni, ";"),
            ('/pres_2012', format_2012_pres, ","),
            ('/reg_2021', format_2021_reg, ","),
            ('/reg_2015', format_2015_reg, ","),
            ('/leg_1_2022', format_2022_leg1, ",")
            ]
    for t in all_formats:
        await seed_election(path=t[0], format=t[1], separator=t[2])
        # verify_format(format=t[1], path=t[0], separator=t[2])