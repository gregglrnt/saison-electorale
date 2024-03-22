import csv
from datetime import datetime
import os
from db.data.formats import Format
data_path = "../../data/scrutins"


def verify_format(path: str, format: Format, separator: str):
    print("%--------------------- FORMAT ", path, "--------------------------%")
    csv_files = [file for file in os.listdir(data_path + path) if file.endswith(".csv")]
    for file_name in csv_files:
        print("----", file_name)
        [date_str, election] = file_name.removesuffix(".csv").split("_")
        date = datetime.strptime(date_str, "%Y-%m-%d")
        [election_type, election_round, *_] = election.split("-")
        print(election_type, election_round, date)
        
        csv_file = os.path.join(data_path + path, file_name)
        with open(csv_file, "r") as file:
            csv_reader = csv.reader(file, delimiter=separator)
            header = next(csv_reader)
            # print([format.get(pos) for pos in format])
            for pos in format:
                if(isinstance(format.get(pos), list)):
                    for f in format.get(pos):
                        print(header[f], end = " ")
                else: 
                    print(header[format[pos]], end=" ")
        print("")
          