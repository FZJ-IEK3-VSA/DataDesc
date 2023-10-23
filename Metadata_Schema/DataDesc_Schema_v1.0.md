# DataDesc Schema v1.0

Table of contents:

- [Introduction](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#introduction)
- [DataDesc Schema](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#datadesc-schema)
- [DataDesc Properties](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#datadesc-properties)
- [DataDesc Document](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#datadesc-document)
- [Examples](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#examples)

## Introduction

The DataDesc schema is a metadata schema developed for the description of research software. In addition to capturing general information relevant to the scientific context, it aims in particular at the detailed documentation of software interfaces. The programming language agnostic schema offers the possibility to treat all functions of an interface and its input and output parameters individually and to define permissible data contents, formats, structures and value ranges. The structured capture of information, which is often only available in this level of detail in the form of instructions and specifications written in free text, enables their automated processing and increases their findability and comparability. Mapping them as machine-actionable metadata allows both humans and computers to discover and understand the capabilities of a software, interact with it, and integrate it with other programs and data without having to refer to the source code or further documentation.

The structure and content of the DataDesc schema is based on the OpenAPI specification, which is a widely used language for the standardized description of web interfaces based on HTTP and REST. However, since research software mostly does not follow a client-server architecture and is not provided as services accessible via web interfaces, DataDesc does not focus on the transmission of data via HTTP requests to be processed on the server side, but on the permissible use of locally installed programs. Largely adopted from OpenAPI are the hierarchically organized documentation structures, which allow code-near descriptions of interface elements. Furthermore, the data type specifications based on JSON Schema are used, with which even nested data models used by an interface can be mapped in detail.

In the area of the general description of research software, the CodeMeta metadata standard and the Schema.org ontology on which it is based were closely followed, and adopted metadata elements were integrated within the hierarchical documentation structure. As a result, the DataDesc schema is largely compatible with both the OpenAPI and the Schema.org or CodeMeta standards and minimizes the amount of necessarily individually defined terminology. This is explicitly shown by the mappings presented in this documentation, which can be used to translate the elements of the DataDesc schema into those of OpenAPI and Schema.org. In addition, the QUDT ontology was used as a basis for the units of measurement.

Meaning of the property descriptions used in this documentation:
- Property: The property describes a characteristic of an object. The name of the property is used within the schema as an identifier of the characteristic.
- Label: The label adds context to the property name, if necessary. It quickly conveys the meaning of the property, but is also short enough to be easily displayed in tables and documentation snippets.
- Data Type/Format: States the data type in which values can be specified for the property. The data types used in this schema are _string_, _number_, _integer_, _boolean_, _array_, and _object_. A _number_ can be a floating-point number, but also an _integer_. Furthermore, a specific format of a data type can be stated. A _string_ can be of format _date_, _uri_, _url_, or _email_. _date_ follows a 'yyyy-mm-dd' notation. The other string formats add contextual meaning, but are not defined as part of this documentation. The format of an _object_ is given as a schema reference. With this description of data types and formats the [OpenAPI specification](https://swagger.io/docs/specification/data-models/data-types/) is followed.
- Required: This characteristic indicates whether the description of the property is mandatory for the DataDesc specification. Along the OpenAPI specification, only the properties that are essential for data consistency and interoperability are marked as required.
- OpenAPI Mapping: To increase interoperability, this description provides an explicit mapping of the DataDesc properties to the elements of the OpenAPI specification. Where no corresponding OpenAPI element exists, the DataDesc property is prefixed with a `x-`, constituting a custom extension of the OpenAPI standard.
- Schema.org Mapping: To increase interoperability, this description provides an explicit mapping of the DataDesc properties to the metadata fields of the Schema.org standard. Missing Schema.org equivalents are marked with a `—`.
- Definition: Contains the definition of the property. Additionally, examples and notes may be given. If the definitions are borrowed from or based on another source, the source is referenced.
- Used in: Lists cross references to DataDesc objects in which the property is used.
- URI: Names a string that acts as an identifier for the property. The string is a URL that points to the corresponding paragraph in this document. The URL can be used to uniquely reference the DataDesc property in external resources.

## DataDesc Schema

### **DataDesc Object**
This is the root object of the DataDesc document.<br>
Conforms to OpenAPI's [OpenAPI Object](https://swagger.io/specification/).

| Property                                                                                     | Label                         | Data Type/Format                                                                                        | Required                         | OpenAPI Mapping                                                                   | Schema.org Mapping                                            |
| -------------------------------------------------------------------------------------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------- | -------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| [dataDescVersion](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#dataDescVersion)           | DataDesc version              | string                                                                                                  | True                             | x-dataDescVersion                                                                 | —                                                             |
| [openapi](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#openapi)                           | OpenAPI version               | string                                                                                                  | True                             | [openapi](https://swagger.io/specification/)                                      | —                                                             |
| [externalDocs](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#externalDocs)                 | External documentations       | array[object/[External Documentation Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#external-documentation-object)] | False       | [externalDocs](https://swagger.io/specification/)                                 | —                                                             |
| [info](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#info)                                 | General software information  | object/[Info Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#info-object)                       | True                             | [info](https://swagger.io/specification/)                                         | —                                                             |
| [apiFunctions](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#apiFunctions)                 | API functions                 | array[object/[API Function Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#api-function-object)] | False                           | x-apiFunctions                                                                    | —                                                             |

### **External Documentation Object**
The object allows referencing an external resource for extended documentation.<br>
Conforms to OpenAPI's [External Documentation Object](https://swagger.io/specification/).

| Property                                                                                     | Label                         | Data Type/Format                                                                                        | Required                         | OpenAPI Mapping                                                                   | Schema.org Mapping                                            |
| -------------------------------------------------------------------------------------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------- | -------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| [description](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#description)                   | Description                   | string                                                                                                  | False                            | [description](https://swagger.io/specification/)                                  | [description](https://schema.org/description)                 |
| [url](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#url)                                   | URL                           | string/url                                                                                              | False                            | [url](https://swagger.io/specification/)                                          | [url](https://schema.org/url)                                 |

### **Info Object**
The object provides metadata about the software.<br>
Conforms to OpenAPI's [Info Object](https://swagger.io/specification/).

| Property                                                                                     | Label                         | Data Type/Format                                                                                        | Required                         | OpenAPI Mapping                                                                   | Schema.org Mapping                                            |
| -------------------------------------------------------------------------------------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------- | -------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| [identifier](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#identifier)                     | Identifier                    | string                                                                                                  | False                            | [identifier](https://swagger.io/specification/)                                   | [identifier](https://schema.org/identifier)                   |
| [title](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#title)                               | Software title                | string                                                                                                  | True                             | [title](https://swagger.io/specification/)                                        | [name](https://schema.org/name)                               |
| [description](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#description)                   | Description                   | string                                                                                                  | False                            | [description](https://swagger.io/specification/)                                  | [description](https://schema.org/description)                 |
| [contact](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#contact)                           | Contact information           | object/[Contact Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#contact-object)                 | False                            | [contact](https://swagger.io/specification/)                                      | [ContactPoint](https://schema.org/ContactPoint)               |
| [license](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#license)                           | License information           | object/[License Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#license-object)                 | False                            | [license](https://swagger.io/specification/)                                      | —                                                             |
| [version](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#version)                           | Software version              | string                                                                                                  | True                             | [version](https://swagger.io/specification/)                                      | [softwareVersion](https://schema.org/softwareVersion)         |
| [codeRepository](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#codeRepository)             | Software repository URL       | string/url                                                                                              | False                            | x-codeRepository                                                                  | [codeRepository](https://schema.org/codeRepository)           |
| [programmingLanguages](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#programmingLanguages) | Programming languages         | array[string]                                                                                           | False                            | x-programmingLanguages                                                            | [programmingLanguage](https://schema.org/programmingLanguage) |
| [downloadUrl](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#downloadUrl)                   | Software download URL         | string/url                                                                                              | False                            | x-downloadUrl                                                                     | [downloadUrl](https://schema.org/downloadUrl)                 |
| [authors](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#authors)                           | Authors of the creative work  | array[object/[Person Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#person-object)]            | False                            | x-authors                                                                         | [author](https://schema.org/author)                           |
| [copyrightHolders](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#copyrightHolders)         | Copyright holders             | array[object/[Organization Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#organization-object) and/or [Person Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#person-object)] | False | x-copyrightHolders    | [copyrightHolder](https://schema.org/copyrightHolder)         |
| [copyrightYear](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#copyrightYear)               | Copyright year                | string                                                                                                  | False                            | x-copyrightYear                                                                   | [copyrightYear](https://schema.org/copyrightYear)             |
| [datePublished](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#datePublished)               | Date published                | string/date                                                                                             | False                            | x-datePublished                                                                   | [datePublished](https://schema.org/datePublished)             |
| [keywords](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#keywords)                         | Keywords                      | array[string]                                                                                           | False                            | x-keywords                                                                        | [keywords](https://schema.org/keywords)                       |
| [funders](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#funders)                           | Funders                       | array[object/[Organization Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#organization-object) and/or [Person Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#person-object)] | False | x-funders             | [funder](https://schema.org/funder)                           |
| [fundings](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#fundings)                         | Funding sources               | array[string]                                                                                           | False                            | x-fundings                                                                        | [funding](https://schema.org/funding)                         |
| [referencePublication](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#referencePublication) | Reference publication         | object/[Scholarly Article Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#scholarly-article-object) | False                        | x-referencePublication                                                            | —                                                             |
| [readme](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#readme)                             | Readme URL                    | string/url                                                                                              | False                            | x-readme                                                                          | —                                                             |

### **Contact Object**
Contact information for the software.<br>
Conforms to OpenAPI's [Contact Object](https://swagger.io/specification/) and Schema.org's [ContactPoint Object](https://schema.org/ContactPoint).

| Property                                                                                     | Label                         | Data Type/Format                                                                                        | Required                         | OpenAPI Mapping                                                                   | Schema.org Mapping                                            |
| -------------------------------------------------------------------------------------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------- | -------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| [name](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#name)                                 | Name                          | string                                                                                                  | False                            | [name](https://swagger.io/specification/)                                         | [name](https://schema.org/name)                               |
| [url](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#url)                                   | URL                           | string/url                                                                                              | False                            | [url](https://swagger.io/specification/)                                          | [url](https://schema.org/url)                                 |
| [email](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#email)                               | Email                         | string/email                                                                                            | False                            | [email](https://swagger.io/specification/)                                        | [email](https://schema.org/email)                             |

### **License Object**
License information for the software.<br>
Conforms to OpenAPI's [License Object](https://swagger.io/specification/).

| Property                                                                                     | Label                         | Data Type/Format                                                                                        | Required                         | OpenAPI Mapping                                                                   | Schema.org Mapping                                            |
| -------------------------------------------------------------------------------------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------- | -------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| [name](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#name)                                 | Name                          | string                                                                                                  | True                             | [name](https://swagger.io/specification/)                                         | [name](https://schema.org/name)                               |
| [identifier](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#identifier)                     | Identifier                    | string                                                                                                  | False                            | [identifier](https://swagger.io/specification/)                                   | [identifier](https://schema.org/identifier)                   |
| [url](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#url)                                   | URL                           | string/url                                                                                              | False                            | [url](https://swagger.io/specification/)                                          | [url](https://schema.org/url)                                 |

### **Person Object**
The object provides metadata about a person.<br>
Conforms to Schema.org's [Person Object](https://schema.org/Person).

| Property                                                                                     | Label                         | Data Type/Format                                                                                        | Required                         | OpenAPI Mapping                                                                   | Schema.org Mapping                                            |
| -------------------------------------------------------------------------------------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------- | -------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| [identifier](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#identifier)                     | Identifier                    | string                                                                                                  | False                            | [identifier](https://swagger.io/specification/)                                   | [identifier](https://schema.org/identifier)                   |
| [givenName](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#givenName)                       | Given name                    | string                                                                                                  | False                            | x-givenName                                                                       | [givenName](https://schema.org/givenName)                     |
| [additionalName](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#additionalName)             | Additional name               | string                                                                                                  | False                            | x-additionalName                                                                  | [additionalName](https://schema.org/additionalName)           |
| [familyName](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#familyName)                     | Family name                   | string                                                                                                  | False                            | x-familyName                                                                      | [familyName](https://schema.org/familyName)                   |
| [honorificPrefix](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#honorificPrefix)           | Honorific prefix              | string                                                                                                  | False                            | x-honorificPrefix                                                                 | [honorificPrefix](https://schema.org/honorificPrefix)         |
| [honorificSuffix](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#honorificSuffix)           | Honorific suffix              | string                                                                                                  | False                            | x-honorificSuffix                                                                 | [honorificSuffix](https://schema.org/honorificSuffix)         |
| [affiliation](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#affiliation)                   | Affiliation                   | object/[Organization Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#organization-object)       | False                            | x-affiliation                                                                     | [affiliation](https://schema.org/affiliation)                 |
| [jobTitle](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#jobTitle)                         | Job title                     | string                                                                                                  | False                            | x-jobTitle                                                                        | [jobTitle](https://schema.org/jobTitle)                       |
| [url](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#url)                                   | URL                           | string/url                                                                                              | False                            | [url](https://swagger.io/specification/)                                          | [url](https://schema.org/url)                                 |
| [email](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#email)                               | Email                         | string/email                                                                                            | False                            | [email](https://swagger.io/specification/)                                        | [email](https://schema.org/email)                             |
| [telephone](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#telephone)                       | Telephone number              | string                                                                                                  | False                            | x-telephone                                                                       | [telephone](https://schema.org/telephone)                     |

### **Organization Object**
The object provides metadata about an organization.<br>
Conforms to Schema.org's [Organization Object](https://schema.org/Organization).

| Property                                                                                     | Label                         | Data Type/Format                                                                                        | Required                         | OpenAPI Mapping                                                                   | Schema.org Mapping                                            |
| -------------------------------------------------------------------------------------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------- | -------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| [legalName](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#legalName)                       | Legal name                    | string                                                                                                  | False                            | x-legalName                                                                       | [legalName](https://schema.org/legalName)                     |
| [alternateName](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#alternateName)               | Alternate name                | string                                                                                                  | False                            | x-alternateName                                                                   | [alternateName](https://schema.org/alternateName)             |
| [url](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#url)                                   | URL                           | string/url                                                                                              | False                            | [url](https://swagger.io/specification/)                                          | [url](https://schema.org/url)                                 |
| [email](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#email)                               | Email                         | string/email                                                                                            | False                            | [email](https://swagger.io/specification/)                                        | [email](https://schema.org/email)                             |
| [telephone](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#telephone)                       | Telephone number              | string                                                                                                  | False                            | x-telephone                                                                       | [telephone](https://schema.org/telephone)                     |

### **Scholarly Article Object**
The object provides metadata about a scholarly article.<br>
Conforms to Schema.org's [ScholarlyArticle Object](https://schema.org/ScholarlyArticle).

| Property                                                                                     | Label                         | Data Type/Format                                                                                        | Required                         | OpenAPI Mapping                                                                   | Schema.org Mapping                                            |
| -------------------------------------------------------------------------------------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------- | -------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| [identifier](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#identifier)                     | Identifier                    | string                                                                                                  | False                            | [identifier](https://swagger.io/specification/)                                   | [identifier](https://schema.org/identifier)                   |
| [headline](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#headline)                         | Article title                 | string                                                                                                  | False                            | x-headline                                                                        | [headline](https://schema.org/headline)                       |
| [authors](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#author)                            | Authors of the creative work  | array[object/[Person Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#person-object)]            | False                            | x-authors                                                                         | [author](https://schema.org/author)                           |
| [datePublished](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#datePublished)               | Date published                | string/date                                                                                             | False                            | x-datePublished                                                                   | [datePublished](https://schema.org/datePublished)             |
| [journal](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#journal)                           | Journal                       | string                                                                                                  | False                            | x-journal                                                                         | —                                                             |
| [volumeNumber](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#volumeNumber)                 | Volume Number                 | integer                                                                                                 | False                            | x-volumeNumber                                                                    | [volumeNumber](https://schema.org/volumeNumber)               |
| [pageStart](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#pageStart)                       | Page Start                    | integer                                                                                                 | False                            | x-pageStart                                                                       | [pageStart](https://schema.org/pageStart)                     |
| [pageEnd](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#pageEnd)                           | Page End                      | integer                                                                                                 | False                            | x-pageEnd                                                                         | [pageEnd](https://schema.org/pageEnd)                         |

### **API Function Object**
The object describes an exposed API function.<br>
The structure of this object is based on OpenAPI's [Operation Object](https://swagger.io/specification/).

| Property                                                                                     | Label                         | Data Type/Format                                                                                        | Required                         | OpenAPI Mapping                                                                   | Schema.org Mapping                                            |
| -------------------------------------------------------------------------------------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------- | -------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| [identifier](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#identifier)                     | Identifier                    | string                                                                                                  | True                             | [identifier](https://swagger.io/specification/)                                   | [identifier](https://schema.org/identifier)                   |
| [description](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#description)                   | Description                   | string                                                                                                  | False                            | [description](https://swagger.io/specification/)                                  | [description](https://schema.org/description)                 |
| [deprecated](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#deprecated)                     | This object is deprecated     | boolean                                                                                                 | False                            | [deprecated](https://swagger.io/specification/)                                   | —                                                             |
| [inputVariables](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#inputVariables)             | Input variables               | array[object/[Variable Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#variable-object)]        | False                            | x-inputVariables                                                                  | —                                                             |
| [outputVariables](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#outputVariables)           | Output variables              | array[object/[Variable Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#variable-object)]        | False                            | x-outputVariables                                                                 | —                                                             |

### **Variable Object**
The object describes a single function parameter.<br>
The structure of this object is based on OpenAPI's [Parameter Object](https://swagger.io/specification/).

| Property                                                                                     | Label                         | Data Type/Format                                                                                        | Required                         | OpenAPI Mapping                                                                   | Schema.org Mapping                                            |
| -------------------------------------------------------------------------------------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------- | -------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| [identifier](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#identifier)                     | Identifier                    | string                                                                                                  | True                             | [identifier](https://swagger.io/specification/)                                   | [identifier](https://schema.org/identifier)                   |
| [description](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#description)                   | Description                   | string                                                                                                  | False                            | [description](https://swagger.io/specification/)                                  | [description](https://schema.org/description)                 |
| [required](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#required)                         | Value input is required       | boolean                                                                                                 | False                            | [required](https://swagger.io/specification/)                                     | [valueRequired](https://schema.org/valueRequired)             |
| [deprecated](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#deprecated)                     | This object is deprecated     | boolean                                                                                                 | False                            | [deprecated](https://swagger.io/specification/)                                   | —                                                             |
| [dataSchema](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#dataSchema)                     | Data schema                   | object/[Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#data-schema-object)         | True                             | x-dataSchema                                                                      | —                                                             |

### **Data Schema Object**
The schema object allows the data type definition of a variable. These types can be primitives, but also (nested) arrays and objects.<br>
The structure of this object is based on OpenAPI's [Schema Object](https://swagger.io/specification/).
<mark>
Wohin?: characterEncoding: Definition: The character encoding of a file. Examples: UTF-8, UTF-16, ...
https://www.iana.org/assignments/character-sets/character-sets.xhtml; https://www.iana.org/assignments/media-types/media-types.xhtml; application/vnd.ms-excel; application/netcdf
</mark>
<mark>Expected values; noch nicht zufrieden mit required properties</mark>

| Property                                                                                     | Label                         | Data Type/Format                                                                                        | Required                         | OpenAPI Mapping                                                                   | Schema.org Mapping                                            |
| -------------------------------------------------------------------------------------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------- | -------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| [identifier](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#identifier)                     | Identifier                    | string                                                                                                  | False                            | [identifier](https://swagger.io/specification/)                                   | [identifier](https://schema.org/identifier)                   |
| [description](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#description)                   | Description                   | string                                                                                                  | False                            | [description](https://swagger.io/specification/)                                  | [description](https://schema.org/description)                 |
| [semanticConcept](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#semanticConcept)           | Semantic concept reference    | string/uri                                                                                              | False                            | x-semanticConcept                                                                 | —                                                             |
| [type](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#type)                                 | Data type                     | string                                                                                                  | True                             | [type](https://swagger.io/docs/specification/data-models/data-types/)             | [DataType](https://schema.org/DataType)                       |
| [format](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#format)                             | Data format                   | string or object                                                                                        | False                            | [format](https://swagger.io/docs/specification/data-models/data-types/)           | —                                                             |
| [minimum](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#minimum)                           | Minimum value                 | number                                                                                                  | False                            | [minimum](https://swagger.io/docs/specification/data-models/data-types/)          | [minValue](https://schema.org/minValue)                       |
| [maximum](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#maximum)                           | Maximum value                 | number                                                                                                  | False                            | [maximum](https://swagger.io/docs/specification/data-models/data-types/)          | [maxValue](https://schema.org/maxValue)                       |
| [exclusiveMinimum](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#exclusiveMinimum)         | Minimum value is exclusive    | boolean                                                                                                 | False                            | [exclusiveMinimum](https://swagger.io/docs/specification/data-models/data-types/) | —                                                             |
| [exclusiveMaximum](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#exclusiveMaximum)         | Maximum value is exclusive    | boolean                                                                                                 | False                            | [exclusiveMaximum](https://swagger.io/docs/specification/data-models/data-types/) | —                                                             |
| [multipleOf](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#multipleOf)                     | Multiple of                   | number                                                                                                  | False                            | [multipleOf](https://swagger.io/docs/specification/data-models/data-types/)       | [stepValue](https://schema.org/stepValue)                     |
| [minLength](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#minLength)                       | Minimum length of string      | integer                                                                                                 | False                            | [minLength](https://swagger.io/docs/specification/data-models/data-types/)        | [valueMinLength](https://schema.org/valueMinLength)           |
| [maxLength](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#maxLength)                       | Maximum length of string      | integer                                                                                                 | False                            | [maxLength](https://swagger.io/docs/specification/data-models/data-types/)        | [valueMaxLength](https://schema.org/valueMaxLength)           |
| [pattern](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#pattern)                           | Pattern                       | string                                                                                                  | False                            | [pattern](https://swagger.io/docs/specification/data-models/data-types/)          | [valuePattern](https://schema.org/valuePattern)               |
| [items](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#items)                               | Data schema of array items    | array[object/[Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#data-schema-object)]  | False                            | [items](https://swagger.io/docs/specification/data-models/data-types/)            | —                                                             |
| [minItems](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#minItems)                         | Minimum length of array       | integer                                                                                                 | False                            | [minItems](https://swagger.io/docs/specification/data-models/data-types/)         | —                                                             |
| [maxItems](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#maxItems)                         | Maximum length of array       | integer                                                                                                 | False                            | [maxItems](https://swagger.io/docs/specification/data-models/data-types/)         | —                                                             |
| [uniqueItems](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#uniqueItems)                   | Items have to be unique       | boolean                                                                                                 | False                            | [uniqueItems](https://swagger.io/docs/specification/data-models/data-types/)      | —                                                             |
| [properties](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#properties)                     | List of object properties     | array[object/[Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#data-schema-object)]  | False                            | [properties](https://swagger.io/docs/specification/data-models/data-types/)       | —                                                             |
| [requiredProperties](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#requiredProperties)     | List of required properties   | array[string]                                                                                           | False                            | [required](https://swagger.io/docs/specification/data-models/data-types/)         | [valueRequired](https://schema.org/valueRequired)             |
| [unit](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#unit)                                 | Unit reference                | string or string/uri                                                                                    | False                            | x-unit                                                                            | [unitCode](https://schema.org/unitCode)                       |
| [quantityKind](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#quantityKind)                 | Quantity kind reference       | string or string/uri                                                                                    | False                            | x-quantityKind                                                                    | —                                                             |
| [nullable](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#nullable)                         | Null value is allowed         | boolean                                                                                                 | False                            | [nullable](https://swagger.io/docs/specification/data-models/data-types/)         | —                                                             |
| [dimensions](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#dimensions)                     | Dimensions                    | array[object/[Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#data-schema-object)]  | False                            | x-dimensions                                                                      | —                                                             |
| [enum](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#enum)                                 | Enumeration of allowed values | _same as type_                                                                                          | False                            | [enum](https://swagger.io/docs/specification/data-models/enums/)                  | —                                                             |
| [default](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#default)                           | Default value                 | _same as type_                                                                                          | False                            | [default](https://swagger.io/docs/specification/describing-parameters/)           | [defaultValue](https://schema.org/defaultValue)               |
| [example](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#example)                           | Example value                 | _same as type_                                                                                          | False                            | [example](https://swagger.io/docs/specification/adding-examples/)                 | —                                                             |
| [mediaType](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#mediaType)                       | Media type                    | string                                                                                                  | False                            | [mediaType](https://swagger.io/docs/specification/media-types/)                   | [encodingFormat](https://schema.org/encodingFormat)           |
| [charSet](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#charSet)                           | Character set                 | string                                                                                                  | False                            | [charSet](https://swagger.io/docs/specification/media-types/)                     | —                                                             |

## DataDesc Properties

### additionalName

|                     |     |
| ------------------- | --- |
| Definition:         | An additional name for a Person, can be used for a middle name. (cf. [Schema.org: additionalName](https://schema.org/additionalName)) |
| Label:              | Additional name |
| Data type/format:   | string |
| Used in:            | [Person Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#person-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#additionalName |
| OpenAPI mapping:    | x-additionalName |
| Schema.org mapping: | [additionalName](https://schema.org/additionalName) |

### affiliation

|                     |     |
| ------------------- | --- |
| Definition:         | An organization that this person is affiliated with. For example, a school/university, a club, or a team. (cf. [Schema.org: affiliation](https://schema.org/affiliation)) |
| Label:              | Affiliation |
| Data type/format:   | object/[Organization Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#organization-object) |
| Used in:            | [Person Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#person-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#affiliation |
| OpenAPI mapping:    | x-affiliation |
| Schema.org mapping: | [affiliation](https://schema.org/affiliation) |

### alternateName

|                     |     |
| ------------------- | --- |
| Definition:         | An alias for the item. (cf. [Schema.org: alternateName](https://schema.org/alternateName)) |
| Label:              | Alternate Name |
| Data type/format:   | string |
| Used in:            | [Organization Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#organization-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#alternateName |
| OpenAPI mapping:    | x-alternateName |
| Schema.org mapping: | [alternateName](https://schema.org/alternateName) |

### apiFunctions

|                     |     |
| ------------------- | --- |
| Definition:         | Holds the software's exposed API functions. |
| Label:              | API functions |
| Data type/format:   | array[object/[API Function Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#api-function-object)] |
| Used in:            | [DataDesc Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#datadesc-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#apiFunctions |
| OpenAPI mapping:    | x-apiFunctions |
| Schema.org mapping: | — |

### authors

|                     |     |
| ------------------- | --- |
| Definition:         | The authors of this content or rating. (cf. [Schema.org: author](https://schema.org/author)) |
| Label:              | Authors of the creative work |
| Data type/format:   | array[object/[Person Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#person-object)] |
| Used in:            | [Info Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#info-object), [Scholarly Article Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#scholarly-article-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#authors |
| OpenAPI mapping:    | x-authors |
| Schema.org mapping: | [author](https://schema.org/author) |

### charSet

|                     |     |
| ------------------- | --- |
| Definition:         | Specifies a collection of characters and its encoding used to represent text in a computer system. |
| Label:              | Character set |
| Data type/format:   | string |
| Used in:            | [Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#data-schema-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#charSet |
| OpenAPI mapping:    | [charSet](https://swagger.io/docs/specification/media-types/) |
| Schema.org mapping: | — |

### codeRepository

|                     |     |
| ------------------- | --- |
| Definition:         | Link to the repository where the un-compiled, human readable code and related code is located (SVN, GitHub, CodePlex). (cf. [Schema.org: codeRepository](https://schema.org/codeRepository)) |
| Label:              | Software repository URL |
| Data type/format:   | string (URL) |
| Used in:            | [Info Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#info-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#codeRepository |
| OpenAPI mapping:    | x-codeRepository |
| Schema.org mapping: | [codeRepository](https://schema.org/codeRepository) |

### contact

|                     |     |
| ------------------- | --- |
| Definition:         | The contact information for the exposed API. (cf. [OpenAPI: contact](https://swagger.io/specification/)) |
| Label:              | Contact information |
| Data type/format:   | object/[Contact Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#contact-object) |
| Used in:            | [Info Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#info-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#contact |
| OpenAPI mapping:    | [contact](https://swagger.io/specification/) |
| Schema.org mapping: | [ContactPoint](https://schema.org/ContactPoint) |

### copyrightHolders

|                     |     |
| ------------------- | --- |
| Definition:         | The parties holding the legal copyright to the creative work. (cf. [Schema.org: copyrightHolder](https://schema.org/copyrightHolder)) |
| Label:              | Copyright holders |
| Data type/format:   | array[object/[Organization Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#organization-object) and/or object/[Person Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#person-object)] |
| Used in:            | [Info Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#info-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#copyrightHolders |
| OpenAPI mapping:    | x-copyrightHolders |
| Schema.org mapping: | [copyrightHolder](https://schema.org/copyrightHolder) |

### copyrightYear
<mark>We use "string" instad of Schema.org "number" to allow for year ranges.</mark>
|                     |     |
| ------------------- | --- |
| Definition:         | The year during which the claimed copyright for the CreativeWork was first asserted. (cf. [Schema.org: copyrightYear](https://schema.org/copyrightYear)) |
| Label:              | Copyright year |
| Data type/format:   | string |
| Used in:            | [Info Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#info-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#copyrightYear |
| OpenAPI mapping:    | x-copyrightYear |
| Schema.org mapping: | [copyrightYear](https://schema.org/copyrightYear) |

### dataDescVersion

|                     |     |
| ------------------- | --- |
| Definition:         | The version number of the DataDesc specification that the DataDesc document uses. |
| Label:              | DataDesc version |
| Data type/format:   | string |
| Used in:            | [DataDesc Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#datadesc-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#dataDescVersion |
| OpenAPI mapping:    | x-dataDescVersion |
| Schema.org mapping: | — |

### dataSchema

|                     |     |
| ------------------- | --- |
| Definition:         | Holds the data type definition of a variable. These types can be primitives, but also (nested) arrays and objects. |
| Label:              | Data schema |
| Data type/format:   | object/[Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#data-schema-object) |
| Used in:            | [Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#data-schema-object), [Variable Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#variable-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#dataSchema |
| OpenAPI mapping:    | x-dataSchema |
| Schema.org mapping: | — |

### datePublished

|                     |     |
| ------------------- | --- |
| Definition:         | Date of first broadcast/publication. (cf. [Schema.org: datePublished](https://schema.org/datePublished)) |
| Label:              | Date published |
| Data type/format:   | string/date |
| Used in:            | [Info Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#info-object), [Scholarly Article Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#scholarly-article-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#datePublished |
| OpenAPI mapping:    | x-datePublished |
| Schema.org mapping: | [datePublished](https://schema.org/datePublished) |

### default

|                     |     |
| ------------------- | --- |
| Definition:         | The default value of the input. For properties that expect a literal, the default is a literal value, for properties that expect an object, it's an ID reference to one of the current values. (cf. [Schema.org: defaultValue](https://schema.org/defaultValue)) |
| Label:              | Default value |
| Data type/format:   | _Same as the data type of the described variable_ |
| Used in:            | [Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#data-schema-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#default |
| OpenAPI mapping:    | [default](https://swagger.io/docs/specification/describing-parameters/) |
| Schema.org mapping: | [defaultValue](https://schema.org/defaultValue) |

### deprecated

|                     |     |
| ------------------- | --- |
| Definition:         | Declares whether this object is deprecated. |
| Label:              | This object is deprecated |
| Data type/format:   | boolean |
| Used in:            | [API Function Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#api-function-object), [Variable Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#variable-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#deprecated |
| OpenAPI mapping:    | [deprecated](https://swagger.io/specification/)|
| Schema.org mapping: | — |

### description

|                     |     |
| ------------------- | --- |
| Definition:         | A description of the item. (cf. [Schema.org: description](https://schema.org/description)) |
| Label:              | Description |
| Data type/format:   | string |
| Used in:            | [API Function Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#api-function-object), [Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#data-schema-object), [External Documentation Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#external-documentation-object), [Info Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#info-object), [Variable Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#variable-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#description |
| OpenAPI mapping:    | [description](https://swagger.io/specification/) |
| Schema.org mapping: | [description](https://schema.org/description) |

### dimensions

|                     |     |
| ------------------- | --- |
| Definition:         | Specifies the shape of a multi-dimensional variable. A dimension can represent, e.g., a temporal, geographical or physical resolution but might also be used to index more abstract quantities, e.g., power plant IDs or application scenarios. |
| Label:              | Dimensions |
| Data type/format:   | array[object/[Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#data-schema-object)] |
| Used in:            | [Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#data-schema-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#dimensions |
| OpenAPI mapping:    | x-dimensions |
| Schema.org mapping: | — |

### downloadUrl

|                     |     |
| ------------------- | --- |
| Definition:         | If the file can be downloaded, URL to download the binary. (cf. [Schema.org: downloadUrl](https://schema.org/downloadUrl)) |
| Label:              | Software download URL |
| Data type/format:   | string/url |
| Used in:            | [Info Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#info-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#downloadUrl |
| OpenAPI mapping:    | x-downloadUrl |
| Schema.org mapping: | [downloadUrl](https://schema.org/downloadUrl) |

### email

|                     |     |
| ------------------- | --- |
| Definition:         | Email address. (cf. [Schema.org: email](https://schema.org/email)) |
| Label:              | Email |
| Data type/format:   | string/email |
| Used in:            | contact, organization, person| <mark>sdf</mark>
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#email |
| OpenAPI mapping:    | [email](https://swagger.io/specification/) |
| Schema.org mapping: | [email](https://schema.org/email) |

### enum

|                     |     |
| ------------------- | --- |
| Definition:         | Specifies possible values of a variable. |
| Label:              | Enumeration of allowed values |
| Data type/format:   | _Same as the data type of the described variable_ |
| Used in:            | [Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#data-schema-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#enum |
| OpenAPI mapping:    | [enum](https://swagger.io/docs/specification/data-models/enums/) |
| Schema.org mapping: | — |

### example

|                     |     |
| ------------------- | --- |
| Definition:         | Adds an example value to a variable to make to make its usage clearer. |
| Label:              | Example value |
| Data type/format:   | _Same as the data type of the described variable_ |
| Used in:            | [Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#data-schema-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#example |
| OpenAPI mapping:    | [example](https://swagger.io/docs/specification/adding-examples/) |
| Schema.org mapping: | — |

### exclusiveMaximum

|                     |     |
| ------------------- | --- |
| Definition:         | Declares whether a specified maximum value is excluded. |
| Label:              | Maximum value is exclusive |
| Data type/format:   | boolean |
| Used in:            | [Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#data-schema-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#exclusiveMaximum |
| OpenAPI mapping:    | [exclusiveMaximum](https://swagger.io/docs/specification/data-models/data-types/) |
| Schema.org mapping: | — |

### exclusiveMinimum

|                     |     |
| ------------------- | --- |
| Definition:         | Declares whether a specified minimum value is excluded. |
| Label:              | Minimum value is exclusive |
| Data type/format:   | boolean |
| Used in:            | [Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#data-schema-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#exclusiveMinimum |
| OpenAPI mapping:    | [exclusiveMinimum](https://swagger.io/docs/specification/data-models/data-types/) |
| Schema.org mapping: | — |

### externalDocs

|                     |     |
| ------------------- | --- |
| Definition:         | Additional external documentations. (cf. [OpenAPI: externalDocs](https://swagger.io/specification/)) |
| Label:              | External documentations |
| Data type/format:   | array[object/[External Documentation Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#external-documentation-object)] |
| Used in:            | [DataDesc Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#datadesc-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#externalDocs |
| OpenAPI mapping:    | [externalDocs](https://swagger.io/specification/) |
| Schema.org mapping: | — |

### familyName

|                     |     |
| ------------------- | --- |
| Definition:         | Family name. In the U.S., the last name of a Person. (cf. [Schema.org: familyName](https://schema.org/familyName)) |
| Label:              | Family name |
| Data type/format:   | string |
| Used in:            | [Person Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#person-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#familyName |
| OpenAPI mapping:    | x-familyName |
| Schema.org mapping: | [familyName](https://schema.org/familyName) |

### format

|                     |     |
| ------------------- | --- |
| Definition:         | Further specifies the data type of a variable by hinting at, e.g. specific numeric types or (custom) string formats. This information can be used for data validation. (cf. [OpenAPI: format](https://swagger.io/docs/specification/data-models/data-types/)) |
| Label:              | Data format |
| Data type/format:   | string |
| Used in:            | [Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#data-schema-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#format |
| OpenAPI mapping:    | [format](https://swagger.io/docs/specification/data-models/data-types/) |
| Schema.org mapping: | — |

### funders

|                     |     |
| ------------------- | --- |
| Definition:         | Persons and/or organizations that support (sponsor) something through some kind of financial contribution. (cf. [Schema.org: funder](https://schema.org/funder)) |
| Label:              | Funders |
| Data type/format:   | array[object/[Organization Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#organization-object) and/or object/[Person Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#person-object)] |
| Used in:            | [Info Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#info-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#funders |
| OpenAPI mapping:    | x-funders |
| Schema.org mapping: | [funder](https://schema.org/funder) |

### fundings

|                     |     |
| ------------------- | --- |
| Definition:         | Grants that directly or indirectly provide funding or sponsorship for this item. (cf. [Schema.org: funding](https://schema.org/funding)) |
| Label:              | Funding sources |
| Data type/format:   | array[string] |
| Used in:            | [Info Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#info-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#fundings |
| OpenAPI mapping:    | x-fundings |
| Schema.org mapping: | [funding](https://schema.org/funding) |

### givenName

|                     |     |
| ------------------- | --- |
| Definition:         | Given name. In the U.S., the first name of a Person. (cf. [Schema.org: givenName](https://schema.org/givenName)) |
| Label:              | Given name |
| Data type/format:   | string |
| Used in:            | [Person Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#person-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#givenName |
| OpenAPI mapping:    | x-givenName |
| Schema.org mapping: | [givenName](https://schema.org/givenName) |

### headline

|                     |     |
| ------------------- | --- |
| Definition:         | Headline of the article. (cf. [Schema.org: headline](https://schema.org/headline)) |
| Label:              | Article title |
| Data type/format:   | string |
| Used in:            | [Scholarly Article Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#scholarly-article-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#headline |
| OpenAPI mapping:    | x-headline |
| Schema.org mapping: | [headline](https://schema.org/headline) |

### honorificPrefix

|                     |     |
| ------------------- | --- |
| Definition:         | An honorific prefix preceding a Person's name such as Dr/Mrs/Mr. (cf. [Schema.org: honorificPrefix](https://schema.org/honorificPrefix)) |
| Label:              | Honorific prefix |
| Data type/format:   | string |
| Used in:            | [Person Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#person-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#honorificPrefix |
| OpenAPI mapping:    | x-honorificPrefix |
| Schema.org mapping: | [honorificPrefix](https://schema.org/honorificPrefix) |

### honorificSuffix

|                     |     |
| ------------------- | --- |
| Definition:         | An honorific suffix following a Person's name such as M.D./PhD/MSCSW. (cf. [Schema.org: honorificSuffix](https://schema.org/honorificSuffix)) |
| Label:              | Honorific suffix |
| Data type/format:   | string |
| Used in:            | [Person Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#person-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#honorificSuffix |
| OpenAPI mapping:    | x-honorificSuffix |
| Schema.org mapping: | [honorificSuffix](https://schema.org/honorificSuffix) |

### identifier
<mark>
See https://spdx.org/licenses/ for a list of SPDX License names and identifiers.
orcid
doi
</mark>

|                     |     |
| ------------------- | --- |
| Definition:         | The identifier property represents any kind of identifier for any kind of thing. (cf. [Schema.org: identifier](https://schema.org/identifier)) |
| Label:              | Identifier |
| Data type/format:   | string |
| Used in:            | [API Function Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#api-function-object), [Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#data-schema-object), [Info Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#info-object), [License Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#license-object), [Person Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#person-object), [Scholarly Article Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#scholarly-article-object), [Variable Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#variable-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#identifier |
| OpenAPI mapping:    | [identifier](https://swagger.io/specification/) |
| Schema.org mapping: | [identifier](https://schema.org/identifier) |

### info

|                     |     |
| ------------------- | --- |
| Definition:         | Provides general metadata about the software. |
| Label:              | General software information |
| Data type/format:   | object/[Info Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#info-object) |
| Used in:            | [DataDesc Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#datadesc-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#info |
| OpenAPI mapping:    | [info](https://swagger.io/specification/) |
| Schema.org mapping: | — |

### inputVariables

|                     |     |
| ------------------- | --- |
| Definition:         | Holds a function's input variables. |
| Label:              | Input variables |
| Data type/format:   | array[object/[Variable Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#variable-object)] |
| Used in:            | [API Function Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#api-function-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#inputVariables |
| OpenAPI mapping:    | x-inputVariables |
| Schema.org mapping: | — |

### items

|                     |     |
| ------------------- | --- |
| Definition:         | Holds a schema that is required for arrays, that describes the type and format of array items. (cf. [OpenAPI: items](https://swagger.io/docs/specification/data-models/data-types/)) |
| Label:              | Data schema of array items |
| Data type/format:   | array[object/[Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#data-schema-object)] |
| Used in:            | [Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#data-schema-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#items |
| OpenAPI mapping:    | [items](https://swagger.io/docs/specification/data-models/data-types/) |
| Schema.org mapping: | — |

### jobTitle

|                     |     |
| ------------------- | --- |
| Definition:         | The job title of the person (for example, Financial Manager). (cf. [Schema.org: jobTitle](https://schema.org/jobTitle)) |
| Label:              | Job title |
| Data type/format:   | string |
| Used in:            | [Person Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#person-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#jobTitle |
| OpenAPI mapping:    | x-jobTitle |
| Schema.org mapping: | [jobTitle](https://schema.org/jobTitle) |

### journal

|                     |     |
| ------------------- | --- |
| Definition:         | References a journal in which a scholarly article was published. |
| Label:              | Journal |
| Data type/format:   | string |
| Used in:            | [Scholarly Article Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#scholarly-article-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#journal |
| OpenAPI mapping:    | x-journal |
| Schema.org mapping: | — |

### keywords

|                     |     |
| ------------------- | --- |
| Definition:         | Keywords or tags used to describe some item. Multiple textual entries in a keywords list are typically delimited by commas, or by repeating the property. (cf. [Schema.org: keywords](https://schema.org/keywords)) |
| Label:              | Keywords |
| Data type/format:   | string |
| Used in:            | [Info Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#info-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#keywords |
| OpenAPI mapping:    | x-keywords |
| Schema.org mapping: | [keywords](https://schema.org/keywords) |

### legalName

|                     |     |
| ------------------- | --- |
| Definition:         | The official name of the organization, e.g. the registered company name. (cf. [Schema.org: legalName](https://schema.org/legalName)) |
| Label:              | Legal name |
| Data type/format:   | string |
| Used in:            | [Organization Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#organization-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#legalName |
| OpenAPI mapping:    | x-legalName |
| Schema.org mapping: | [legalName](https://schema.org/legalName) |

### license

|                     |     |
| ------------------- | --- |
| Definition:         | Holds the information about a software's license. |
| Label:              | License information |
| Data type/format:   | object/[License Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#license-object) |
| Used in:            | [Info Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#info-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#license |
| OpenAPI mapping:    | [license](https://swagger.io/specification/) |
| Schema.org mapping: | — |

### maximum

|                     |     |
| ------------------- | --- |
| Definition:         | The upper value of some characteristic or property. (cf. [Schema.org: maxValue](https://schema.org/maxValue)) |
| Label:              | Maximum value |
| Data type/format:   | number |
| Used in:            | [Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#data-schema-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#maximum |
| OpenAPI mapping:    | [maximum](https://swagger.io/docs/specification/data-models/data-types/) |
| Schema.org mapping: | [maxValue](https://schema.org/maxValue) |

### maxItems

|                     |     |
| ------------------- | --- |
| Definition:         | Specifies the maximum length of an array. (cf. [OpenAPI: maxItems](https://swagger.io/docs/specification/data-models/data-types/)) |
| Label:              | Maximum length of array |
| Data type/format:   | integer |
| Used in:            | [Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#data-schema-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#maxItems|
| OpenAPI mapping:    | [maxItems](https://swagger.io/docs/specification/data-models/data-types/) |
| Schema.org mapping: | — |

### maxLength

|                     |     |
| ------------------- | --- |
| Definition:         | Specifies the allowed range for number of characters in a literal value. (cf. [Schema.org: valueMaxLength](https://schema.org/valueMaxLength)) |
| Label:              | Maximum length of string|
| Data type/format:   | integer |
| Used in:            | [Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#data-schema-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#maxLength |
| OpenAPI mapping:    | [maxLength](https://swagger.io/docs/specification/data-models/data-types/) |
| Schema.org mapping: | [valueMaxLength](https://schema.org/valueMaxLength) |

### mediaType

|                     |     |
| ------------------- | --- |
| Definition:         | Specifies the media type and thereby the the format of a file and its data contents. |
| Label:              | Media type |
| Data type/format:   | string |
| Used in:            | [Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#data-schema-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#mediaType |
| OpenAPI mapping:    | [mediaType](https://swagger.io/docs/specification/media-types/) |
| Schema.org mapping: | [encodingFormat](https://schema.org/encodingFormat) |

### minimum

|                     |     |
| ------------------- | --- |
| Definition:         | The lower value of some characteristic or property. (cf. [Schema.org: minValue](https://schema.org/minValue)) |
| Label:              | Minimum value |
| Data type/format:   | number |
| Used in:            | [Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#data-schema-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#minimum |
| OpenAPI mapping:    | [minimum](https://swagger.io/docs/specification/data-models/data-types/) |
| Schema.org mapping: | [minValue](https://schema.org/minValue) |

### minItems

|                     |     |
| ------------------- | --- |
| Definition:         | Specifies the minimum length of an array. (cf. [OpenAPI: minItems](https://swagger.io/docs/specification/data-models/data-types/)) |
| Label:              | Minimum length of array |
| Data type/format:   | integer |
| Used in:            | [Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#data-schema-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#minItems|
| OpenAPI mapping:    | [minItems](https://swagger.io/docs/specification/data-models/data-types/) |
| Schema.org mapping: | — |

### minLength

|                     |     |
| ------------------- | --- |
| Definition:         | Specifies the minimum allowed range for number of characters in a literal value. (cf. [Schema.org: valueMinLength](https://schema.org/valueMinLength)) |
| Label:              | Minimum length of string |
| Data type/format:   | integer |
| Used in:            | [Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#data-schema-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#minLength |
| OpenAPI mapping:    | [minLength](https://swagger.io/docs/specification/data-models/data-types/) |
| Schema.org mapping: | [valueMinLength](https://schema.org/valueMinLength) |

### multipleOf

|                     |     |
| ------------------- | --- |
| Definition:         | Specifies that a number must be the multiple of another number. (cf. [OpenAPI: multipleOf](https://swagger.io/docs/specification/data-models/data-types/)) |
| Label:              | Multiple of |
| Data type/format:   | number |
| Used in:            | [Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#data-schema-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#multipleOf |
| OpenAPI mapping:    | [multipleOf](https://swagger.io/docs/specification/data-models/data-types/) |
| Schema.org mapping: | [stepValue](https://schema.org/stepValue) |

### name

|                     |     |
| ------------------- | --- |
| Definition:         | The name of the item. (cf. [Schema.org: name](https://schema.org/name)) |
| Label:              | Name |
| Data type/format:   | string |
| Used in:            | [Contact Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#contact-object), [License Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#license-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#name |
| OpenAPI mapping:    | [name](https://swagger.io/specification/) |
| Schema.org mapping: | [name](https://schema.org/name) |

### nullable

|                     |     |
| ------------------- | --- |
| Definition:         | Declares whether the null value is allowed. (cf. [OpenAPI: nullable](https://swagger.io/docs/specification/data-models/data-types/)) |
| Label:              | Null value is allowed |
| Data type/format:   | boolean |
| Used in:            | [Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#data-schema-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#nullable |
| OpenAPI mapping:    | [nullable](https://swagger.io/docs/specification/data-models/data-types/) |
| Schema.org mapping: | — |

### openapi

|                     |     |
| ------------------- | --- |
| Definition:         | The version number of the OpenAPI specification that the DataDesc document uses. |
| Label:              | OpenAPI version |
| Data type/format:   | string |
| Used in:            | [DataDesc Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#datadesc-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#openapi |
| OpenAPI mapping:    | [openapi](https://swagger.io/specification/) |
| Schema.org mapping: | — |

### outputVariables

|                     |     |
| ------------------- | --- |
| Definition:         | Holds a function's output variables. |
| Label:              | Output variables |
| Data type/format:   | array[object/[Variable Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#variable-object)] |
| Used in:            | [API Function Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#api-function-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#outputVariables |
| OpenAPI mapping:    | x-outputVariables |
| Schema.org mapping: | — |

### pageEnd

|                     |     |
| ------------------- | --- |
| Definition:         | The page on which the work ends; for example "138" or "xvi". (cf. [Schema.org: pageEnd](https://schema.org/pageEnd)) |
| Label:              | Page End |
| Data type/format:   | integer |
| Used in:            | [Scholarly Article Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#scholarly-article-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#pageEnd |
| OpenAPI mapping:    | x-pageEnd |
| Schema.org mapping: | [pageEnd](https://schema.org/pageEnd) |

### pageStart

|                     |     |
| ------------------- | --- |
| Definition:         | The page on which the work starts; for example "135" or "xiii". (cf. [Schema.org: pageStart](https://schema.org/pageStart)) |
| Label:              | Page Start |
| Data type/format:   | integer |
| Used in:            | [Scholarly Article Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#scholarly-article-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#pageStart |
| OpenAPI mapping:    | x-pageStart |
| Schema.org mapping: | [pageStart](https://schema.org/pageStart) |

### pattern

|                     |     |
| ------------------- | --- |
| Definition:         | Defines a regular expression template for a string value. Only the values that match this template will be accepted. (cf. [OpenAPI: pattern](https://swagger.io/docs/specification/data-models/data-types/)) |
| Label:              | Pattern |
| Data type/format:   | string |
| Used in:            | [Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#data-schema-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#pattern |
| OpenAPI mapping:    | [pattern](https://swagger.io/docs/specification/data-models/data-types/) |
| Schema.org mapping: | [valuePattern](https://schema.org/valuePattern) |

### programmingLanguages

|                     |     |
| ------------------- | --- |
| Definition:         | The computer programming languages. (cf. [Schema.org: programmingLanguage](https://schema.org/programmingLanguage)) |
| Label:              | Programming languages |
| Data type/format:   | array[string] |
| Used in:            | [Info Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#info-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#programmingLanguages |
| OpenAPI mapping:    | x-programmingLanguages |
| Schema.org mapping: | [programmingLanguage](https://schema.org/programmingLanguage) |

### properties

|                     |     |
| ------------------- | --- |
| Definition:         | Holds an object's properties. (cf. [OpenAPI: properties](https://swagger.io/docs/specification/data-models/data-types/)) |
| Label:              | List of object properties |
| Data type/format:   | array[object/[Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#data-schema-object)] |
| Used in:            | [Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#data-schema-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#properties |
| OpenAPI mapping:    | [properties](https://swagger.io/docs/specification/data-models/data-types/) |
| Schema.org mapping: | — |

### quantityKind

|                     |     |
| ------------------- | --- |
| Definition:         | A Quantity Kind is any observable property that can be measured and quantified numerically. Familiar examples include physical properties such as length, mass, time, force, energy, power, electric charge, etc. Less familiar examples include currency, interest rate, price to earning ratio, and information capacity. (cf. [qudt: QuantityKind](https://qudt.org/schema/qudt/QuantityKind)) |
| Label:              | Quantity kind reference |
| Data type/format:   | string or string/uri |
| Used in:            | [Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#data-schema-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#quantityKind |
| OpenAPI mapping:    | x-quantityKind |
| Schema.org mapping: | — |

### readme

|                     |     |
| ------------------- | --- |
| Definition:         | Link to software Readme file. (cf. [CodeMeta: readme](https://codemeta.github.io/terms/)) |
| Label:              | Readme URL |
| Data type/format:   | string/url |
| Used in:            | [Info Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#info-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#readme |
| OpenAPI mapping:    | x-readme |
| Schema.org mapping: | — |

### referencePublication

|                     |     |
| ------------------- | --- |
| Definition:         | An academic publication related to the software. (cf. [CodeMeta: referencePublication](https://codemeta.github.io/terms/)) |
| Label:              | Reference publication |
| Data type/format:   | object/[Scholarly Article Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#scholarly-article-object) |
| Used in:            | [Info Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#info-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#referencePublication |
| OpenAPI mapping:    | x-referencePublication |
| Schema.org mapping: | — |

### required
<mark>
Our schema could specify default falues for certain properties: e.g. requiredProperties. Search for "default" in this markdown.
deprecated: openapi has default values for it. our schema could have default values.
Default values for all booleans?
</mark>

|                     |     |
| ------------------- | --- |
| Definition:         | Whether the property must be filled in to complete the action. Default is false. (cf. [Schema.org: valueRequired](https://schema.org/valueRequired)) |
| Label:              | Value input is required |
| Data type/format:   | boolean |
| Used in:            | [Variable Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#variable-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#required |
| OpenAPI mapping:    | [required](https://swagger.io/specification/) |
| Schema.org mapping: | [valueRequired](https://schema.org/valueRequired) |

### requiredProperties
<mark>required: hat zwei links / zwei formate in openapi</mark>
|                     |     |
| ------------------- | --- |
| Definition:         | Lists all properties of an object that are required. By default, all object properties are optional. (cf. [OpenAPI: type](https://swagger.io/docs/specification/data-models/data-types/)) |
| Label:              | List of required properties |
| Data type/format:   | array[string] |
| Used in:            | [Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#data-schema-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#requiredProperties |
| OpenAPI mapping:    | [required](https://swagger.io/docs/specification/data-models/data-types/) |
| Schema.org mapping: | [valueRequired](https://schema.org/valueRequired) |

### semanticConcept

|                     |     |
| ------------------- | --- |
| Definition:         | References a semantic concept and thus unambiguously specifies the content-related meaning of a variable and its values. |
| Label:              | Semantic concept reference |
| Data type/format:   | string/uri |
| Used in:            | [Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#data-schema-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#semanticConcept |
| OpenAPI mapping:    | x-semanticConcept |
| Schema.org mapping: | — |

### telephone

|                     |     |
| ------------------- | --- |
| Definition:         | The telephone number. (cf. [Schema.org: telephone](https://schema.org/telephone)) |
| Label:              | Telephone number |
| Data type/format:   | string |
| Used in:            | [Organization Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#organization-object), [Person Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#person-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#telephone |
| OpenAPI mapping:    | x-telephone |
| Schema.org mapping: | [telephone](https://schema.org/telephone) |

### title

|                     |     |
| ------------------- | --- |
| Definition:         | The title of the software. (cf. [OpenAPI: title](https://swagger.io/specification/))|
| Label:              | Software title |
| Data type/format:   | string |
| Used in:            | [Info Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#info-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#title |
| OpenAPI mapping:    | [title](https://swagger.io/specification/) |
| Schema.org mapping: | [name](https://schema.org/name) |

### type

|                     |     |
| ------------------- | --- |
| Definition:         | The data type of a schema is defined by the type keyword, for example, type: string. (cf. [OpenAPI: type](https://swagger.io/docs/specification/data-models/data-types/)) |
| Label:              | Data type |
| Data type/format:   | string or object |
| Used in:            | [Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#data-schema-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#type |
| OpenAPI mapping:    | [type](https://swagger.io/docs/specification/data-models/data-types/) |
| Schema.org mapping: | [DataType](https://schema.org/DataType) |

### uniqueItems

|                     |     |
| ------------------- | --- |
| Definition:         | Declares whether all items in an array must be unique. (cf. [OpenAPI: uniqueItems](https://swagger.io/docs/specification/data-models/data-types/)) |
| Label:              | Items have to be unique |
| Data type/format:   | boolean |
| Used in:            | [Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#data-schema-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#uniqueItems |
| OpenAPI mapping:    | [uniqueItems](https://swagger.io/docs/specification/data-models/data-types/) |
| Schema.org mapping: | — |

### unit

|                     |     |
| ------------------- | --- |
| Definition:         | A reference to the unit of measure of a quantity (variable or constant) of interest. (cf. [qudt: unit](https://qudt.org/schema/qudt/unit)) |
| Label:              | Unit reference |
| Data type/format:   | string or string/uri |
| Used in:            | [Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#data-schema-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#unit |
| OpenAPI mapping:    | x-unit |
| Schema.org mapping: | [unitCode](https://schema.org/unitCode) |

### url

|                     |     |
| ------------------- | --- |
| Definition:         | URL of the item. (cf. [Schema.org: url](https://schema.org/url)) |
| Label:              | URL |
| Data type/format:   | string/url |
| Used in:            | [Contact Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#contact-object), [External Documentation Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#external-documentation-object), [License Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#license-object), [Organization Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#organization-object), [Person Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#person-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#url |
| OpenAPI mapping:    | [url](https://swagger.io/specification/) |
| Schema.org mapping: | [url](https://schema.org/url) |

### version

|                     |     |
| ------------------- | --- |
| Definition:         | Version of the software instance. (cf. [Schema.org: softwareVersion](https://schema.org/softwareVersion)) |
| Label:              | Software version |
| Data type/format:   | string |
| Used in:            | [Info Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#info-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#version |
| OpenAPI mapping:    | [version](https://swagger.io/specification/) |
| Schema.org mapping: | [softwareVersion](https://schema.org/softwareVersion) |

### volumeNumber

|                     |     |
| ------------------- | --- |
| Definition:         | Identifies the volume of publication or multi-part work; for example, "iii" or "2". (cf. [Schema.org: volumeNumber](https://schema.org/volumeNumber)) |
| Label:              | Volume Number |
| Data type/format:   | integer |
| Used in:            | [Scholarly Article Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#scholarly-article-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/Metadata_Schema/DataDesc_Schema_v1.0.md#volumeNumber |
| OpenAPI mapping:    | x-volumeNumber |
| Schema.org mapping: | [volumeNumber](https://schema.org/volumeNumber) |

## DataDesc Document

Explaining the structure of DataDesc JSON documents.

... is structured into `info` on the software in general, `components` which groups the software's functions ...
The DataDesc vocabulary is used in the `info` and `components` section.

## Examples