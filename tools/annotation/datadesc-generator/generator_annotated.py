from __future__ import annotations
from typing import get_origin, get_args, Annotated, TypeGuard, Union, Callable, Generic, Dict, Any, _AnnotatedAlias, Optional, TypeVar, List, Type, Any
import inspect
import importlib
import json
import copy
import os

class DataModel(object):
    """
    A class representing a data model with associated metadata.

    Attributes:
    - typename (str): The type of the data model.
    - name (str): The name of the data model (optional).
    - is_optional (bool): Indicates if the data model is optional.
    - desc (str): A description of the data model (optional).
    - metadata (Dict[str, object]): Additional metadata associated with the data model.
    """

    def __init__(self,
                 typename : str,
                 name : str = None,
                 is_optional : bool = False,
                 desc : str = None,
                 **kwargs):
        """
        Initializes a new DataModel instance.

        Parameters:
        - typename (str): The type of the data model.
        - name (str, optional): The name of the data model.
        - is_optional (bool, optional): Indicates if the data model is optional.
        - desc (str, optional): A description of the data model.
        - **kwargs: Additional key-value pairs for metadata.

        Returns:
        - DataModel: A new instance of the DataModel class.
        """
        self.typename : str = typename
        self.name = name
        self.desc = desc
        self.is_optional = is_optional
        self.metadata : Dict[str, object] = {}
        self.dimensions = []

        self.append_metadata(kwargs)

    def append_metadata(self, obj):
        """
        Appends metadata to the data model.

        Parameters:
        - obj: Metadata to be appended. Can be a single item or a list/tuple of items.

        Returns:
        - None
        """
        if isinstance(obj, (list,tuple)):
            [ self.append_metadata(item) for item in obj ]
        if isinstance(obj, Dict):
            for k,v in obj.items():
                if k == "dimensions":
                    self.append_dimension({k : v})
                else:
                    self.metadata.update({k : v})
            #[ self.metadata.update({k : v}) for k,v in obj.items() ]
                
    def append_dimension(self, dim):
        """
        Appends a dimension to the data model.

        Parameters:
        - dim: The dimension to be appended.

        Returns:
        - None
        """
        self.dimensions += dim["dimensions"]

    def to_dict(self, prefix=None):
        """
        Converts the DataModel instance to a dictionary representation.

        Returns:
        - dict: A dictionary representing the data model.
        """
        direct_schema_properties = ["semanticConcept", "format", "minimum", "maximum", "exclusiveMinimum", "exclusiveMaximum",
                                    "multipleOf", "minLength", "maxLength", "pattern", "items", "minItems", "maxItems",
                                    "uniqueItems", "unit", "quantityKind", "nullable", "enum", "default", "example", 
                                    "mediaType", "charSet", "properties"]
       
        dataSchema = { "type" : self.typename }
        direct_metadata = { k : v for k,v in self.metadata.items() if k in direct_schema_properties and v is not None }
        property_metadata = [
            { "identifier" : k, "type" : type(v).__name__, "default" : v }
            for k,v in self.metadata.items()
            if k not in direct_schema_properties and v is not None
        ]

        if property_metadata:
            dataSchema.update({ "properties" : property_metadata })
        dataSchema.update(direct_metadata)

        if self.dimensions:
            dataSchema.update({"dimensions" : self.dimensions})

        dict_ = {
            "identifier" : f"{prefix}.{self.name}" if prefix else self.name,
            "description" : self.desc,
            "required" : not self.is_optional,
            "dataSchema" : dataSchema
        }

        return { k : v for k, v in dict_.items() if v is not None }

    def to_json(self):
        """
        Converts the DataModel instance to a JSON string.

        Returns:
        - str: A JSON string representing the data model.
        """
        return json.dumps(
            self.to_dict(),
            indent=4
        )
    
