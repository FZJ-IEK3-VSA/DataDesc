import os, json, copy
from deepdiff import DeepDiff
import re

FILES_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'files')

def version_check(j1, j2):
    """
    Checks if the versions of two JSON objects match for specified keys.

    Parameters:
    - j1 (dict): The first JSON object (primarily technical information).
    - j2 (dict): The second JSON object (general information).

    Returns:
    - None

    Raises:
    - ValueError: If the versions for the specified keys do not match.
    """
    matching_keys = ["openapi", "dataDescVersion"]
    for mk in matching_keys:
        if j1[mk] != j2[mk]:
            raise ValueError(f"Encountered version mismatch: {j1[mk]}/{j2[mk]} ({mk})")
    return True

def update_at_path(j_dict : dict, key_path : list[str], updated_value, build_path=False):
    """
    Updates the value at the specified nested path in a dictionary.

    Parameters:
    - j_dict (dict): The input dictionary.
    - key_path (list[str]): A list of keys forming the nested path.
    - updated_value (Any): The new value to set at the specified path.
    - build_path (bool, optional): If True, creates missing keys along the path.

    Returns:
    - None

    Raises:
    - ValueError: If a key in the path is not found in the dictionary and build_path is False.
    """
    current_dict = j_dict
    
    for key in key_path[:-1]:
        if key in current_dict:
            current_dict = current_dict[key]
        else:
            if not build_path:
                raise ValueError(f"Key {key} not found in {current_dict}")
            current_dict[key] = {}
            current_dict = current_dict[key]
    
    last_key = key_path[-1]
    if updated_value == None:
        current_dict.pop(last_key)
        return
    current_dict[last_key] = updated_value

def get_at_path(j_dict : dict, key_path : list[str]):
    """
    Retrieves the value at the specified nested path in a dictionary.

    Parameters:
    - j_dict (dict): The input dictionary.
    - key_path (list[str]): A list of keys forming the nested path.

    Returns:
    - Any: The value found at the specified path.

    Raises:
    - ValueError: If any key in the path is not found in the dictionary.
    """
    current_dict = j_dict
    
    for key in key_path[:-1]:
        if key in current_dict:
            current_dict = current_dict[key]
        else:
            raise ValueError(f"Key {key} not found in {current_dict}")
    
    last_key = key_path[-1]
    return current_dict[last_key]

def merge_schemas(j1, j2, override=False):
    """
    Merges two JSON schemas with the option to override specific fields.

    Parameters:
    - j1 (dict): The first JSON schema.
    - j2 (dict): The second JSON schema.
    - override (bool, optional): If True, overrides specific fields from j1 with corresponding fields from j2.

    Returns:
    - dict: The merged JSON schema.
    """
    if override:
        override_fields = ["externalDocs", "info"]
        for of in override_fields:
            if not of in j2: continue
            j1[of] = copy.deepcopy(j2[of])
    else:
        merge_fields = ["externalDocs", "info"]
        j1_snippet = copy.deepcopy(j1)
        j1_snippet = { k : j1_snippet[k] for k in merge_fields if k in j1_snippet }

        j2_snippet = copy.deepcopy(j2)
        j2_snippet = { k : j2_snippet[k] for k in merge_fields if k in j2_snippet }

        ddiff = DeepDiff(j1_snippet, j2_snippet)

        pattern = re.compile(r"'([^']+)'")

        if ddiff.get("values_changed"):
            for k,v in ddiff.get("values_changed").items():
                acc_value = input(
                    """Field {} is ambiguous; which value to accept?
        #-- {} (1 - default)
        #-- {} (2 - new)
            >> """.format(k,v["old_value"],v["new_value"]))
                if acc_value not in ["1","2"]:
                    acc_value = "1"

                if acc_value == "2":
                    matches = pattern.findall(k)
                    update_at_path( j1_snippet, matches, v["new_value"] )

        if ddiff.get("dictionary_item_added"):
            for item in ddiff.get("dictionary_item_added"):
                matches = pattern.findall(item)
                new_value = get_at_path(j2_snippet, matches)
                update_at_path( j1_snippet, matches, new_value, build_path=True )

        if ddiff.get("dictionary_item_removed"):
            for item in ddiff.get("dictionary_item_removed"):
                matches = pattern.findall(item)
                print(item, matches)
                acc_value = input(
                    """Field {} is removed in new version; which value to accept?
        #-- {} (1 - default)
        #-- [REMOVE] (2 - new)
            >> """.format(item,get_at_path(j1_snippet, matches)))
                if acc_value not in ["1","2"]:
                    acc_value = "1"
                if acc_value == "2":
                    update_at_path( j1_snippet, matches, None )
        
        new_j1 = copy.deepcopy(j1)
        
        for k,v in j1_snippet.items():
            new_j1[k] = v

        return new_j1

def merge_files(j1_path, j2_path, out):
    """
    Merges two JSON files and writes the result to a new file.

    Parameters:
    - j1_path (str): The path to the first JSON file.
    - j2_path (str): The path to the second JSON file.
    - out (str): The path to the output file.

    Returns:
    - None
    """
    j1 = json.load( open(j1_path) )
    j2 = json.load( open(j2_path) )

    if version_check(j1,j2):
        schema = merge_schemas(j1,j2)

    with open(out, 'w+') as f:
        json.dump(schema, f, indent=4)


def parse_arguments():
    """
    Parses command line arguments.

    Returns:
    - argparse.Namespace: An object containing parsed command line arguments.
    """
    from argparse import ArgumentParser

    parser = ArgumentParser()

    parser.add_argument("-f1", "--file_main", help="Main metadata file (to merge into)", required=True)
    parser.add_argument("-f2", "--file_general", help="General metadata file", required=True)
    parser.add_argument("-o", "--output", help="Output file", default="merged.json", required=False)

    return parser.parse_args()

if __name__ == '__main__':
    args = vars(parse_arguments())

    j1_path = os.path.join(FILES_PATH,args["file_main"]) # primarily technical metadata
    j2_path = os.path.join(FILES_PATH,args["file_general"]) # general metadata
    out_path = os.path.join(FILES_PATH,args["output"])

    merge_files(j1_path=j1_path, j2_path=j2_path, out=out_path)
