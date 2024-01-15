from enum import Enum
from typing import Dict, List, Optional


class MyEnum(str, Enum):
    ValueA = "ValueA"
    ValueB = "ValueB"
    ValueC = "ValueC"

class ExampleClass:
    """This is a simple example class"""
    Id: int = 0
    Text: Optional[str] = ""

class MyComplexDataType:
    """This is a complex class with different properties"""

    MyFloat: float = 0

    MyInt: int = 0

    MyString: str = ""

    MyEnumValue: MyEnum = MyEnum.ValueA

    MyOptionalString: Optional[str] = ""

    MySubObject: ExampleClass = None

    MyList: List[float] = []  

    MyObjectList: List[ExampleClass] = []

    MyDictionary: Dict[str, str] = {}

    MyNestedList: Optional[List[List[List[int]]]] = None

class MyMonetaryClass:
    """This is a simple monetary class"""
    Value: int = 0