class ObjectModel(DataModel):
    """
    A class representing an object model, inheriting from DataModel.

    Attributes:
    - vars (List[DataModel]): A list of variable data models associated with the object model.
    - funcs (List[DataModel]): A list of function data models associated with the object model.
    - name (str): The name of the object model.
    - desc (str): A description of the object model.
    - is_optional (bool): Indicates if the object model is optional.
    """

    def __init__(self, 
                 name,
                 desc,
                 is_optional : bool = False,
                 **kwargs):
        """
        Initializes a new ObjectModel instance.

        Parameters:
        - name (str): The name of the object model.
        - desc (str): A description of the object model.
        - is_optional (bool, optional): Indicates if the object model is optional.
        - **kwargs: Additional key-value pairs for metadata.

        Returns:
        - ObjectModel: A new instance of the ObjectModel class.
        """
        self.vars = []
        self.funcs = []
        self.format = None
        
        typename="object"
        if "ctype" in kwargs.keys():
            if kwargs["ctype"]=="Any":
                typename="*"
            else: 
                typename="object"
                self.format = kwargs["ctype"]
            kwargs.pop("ctype", None)

        super().__init__(typename=typename, 
                         name=name,
                         is_optional=is_optional, 
                         desc=desc,
                         **kwargs)

    def to_dict(self, prefix=None):
        """
        Converts the ObjectModel instance to a dictionary representation.

        Returns:
        - dict: A dictionary representing the object model.
        """
        dict_ = super().to_dict(prefix=prefix)
        
        vars = [ v.to_dict(prefix=prefix) for v in self.vars if v is not None ]
        funcs = [ f.to_dict(prefix=prefix) for f in self.funcs if f is not None]

        props = { v["identifier"] : v for v in vars if v is not None }
        props.update({ f["identifier"] : f for f in funcs if f is not None })


        if not "dataSchema" in dict_.keys():
            dict_["dataSchema"] = {}
        properties = [ val for _, val in props.items() if val is not None ]
        dict_schema = copy.deepcopy(dict_["dataSchema"])
        if properties:
            dict_schema.update({"properties" : properties})
        if self.format:
            dict_schema.update({"format" : {"example" : self.format}})
        dict_["dataSchema"] = dict_schema
        
        return dict_
    
    def get_api_functions(self):
        """
        Retrieves API functions associated with the object model.

        Returns:
        - List[dict]: A list of dictionaries representing API functions.
        """
        api_functions = []

        for func in self.funcs:
            api_function_obj = {}
            api_function_obj["name"] = f"{self.name}.{func.name}"
            api_function_obj["description"] = func.desc
            api_function_obj["inputVariables"] = [ v.to_dict() for v in func.vars if v is not None ]
            api_function_obj["outputVariables"] = func.return_type.to_dict()

            api_function_obj = { k : v for k,v in api_function_obj.items() if v is not None }

            api_functions.append(api_function_obj)

    def append_function(self, func):
        """
        Appends a function to the list of functions associated with the object model.

        Parameters:
        - func: The function data model to be appended.

        Returns:
        - None
        """
        self.funcs.append(func)

    def append_variable(self, var):
        """
        Appends a variable to the list of variables associated with the object model.

        Parameters:
        - var: The variable data model to be appended.

        Returns:
        - None
        """
        self.vars.append(var)

class ArrayModel(DataModel):
    """
    A class representing an array model, inheriting from DataModel.

    Attributes:
    - name (str): The name of the array model.
    - desc (str): A description of the array model.
    - is_optional (bool): Indicates if the array model is optional.
    - array_type (Union[str, DataModel]): The type of elements in the array, can be a string or another DataModel.
    """

    def __init__(self, 
                 name,
                 desc,
                 is_optional : bool = False,
                 array_type : Union[str, DataModel] = None):
        """
        Initializes a new ArrayModel instance.

        Parameters:
        - name (str): The name of the array model.
        - desc (str): A description of the array model.
        - is_optional (bool, optional): Indicates if the array model is optional.
        - array_type (Union[str, DataModel], optional): The type of elements in the array, can be a string or another DataModel.

        Returns:
        - ArrayModel: A new instance of the ArrayModel class.
        """
        super().__init__(typename="array", 
                         name=name,
                         is_optional=is_optional,
                         )#desc=desc)
        self.array_type = array_type
        
    def to_dict(self, prefix=None):
        """
        Converts the ArrayModel instance to a dictionary representation.

        Returns:
        - dict: A dictionary representing the array model.
        """
        dict_ = super().to_dict(prefix=prefix)
        if not "dataSchema" in dict_.keys():
            dict_["dataSchema"] = {}

        items_list = []
        array_type = self.array_type.to_dict()
        array_type_schema = copy.deepcopy(array_type["dataSchema"])
        if array_type_schema["type"] == "*":
            array_type.pop("description", None)
            array_type_schema_props = copy.deepcopy(array_type_schema["properties"])
            array_type_schema.pop("properties", None)
            index = None
            for i, item in enumerate(array_type_schema_props):
                if item.get('default') == "Any":
                    index = i
                    break
            array_type_schema_props.pop( index )
            if array_type_schema_props:
                array_type_schema["properties"] = array_type_schema_props
            
        array_type.pop("dataSchema", None)
        array_type.pop("identifier", None)
        array_type.pop("required", None)
        array_type.update(array_type_schema)
        items_list.append(array_type)
        
        dict_schema = copy.deepcopy(dict_["dataSchema"])
        dict_schema.update({"items" : items_list})
        dict_["dataSchema"] = dict_schema

        return dict_

