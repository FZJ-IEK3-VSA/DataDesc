# Publication of DataDesc documents on various platforms

Table of contents:

- [Introduction](https://github.com/FZJ-IEK3-VSA/DataDesc/tree/main/tools/publication#introduction)
- [Publication of software metadata on...](https://github.com/FZJ-IEK3-VSA/DataDesc/tree/main/tools/publication#publication-of-software-metadata-on...)
    - [GitHub](https://github.com/FZJ-IEK3-VSA/DataDesc/tree/main/tools/publication#github)
    - [Python Package Index (PyPi)](https://github.com/FZJ-IEK3-VSA/DataDesc/tree/main/tools/publication#python-package-index-(pypi))
    - [ReadTheDocs](https://github.com/FZJ-IEK3-VSA/DataDesc/tree/main/tools/publication#readthedocs)
    - [SwaggerHub](https://github.com/FZJ-IEK3-VSA/DataDesc/tree/main/tools/publication#swaggerhub)
    - [Open Research Knowledge Graph (ORKG)](https://github.com/FZJ-IEK3-VSA/DataDesc/tree/main/tools/publication#open-research-knowledge-graph-(orkg))

## Introduction

All information on the software needed for publishing it is stored in the merged metadata file.

However, for most platforms, you need to provide some sort of Authorization (such as an Access Token or login credentials) to have it automatically uploaded by the pipeline.
All relevant info may be added in the `config.sh` file of this folder.
Afterwards, feel free to initiate **any** of the surrounding publication processes by running the appropriate shell script (`*.sh`) from the command line.

## Publication of software metadata on...

### GitHub
Executing the `github_pub.sh` script requires to have filled in `$TITLE`, `$DESCRIPTION`, `$REPO_PRIV`, `$REPO_TEMP`, `$GIT_AUTH`, `$GIT_OWNER`, `$RELEASE_NOTES`, `$LICENSE_NAME`, `$CONTACT_NAME`, `$FUNDER`, and `$FUNDING` in the `config.sh` file. The script then creates a new repository on GitHub by authenticating on the user's behalf and creates a `README.md` according to the given information which is added alongside the contents of the current working directory. The metadata sheet is added to the repository in respect to its position in the working directory.

### Python Package Index (PyPi)
`pypi_pub.sh` automates the process of creating a Python package, generating source distribution files using `Twine` and publishing the package to the Python Package Index (PyPI). It is dependant on the variables `$TITLE`, `$VERSION`, `$LICENSE_NAME`, `$CONTACT_NAME`, `$CONTACT_EMAIL`, `$REPOSITORY`, `$KEYWORDS`, `$PYPI_USER`, and `$PYPI_PASS`. configured in the `config.sh` file.

### ReadTheDocs
The script `readthedocs_pub.sh` is dependant on the variables `$TITLE`, `$CONTACT_NAME`, `$VERSION`, `$REPOSITORY`, and `$RTD_AUTH` of the `config.sh` file. It sets up a rudimentary Sphinx documentation for a Python project, creating or updating the project on ReadTheDocs and triggering the documentation build. The information for the project is sourced from the configuration file.

### SwaggerHub
The `swaggerhub_push.sh` file takes the metadata sheet (`$YAML_URL`) in its entirety and uploads it to `swaggerhub.com` using the user's credentials (`$SWAGGER_USER`, `$SWAGGER_AUTH`) under the name `$TITLE` configured in `config.sh`. Note that publishing the DataDesc metadata sheet on SwaggerHub is bound to yield errors, as DataDesc is largely inspired by `OpenAPI` but not entirely compatible with it.

### Open Research Knowledge Graph (ORKG)
Uploading to `Open Research Knowledge Graph` is more complex. For now, `filename`, `orkg hostname` and `username` have to be changed in the `orkg_uploader.py` script itself (line 118ff.) The script then parses information from the provided file and restructures it in a way that is fit for the `ORKG` using a template provided by the `orkg_connector` class. The upload itself is also handled through the `orkg_connector`. 