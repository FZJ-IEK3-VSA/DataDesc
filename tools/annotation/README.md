# Annotation of research data artifacts with the DataDesc schema

Table of contents:

- [Annotation of research software](https://github.com/FZJ-IEK3-VSA/DataDesc/tree/main/tools/annotation#annotation-of-research-software)
    - [General information about a software](https://github.com/FZJ-IEK3-VSA/DataDesc/tree/main/tools/annotation#general-information-about-a-software)
    - [Technical information about a software interface](https://github.com/FZJ-IEK3-VSA/DataDesc/tree/main/tools/annotation#technical-information-about-a-software-interface)
    - [Merging general and technical information in one DataDesc document](https://github.com/FZJ-IEK3-VSA/DataDesc/tree/main/tools/annotation#merging-general-and-technical-information-in-one-datadesc-document)
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

Afterwards, generate and download your metadata file using the `generate meta.json` button underneath the form.

### Technical information about a software interface

To allow for maximum robustness against user error, we propose a new non-invasive way of annotating software interfaces by leveraging Python's typing.Annotated for type hint checking. This method does not require any external packages or installation and can be performed simply by running the `generator_annotated.py` script in `datadesc-generator` folder.

_Usage_

In Python, `typing.Annotated` is used to add metadata or annotations to type hints. It allows a user to attach additional information to a type hint, which is then parsed by the `generator_annotated.py` script to create a DataDesc compliant metadata sheet. The inclusion of `typing.Annotated` might introduce a small amount of refactoring in existing code to fully leverage its potential but is otherwise non-destructive.
```
# Limited information: data type and default value 
my_price : float = 9.99

# Additional context metadata
my_price : Annotated[ float, { "currency" : "EUR", "toUSD" : 1.2 } ] = 9.99
```

Here, `Annotated` takes two arguments. The first argument is the base type (`float` in this case), and the second argument is a dictionary containing metadata. In the example, the metadata includes two key-value pairs: `currency` with the value `EUR` and `toUSD` with the value `1.2`.

This allows you to provide additional information about the variable's intended usage, special constraints, or any other relevant details.

_Using the parser to create DataDesc-conform JSON_

After annotating your code, you may parse its information into a standardized YAML file using our dedicated parser (`generator_annotated.py`).

Navigate to `datadesc-generator` and use it as follows:
```
python -m generator_annotated -m <FILE_TO_PARSE> -o <OUTPUT_FILE_NAME>
```

### Merging general and technical information in one DataDesc document

Last but not least, the workflow needs information on both the general as well as the technical side of the software. Since the form and parser focus on two separate sections of the final metadata file - `info` and `components` - merging the two is relatively easy by appending one file's contents to the other's.

## Annotation of datasets

As of now, datasets can only be manually annotated using the DataDesc schema. Refer to the [*DataDesc Schema Examples section*](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#netcdf--xarray) for details.
