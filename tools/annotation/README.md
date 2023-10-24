# Annotation of research data artifacts with the DataDesc schema

Table of contents:

- [Annotation of research software](https://github.com/FZJ-IEK3-VSA/DataDesc/tree/main/tools/annotation#annotation-of-research-software)
    - [General information about a software](https://github.com/FZJ-IEK3-VSA/DataDesc/tree/main/tools/annotation#general-information-about-a-software)
    - [Technical information about a software interface](https://github.com/FZJ-IEK3-VSA/DataDesc/tree/main/tools/annotation#technical-information-about-a-software-interface)
    - [Merging general and technical information in one metadata document](https://github.com/FZJ-IEK3-VSA/DataDesc/tree/main/tools/annotation#merging-general-and-technical-information-in-one-metadata-document)
- [Annotation of datasets](https://github.com/FZJ-IEK3-VSA/DataDesc/tree/main/tools/annotation#annotation-of-datasets)

## Annotation of research software

### General information about a software

General Metadata refers to information on the software - name, author and version to name a few.
It is usually collected during the software publication step and only specified on a publication platform. 
Some metadata, such as licenses or version numbering may, in some instances, also be provided alongside the code in DocStrings.

To provide a clearer distinction between general and technical metadata, we suggest outsourcing all general metadata to a dedicated file.
The `general-metadata-form` may aid in the creation of this file.

Navigate to the `general-metadata-form` usind the command line and execute `jupyter notebook` to use the form.

In your browser, access the notebook titled `GeneralMetadataCollectorTabbed.ipynb` and fill in your information.

Afterwards, generate and download your metadata file using the `generate meta.yaml` button underneath the form.

### Technical information about a software interface

To allow for maximum robustness against user error, we propose a new way of annotating software interfaces by leveraging Python decorators.

_Installation_

Install it, by navigating to the `xattrclass` folder under `Python\openapi-generator` and executing
```
pip install -e .
```
on the command line.

_Usage_

In your code, import it by adding the following line at the top
```
from xattr.xattr import xattr
```

The `xattr` notation leverages the Python decorator concept to append additional information to Python objects - classes, functions, variables and parameters.
Check out the `Examples` folder under `Python\openapi-generator` to get a gist of how to annotate even more complex data types, such as Pandas' dataframes.

In general, prefix your class definition with `@xattr(xattr=...)`, where the `xattr` parameter must be a dictionary. The keys of the dictionary refer to the object names of the class. They are case-sensitive and must match either a variable, function or parameter name as they will be ignored otherwise.
The values of the dictionary may be given as a tuple, a list of tuples or another dictionary.
The first tuple entry always refers to the name of the metadata you want to append to your object. The second entry realizes said attribute and may either be a single value or a dictionary if you want to break the attribute down into smaller pieces (e.g. describing *multiple* dimensions of a table).

_Using the parser to create OpenAPI-conform YAML_

After annotating your code, you may parse its information into a standardized YAML file using our dedicated parser (`openapi_generator.py`).

Navigate to `Python\openapi-generator` and use it as follows:
```
python -m openapi_generator -m <FILE_TO_PARSE> -o <OUTPUT_FILE_NAME> [--json]
```
The optional `--json` flag at the end creates a JSON file instead of YAML but is not compatible with the rest of the publication pipeline.

### Merging general and technical information in one metadata document

Last but not least, the workflow needs information on both the general as well as the technical side of the software. Since the form and parser focus on two separate sections of the final metadata file - `info` and `components` - merging the two is relatively easy by appending one file's contents to the other's.

## Annotation of datasets