class DictModel(DataModel):
    """
    A class representing a dictionary model, inheriting from DataModel.

    Attributes:
    - name (str): The name of the dictionary model.
    - desc (str): A description of the dictionary model.
    - is_optional (bool): Indicates if the dictionary model is optional.
    - dict_type (Union[str, DataModel]): The type of values in the dictionary, can be a string or another DataModel.
    """
    def __init__(self, 
                 name,
                 desc,
                 is_optional : bool = False,
                 dict_type : Union[str, DataModel] = None):
        """
        Initializes a new DictModel instance.

        Parameters:
        - name (str): The name of the dictionary model.
        - desc (str): A description of the dictionary model.
        - is_optional (bool, optional): Indicates if the dictionary model is optional.
        - dict_type (Union[str, DataModel], optional): The type of values in the dictionary, can be a string or another DataModel.

        Returns:
        - DictModel: A new instance of the DictModel class.
        """
        super().__init__(typename="object", 
                         name=name,
                         #desc=desc,
                         is_optional=is_optional)
        self.dict_type = dict_type

    def to_dict(self, prefix=None):
        """
        Converts the DictModel instance to a dictionary representation.

        Returns:
        - dict: A dictionary representing the dictionary model.
        """
        dict_ = super().to_dict(prefix=prefix)

        if not "dataSchema" in dict_.keys():
            dict_["dataSchema"] = {}

        items_list = []
        array_type = self.dict_type.to_dict()
        array_type_schema = copy.deepcopy(array_type["dataSchema"])
        if array_type_schema["type"] == "*":
            array_type.pop("description", None)
            array_type_schema_props = copy.deepcopy(array_type_schema["properties"])
            array_type_schema.pop("properties", None)
            index = None
            for i, item in enumerate(array_type_schema_props):
                if item.get('default') == "Any":
                    index = i
                    break
            array_type_schema_props.pop( index )
            if array_type_schema_props:
                array_type_schema["properties"] = array_type_schema_props
            
        array_type.pop("dataSchema", None)
        array_type.pop("identifier", None)
        array_type.pop("required", None)
        array_type.update(array_type_schema)
        items_list.append(array_type)
        
        dict_schema = copy.deepcopy(dict_["dataSchema"])
        dict_schema.update({"items" : items_list})
        dict_["dataSchema"] = dict_schema

        return dict_



class StringModel(DataModel):
    """
    A class representing a string model, inheriting from DataModel.

    Attributes:
    - name (str): The name of the string model.
    - desc (str): A description of the string model.
    - is_optional (bool): Indicates if the string model is optional.
    """

    def __init__(self, 
                 name,
                 desc,
                 is_optional : bool = False):
        """
        Initializes a new StringModel instance.

        Parameters:
        - name (str): The name of the string model.
        - desc (str): A description of the string model.
        - is_optional (bool, optional): Indicates if the string model is optional.

        Returns:
        - StringModel: A new instance of the StringModel class.
        """
        super().__init__(typename="string", 
                         name=name,
                         #desc=desc,
                         is_optional=is_optional)

class EnumModel(DataModel):
    """
    A class representing an enum model, inheriting from DataModel.

    Attributes:
    - name (str): The name of the enum model.
    - desc (str): A description of the enum model.
    - is_optional (bool): Indicates if the enum model is optional.
    """

    def __init__(self, 
                 name,
                 desc,
                 is_optional : bool = False):
        """
        Initializes a new EnumModel instance.

        Parameters:
        - name (str): The name of the enum model.
        - desc (str): A description of the enum model.
        - is_optional (bool, optional): Indicates if the enum model is optional.

        Returns:
        - EnumModel: A new instance of the EnumModel class.
        """
        super().__init__(typename="string", 
                         name=name,
                         is_optional=is_optional,
                         )#desc=desc)

