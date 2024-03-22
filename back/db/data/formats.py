from typing import List, TypedDict

class Format(TypedDict):
    dep_code: int
    com_code: int
    abst: int
    voters: int
    invalid: int | List[int]
    
format_2012_leg = Format(dep_code=0, com_code=4, abst=8, voters=10, invalid=12)
format_2012_pres = Format(dep_code=0, com_code=2, abst=6, voters=8, invalid=11)
format_2015 = Format(dep_code=1, com_code=5, abst=9, voters=11, invalid=[13, 16])
format_2014_muni = Format(dep_code=1, com_code=4, abst=8, voters=10, invalid=12)
format_2014_euro = Format(dep_code=1, com_code=4, abst=8, voters=10, invalid=[12, 15])
format_2017 = Format(dep_code=0, com_code=2, abst=6, voters=8, invalid=[10, 13])
format_2021_reg = Format(dep_code=0, com_code=3, abst=7, voters=9, invalid=[11, 14])
format_2021_dep = Format(dep_code=0, com_code=4, abst=8, voters=10, invalid=[12, 15])
format_2022 = Format(dep_code=0, com_code=2, abst=7, voters=9, invalid=[11, 14])
format_2015_reg = Format(dep_code=1, com_code=3, abst=7, voters=9, invalid=[12, 14])
format_2022_leg1 = Format(dep_code=0, com_code=4, abst=9, voters=11, invalid=[13, 16])

