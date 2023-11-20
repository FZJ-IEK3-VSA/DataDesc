import datetime
import getpass
import inspect
import traceback
from typing import Any, Dict, List, Mapping

#import yaml
import json
from orkg import ORKG  # type: ignore

# The ORKG currently does not support optional parameters. This placeholder
# is used for parameters that are not contained in the json metadata file.
# TODO: use type-specific placeholders
EMPTY_PARAM_PLACEHOLDERS = {
    str: "EMPTY PARAMETER",
    datetime.date: datetime.date(1, 1, 1),
    int: -999999,
    bool: False,
}

# maps the ORKG fields to the corresponding paths in the json metadata file
MAPPING: Dict[str, List[str]] = {
    "email": ["contact", "email"],
    "author": ["contact", "name"],
    "url": ["contact", "url"],  # TODO: in json, this seems to be an orcid - correct ORKG field?
    "affiliation": ["authors", 0, "affiliation"],
    "description": ["description"],
    "license": ["license", "name"],
    "name": ["title"],
    "version": ["version"],
    #"application_category": ["x-category"],
    #"cont_integration": ["x-ci"],
    #"date_created": ["x-created"],
    #"development_status": ["x-dev-status"],
    "download_url": ["downloadUrl"],
    "release": ["datePublished"],
    "funder": ["funders"],
    "funding": ["fundings"],
    "identifier": ["identifier"],
    #"issue_tracker": ["x-issue-tracker"],
    "keywords": ["keywords"],
    #"operating_system": ["x-os"],
    #"is_part_of": ["x-part-of"],
    #"runtime_platform": ["x-platform"],
    "programming_language": ["programmingLanguages"],
    "reference_publication": ["reference_publication"],
    #"related_link": ["x-related-links"],
    "release_notes": ["readme"],
    "code_repository": ["codeRepository"],
}

date_parser = lambda s: datetime.datetime.strptime(s, "%Y-%m-%d")

# stores conversion functions for all attributes with a type
# other than str
ORKG_ATTRIBUTE_CONVERTERS = {
    "date_created": date_parser,
}


    # TODO: remove; list of all parameters of the software metadata template
    # all_fields = {"label", "software_features", "documentation", "readme", "issue_tracker",
    # "reference_publication", "embargo_date": datetime.date, "funding", "development_status",
    # "cont_integration", "build_instructions", maintainer, software_suggestions, addresses,
    # affiliation, given_name, family_name, email, same_as, related_link, description, name,
    # identifier, position: int, has_part, is_part_of, is_accessible_for_free: bool, provider,
    # sponsor, publisher, producer, funder, keywords, editor, encoding, file_format,
    # date_published: datetime.date, date_created: datetime.date, date_modified: datetime.date,
    # creator, copyright_holder, copyright_year: int, contributor, author, supporting_data,
    # software_requirements, software_help, storage_requirements, release_notes,
    # processor_requirements, permissions, operating_system, memory_requirements, install_url,
    # download_url, file_size: int, application_sub_category, application_category,
    # runtime_platform, target_product, programming_language, softwaretype, extension,
    # code_repository, release, developer, license, version, url, alternativename,
    # abbreviation, citation}

def get_json_value(data: Dict, keys: List[str], orkg_key: str, top_level_key: str = "info") -> Any:
    """
    Extracts the value of a property in the metadata dictionary, given the path to
    the property.

    :param data: the metadata dictionary parsed from the json file
    :type data: Dict
    :param keys: a list of keys that show which property of the metadata dictionary
                 is needed
    :type keys: List[str]
    :param top_level_key: optional top-level key that contains all metadata properties,
                          defaults to "info"
    :type top_level_key: str, optional
    :return: the value of the property from the metadata dictionary
    :rtype: Any
    """
    d = data[top_level_key] if top_level_key else data
    for key in keys:
        assert isinstance(d, Mapping), "Key list is too long or data is invalid"
        if orkg_key in ORKG_ATTRIBUTE_CONVERTERS:
            d = ORKG_ATTRIBUTE_CONVERTERS[orkg_key](d[key])
        else:
            d = d[key]
    return d


def get_values_from_json(data: Dict) -> Dict[str, str]:
    """
    Collects the supported metadata attributes from the metadata dictionary in another
    dictionary, using the keys defined by the ORKG Software template.

    :param data: the metadata dictionary parsed from the json file
    :type data: Dict
    :return: a dictionary that contains all metadata properties using the ORKG field names
    :rtype: Dict[str, str]
    """
    return {key: get_json_value(data, json_path, key) for key, json_path in MAPPING.items()}


def main():
    # read the json metadata file
    filename = "meta.json"
    with open(filename) as file:
        try:
            #data = yaml.safe_load(file)
            data = json.load(file)
        except Exception as e:
            print(e)

    # create the connector to the ORKG
    host = "https://sandbox.orkg.org/"
    username = "d.neuroth@fz-juelich.de"
    password = getpass.getpass(prompt="Password:")
    orkg_connector = ORKG(host=host, creds=(username, password))
    # orkg_connector = ORKG(host=host) # without credentials

    # materialize the Software template
    template_id = "R166722" # ID of 'Software template'
    template_id = "R253265" # ID of 'Smaller Test Template'
    result = orkg_connector.templates.materialize_template(template_id)
    assert result, f"Could not materialize the template '{template_id}'"

    # get the metadata values from the json file
    values = get_values_from_json(data)

    # get the list of parameters required by the Software template
    parameters = inspect.signature(orkg_connector.templates.test_for_nfdi4ing_sw_md_pipeline).parameters

    # remove metadata values from the json file that are not contained in the template
    for name in list(values.keys()):
        if name not in parameters:
            del values[name]
            print(f"Metadata field {name} is not contained in the template.")
    
    # manually add label
    if "label" in parameters and "name" in values:
        values["label"] = values["name"]

    # add the placeholder value for all unused metadata fields in the Software template
    for name, param in parameters.items():
        if name not in values.keys():
            param_type = param._annotation
            values[name] = EMPTY_PARAM_PLACEHOLDERS[param_type]
            print(f"Unused parameter: {name}")

    # instantiate the Software template
    entry = orkg_connector.templates.test_for_nfdi4ing_sw_md_pipeline(**values)
    assert entry is not None
    try:
        result = entry.save()
    except Exception:
        print("Upload to ORKG failed")
        with open("./stacktrace.txt", "w") as f:
            stacktrace = traceback.format_exc()
            f.write(stacktrace)
    assert result

    orkg_file = "orkg_test.txt"
    entry.serialize_to_file(orkg_file)


if __name__ == "__main__":
    main()