from typing import Annotated
import pandas as pd

class MyMonetaryClass:
    """This is a simple monetary class"""
    Value: Annotated[int, {"currency" : "euro", "toUSD" : 1.1}]
    Time: Annotated[str, {"format" : "YYYY-mm-dd"}]

class PowerOutputCalculator:
    """This is a simple calculator class"""
    PowerMeasurement: Annotated[pd.DataFrame, {"dimensions" : {
                                                    "location_of_measurement" : {
                                                        "unit_type": "location", 
                                                        "unit": "country name"
                                                        }, 
                                                    "time_of_measurement" : {
                                                        "unit_type": "time", 
                                                        "unit": "days since 1895-01-01"
                                                        }
                                                }}]

    def subtract_value(self, minuend : Annotated[int, {"domain" : "real"}], subtrahend : Annotated[int, {"domain" : "real"}]):
        difference = minuend - subtrahend
        return difference