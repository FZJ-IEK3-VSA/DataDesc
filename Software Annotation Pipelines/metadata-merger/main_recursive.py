import yaml
import os

FILES_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'files')

def load_yaml_as_dict(_path):
    yaml_dict = {}
    with open(_path, 'r') as fstream:
        try:
            content = yaml.safe_load(fstream)
            yaml_dict = content
        except yaml.YAMLError as exc:
            print(exc)
    return yaml_dict

def __pretty_print_dict(_dict):
    import json
    print(json.dumps(_dict, indent=2))

def version_check(y1, y2):
    y1_ver = y1["openapi"]
    y2_ver = y2["openapi"]

    if y1_ver == y2_ver:
        return True
    else:
        raise ValueError("Encountered version mismatch: {}/{}".format(y1_ver, y2_ver))

def get_dict_key_intersection(d1, d2):
    d1_keys = list(d1.keys())
    d2_keys = list(d2.keys())

    intersecting_keys = list(set(d1_keys) & set(d2_keys))

    return intersecting_keys

def recursive_properties(y1,y2):
    y1_schemas = y1["properties"]
    y2_schemas = y2["properties"]

    intersecting_keys = get_dict_key_intersection(y1_schemas, y2_schemas)

    # merged schema; can be thought of as 'y3'
    ret_schemas = {}

    for key in intersecting_keys:
        y1_schema = y1_schemas[key]
        y2_schema = y2_schemas[key]

        ## ret_schemas[schema] = ...
        ret_schema_fields = {}

        # semantically-critical fields are compared here; 
        # e.g. type must always be the same between both objects
        must_match_fields = ["type",]
        for mm in must_match_fields:
            val1 = y1_schema[mm]
            val2 = y2_schema[mm]
            if val1 != val2:
                ret_schema_fields[mm] = 'NIL'
                print("Mismatch in must-match field: {} ({}/{}); 'NIL' placed.".format(mm, val1, val2))
            else:
                ret_schema_fields[mm] = val1
                print("Matching {}!".format(mm))
        
        # not-so-critical fields are compared here;
        # usually descriptive text
        ask_override_fields = ["description",]
        for ov in ask_override_fields:
            val1 = y1_schema[ov]
            val2 = y2_schema[ov]
            if val1 != val2:
                acc_value = input(
                    """Field '{}' is ambiguous; which value to accept?
        #-- {} (1)
        #-- {} (2)
        """.format(ov,val1,val2))
                if acc_value not in ["1","2"]:
                    acc_value = "1"
                
                ret_schema_fields[ov] = val1 if acc_value=="1" else val2
            else:
                ret_schema_fields[ov] = val1

        # properties are merged here
        ret_schema_fields_properties = {}
        property_intersections = get_dict_key_intersection(y1_schema["properties"], y2_schema["properties"])

        ret_schema_fields_properties = {}

def merge_schemas(y1, y2):
    y1_schemas = y1["components"]["schemas"]
    y2_schemas = y2["components"]["schemas"]

    intersecting_keys = get_dict_key_intersection(y1_schemas, y2_schemas)

    # merged schema; can be thought of as 'y3'
    ret_schemas = {}

    for schema in intersecting_keys:
        y1_schema = y1_schemas[schema]
        y2_schema = y2_schemas[schema]

        ## ret_schemas[schema] = ...
        ret_schema_fields = {}

        # semantically-critical fields are compared here; 
        # e.g. type must always be the same between both objects
        must_match_fields = ["type",]
        for mm in must_match_fields:
            val1 = y1_schema[mm]
            val2 = y2_schema[mm]
            if val1 != val2:
                ret_schema_fields[mm] = 'NIL'
                print("Mismatch in must-match field: {} ({}/{}); 'NIL' placed.".format(mm, val1, val2))
            else:
                ret_schema_fields[mm] = val1
                print("Matching {}!".format(mm))
        
        # not-so-critical fields are compared here;
        # usually descriptive text
        ask_override_fields = ["description",]
        for ov in ask_override_fields:
            val1 = y1_schema[ov]
            val2 = y2_schema[ov]
            if val1 != val2:
                acc_value = input(
                    """Field '{}' is ambiguous; which value to accept?
        #-- {} (1)
        #-- {} (2)
        """.format(ov,val1,val2))
                if acc_value not in ["1","2"]:
                    acc_value = "1"
                
                ret_schema_fields[ov] = val1 if acc_value=="1" else val2
            else:
                ret_schema_fields[ov] = val1

        # properties are merged here
        ret_schema_fields_properties = {}
        property_intersections = get_dict_key_intersection(y1_schema["properties"], y2_schema["properties"])

        ret_schema_fields_properties = {}
        for pi in property_intersections:
            # semantically-critical fields are compared here; 
            # e.g. type must always be the same between both objects
            must_match_fields = ["type",]
            for mm in must_match_fields:
                val1 = y1_schema["properties"][mm]
                val2 = y2_schema["properties"][mm]
                if val1 != val2:
                    ret_schema_fields_properties[mm] = 'NIL'
                    print("Mismatch in must-match field: {} ({}/{}); 'NIL' placed.".format(mm, val1, val2))
                else:
                    ret_schema_fields_properties[mm] = val1
                    print("Matching {}!".format(mm))
            print(pi)
        # ...

        ret_schema_fields["properties"] = ret_schema_fields_properties


def merge_yaml_files(yaml1_path, yaml2_path):
    y1 = load_yaml_as_dict(yaml1_path)
    y2 = load_yaml_as_dict(yaml2_path)

    if(version_check(y1,y2)):
        merge_schemas(y1,y2)

def main():
    y1_path = os.path.join(FILES_PATH,'minimal_xattr.yaml')
    y2_path = os.path.join(FILES_PATH,'addition.yaml')
    merge_yaml_files(yaml1_path=y1_path, yaml2_path=y2_path)

main()