class NumberModel(DataModel):
    """
    A class representing a number model, inheriting from DataModel.

    Attributes:
    - name (str): The name of the number model.
    - desc (str): A description of the number model.
    - integer (bool): Indicates if the number model is an integer.
    - is_optional (bool): Indicates if the number model is optional.
    """

    def __init__(self, 
                 name,
                 desc,
                 integer : bool = False,
                 is_optional : bool = False):
        """
        Initializes a new NumberModel instance.

        Parameters:
        - name (str): The name of the number model.
        - desc (str): A description of the number model.
        - integer (bool, optional): Indicates if the number model is an integer.
        - is_optional (bool, optional): Indicates if the number model is optional.

        Returns:
        - NumberModel: A new instance of the NumberModel class.
        """
        super().__init__(typename="integer" if integer else "float", 
                         name=name,
                         is_optional=is_optional,
                         )#desc=desc)
    
class FunctionModel(ObjectModel):
    """
    A class representing a function model, inheriting from ObjectModel.

    Attributes:
    - name (str): The name of the function model.
    - desc (str): A description of the function model.
    - return_type (List[DataModel]): The return type of the function, represented as a list of DataModel instances.
    """
    def __init__(self, 
                 name,
                 desc):
        """
        Initializes a new FunctionModel instance.

        Parameters:
        - name (str): The name of the function model.
        - desc (str): A description of the function model.

        Returns:
        - FunctionModel: A new instance of the FunctionModel class.
        """
        super().__init__(name=name,desc=desc)
        self.name = name
        self.return_type = []

    def to_dict(self, prefix=None):
        """
        Converts the FunctionModel instance to a dictionary representation matching the DataDesc standard structure.

        Parameters:
        - prefix (str, optional): A prefix to be added to the identifier.

        Returns:
        - dict: A dictionary representing the function model.
        """
        dict_ = {}
        dict_["identifier"] = f"{prefix}.{self.name}" if prefix else self.name
        dict_["description"] = self.desc
        dict_["inputVariables"] = [ v.to_dict() for v in self.vars if v is not None ]
        dict_["outputVariables"] = [ v.to_dict() for v in self.return_type if v is not None ]

        dict_ = { k : v for k,v in dict_.items() if v is not None }
        
        return dict_
    
    def append_return(self, rtn):
        """
        Appends a return type to the list of return types associated with the function model.

        Parameters:
        - rtn: The return type data model to be appended.

        Returns:
        - None
        """
        self.return_type.append(rtn)

