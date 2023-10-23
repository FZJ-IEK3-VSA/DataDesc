from audioop import mul
import dataclasses
from enum import Enum
import string
from typing import Dict, List, Optional
import pandas as pd

from dataclasses_json import LetterCase, dataclass_json  # type: ignore

from xattr.xattr import xattr

@dataclass_json
@dataclasses.dataclass
@xattr(xattr={
    "Value" : [("currency", "euro"),
                ("toUSD", 1.1)],
    "Time" : ("format", "YYYY-mm-dd")
    })
class MyMonetaryClass:
    """This is a simple monetary class"""
    Value: int
    Time: str

@dataclass_json
@dataclasses.dataclass
@xattr(xattr={
     "PowerMeasurement" : (
        "dimensions", 
        {
            "location_of_measurement" : {
                    "unit_type": "location", 
                    "unit": "country name"
                },
            "time_of_measurement" : {
                    "unit_type": "time", 
                    "unit": "days since 1895-01-01"
                }
        }
        ),
     "subtract_value" : [ 
            {
                "minuend" : [
                    ("domain", "real")
                    ],
                "subtrahend" : [
                    ("domain", "real")
                    ],
            }
        ]
     })
class PowerOutputCalculator:
    """This is a simple calculator class"""
    PowerMeasurement: pd.DataFrame

    def subtract_value(self, minuend : int, subtrahend : int):
        difference = minuend - subtrahend
        return difference