import csv
import os


from elections.create import create_or_get_election, create_result
data_path = "../../data"

csv_files = [file for file in os.listdir(data_path + "/scrutins") if file.endswith(".csv")]
relevant_columns = [0, 4, 5, 8, 10, 13]

async def seed_election_1():
    for file_name in csv_files: 
        election = await create_or_get_election(file_name)
        csv_file = os.path.join(data_path + "/scrutins", file_name)
        
        with open(csv_file, "r") as file:
            csv_reader = csv.reader(file, delimiter=",")
            header = next(csv_reader)
            
            for _ in range(1000): 
                row = next(csv_reader)
                code= row[0].zfill(2) + row[4].zfill(3)
                await create_result(code=code, abs=float(row[8]), voters=float(row[10]), invalid=float(row[12]), election=election)

            # print([row[pos] for pos in relevant_columns])