class Generator(object):
    """
    A class responsible for generating data description definitions according to the DataDesc documentation standard.
    See: https://github.com/FZJ-IEK3-VSA/DataDesc/tree/main/schema

    Attributes:
    - API_DEFINITION_TEMPLATE (dict): A template for the data description definition.
    - class_models (List[ObjectModel]): A list to store class models.
    - func_models (List[FunctionModel]): A list to store function models.
    - var_models (List[DataModel]): A list to store variable models.
    """

    API_DEFINITION_TEMPLATE = {
        "dataDescVersion" : "1.0",
        "openapi" : "3.0.0",
        "info" : {"title" : "API Spec", "version" : "1.0.0"},
        "apiFunctions" : [],
        "variables" : []
    }

    def __init__(self) -> None:
        """
        Initializes a new Generator instance.

        Returns:
        - Generator: A new instance of the Generator class.
        """
        self.class_models = []
        self.func_models = []
        self.var_models = []


    def create_datadesc_definition_file(self, 
                                   collection, 
                                   filename, 
                                   export_to_json : bool,
                                   do_export_class_vars : bool = False):
        """
        Creates a data description definition file.

        Parameters:
        - collection: A collection of classes, functions, and variables.
        - filename (str): The name of the file to be created.
        - export_to_json (bool): Indicates whether to export to JSON or YAML.

        Returns:
        - None
        """
        definition = self.create_datadesc_definition(collection, 
                                                     export_to_json,
                                                     do_export_class_vars=do_export_class_vars)
        if definition is None:
            return
        
        file_extension = ".json" if export_to_json else ".yaml"
        if not filename.endswith(file_extension):
            filename += file_extension

        #file_dir = os.path.dirname(filename)
        #if not os.path.exists(file_dir):
        #    os.makedirs(file_dir)
            
        filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)

        with open(filename, "w+") as dd_file:
            dd_file.write( json.dumps(
                    definition,
                    indent=4) )

    def create_datadesc_definition(self,
                                   collection,
                                   export_to_json : bool,
                                   do_export_class_vars : bool = False):
        """
        Creates a data description definition according to the DataDesc schema.

        Parameters:
        - collection: A collection of classes, functions, and variables.
        - export_to_json (bool): Indicates whether to export to JSON or YAML.
        - do_export_class_vars (bool): Indicates whether to export class variables.

        Returns:
        - dict: A dictionary representing the data description definition.
        """
        # create model definitions for classes
        for class_ in collection[0]:
            class_model = self.create_model(class_)
            self.class_models.append(class_model)

        # create model definitions for functions
        for func_ in collection[1]:
            func_model = self.create_model(func_)
            self.func_models.append(func_model)

        # create model definitions for floating variables
        for var_ in collection[2]:
            var_model = self.create_model(var_[1], var_[0])
            self.var_models.append(var_model)

        definition = copy.deepcopy(Generator.API_DEFINITION_TEMPLATE)

        # add class models to definition
        for class_model in self.class_models:
            if do_export_class_vars:
                for var_model in class_model.vars:
                    var_obj = {}
                    var_obj["name"] = var_model.name
                    if var_model.name == "PowerMeasurement":
                        pass
                    definition["variables"].append(var_model.to_dict(prefix=class_model.name))
            # Add class model functions (API Function objects) to definition
            for func_model in class_model.funcs:
                api_function_obj = {}
                api_function_obj["name"] = func_model.name
                definition["apiFunctions"].append(func_model.to_dict(prefix=class_model.name))

        return { k : v for k,v in definition.items() if v}
    
    def create_model(self, 
                     type_,
                     name=None,
                     ref_existing=False,
                     is_optional=False):
        """
        Creates a data model for the various Python elements.

        Parameters:
        - type_: The type of the data model.
        - name (str, optional): The name of the data model.
        - ref_existing (bool, optional): Indicates whether to reference an existing model. Not yet implemented.
        - is_optional (bool, optional): Indicates whether the model is optional.

        Returns:
        - DataModel: A new instance of a data model.
        """
        type_name = type_.__name__ if hasattr(type_, "__name__") else type(type_).__name__
        model_name = type_name if name is None else name
        type_desc = type_.__doc__ if hasattr(type_, "__doc__") else type(type_).__doc__
        type_origin = get_origin(type_)

        datatype_dict = {
            str : lambda: StringModel(name=model_name, is_optional=is_optional, desc=type_desc),
            int : lambda: NumberModel(name=model_name, integer=True, is_optional=is_optional, desc=type_desc),
            float : lambda: NumberModel(name=model_name, integer=False, is_optional=is_optional, desc=type_desc),
            dict : lambda: DictModel(name=model_name, dict_type=self.create_model(type_.__args__[0] if hasattr(type_, '__args__') else Any), is_optional=is_optional, desc=type_desc),
            list : lambda: ArrayModel(name=model_name, array_type=self.create_model(type_.__args__[0] if hasattr(type_, '__args__') else Any), is_optional=is_optional, desc=type_desc),
        }

        if inspect.isclass(type_) or (type_origin in datatype_dict and type_origin is not None):        
            if type_ in datatype_dict:
                return datatype_dict[type_]()
            elif type_origin in datatype_dict:
                return datatype_dict[type_origin]()
            
            model = ObjectModel(name=model_name, is_optional=is_optional, ctype=type_name, desc=type_desc)

            # convert class functions to models and append to class model
            #instanced_type = type_() if inspect.isclass(type_) else type_
            #filter_cond = lambda x : (inspect.isroutine(x[1]) and not isinstance(x[1], type(instanced_type.__init__)) ) and not inspect.isbuiltin(x[1]) and not x[0].startswith("_")
            #functions = inspect.getmembers(instanced_type)
            #functions = list( filter(filter_cond, functions) )

            try:
                instanced_type = type_() if inspect.isclass(type_) else type_
                instanced_functions = [ i[0] for i in inspect.getmembers(instanced_type, lambda x: inspect.isroutine(x) and not isinstance(x, type(instanced_type.__init__)) and not inspect.isbuiltin(x) and not x.__name__.startswith("_") and not x.__name__.endswith("_")) ]
            except TypeError:
                instanced_functions = None
                
            functions = inspect.getmembers(type_, lambda x: inspect.isfunction(x) and not inspect.isbuiltin(x) and not (x.__name__.startswith("_") or x.__name__.endswith("_")) and (x.__name__ in instanced_functions if instanced_functions else True))
            if functions:
                for func_name, func in functions:
                    f_model = self.create_model(func, name=func_name)
                    model.append_function(f_model)

            # convert class variables to models and append to class model
            variables = inspect.getmembers(type_, lambda x: not inspect.isclass(x) and not inspect.isfunction(x) and not inspect.ismodule(x))
            variables_annotations = next((k[1] for k in variables if k[0] == "__annotations__"), None)
            if variables_annotations: 
                for var_name, var_type in variables_annotations.items():
                    if var_name.startswith("_") or var_name.endswith("_"):
                        continue
                    var_model = self.create_model(type_=var_type, name=var_name)
                    model.append_variable(var_model)
            return model
        
        elif inspect.isfunction(type_):
            function_params = type_.__annotations__
            func_model = FunctionModel(model_name, desc=type_desc)
            for k,v in function_params.items():
                if k == "return" : 
                    continue
                k_model = self.create_model(v,name=k)
                func_model.append_variable(k_model)
            return_model = self.create_model(inspect.signature(type_).return_annotation, name="return")
            func_model.append_return(return_model)

            return func_model
        
        elif isinstance(type_, _AnnotatedAlias):
            origin_class = type_.__origin__
            meta = type_.__metadata__

            model = self.create_model(origin_class, name=model_name)
            model.append_metadata(meta)
            return model
        
        elif get_origin(type_) == Union:
            if any( arg == type(None) for arg in get_args(type_) ): 
                is_optional = True
            origin_class = (type_.__args__[0])
            model = self.create_model(origin_class, name=model_name, is_optional=is_optional)
            return model
        
        else:
            model = ObjectModel(name=model_name, ctype=type_name, desc=type_desc)
            return model
        
