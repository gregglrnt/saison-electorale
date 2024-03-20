from enum import Enum
from typing import TypedDict

# _format = dict(dep_code= 0, com_code=0, abs=0, vot=0, inv= 0)
class Format(TypedDict):
    dep_code: int
    com_code: int
    abst: int
    voters: int
    invalid: int
    
format_2012_leg = Format(dep_code=0, com_code=4, abst=8, voters=10, invalid=12)
format_2012_pres = Format(dep_code=0, com_code=2, abst=6, voters=8, invalid=11)

    
# class Format2012(_Format):
#     DEP_CODE=0,
#     COM_CODE=3,
#     ABS=6,
#     VOT=8,
#     INV=11

# class Format2015(_Format):
#     DEP_CODE = 0,
#     COM_CODE = 4,
#     ABS = 10,
#     VOT = 12,
#     INV = 13
    