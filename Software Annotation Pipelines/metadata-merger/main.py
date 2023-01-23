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

        # - type
        # semantically-critical fields are compared here; 
        # e.g. type must always be the same between both objects
        must_match_fields = ["type",]
        for mm in must_match_fields:
            if mm in y1_schema and mm in y2_schema:
                val1 = y1_schema[mm]
                val2 = y2_schema[mm]
                if val1 != val2:
                    ret_schema_fields[mm] = 'NIL'
                    print("Mismatch in must-match field: {} ({}/{}); 'NIL' placed.".format(mm, val1, val2))
                else:
                    ret_schema_fields[mm] = val1
                    print("Matching {}!".format(mm))
        
        # - description
        # not-so-critical fields are compared here;
        # usually descriptive text
        ask_override_fields = ["description",]
        for ov in ask_override_fields:
            if ov in y1_schema and ov in y2_schema:
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
            else:
                if ov in y1_schema:
                    ret_schema_fields[ov] = y1_schema[ov]
                if ov in y2_schema:
                    ret_schema_fields[ov] = y2_schema[ov]

        # - properties
        # properties are merged here
        ret_schema_fields_properties = {}
        property_intersections = get_dict_key_intersection(y1_schema["properties"], y2_schema["properties"])

        ret_schema_fields_properties = {}
        for pi in property_intersections:
            # semantically-critical fields are compared here; 
            # e.g. type must always be the same between both objects
            must_match_fields = ["type","$ref"]
            for mm in must_match_fields:
                if mm in y1_schema["properties"][pi] and mm in y2_schema["properties"][pi]:
                    val1 = y1_schema["properties"][pi][mm]
                    val2 = y2_schema["properties"][pi][mm]
                    ret_schema_fields_properties[pi] = {}
                    if val1 != val2:
                        ret_schema_fields_properties[pi][mm] = 'NIL'
                        print("Mismatch in must-match field: {} ({}/{}); 'NIL' placed.".format(mm, val1, val2))
                    else:
                        ret_schema_fields_properties[pi][mm] = val1
                        print("Matching {}!".format(mm))

            # x-attributes are compared here;
            for x in [ i for i in y1_schema["properties"][pi] if i.startswith('x-')]:
                val1 = y1_schema["properties"][pi][x]
                val2 = y2_schema["properties"][pi][x]
                if val1 != val2:
                    acc_value = input(
                    """Field '{}' is ambiguous; which value to accept?
        #-- {} (1)
        #-- {} (2)
            """.format(x,val1,val2))
                    if acc_value not in ["1","2"]:
                        acc_value = "1"
                    
                    ret_schema_fields_properties[pi][x] = val1 if acc_value=="1" else val2
                else:
                    ret_schema_fields_properties[pi][x] = val1
        # ...

        y1_schema_properties_set = set(list(y1_schema["properties"].keys()))
        y2_schema_properties_set = set(list(y2_schema["properties"].keys()))
        for property in list( y1_schema_properties_set - set(property_intersections) ):
            ret_schema_fields_properties[property] = y1_schema["properties"][property]
        
        for property in list( y2_schema_properties_set - set(property_intersections) ):
            ret_schema_fields_properties[property] = y2_schema["properties"][property]

        ret_schema_fields["properties"] = ret_schema_fields_properties

        # - required; - enum are represented as lists in JSON-notation
        # list merges
        list_merges = ["required", "enum"]
        for lim in list_merges:
            ret_schema_fields_list = []
            do_add_lim_to_fields = False
            if lim in y1_schema:
                do_add_lim_to_fields = True
                for req in y1_schema[lim]:
                    ret_schema_fields_list.append(req)
            if lim in y2_schema:
                do_add_lim_to_fields = True
                for req in y2_schema[lim]:
                    ret_schema_fields_list.append(req)
            if do_add_lim_to_fields:
                ret_schema_fields[lim] = ret_schema_fields_list
        
        ret_schemas[schema] = ret_schema_fields

    for schema in list( set(list(y1_schemas.keys())) - set(intersecting_keys) ):
        ret_schemas[schema] = y1_schemas[schema]

    for schema in list( set(list(y2_schemas.keys())) - set(intersecting_keys) ):
        ret_schemas[schema] = y2_schemas[schema]

    return ret_schemas


def merge_yaml_files(yaml1_path, yaml2_path):
    y1 = load_yaml_as_dict(yaml1_path)
    y2 = load_yaml_as_dict(yaml2_path)

    __pretty_print_dict(y2)

    if(version_check(y1,y2)):
        y3 = merge_schemas(y1,y2)
        __pretty_print_dict(y3)

def main():
    y1_path = os.path.join(FILES_PATH,'minimal_xattr.yaml')
    y2_path = os.path.join(FILES_PATH,'addition.yaml')
    merge_yaml_files(yaml1_path=y1_path, yaml2_path=y2_path)

main()