def collect_from_module(module : object, 
                        inspect_cond : TypeGuard[type]):
    """
    Collects items from a module based on the provided condition.

    Parameters:
    - module (object): The module to collect items from.
    - inspect_cond (TypeGuard[type]): The condition for inspecting items.

    Returns:
    - List[type]: A list of items that satisfy the condition.
    """
    return [
        c
        for _, c in inspect.getmembers(module, inspect_cond)
        if c.__module__ == module.__name__
    ]

def collect_variables_from_module(module : object):
    """
    Collects variables from a module and filter for instantiated variables.

    Parameters:
    - module (object): The module to collect variables from.

    Returns:
    - List[type]: A list of variables from the module.
    """
    vars=[
        v
        for v in inspect.getmembers(module, lambda x: not inspect.isclass(x) and not inspect.isfunction(x) and not inspect.ismodule(x))
        if (not v[0].startswith("__"))
    ]

    filtered = [v for v in vars if hasattr(v[1], '__dict__') and v[1].__dict__.get('_inst', True)]

    return filtered

def parse_arguments():
    """
    Parses command line arguments.

    Returns:
    - argparse.Namespace: An object containing parsed command line arguments.
    """
    from argparse import ArgumentParser

    parser = ArgumentParser()

    parser.add_argument("-m", "--module", help="python module to generate DataDesc document from", required=True)
    parser.add_argument("-o", "--out", help="DataDesc output filename", required=True)
    parser.add_argument("-v", "--variables", help="append to parse variables", default=False, action="store_true")

    return parser.parse_args()

if __name__ == '__main__':
    import importlib
    generator = Generator()

    to_json = True

    args = vars(parse_arguments())
    parse_vars = args["variables"]
    output_fname = args["out"]
    import_mod = importlib.import_module(args["module"])

    #parse_vars = True
    #output_fname = 'Examples/annotated_complex.json' #args["out"]
    #import_mod = importlib.import_module('Examples.annotated_complex') 
    types = collect_from_module( import_mod, inspect.isclass )
    funcs = collect_from_module( import_mod, inspect.isfunction )
    fvars = collect_variables_from_module(  import_mod )

    collection = [ types, funcs, fvars ]

    generator.create_datadesc_definition_file(collection, output_fname, to_json, parse_vars)
