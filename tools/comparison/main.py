import json, os, re, copy
from deepdiff import DeepDiff

FILES_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'files')

class Comparator(object):
    def load_json(self, file):
        """
            Load JSON data from a file.

            Args:
            - file (str): Path to the JSON file.

            Returns:
            - dict: Loaded JSON data.
        """
        with open(file, "r") as f:
            return json.load(f)
        
    def save_json(self, file, data):
        """
            Save JSON data to a file.

            Args:
            - file (str): Path to the output JSON file.
            - data (dict): JSON data to be saved.
        """
        with open(file, 'w+') as f:
            json.dump(data, f, indent=4)
        
    def get_variable(self, mod_sheet, func_name, var_name):
        """
            Get a variable from a module sheet.

            Args:
            - mod_sheet (dict): Module sheet containing function and variable information.
            - func_name (str): Identifier of the function.
            - var_name (str): Identifier of the variable.

            Returns:
            - dict: The variable information.
        """
        # Get the function from the module
        funcs = mod_sheet["apiFunctions"]
        for f in funcs:
            if f["identifier"] == func_name:
                func = f
                break

        # Get the variable from the function
        for v in func["inputVariables"]:
            if v["identifier"] == var_name:
                var = v
                break

        return var
        
    def _assimilate_lists(self, l1, l2):
        """
            Assimilate two lists.

            Args:
            - l1 (list): First list.
            - l2 (list): Second list.

            Returns:
            - tuple: Tuple containing assimilated lists.
        """
        def __is_id_in_list( id_elem, l):
            for item in l:
                if type(item) == str:
                    return id_elem in l
                try:
                    if item["identifier"] == id_elem["identifier"]:
                        return True
                except KeyError as e:
                    if e.args[0] == "identifier":
                        return False
            return False
        
        def __get_index_of_id(id_elem, l):
            for i, item in enumerate(l):
                if type(item) == str:
                    if item == id_elem:
                        return i
                elif type(item) == dict:
                    try:
                        if item["identifier"] == id_elem["identifier"]:
                            return i
                    except KeyError as e:
                        if e.args[0] == "identifier":
                            return False
            return -1
        
        for item in l2:
            if not __is_id_in_list(item, l1):
                l1.append({})

        l2_updated = []
        for element in l1:
            if __is_id_in_list(element,l2):
                l2_element_idx = __get_index_of_id(element, l2)
                l2_updated.append( l2[l2_element_idx] )
            else:
                l2_updated.append({})

        return l1, l2_updated
    
    def _assimilate_data(self, d1, d2):
        """
            Assimilate two data structures.

            Args:
            - d1 (dict): First data structure.
            - d2 (dict): Second data structure.

            Returns:
            - tuple: Tuple containing assimilated data structures.
        """
        d1_copy = copy.deepcopy(d1)
        d2_copy = copy.deepcopy(d2)

        for k,v in d1.items():
            if isinstance(v, dict):
                if k in d2_copy:
                    d1_copy[k] = self._assimilate_data(v, d2_copy[k])
            elif isinstance(v, list):
                if k in d2_copy:
                    l1,l2 = self._assimilate_lists(v,d2_copy[k])

                    if l1:
                        d1_copy[k] = l1
                    if l2:
                        d2_copy[k] = l2
        return d1_copy, d2_copy

    def compare(self, d1, d2):
        """
            Compare two data structures and identify differences.

            Args:
            - d1 (dict): First data structure.
            - d2 (dict): Second data structure.

            Returns:
            - DeepDiff: DeepDiff object containing the differences.
        """
        d1_schema = d1["dataSchema"]
        d2_schema = d2["dataSchema"]

        d1_assimilated, d2_assimilated = self._assimilate_data(d1_schema, d2_schema)

        dd = DeepDiff(d1_assimilated, d2_assimilated)

        return dd
    
    def process_change(self, data, report, report_type, report_structure):
        """
            Process and update a compatibility report based on detected changes.
            Handle changes in dictionaries and lists accordingly.

            Args:
            - data (dict): Original data structure.
            - report (DeepDiff): DeepDiff object containing the differences.
            - report_type (str): Type of report (e.g., "values_changed", "dictionary_item_added").
            - report_structure (dict): Current structure of the compatibility report.

            Returns:
            - tuple: Tuple containing the updated report structure and a boolean indicating whether the data matches.
        """
        does_match = True
        pattern = re.compile(r"\[([^]]*)\]")
        iterable_types = ["iterable_item_removed", "values_changed"]
        key_value_types = ["dictionary_item_added", "dictionary_item_removed"]

        if report.get(report_type):
            # Handle list or dictionary traversal based on the data structure
            if report_type in iterable_types:
                does_match = False
                for k,v in report.get(report_type).items():
                    matches = [int(v) if v.isnumeric() else str(v).strip("'") for v in pattern.findall(k)]

                    data_dict = copy.deepcopy(data)
                    data_dict = data_dict["dataSchema"]
                    sub_dict = report_structure["dataSchema"]

                    for m in matches[:-1]:
                        if m in data_dict or (type(m)==int and m < len(data_dict)) or (type(m)==str and m.isnumeric() and int(m) < len(data_dict)):
                            if type(m)==str and m.isnumeric(): m = int(m)
                            if type(data_dict) == list:
                                # For lists, identify the data identifier and update sub_dict, as they are not identified by keys
                                data_identifier = data_dict[m]["identifier"]

                                _append_list = True
                                for sub in sub_dict:
                                    if sub["identifier"] == data_identifier:
                                        sub_dict = sub
                                        _append_list = False
                                        break
                                if _append_list:
                                    sub_dict.append( { "identifier" : data_identifier } )
                                    sub_dict = sub_dict[-1]
                                    data_dict = data_dict[m]
                                    continue
                            elif type(data_dict) == dict:
                                # For dictionaries, traverse sub_dict based on the key
                                if type(sub_dict) == dict:
                                    if m in sub_dict:
                                        sub_dict = sub_dict[m]
                                    else:
                                        sub_dict[m] = type(data_dict[m])()
                                        sub_dict = sub_dict[m]
                                else: 
                                    sub_dict.append(type(data_dict[m])())
                                    sub_dict = sub_dict[-1]
                            data_dict = data_dict[m]
                    last_key = matches[-1]
                    if report_type == "values_changed":
                        # Update sub_dict based on the type of difference
                        if type(sub_dict) == list:
                            sub_dict.append({ "expected" : v["old_value"], "received" : v["new_value"] })
                        if type(sub_dict) == dict:
                            sub_dict[last_key] = { "expected" : v["old_value"], "received" : v["new_value"] }
                    elif report_type == "iterable_item_removed":
                        # Update sub_dict for removed iterable items
                        if type(sub_dict) == list:
                            sub_dict.append({ "expected" : data_dict[last_key], "received" : None })
                        elif type(sub_dict) == dict:
                            sub_dict[last_key] = { "expected" : v, "received" : None }
            elif report_type in key_value_types:
                does_match = False if report_type == "dictionary_item_removed" else True
                for e in report.get(report_type):
                    matches = [int(v) if v.isnumeric() else str(v).strip("'") for v in pattern.findall(e)]

                    data_dict = copy.deepcopy(data)
                    data_dict = data_dict["dataSchema"]
                    sub_dict = report_structure["dataSchema"]

                    for m in matches[:-1]:
                        if m in data_dict or (type(m)==int and m < len(data_dict)) or (type(m)==str and m.isnumeric() and int(m) < len(data_dict)):
                            if type(m)==str and m.isnumeric(): m = int(m)
                            if type(data_dict) == list:
                                data_identifier = data_dict[m]["identifier"]

                                _append_list = True
                                for sub in sub_dict:
                                    if sub["identifier"] == data_identifier:
                                        sub_dict = sub
                                        _append_list = False
                                        break
                                if _append_list:
                                    sub_dict.append( { "identifier" : data_identifier } )
                                    sub_dict = sub_dict[-1]
                                    data_dict = data_dict[m]
                                    continue
                            elif type(data_dict) == dict:
                                if type(sub_dict) == dict:
                                    if m in sub_dict:
                                        sub_dict = sub_dict[m]
                                    else:
                                        sub_dict[m] = type(data_dict[m])()
                                        sub_dict = sub_dict[m]
                                else: 
                                    sub_dict.append(type(data_dict[m])())
                                    sub_dict = sub_dict[-1]
                            data_dict = data_dict[m]
                    last_key = matches[-1]
                    if report_type == "dictionary_item_added":
                        if type(sub_dict) == list:
                            sub_dict.append({ "expected" : None, "received" : data_dict[last_key] })
                        if type(sub_dict) == dict:
                            sub_dict[last_key] = { "expected" : None, "received" : data_dict[last_key] }
                    elif report_type == "dictionary_item_removed":
                        if type(sub_dict) == list:
                            sub_dict.append({ "expected" : data_dict[last_key], "received" : None })
                        if type(sub_dict) == dict:
                            sub_dict[last_key] = { "expected" : data_dict[last_key], "received" : None }
        return report_structure, does_match
    
    def evaluate_report(self, report, d1, d2):
        """
            Evaluate a compatibility report.

            Args:
            - report (DeepDiff): DeepDiff object containing the differences.
            - d1 (dict): First data structure.
            - d2 (dict): Second data structure.

            Returns:
            - tuple: Tuple containing the final report structure and a boolean indicating overall compatibility.
        """
        report_structure = {
             "dataSchema" : {}
        }

        match_results = []

        report_structure, new_match = self.process_change(d1, report, "values_changed", report_structure)
        match_results.append(new_match)
        
        report_structure, new_match = self.process_change(d2, report, "dictionary_item_added", report_structure)
        match_results.append(new_match)

        report_structure, new_match = self.process_change(d1, report, "dictionary_item_removed", report_structure)
        match_results.append(new_match)

        report_structure, new_match = self.process_change(d1, report, "iterable_item_removed", report_structure)
        match_results.append(new_match)

        return report_structure, False in match_results

    def create_compatibility_report(self, 
                                    mod_sheet, 
                                    func_name,
                                    var_name, 
                                    data_sheet, 
                                    out_name):
        """
            Create a compatibility report and save it to a file.

            Args:
            - mod_sheet (str): Path to the module sheet.
            - func_name (str): Identifier of the function.
            - var_name (str): Identifier of the variable.
            - data_sheet (str): Path to the input data sheet.
            - out_name (str): Path to the output compatibility report.

            Returns:
            - None
        """
        mod_sheet = self.load_json(mod_sheet)
        data_sheet = self.load_json(data_sheet)
        var_dict = self.get_variable(mod_sheet, func_name, var_name)

        report = self.compare(var_dict, data_sheet)
        report_structure, does_match = self.evaluate_report(report, var_dict, data_sheet)

        compatability_report = { "match" : does_match, "detail" : report_structure, "data" : data_sheet }
        self.save_json(out_name, compatability_report)

