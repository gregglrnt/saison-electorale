
import csv

from prisma.models import Commune

commune_data_path = "../../data/communes/"

async def seed_communes():
    print("seeding communes....")
    with open(commune_data_path + "/insee_codes.csv", 'r') as file:
        csvreader = csv.reader(file, delimiter=';')
        next(csvreader)
        for row in csvreader:
            code= row[15].zfill(2) + row[12].zfill(3)
            exists = await Commune.prisma().find_unique(where={"code": code})
            if exists:
                continue
            try: 
                await Commune.prisma().create({
                "code": code,
                "label": row[2],
                "departement": row[3].replace("[", "").replace("]", "").replace('"', ""),
                "centroid": row[9],
                "insee_code": row[0],
                "zip": row[1]
            })
            except:
                print(f"Not creating {code}")
