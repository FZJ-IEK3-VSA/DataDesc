from typing import Annotated
import pandas as pd

class MyMonetaryClass:
    """This is a simple monetary class"""
    Value: Annotated[int, {"currency" : "euro", "toUSD" : 1.1}]
    Time: Annotated[str, {"format" : "YYYY-mm-dd"}]

class PowerOutputCalculator:
    """This is a simple calculator class"""
    PowerMeasurement: Annotated[pd.DataFrame, {
                                                "dimensions" : [ 
                                                    {
                                                        "identifier" : "location_of_measurement",
                                                        "properties" : 
                                                        [
                                                            {
                                                                "identifier" : "location",
                                                                "type" : "string",
                                                                "description" : "The location of the measurement",
                                                                "unit" : "country name"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "identifier" : "time_of_measurement",
                                                        "properties" : 
                                                        [
                                                            {
                                                                "identifier" : "time",
                                                                "type" : "string",
                                                                "description" : "The location of the measurement",
                                                                "unit" : "days since 1895-01-01"
                                                            }
                                                        ]
                                                    }
                                                ],
                                                "properties" : {
                                                    "identifier" : "T2M",
                                                    "type" : "number",
                                                    "properties" : 
                                                    [
                                                        {
                                                            "identifier" : "long_name",
                                                            "type" : "string",
                                                            "example" : "2 meter air temperature"
                                                        }
                                                    ],
                                                    "unit" : "K",
                                                    "dimensions" : [ "lat", "lon", "time" ]
                                                }
                                            },
                                            
                                        ]

    def subtract_value(self, minuend : Annotated[int, {"domain" : "real"}], subtrahend : Annotated[int, {"domain" : "real"}]):
        difference = minuend - subtrahend
        return difference
    
    def process_pm(self, pm : Annotated[pd.DataFrame, {
                                                "dimensions" : [ 
                                                    {
                                                        "identifier" : "location_of_measurement",
                                                        "properties" : 
                                                        [
                                                            {
                                                                "identifier" : "location",
                                                                "type" : "string",
                                                                "description" : "The location of the measurement",
                                                                "unit" : "country name"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "identifier" : "time_of_measurement",
                                                        "properties" : 
                                                        [
                                                            {
                                                                "identifier" : "time",
                                                                "type" : "string",
                                                                "description" : "The location of the measurement",
                                                                "unit" : "days since 1895-01-01"
                                                            }
                                                        ]
                                                    }
                                                ],
                                                "properties" : [
                                                    {
                                                    "identifier" : "T2M",
                                                    "type" : "number",
                                                    "properties" : 
                                                    [
                                                        {
                                                            "identifier" : "long_name",
                                                            "type" : "string",
                                                            "example" : "2 meter air temperature"
                                                        }
                                                    ],
                                                    "unit" : "K",
                                                    "dimensions" : [ "lat", "lon", "time" ]
                                                }]
                                            },
                                            
                                        ]):
        return pm