def parse_arguments():
    """
        Parses command line arguments.

        Returns:
        - argparse.Namespace: An object containing parsed command line arguments.
    """
    from argparse import ArgumentParser

    parser = ArgumentParser()

    parser.add_argument("-m", "--module", help="module datasheet to retrieve function information from", required=True)
    parser.add_argument("-f", "--function", help="module function identifier", required=True)
    parser.add_argument("-v", "--variable", help="function variable identifier", required=True)
    parser.add_argument("-d", "--data", help="input data datasheet", required=True)
     
    parser.add_argument("-o", "--out", help="comparison output file", required=True)

    return parser.parse_args()

if __name__ == '__main__':
    comparator = Comparator()

    args = vars(parse_arguments())

    mod_sheet = args["module"]
    func_name = args["function"]
    var_name = args["variable"]
    data_sheet = args["data"]
    out_name = args["out"]

    #mod_sheet = "annotated_complex.json"
    #func_name = "PowerOutputCalculator.process_pm"
    #var_name = "pm"
    #data_sheet = "data.json"
    #out_name = "report.json"

    mod_sheet = os.path.join(FILES_PATH, mod_sheet)
    data_sheet = os.path.join(FILES_PATH, data_sheet)
    out_name = os.path.join(FILES_PATH, out_name)

    comparator.create_compatibility_report(mod_sheet, func_name, var_name, data_sheet, out_name)