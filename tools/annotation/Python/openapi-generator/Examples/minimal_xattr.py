import dataclasses
from enum import Enum
from typing import Dict, List, Optional

from dataclasses_json import LetterCase, dataclass_json  # type: ignore

from xattr.xattr import xattr

#import openapi_generator


class MyEnum(str, Enum):
    ValueA = "ValueA"
    ValueB = "ValueB"
    ValueC = "ValueC"


@dataclass_json
@dataclasses.dataclass
class ExampleClass:
    """This is a simple example class"""
    Id: int = 0
    Text: Optional[str] = ""


@dataclass_json
@dataclasses.dataclass
class MyComplexDataType:
    """This is a complex class with different properties"""

    MyFloat: float = 0

    MyInt: int = 0

    MyString: str = ""

    MyEnumValue: MyEnum = MyEnum.ValueA

    MyOptionalString: Optional[str] = ""

    MySubObject: ExampleClass = None

    MyList: List[float] = dataclasses.field(default_factory=list)  # the 'field' function is a peculiarity of dataclasses for initializing lists or dicts

    MyObjectList: List[ExampleClass] = dataclasses.field(default_factory=list)

    MyDictionary: Dict[str, str] = dataclasses.field(default_factory=dict)

    MyNestedList: Optional[List[List[List[int]]]] = None


@dataclass_json
@dataclasses.dataclass
@xattr(x_attr={
    "Value" : [("currency", "euro"),
                ("toUSD", 1.1)],
    "Time" : ("format", "YYYY-mm-dd")
    })
class MyMonetaryClass:
    """This is a simple monetary class"""
    Value: int
    Time: str

    def __init__(self):
        self.Value = 0
        self.Time = ""

"""
@dataclass_json
@dataclasses.dataclass
class MyMonetaryClass:
    #""This is a simple monetary class
    
    str@Value.currency:euro
    float@Value.toUSD:1.1

    str@Time.format:YYYY-mm-dd
    #""
    Value: int
    Time: str

    def __init__(self):
        self.Value = 0
        self.Time = ""
"""

moneyClass = MyMonetaryClass()

# types = [MyComplexDataType]
# oa_definition = openapi_generator.generator.create_api_definition(types)
# with open("minimal.yaml", "w+") as oa_definition_file:
#     oa_definition_file.write(oa_definition)