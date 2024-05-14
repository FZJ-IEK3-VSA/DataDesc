# DataDesc Schema v1.1

Table of contents:

- [Introduction](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#introduction)
- [DataDesc Schema](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#datadesc-schema)
- [DataDesc Properties](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#datadesc-properties)
- [DataDesc Document](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#datadesc-document)
- [Examples](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#examples)

## Introduction

The DataDesc schema is a metadata schema developed for the description of research software. In addition to capturing general information relevant to the scientific context, it aims in particular at the detailed documentation of software interfaces. The programming language agnostic schema offers the possibility to treat all functions of an interface and its input and output parameters individually and to define permissible data contents, formats, structures and value ranges. The structured capture of information, which is often only available in this level of detail in the form of instructions and specifications written in free text, enables their automated processing and increases their findability and comparability. Mapping them as machine-actionable metadata allows both humans and computers to discover and understand the capabilities of a software, interact with it, and integrate it with other programs and data without having to refer to the source code or further documentation.

The structure and content of the DataDesc schema is based on the OpenAPI specification, which is a widely used language for the standardized description of web interfaces based on HTTP and REST. However, since research software mostly does not follow a client-server architecture and is not provided as services accessible via web interfaces, DataDesc does not focus on the transmission of data via HTTP requests to be processed on the server side, but on the permissible use of locally installed programs. Largely adopted from OpenAPI are the hierarchically organized documentation structures, which allow code-near descriptions of interface elements. Furthermore, the data type specifications based on JSON Schema are used, with which even nested data models used by an interface can be mapped in detail.

In the area of the general description of research software, the CodeMeta metadata standard and the Schema.org ontology on which it is based were closely followed, and adopted metadata elements were integrated within the hierarchical documentation structure. As a result, the DataDesc schema is largely compatible with both the OpenAPI and the Schema.org or CodeMeta standards and minimizes the amount of necessarily individually defined terminology. This is explicitly shown by the mappings presented in this documentation, which can be used to translate the elements of the DataDesc schema into those of OpenAPI and Schema.org. In addition, the QUDT ontology was used as a basis for the units of measurement.

</br>
<p align="center">
    <div style="width: 100%; display: inline-block" align="center">
        <img src="https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDescSchema.png?raw=true" style="width: 50%">
    </div>
     <div align="center">
       <em>Structure and content of the DataDesc schema for describing software and their interface data models. Both the general and the technical information are organized in information objects, with arrows indicating the different relationships between them. DataDesc properties that comply with the OpenAPI specification directly or via extensions are marked with white circles or white triangles respectively. Properties that map to the Schema.org ontology are indicated by a gray square.</em>
    </div>
    
</p></br>

Meaning of the property descriptions used in this documentation:
- Property: The property describes a characteristic of an object. The name of the property is used within the schema as an identifier of the characteristic.
- Label: The label adds context to the property name, if necessary. It quickly conveys the meaning of the property, but is also short enough to be easily displayed in tables and documentation snippets.
- Data Type/Format: States the data type in which values can be specified for the property. The data types used in this schema are _string_, _number_, _integer_, _boolean_, _array_, and _object_. A _number_ can be a floating-point number, but also an _integer_. The default value of all schema properties of _boolean_ data type is _False_. Furthermore, a specific format of a data type can be stated. A _string_ can be of format _date_, _uri_, _url_, or _email_. _date_ follows a 'yyyy-mm-dd' notation. The other string formats add contextual meaning, but are not defined as part of this documentation. The format of an _object_ is given as a schema reference. With this description of data types and formats the [OpenAPI specification](https://swagger.io/docs/specification/data-models/data-types/) is followed.
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

| Property                                                                                                                       | Label                         | Data Type/Format                                                                                        | Required                         | OpenAPI Mapping                                                                   | Schema.org Mapping                                            |
| ------------------------------------------------------------------------------------------------------------------------------ | ----------------------------- | ------------------------------------------------------------------------------------------------------- | -------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| [dataDescVersion](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#dataDescVersion)           | DataDesc version              | string                                                                                                  | True                             | x-dataDescVersion                                                                 | —                                                             |
| [openapi](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#openapi)                           | OpenAPI version               | string                                                                                                  | True                             | [openapi](https://swagger.io/specification/)                                      | —                                                             |
| [externalDocs](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#externalDocs)                 | External documentations       | array[object/[External Documentation Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#external-documentation-object)] | False | [externalDocs](https://swagger.io/specification/)     | —                                                             |
| [info](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#info)                                 | General software information  | object/[Info Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#info-object) | True                 | [info](https://swagger.io/specification/)                                         | —                                                             |
| [apiFunctions](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#apiFunctions)                 | API functions                 | array[object/[API Function Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#api-function-object)] | False | x-apiFunctions                                                            | —                                                             |

### **External Documentation Object**
The object allows referencing an external resource for extended documentation.<br>
Conforms to OpenAPI's [External Documentation Object](https://swagger.io/specification/).

| Property                                                                                                                       | Label                         | Data Type/Format                                                                                        | Required                         | OpenAPI Mapping                                                                   | Schema.org Mapping                                            |
| ------------------------------------------------------------------------------------------------------------------------------ | ----------------------------- | ------------------------------------------------------------------------------------------------------- | -------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| [description](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#description)                   | Description                   | string                                                                                                  | False                            | [description](https://swagger.io/specification/)                                  | [description](https://schema.org/description)                 |
| [url](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#url)                                   | URL                           | string/url                                                                                              | False                            | [url](https://swagger.io/specification/)                                          | [url](https://schema.org/url)                                 |

### **Info Object**
The object provides metadata about the software.<br>
Conforms to OpenAPI's [Info Object](https://swagger.io/specification/).

| Property                                                                                                                       | Label                         | Data Type/Format                                                                                        | Required                         | OpenAPI Mapping                                                                   | Schema.org Mapping                                            |
| ------------------------------------------------------------------------------------------------------------------------------ | ----------------------------- | ------------------------------------------------------------------------------------------------------- | -------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| [identifier](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#identifier)                     | Identifier                    | string                                                                                                  | False                            | [identifier](https://swagger.io/specification/)                                   | [identifier](https://schema.org/identifier)                   |
| [title](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#title)                               | Software title                | string                                                                                                  | True                             | [title](https://swagger.io/specification/)                                        | [name](https://schema.org/name)                               |
| [description](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#description)                   | Description                   | string                                                                                                  | False                            | [description](https://swagger.io/specification/)                                  | [description](https://schema.org/description)                 |
| [contact](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#contact)                           | Contact information           | object/[Contact Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#contact-object) | False          | [contact](https://swagger.io/specification/)                                      | [ContactPoint](https://schema.org/ContactPoint)               |
| [license](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#license)                           | License information           | object/[License Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#license-object) | False          | [license](https://swagger.io/specification/)                                      | —                                                             |
| [version](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#version)                           | Software version              | string                                                                                                  | True                             | [version](https://swagger.io/specification/)                                      | [softwareVersion](https://schema.org/softwareVersion)         |
| [codeRepository](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#codeRepository)             | Software repository URL       | string/url                                                                                              | False                            | x-codeRepository                                                                  | [codeRepository](https://schema.org/codeRepository)           |
| [programmingLanguages](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#programmingLanguages) | Programming languages         | array[string]                                                                                           | False                            | x-programmingLanguages                                                            | [programmingLanguage](https://schema.org/programmingLanguage) |
| [downloadUrl](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#downloadUrl)                   | Software download URL         | string/url                                                                                              | False                            | x-downloadUrl                                                                     | [downloadUrl](https://schema.org/downloadUrl)                 |
| [authors](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#authors)                           | Authors of the creative work  | array[object/[Person Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#person-object)] | False     | x-authors                                                                         | [author](https://schema.org/author)                           |
| [copyrightHolders](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#copyrightHolders)         | Copyright holders             | array[object/[Organization Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#organization-object) and/or [Person Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#person-object)] | False | x-copyrightHolders | [copyrightHolder](https://schema.org/copyrightHolder) |
| [copyrightYear](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#copyrightYear)               | Copyright year                | string                                                                                                  | False                            | x-copyrightYear                                                                   | [copyrightYear](https://schema.org/copyrightYear)             |
| [datePublished](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#datePublished)               | Date published                | string/date                                                                                             | False                            | x-datePublished                                                                   | [datePublished](https://schema.org/datePublished)             |
| [keywords](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#keywords)                         | Keywords                      | array[string]                                                                                           | False                            | x-keywords                                                                        | [keywords](https://schema.org/keywords)                       |
| [funders](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#funders)                           | Funders                       | array[object/[Organization Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#organization-object) and/or [Person Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#person-object)] | False | x-funders | [funder](https://schema.org/funder) |
| [fundings](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#fundings)                         | Funding sources               | array[string]                                                                                           | False                            | x-fundings                                                                        | [funding](https://schema.org/funding)                         |
| [referencePublication](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#referencePublication) | Reference publication         | object/[Scholarly Article Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#scholarly-article-object) | False | x-referencePublication                                                 | —                                                             |
| [readme](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#readme)                             | Readme URL                    | string/url                                                                                              | False                            | x-readme                                                                          | —                                                             |

### **Contact Object**
Contact information for the software.<br>
Conforms to OpenAPI's [Contact Object](https://swagger.io/specification/) and Schema.org's [ContactPoint Object](https://schema.org/ContactPoint).

| Property                                                                                                                       | Label                         | Data Type/Format                                                                                        | Required                         | OpenAPI Mapping                                                                   | Schema.org Mapping                                            |
| ------------------------------------------------------------------------------------------------------------------------------ | ----------------------------- | ------------------------------------------------------------------------------------------------------- | -------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| [name](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#name)                                 | Name                          | string                                                                                                  | False                            | [name](https://swagger.io/specification/)                                         | [name](https://schema.org/name)                               |
| [url](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#url)                                   | URL                           | string/url                                                                                              | False                            | [url](https://swagger.io/specification/)                                          | [url](https://schema.org/url)                                 |
| [email](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#email)                               | Email                         | string/email                                                                                            | False                            | [email](https://swagger.io/specification/)                                        | [email](https://schema.org/email)                             |

### **License Object**
License information for the software.<br>
Conforms to OpenAPI's [License Object](https://swagger.io/specification/).

| Property                                                                                                                       | Label                         | Data Type/Format                                                                                        | Required                         | OpenAPI Mapping                                                                   | Schema.org Mapping                                            |
| ------------------------------------------------------------------------------------------------------------------------------ | ----------------------------- | ------------------------------------------------------------------------------------------------------- | -------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| [name](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#name)                                 | Name                          | string                                                                                                  | True                             | [name](https://swagger.io/specification/)                                         | [name](https://schema.org/name)                               |
| [identifier](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#identifier)                     | Identifier                    | string                                                                                                  | False                            | [identifier](https://swagger.io/specification/)                                   | [identifier](https://schema.org/identifier)                   |
| [url](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#url)                                   | URL                           | string/url                                                                                              | False                            | [url](https://swagger.io/specification/)                                          | [url](https://schema.org/url)                                 |

### **Person Object**
The object provides metadata about a person.<br>
Conforms to Schema.org's [Person Object](https://schema.org/Person).

| Property                                                                                                                       | Label                         | Data Type/Format                                                                                        | Required                         | OpenAPI Mapping                                                                   | Schema.org Mapping                                            |
| ------------------------------------------------------------------------------------------------------------------------------ | ----------------------------- | ------------------------------------------------------------------------------------------------------- | -------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| [identifier](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#identifier)                     | Identifier                    | string                                                                                                  | False                            | [identifier](https://swagger.io/specification/)                                   | [identifier](https://schema.org/identifier)                   |
| [givenName](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#givenName)                       | Given name                    | string                                                                                                  | False                            | x-givenName                                                                       | [givenName](https://schema.org/givenName)                     |
| [additionalName](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#additionalName)             | Additional name               | string                                                                                                  | False                            | x-additionalName                                                                  | [additionalName](https://schema.org/additionalName)           |
| [familyName](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#familyName)                     | Family name                   | string                                                                                                  | False                            | x-familyName                                                                      | [familyName](https://schema.org/familyName)                   |
| [honorificPrefix](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#honorificPrefix)           | Honorific prefix              | string                                                                                                  | False                            | x-honorificPrefix                                                                 | [honorificPrefix](https://schema.org/honorificPrefix)         |
| [honorificSuffix](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#honorificSuffix)           | Honorific suffix              | string                                                                                                  | False                            | x-honorificSuffix                                                                 | [honorificSuffix](https://schema.org/honorificSuffix)         |
| [affiliation](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#affiliation)                   | Affiliation                   | object/[Organization Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#organization-object) | False | x-affiliation                                                                    | [affiliation](https://schema.org/affiliation)                 |
| [jobTitle](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#jobTitle)                         | Job title                     | string                                                                                                  | False                            | x-jobTitle                                                                        | [jobTitle](https://schema.org/jobTitle)                       |
| [url](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#url)                                   | URL                           | string/url                                                                                              | False                            | [url](https://swagger.io/specification/)                                          | [url](https://schema.org/url)                                 |
| [email](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#email)                               | Email                         | string/email                                                                                            | False                            | [email](https://swagger.io/specification/)                                        | [email](https://schema.org/email)                             |
| [telephone](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#telephone)                       | Telephone number              | string                                                                                                  | False                            | x-telephone                                                                       | [telephone](https://schema.org/telephone)                     |

### **Organization Object**
The object provides metadata about an organization.<br>
Conforms to Schema.org's [Organization Object](https://schema.org/Organization).

| Property                                                                                                                       | Label                         | Data Type/Format                                                                                        | Required                         | OpenAPI Mapping                                                                   | Schema.org Mapping                                            |
| ------------------------------------------------------------------------------------------------------------------------------ | ----------------------------- | ------------------------------------------------------------------------------------------------------- | -------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| [legalName](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#legalName)                       | Legal name                    | string                                                                                                  | False                            | x-legalName                                                                       | [legalName](https://schema.org/legalName)                     |
| [alternateName](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#alternateName)               | Alternate name                | string                                                                                                  | False                            | x-alternateName                                                                   | [alternateName](https://schema.org/alternateName)             |
| [url](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#url)                                   | URL                           | string/url                                                                                              | False                            | [url](https://swagger.io/specification/)                                          | [url](https://schema.org/url)                                 |
| [email](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#email)                               | Email                         | string/email                                                                                            | False                            | [email](https://swagger.io/specification/)                                        | [email](https://schema.org/email)                             |
| [telephone](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#telephone)                       | Telephone number              | string                                                                                                  | False                            | x-telephone                                                                       | [telephone](https://schema.org/telephone)                     |

### **Scholarly Article Object**
The object provides metadata about a scholarly article.<br>
Conforms to Schema.org's [ScholarlyArticle Object](https://schema.org/ScholarlyArticle).

| Property                                                                                                                       | Label                         | Data Type/Format                                                                                        | Required                         | OpenAPI Mapping                                                                   | Schema.org Mapping                                            |
| ------------------------------------------------------------------------------------------------------------------------------ | ----------------------------- | ------------------------------------------------------------------------------------------------------- | -------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| [identifier](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#identifier)                     | Identifier                    | string                                                                                                  | False                            | [identifier](https://swagger.io/specification/)                                   | [identifier](https://schema.org/identifier)                   |
| [headline](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#headline)                         | Article title                 | string                                                                                                  | False                            | x-headline                                                                        | [headline](https://schema.org/headline)                       |
| [authors](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#author)                            | Authors of the creative work  | array[object/[Person Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#person-object)] | False     | x-authors                                                                         | [author](https://schema.org/author)                           |
| [datePublished](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#datePublished)               | Date published                | string/date                                                                                             | False                            | x-datePublished                                                                   | [datePublished](https://schema.org/datePublished)             |
| [journal](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#journal)                           | Journal                       | string                                                                                                  | False                            | x-journal                                                                         | —                                                             |
| [volumeNumber](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#volumeNumber)                 | Volume Number                 | integer                                                                                                 | False                            | x-volumeNumber                                                                    | [volumeNumber](https://schema.org/volumeNumber)               |
| [pageStart](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#pageStart)                       | Page Start                    | integer                                                                                                 | False                            | x-pageStart                                                                       | [pageStart](https://schema.org/pageStart)                     |
| [pageEnd](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#pageEnd)                           | Page End                      | integer                                                                                                 | False                            | x-pageEnd                                                                         | [pageEnd](https://schema.org/pageEnd)                         |

### **API Function Object**
The object describes an exposed API function.<br>
The structure of this object is based on OpenAPI's [Operation Object](https://swagger.io/specification/).

| Property                                                                                                                       | Label                         | Data Type/Format                                                                                        | Required                         | OpenAPI Mapping                                                                   | Schema.org Mapping                                            |
| ------------------------------------------------------------------------------------------------------------------------------ | ----------------------------- | ------------------------------------------------------------------------------------------------------- | -------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| [identifier](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#identifier)                     | Identifier                    | string                                                                                                  | True                             | [identifier](https://swagger.io/specification/)                                   | [identifier](https://schema.org/identifier)                   |
| [description](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#description)                   | Description                   | string                                                                                                  | False                            | [description](https://swagger.io/specification/)                                  | [description](https://schema.org/description)                 |
| [deprecated](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#deprecated)                     | This object is deprecated     | boolean                                                                                                 | False                            | [deprecated](https://swagger.io/specification/)                                   | —                                                             |
| [inputVariables](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#inputVariables)             | Input variables               | array[object/[Variable Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#variable-object)] | False | x-inputVariables                                                                  | —                                                             |
| [outputVariables](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#outputVariables)           | Output variables              | array[object/[Variable Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#variable-object)] | False | x-outputVariables                                                                 | —                                                             |

### **Variable Object**
The object describes a single function parameter.<br>
The structure of this object is based on OpenAPI's [Parameter Object](https://swagger.io/specification/).

| Property                                                                                                                       | Label                         | Data Type/Format                                                                                        | Required                         | OpenAPI Mapping                                                                   | Schema.org Mapping                                            |
| ------------------------------------------------------------------------------------------------------------------------------ | ----------------------------- | ------------------------------------------------------------------------------------------------------- | -------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| [identifier](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#identifier)                     | Identifier                    | string                                                                                                  | True                             | [identifier](https://swagger.io/specification/)                                   | [identifier](https://schema.org/identifier)                   |
| [description](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#description)                   | Description                   | string                                                                                                  | False                            | [description](https://swagger.io/specification/)                                  | [description](https://schema.org/description)                 |
| [required](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#required)                         | Value input is required       | boolean                                                                                                 | False                            | [required](https://swagger.io/specification/)                                     | [valueRequired](https://schema.org/valueRequired)             |
| [deprecated](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#deprecated)                     | This object is deprecated     | boolean                                                                                                 | False                            | [deprecated](https://swagger.io/specification/)                                   | —                                                             |
| [dataSchema](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#dataSchema)                     | Data schema                   | object/[Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#data-schema-object) | True   | x-dataSchema                                                                      | —                                                             |

### **Data Schema Object**
The schema object allows the data type definition of a variable. These types can be primitives, but also (nested) arrays and objects.<br>
The structure of this object is based on OpenAPI's [Schema Object](https://swagger.io/specification/).

| Property                                                                                                                       | Label                         | Data Type/Format                                                                                        | Required                         | OpenAPI Mapping                                                                   | Schema.org Mapping                                            |
| ------------------------------------------------------------------------------------------------------------------------------ | ----------------------------- | ------------------------------------------------------------------------------------------------------- | -------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| [identifier](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#identifier)                     | Identifier                    | string                                                                                                  | False                            | [identifier](https://swagger.io/specification/)                                   | [identifier](https://schema.org/identifier)                   |
| [description](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#description)                   | Description                   | string                                                                                                  | False                            | [description](https://swagger.io/specification/)                                  | [description](https://schema.org/description)                 |
| [semanticConcept](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#semanticConcept)           | Semantic concept reference    | string/uri                                                                                              | False                            | x-semanticConcept                                                                 | —                                                             |
| [type](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#type)                                 | Data type                     | string                                                                                                  | True                             | [type](https://swagger.io/docs/specification/data-models/data-types/)             | [DataType](https://schema.org/DataType)                       |
| [format](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#format)                             | Data format                   | string or object                                                                                        | False                            | [format](https://swagger.io/docs/specification/data-models/data-types/)           | —                                                             |
| [minimum](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#minimum)                           | Minimum value                 | number                                                                                                  | False                            | [minimum](https://swagger.io/docs/specification/data-models/data-types/)          | [minValue](https://schema.org/minValue)                       |
| [maximum](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#maximum)                           | Maximum value                 | number                                                                                                  | False                            | [maximum](https://swagger.io/docs/specification/data-models/data-types/)          | [maxValue](https://schema.org/maxValue)                       |
| [exclusiveMinimum](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#exclusiveMinimum)         | Minimum value is exclusive    | boolean                                                                                                 | False                            | [exclusiveMinimum](https://swagger.io/docs/specification/data-models/data-types/) | —                                                             |
| [exclusiveMaximum](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#exclusiveMaximum)         | Maximum value is exclusive    | boolean                                                                                                 | False                            | [exclusiveMaximum](https://swagger.io/docs/specification/data-models/data-types/) | —                                                             |
| [multipleOf](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#multipleOf)                     | Multiple of                   | number                                                                                                  | False                            | [multipleOf](https://swagger.io/docs/specification/data-models/data-types/)       | [stepValue](https://schema.org/stepValue)                     |
| [minLength](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#minLength)                       | Minimum length of string      | integer                                                                                                 | False                            | [minLength](https://swagger.io/docs/specification/data-models/data-types/)        | [valueMinLength](https://schema.org/valueMinLength)           |
| [maxLength](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#maxLength)                       | Maximum length of string      | integer                                                                                                 | False                            | [maxLength](https://swagger.io/docs/specification/data-models/data-types/)        | [valueMaxLength](https://schema.org/valueMaxLength)           |
| [pattern](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#pattern)                           | Pattern                       | string                                                                                                  | False                            | [pattern](https://swagger.io/docs/specification/data-models/data-types/)          | [valuePattern](https://schema.org/valuePattern)               |
| [items](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#items)                               | Data schema of array items    | array[object/[Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#data-schema-object)] | False | [items](https://swagger.io/docs/specification/data-models/data-types/)      | —                                                             |
| [minItems](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#minItems)                         | Minimum length of array       | integer                                                                                                 | False                            | [minItems](https://swagger.io/docs/specification/data-models/data-types/)         | —                                                             |
| [maxItems](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#maxItems)                         | Maximum length of array       | integer                                                                                                 | False                            | [maxItems](https://swagger.io/docs/specification/data-models/data-types/)         | —                                                             |
| [uniqueItems](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#uniqueItems)                   | Items have to be unique       | boolean                                                                                                 | False                            | [uniqueItems](https://swagger.io/docs/specification/data-models/data-types/)      | —                                                             |
| [properties](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#properties)                     | List of object properties     | array[object/[Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#data-schema-object)] | False | [properties](https://swagger.io/docs/specification/data-models/data-types/) | —                                                             |
| [requiredProperties](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#requiredProperties)     | List of required properties   | array[string]                                                                                           | False                            | [required](https://swagger.io/docs/specification/data-models/data-types/)         | [valueRequired](https://schema.org/valueRequired)             |
| [unit](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#unit)                                 | Unit reference                | string                                                                                                  | False                            | x-unit                                                                            | [unitText](https://schema.org/unitText)                       |
| [quantityKind](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#quantityKind)                 | Quantity kind reference       | string                                                                                                  | False                            | x-quantityKind                                                                    | —                                                             |
| [nullable](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#nullable)                         | Null value is allowed         | boolean                                                                                                 | False                            | [nullable](https://swagger.io/docs/specification/data-models/data-types/)         | —                                                             |
| [dimensions](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#dimensions)                     | Dimensions                    | array[object/[Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#data-schema-object)] | False | x-dimensions                                                                | —                                                             |
| [enum](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#enum)                                 | Enumeration of allowed values | _same as type_                                                                                          | False                            | [enum](https://swagger.io/docs/specification/data-models/enums/)                  | —                                                             |
| [default](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#default)                           | Default value                 | _same as type_                                                                                          | False                            | [default](https://swagger.io/docs/specification/describing-parameters/)           | [defaultValue](https://schema.org/defaultValue)               |
| [example](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#example)                           | Example value                 | _same as type_                                                                                          | False                            | [example](https://swagger.io/docs/specification/adding-examples/)                 | —                                                             |
| [mediaType](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#mediaType)                       | Media type                    | string                                                                                                  | False                            | [mediaType](https://swagger.io/docs/specification/media-types/)                   | [encodingFormat](https://schema.org/encodingFormat)           |
| [charSet](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#charSet)                           | Character set                 | string                                                                                                  | False                            | [charSet](https://swagger.io/docs/specification/media-types/)                     | —                                                             |

## DataDesc Properties

### additionalName

|                     |     |
| ------------------- | --- |
| Definition:         | An additional name for a Person, can be used for a middle name. (cf. [Schema.org: additionalName](https://schema.org/additionalName)) |
| Label:              | Additional name |
| Data type/format:   | string |
| Used in:            | [Person Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#person-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#additionalName |
| OpenAPI mapping:    | x-additionalName |
| Schema.org mapping: | [additionalName](https://schema.org/additionalName) |

### affiliation

|                     |     |
| ------------------- | --- |
| Definition:         | An organization that this person is affiliated with. For example, a school/university, a club, or a team. (cf. [Schema.org: affiliation](https://schema.org/affiliation)) |
| Label:              | Affiliation |
| Data type/format:   | object/[Organization Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#organization-object) |
| Used in:            | [Person Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#person-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#affiliation |
| OpenAPI mapping:    | x-affiliation |
| Schema.org mapping: | [affiliation](https://schema.org/affiliation) |

### alternateName

|                     |     |
| ------------------- | --- |
| Definition:         | An alias for the item. (cf. [Schema.org: alternateName](https://schema.org/alternateName)) |
| Label:              | Alternate Name |
| Data type/format:   | string |
| Used in:            | [Organization Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#organization-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#alternateName |
| OpenAPI mapping:    | x-alternateName |
| Schema.org mapping: | [alternateName](https://schema.org/alternateName) |

### apiFunctions

|                     |     |
| ------------------- | --- |
| Definition:         | Holds the software's exposed API functions. |
| Label:              | API functions |
| Data type/format:   | array[object/[API Function Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#api-function-object)] |
| Used in:            | [DataDesc Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#datadesc-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#apiFunctions |
| OpenAPI mapping:    | x-apiFunctions |
| Schema.org mapping: | — |

### authors

|                     |     |
| ------------------- | --- |
| Definition:         | The authors of this content or rating. (cf. [Schema.org: author](https://schema.org/author)) |
| Label:              | Authors of the creative work |
| Data type/format:   | array[object/[Person Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#person-object)] |
| Used in:            | [Info Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#info-object), [Scholarly Article Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#scholarly-article-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#authors |
| OpenAPI mapping:    | x-authors |
| Schema.org mapping: | [author](https://schema.org/author) |

### charSet

|                     |     |
| ------------------- | --- |
| Definition:         | Specifies a collection of characters and its encoding used to represent text in a computer system. |
| Label:              | Character set |
| Data type/format:   | string |
| Used in:            | [Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#data-schema-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#charSet |
| OpenAPI mapping:    | [charSet](https://swagger.io/docs/specification/media-types/) |
| Schema.org mapping: | — |

### codeRepository

|                     |     |
| ------------------- | --- |
| Definition:         | Link to the repository where the un-compiled, human readable code and related code is located (SVN, GitHub, CodePlex). (cf. [Schema.org: codeRepository](https://schema.org/codeRepository)) |
| Label:              | Software repository URL |
| Data type/format:   | string (URL) |
| Used in:            | [Info Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#info-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#codeRepository |
| OpenAPI mapping:    | x-codeRepository |
| Schema.org mapping: | [codeRepository](https://schema.org/codeRepository) |

### contact

|                     |     |
| ------------------- | --- |
| Definition:         | The contact information for the exposed API. (cf. [OpenAPI: contact](https://swagger.io/specification/)) |
| Label:              | Contact information |
| Data type/format:   | object/[Contact Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#contact-object) |
| Used in:            | [Info Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#info-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#contact |
| OpenAPI mapping:    | [contact](https://swagger.io/specification/) |
| Schema.org mapping: | [ContactPoint](https://schema.org/ContactPoint) |

### copyrightHolders

|                     |     |
| ------------------- | --- |
| Definition:         | The parties holding the legal copyright to the creative work. (cf. [Schema.org: copyrightHolder](https://schema.org/copyrightHolder)) |
| Label:              | Copyright holders |
| Data type/format:   | array[object/[Organization Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#organization-object) and/or object/[Person Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#person-object)] |
| Used in:            | [Info Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#info-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#copyrightHolders |
| OpenAPI mapping:    | x-copyrightHolders |
| Schema.org mapping: | [copyrightHolder](https://schema.org/copyrightHolder) |

### copyrightYear

|                     |     |
| ------------------- | --- |
| Definition:         | The year during which the claimed copyright for the CreativeWork was first asserted. (cf. [Schema.org: copyrightYear](https://schema.org/copyrightYear)) |
| Label:              | Copyright year |
| Data type/format:   | string |
| Used in:            | [Info Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#info-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#copyrightYear |
| OpenAPI mapping:    | x-copyrightYear |
| Schema.org mapping: | [copyrightYear](https://schema.org/copyrightYear) |

### dataDescVersion

|                     |     |
| ------------------- | --- |
| Definition:         | The version number of the DataDesc specification that the DataDesc document uses. |
| Label:              | DataDesc version |
| Data type/format:   | string |
| Used in:            | [DataDesc Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#datadesc-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#dataDescVersion |
| OpenAPI mapping:    | x-dataDescVersion |
| Schema.org mapping: | — |

### dataSchema

|                     |     |
| ------------------- | --- |
| Definition:         | Holds the data type definition of a variable. These types can be primitives, but also (nested) arrays and objects. |
| Label:              | Data schema |
| Data type/format:   | object/[Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#data-schema-object) |
| Used in:            | [Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#data-schema-object), [Variable Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#variable-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#dataSchema |
| OpenAPI mapping:    | x-dataSchema |
| Schema.org mapping: | — |

### datePublished

|                     |     |
| ------------------- | --- |
| Definition:         | Date of first broadcast/publication. (cf. [Schema.org: datePublished](https://schema.org/datePublished)) |
| Label:              | Date published |
| Data type/format:   | string/date |
| Used in:            | [Info Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#info-object), [Scholarly Article Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#scholarly-article-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#datePublished |
| OpenAPI mapping:    | x-datePublished |
| Schema.org mapping: | [datePublished](https://schema.org/datePublished) |

### default

|                     |     |
| ------------------- | --- |
| Definition:         | The default value of the input. For properties that expect a literal, the default is a literal value, for properties that expect an object, it's an ID reference to one of the current values. (cf. [Schema.org: defaultValue](https://schema.org/defaultValue)) |
| Label:              | Default value |
| Data type/format:   | _Same as the data type of the described variable_ |
| Used in:            | [Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#data-schema-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#default |
| OpenAPI mapping:    | [default](https://swagger.io/docs/specification/describing-parameters/) |
| Schema.org mapping: | [defaultValue](https://schema.org/defaultValue) |

### deprecated

|                     |     |
| ------------------- | --- |
| Definition:         | Declares whether this object is deprecated. |
| Label:              | This object is deprecated |
| Data type/format:   | boolean |
| Used in:            | [API Function Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#api-function-object), [Variable Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#variable-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#deprecated |
| OpenAPI mapping:    | [deprecated](https://swagger.io/specification/)|
| Schema.org mapping: | — |

### description

|                     |     |
| ------------------- | --- |
| Definition:         | A description of the item. (cf. [Schema.org: description](https://schema.org/description)) |
| Label:              | Description |
| Data type/format:   | string |
| Used in:            | [API Function Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#api-function-object), [Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#data-schema-object), [External Documentation Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#external-documentation-object), [Info Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#info-object), [Variable Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#variable-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#description |
| OpenAPI mapping:    | [description](https://swagger.io/specification/) |
| Schema.org mapping: | [description](https://schema.org/description) |

### dimensions

|                     |     |
| ------------------- | --- |
| Definition:         | Specifies the shape of a multi-dimensional variable. A dimension can represent, e.g., a temporal, geographical or physical resolution but might also be used to index more abstract quantities, e.g., power plant IDs or application scenarios. |
| Label:              | Dimensions |
| Data type/format:   | array[object/[Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#data-schema-object)] |
| Used in:            | [Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#data-schema-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#dimensions |
| OpenAPI mapping:    | x-dimensions |
| Schema.org mapping: | — |

### downloadUrl

|                     |     |
| ------------------- | --- |
| Definition:         | If the file can be downloaded, URL to download the binary. (cf. [Schema.org: downloadUrl](https://schema.org/downloadUrl)) |
| Label:              | Software download URL |
| Data type/format:   | string/url |
| Used in:            | [Info Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#info-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#downloadUrl |
| OpenAPI mapping:    | x-downloadUrl |
| Schema.org mapping: | [downloadUrl](https://schema.org/downloadUrl) |

### email

|                     |     |
| ------------------- | --- |
| Definition:         | Email address. (cf. [Schema.org: email](https://schema.org/email)) |
| Label:              | Email |
| Data type/format:   | string/email |
| Used in:            | contact, organization, person |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#email |
| OpenAPI mapping:    | [email](https://swagger.io/specification/) |
| Schema.org mapping: | [email](https://schema.org/email) |

### enum

|                     |     |
| ------------------- | --- |
| Definition:         | Specifies possible values of a variable. |
| Label:              | Enumeration of allowed values |
| Data type/format:   | _Same as the data type of the described variable_ |
| Used in:            | [Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#data-schema-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#enum |
| OpenAPI mapping:    | [enum](https://swagger.io/docs/specification/data-models/enums/) |
| Schema.org mapping: | — |

### example

|                     |     |
| ------------------- | --- |
| Definition:         | Adds an example value to a variable to make to make its usage clearer. |
| Label:              | Example value |
| Data type/format:   | _Same as the data type of the described variable_ |
| Used in:            | [Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#data-schema-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#example |
| OpenAPI mapping:    | [example](https://swagger.io/docs/specification/adding-examples/) |
| Schema.org mapping: | — |

### exclusiveMaximum

|                     |     |
| ------------------- | --- |
| Definition:         | Declares whether a specified maximum value is excluded. |
| Label:              | Maximum value is exclusive |
| Data type/format:   | boolean |
| Used in:            | [Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#data-schema-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#exclusiveMaximum |
| OpenAPI mapping:    | [exclusiveMaximum](https://swagger.io/docs/specification/data-models/data-types/) |
| Schema.org mapping: | — |

### exclusiveMinimum

|                     |     |
| ------------------- | --- |
| Definition:         | Declares whether a specified minimum value is excluded. |
| Label:              | Minimum value is exclusive |
| Data type/format:   | boolean |
| Used in:            | [Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#data-schema-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#exclusiveMinimum |
| OpenAPI mapping:    | [exclusiveMinimum](https://swagger.io/docs/specification/data-models/data-types/) |
| Schema.org mapping: | — |

### externalDocs

|                     |     |
| ------------------- | --- |
| Definition:         | Additional external documentations. (cf. [OpenAPI: externalDocs](https://swagger.io/specification/)) |
| Label:              | External documentations |
| Data type/format:   | array[object/[External Documentation Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#external-documentation-object)] |
| Used in:            | [DataDesc Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#datadesc-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#externalDocs |
| OpenAPI mapping:    | [externalDocs](https://swagger.io/specification/) |
| Schema.org mapping: | — |

### familyName

|                     |     |
| ------------------- | --- |
| Definition:         | Family name. In the U.S., the last name of a Person. (cf. [Schema.org: familyName](https://schema.org/familyName)) |
| Label:              | Family name |
| Data type/format:   | string |
| Used in:            | [Person Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#person-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#familyName |
| OpenAPI mapping:    | x-familyName |
| Schema.org mapping: | [familyName](https://schema.org/familyName) |

### format

|                     |     |
| ------------------- | --- |
| Definition:         | Further specifies the data type of a variable by hinting at, e.g. specific numeric types or (custom) string formats. This information can be used for data validation. (cf. [OpenAPI: format](https://swagger.io/docs/specification/data-models/data-types/)) |
| Label:              | Data format |
| Data type/format:   | string |
| Used in:            | [Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#data-schema-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#format |
| OpenAPI mapping:    | [format](https://swagger.io/docs/specification/data-models/data-types/) |
| Schema.org mapping: | — |

### funders

|                     |     |
| ------------------- | --- |
| Definition:         | Persons and/or organizations that support (sponsor) something through some kind of financial contribution. (cf. [Schema.org: funder](https://schema.org/funder)) |
| Label:              | Funders |
| Data type/format:   | array[object/[Organization Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#organization-object) and/or object/[Person Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#person-object)] |
| Used in:            | [Info Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#info-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#funders |
| OpenAPI mapping:    | x-funders |
| Schema.org mapping: | [funder](https://schema.org/funder) |

### fundings

|                     |     |
| ------------------- | --- |
| Definition:         | Grants that directly or indirectly provide funding or sponsorship for this item. (cf. [Schema.org: funding](https://schema.org/funding)) |
| Label:              | Funding sources |
| Data type/format:   | array[string] |
| Used in:            | [Info Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#info-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#fundings |
| OpenAPI mapping:    | x-fundings |
| Schema.org mapping: | [funding](https://schema.org/funding) |

### givenName

|                     |     |
| ------------------- | --- |
| Definition:         | Given name. In the U.S., the first name of a Person. (cf. [Schema.org: givenName](https://schema.org/givenName)) |
| Label:              | Given name |
| Data type/format:   | string |
| Used in:            | [Person Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#person-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#givenName |
| OpenAPI mapping:    | x-givenName |
| Schema.org mapping: | [givenName](https://schema.org/givenName) |

### headline

|                     |     |
| ------------------- | --- |
| Definition:         | Headline of the article. (cf. [Schema.org: headline](https://schema.org/headline)) |
| Label:              | Article title |
| Data type/format:   | string |
| Used in:            | [Scholarly Article Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#scholarly-article-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#headline |
| OpenAPI mapping:    | x-headline |
| Schema.org mapping: | [headline](https://schema.org/headline) |

### honorificPrefix

|                     |     |
| ------------------- | --- |
| Definition:         | An honorific prefix preceding a Person's name such as Dr/Mrs/Mr. (cf. [Schema.org: honorificPrefix](https://schema.org/honorificPrefix)) |
| Label:              | Honorific prefix |
| Data type/format:   | string |
| Used in:            | [Person Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#person-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#honorificPrefix |
| OpenAPI mapping:    | x-honorificPrefix |
| Schema.org mapping: | [honorificPrefix](https://schema.org/honorificPrefix) |

### honorificSuffix

|                     |     |
| ------------------- | --- |
| Definition:         | An honorific suffix following a Person's name such as M.D./PhD/MSCSW. (cf. [Schema.org: honorificSuffix](https://schema.org/honorificSuffix)) |
| Label:              | Honorific suffix |
| Data type/format:   | string |
| Used in:            | [Person Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#person-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#honorificSuffix |
| OpenAPI mapping:    | x-honorificSuffix |
| Schema.org mapping: | [honorificSuffix](https://schema.org/honorificSuffix) |

### identifier

|                     |     |
| ------------------- | --- |
| Definition:         | The identifier property represents any kind of identifier for any kind of thing (e.g. orcid, URI, DOI, SPDX license identifier). (cf. [Schema.org: identifier](https://schema.org/identifier)) |
| Label:              | Identifier |
| Data type/format:   | string |
| Used in:            | [API Function Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#api-function-object), [Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#data-schema-object), [Info Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#info-object), [License Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#license-object), [Person Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#person-object), [Scholarly Article Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#scholarly-article-object), [Variable Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#variable-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#identifier |
| OpenAPI mapping:    | [identifier](https://swagger.io/specification/) |
| Schema.org mapping: | [identifier](https://schema.org/identifier) |

### info

|                     |     |
| ------------------- | --- |
| Definition:         | Provides general metadata about the software. |
| Label:              | General software information |
| Data type/format:   | object/[Info Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#info-object) |
| Used in:            | [DataDesc Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#datadesc-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#info |
| OpenAPI mapping:    | [info](https://swagger.io/specification/) |
| Schema.org mapping: | — |

### inputVariables

|                     |     |
| ------------------- | --- |
| Definition:         | Holds a function's input variables. |
| Label:              | Input variables |
| Data type/format:   | array[object/[Variable Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#variable-object)] |
| Used in:            | [API Function Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#api-function-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#inputVariables |
| OpenAPI mapping:    | x-inputVariables |
| Schema.org mapping: | — |

### items

|                     |     |
| ------------------- | --- |
| Definition:         | Holds a schema that is required for arrays, that describes the type and format of array items. (cf. [OpenAPI: items](https://swagger.io/docs/specification/data-models/data-types/)) |
| Label:              | Data schema of array items |
| Data type/format:   | array[object/[Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#data-schema-object)] |
| Used in:            | [Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#data-schema-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#items |
| OpenAPI mapping:    | [items](https://swagger.io/docs/specification/data-models/data-types/) |
| Schema.org mapping: | — |

### jobTitle

|                     |     |
| ------------------- | --- |
| Definition:         | The job title of the person (for example, Financial Manager). (cf. [Schema.org: jobTitle](https://schema.org/jobTitle)) |
| Label:              | Job title |
| Data type/format:   | string |
| Used in:            | [Person Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#person-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#jobTitle |
| OpenAPI mapping:    | x-jobTitle |
| Schema.org mapping: | [jobTitle](https://schema.org/jobTitle) |

### journal

|                     |     |
| ------------------- | --- |
| Definition:         | References a journal in which a scholarly article was published. |
| Label:              | Journal |
| Data type/format:   | string |
| Used in:            | [Scholarly Article Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#scholarly-article-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#journal |
| OpenAPI mapping:    | x-journal |
| Schema.org mapping: | — |

### keywords

|                     |     |
| ------------------- | --- |
| Definition:         | Keywords or tags used to describe some item. Multiple textual entries in a keywords list are typically delimited by commas, or by repeating the property. (cf. [Schema.org: keywords](https://schema.org/keywords)) |
| Label:              | Keywords |
| Data type/format:   | string |
| Used in:            | [Info Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#info-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#keywords |
| OpenAPI mapping:    | x-keywords |
| Schema.org mapping: | [keywords](https://schema.org/keywords) |

### legalName

|                     |     |
| ------------------- | --- |
| Definition:         | The official name of the organization, e.g. the registered company name. (cf. [Schema.org: legalName](https://schema.org/legalName)) |
| Label:              | Legal name |
| Data type/format:   | string |
| Used in:            | [Organization Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#organization-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#legalName |
| OpenAPI mapping:    | x-legalName |
| Schema.org mapping: | [legalName](https://schema.org/legalName) |

### license

|                     |     |
| ------------------- | --- |
| Definition:         | Holds the information about a software's license. |
| Label:              | License information |
| Data type/format:   | object/[License Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#license-object) |
| Used in:            | [Info Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#info-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#license |
| OpenAPI mapping:    | [license](https://swagger.io/specification/) |
| Schema.org mapping: | — |

### maximum

|                     |     |
| ------------------- | --- |
| Definition:         | The upper value of some characteristic or property. (cf. [Schema.org: maxValue](https://schema.org/maxValue)) |
| Label:              | Maximum value |
| Data type/format:   | number |
| Used in:            | [Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#data-schema-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#maximum |
| OpenAPI mapping:    | [maximum](https://swagger.io/docs/specification/data-models/data-types/) |
| Schema.org mapping: | [maxValue](https://schema.org/maxValue) |

### maxItems

|                     |     |
| ------------------- | --- |
| Definition:         | Specifies the maximum length of an array. (cf. [OpenAPI: maxItems](https://swagger.io/docs/specification/data-models/data-types/)) |
| Label:              | Maximum length of array |
| Data type/format:   | integer |
| Used in:            | [Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#data-schema-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#maxItems|
| OpenAPI mapping:    | [maxItems](https://swagger.io/docs/specification/data-models/data-types/) |
| Schema.org mapping: | — |

### maxLength

|                     |     |
| ------------------- | --- |
| Definition:         | Specifies the allowed range for number of characters in a literal value. (cf. [Schema.org: valueMaxLength](https://schema.org/valueMaxLength)) |
| Label:              | Maximum length of string|
| Data type/format:   | integer |
| Used in:            | [Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#data-schema-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#maxLength |
| OpenAPI mapping:    | [maxLength](https://swagger.io/docs/specification/data-models/data-types/) |
| Schema.org mapping: | [valueMaxLength](https://schema.org/valueMaxLength) |

### mediaType

|                     |     |
| ------------------- | --- |
| Definition:         | Specifies the media type and thereby the the format of a file and its data contents. |
| Label:              | Media type |
| Data type/format:   | string |
| Used in:            | [Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#data-schema-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#mediaType |
| OpenAPI mapping:    | [mediaType](https://swagger.io/docs/specification/media-types/) |
| Schema.org mapping: | [encodingFormat](https://schema.org/encodingFormat) |

### minimum

|                     |     |
| ------------------- | --- |
| Definition:         | The lower value of some characteristic or property. (cf. [Schema.org: minValue](https://schema.org/minValue)) |
| Label:              | Minimum value |
| Data type/format:   | number |
| Used in:            | [Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#data-schema-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#minimum |
| OpenAPI mapping:    | [minimum](https://swagger.io/docs/specification/data-models/data-types/) |
| Schema.org mapping: | [minValue](https://schema.org/minValue) |

### minItems

|                     |     |
| ------------------- | --- |
| Definition:         | Specifies the minimum length of an array. (cf. [OpenAPI: minItems](https://swagger.io/docs/specification/data-models/data-types/)) |
| Label:              | Minimum length of array |
| Data type/format:   | integer |
| Used in:            | [Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#data-schema-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#minItems|
| OpenAPI mapping:    | [minItems](https://swagger.io/docs/specification/data-models/data-types/) |
| Schema.org mapping: | — |

### minLength

|                     |     |
| ------------------- | --- |
| Definition:         | Specifies the minimum allowed range for number of characters in a literal value. (cf. [Schema.org: valueMinLength](https://schema.org/valueMinLength)) |
| Label:              | Minimum length of string |
| Data type/format:   | integer |
| Used in:            | [Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#data-schema-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#minLength |
| OpenAPI mapping:    | [minLength](https://swagger.io/docs/specification/data-models/data-types/) |
| Schema.org mapping: | [valueMinLength](https://schema.org/valueMinLength) |

### multipleOf

|                     |     |
| ------------------- | --- |
| Definition:         | Specifies that a number must be the multiple of another number. (cf. [OpenAPI: multipleOf](https://swagger.io/docs/specification/data-models/data-types/)) |
| Label:              | Multiple of |
| Data type/format:   | number |
| Used in:            | [Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#data-schema-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#multipleOf |
| OpenAPI mapping:    | [multipleOf](https://swagger.io/docs/specification/data-models/data-types/) |
| Schema.org mapping: | [stepValue](https://schema.org/stepValue) |

### name

|                     |     |
| ------------------- | --- |
| Definition:         | The name of the item. (cf. [Schema.org: name](https://schema.org/name)) |
| Label:              | Name |
| Data type/format:   | string |
| Used in:            | [Contact Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#contact-object), [License Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#license-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#name |
| OpenAPI mapping:    | [name](https://swagger.io/specification/) |
| Schema.org mapping: | [name](https://schema.org/name) |

### nullable

|                     |     |
| ------------------- | --- |
| Definition:         | Declares whether the null value is allowed. (cf. [OpenAPI: nullable](https://swagger.io/docs/specification/data-models/data-types/)) |
| Label:              | Null value is allowed |
| Data type/format:   | boolean |
| Used in:            | [Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#data-schema-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#nullable |
| OpenAPI mapping:    | [nullable](https://swagger.io/docs/specification/data-models/data-types/) |
| Schema.org mapping: | — |

### openapi

|                     |     |
| ------------------- | --- |
| Definition:         | The version number of the OpenAPI specification that the DataDesc document uses. |
| Label:              | OpenAPI version |
| Data type/format:   | string |
| Used in:            | [DataDesc Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#datadesc-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#openapi |
| OpenAPI mapping:    | [openapi](https://swagger.io/specification/) |
| Schema.org mapping: | — |

### outputVariables

|                     |     |
| ------------------- | --- |
| Definition:         | Holds a function's output variables. |
| Label:              | Output variables |
| Data type/format:   | array[object/[Variable Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#variable-object)] |
| Used in:            | [API Function Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#api-function-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#outputVariables |
| OpenAPI mapping:    | x-outputVariables |
| Schema.org mapping: | — |

### pageEnd

|                     |     |
| ------------------- | --- |
| Definition:         | The page on which the work ends; for example "138" or "xvi". (cf. [Schema.org: pageEnd](https://schema.org/pageEnd)) |
| Label:              | Page End |
| Data type/format:   | integer |
| Used in:            | [Scholarly Article Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#scholarly-article-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#pageEnd |
| OpenAPI mapping:    | x-pageEnd |
| Schema.org mapping: | [pageEnd](https://schema.org/pageEnd) |

### pageStart

|                     |     |
| ------------------- | --- |
| Definition:         | The page on which the work starts; for example "135" or "xiii". (cf. [Schema.org: pageStart](https://schema.org/pageStart)) |
| Label:              | Page Start |
| Data type/format:   | integer |
| Used in:            | [Scholarly Article Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#scholarly-article-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#pageStart |
| OpenAPI mapping:    | x-pageStart |
| Schema.org mapping: | [pageStart](https://schema.org/pageStart) |

### pattern

|                     |     |
| ------------------- | --- |
| Definition:         | Defines a regular expression template for a string value. Only the values that match this template will be accepted. (cf. [OpenAPI: pattern](https://swagger.io/docs/specification/data-models/data-types/)) |
| Label:              | Pattern |
| Data type/format:   | string |
| Used in:            | [Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#data-schema-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#pattern |
| OpenAPI mapping:    | [pattern](https://swagger.io/docs/specification/data-models/data-types/) |
| Schema.org mapping: | [valuePattern](https://schema.org/valuePattern) |

### programmingLanguages

|                     |     |
| ------------------- | --- |
| Definition:         | The computer programming languages. (cf. [Schema.org: programmingLanguage](https://schema.org/programmingLanguage)) |
| Label:              | Programming languages |
| Data type/format:   | array[string] |
| Used in:            | [Info Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#info-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#programmingLanguages |
| OpenAPI mapping:    | x-programmingLanguages |
| Schema.org mapping: | [programmingLanguage](https://schema.org/programmingLanguage) |

### properties

|                     |     |
| ------------------- | --- |
| Definition:         | Holds an object's properties. (cf. [OpenAPI: properties](https://swagger.io/docs/specification/data-models/data-types/)) |
| Label:              | List of object properties |
| Data type/format:   | array[object/[Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#data-schema-object)] |
| Used in:            | [Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#data-schema-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#properties |
| OpenAPI mapping:    | [properties](https://swagger.io/docs/specification/data-models/data-types/) |
| Schema.org mapping: | — |

### quantityKind

|                     |     |
| ------------------- | --- |
| Definition:         | A Quantity Kind is any observable property that can be measured and quantified numerically. Familiar examples include physical properties such as length, mass, time, force, energy, power, electric charge, etc. Less familiar examples include currency, interest rate, price to earning ratio, and information capacity. (cf. [qudt: QuantityKind](https://qudt.org/schema/qudt/QuantityKind)) |
| Label:              | Quantity kind reference |
| Data type/format:   | string |
| Used in:            | [Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#data-schema-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#quantityKind |
| OpenAPI mapping:    | x-quantityKind |
| Schema.org mapping: | — |

### readme

|                     |     |
| ------------------- | --- |
| Definition:         | Link to software Readme file. (cf. [CodeMeta: readme](https://codemeta.github.io/terms/)) |
| Label:              | Readme URL |
| Data type/format:   | string/url |
| Used in:            | [Info Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#info-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#readme |
| OpenAPI mapping:    | x-readme |
| Schema.org mapping: | — |

### referencePublication

|                     |     |
| ------------------- | --- |
| Definition:         | An academic publication related to the software. (cf. [CodeMeta: referencePublication](https://codemeta.github.io/terms/)) |
| Label:              | Reference publication |
| Data type/format:   | object/[Scholarly Article Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#scholarly-article-object) |
| Used in:            | [Info Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#info-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#referencePublication |
| OpenAPI mapping:    | x-referencePublication |
| Schema.org mapping: | — |

### required

|                     |     |
| ------------------- | --- |
| Definition:         | Whether the property must be filled in to complete the action. Default is false. (cf. [Schema.org: valueRequired](https://schema.org/valueRequired)) |
| Label:              | Value input is required |
| Data type/format:   | boolean |
| Used in:            | [Variable Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#variable-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#required |
| OpenAPI mapping:    | [required](https://swagger.io/specification/) |
| Schema.org mapping: | [valueRequired](https://schema.org/valueRequired) |

### requiredProperties

|                     |     |
| ------------------- | --- |
| Definition:         | Lists all properties of an object that are required. By default, all object properties are optional. (cf. [OpenAPI: type](https://swagger.io/docs/specification/data-models/data-types/)) |
| Label:              | List of required properties |
| Data type/format:   | array[string] |
| Used in:            | [Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#data-schema-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#requiredProperties |
| OpenAPI mapping:    | [required](https://swagger.io/docs/specification/data-models/data-types/) |
| Schema.org mapping: | [valueRequired](https://schema.org/valueRequired) |

### semanticConcept

|                     |     |
| ------------------- | --- |
| Definition:         | References a semantic concept and thus unambiguously specifies the content-related meaning of a variable and its values. |
| Label:              | Semantic concept reference |
| Data type/format:   | string/uri |
| Used in:            | [Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#data-schema-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#semanticConcept |
| OpenAPI mapping:    | x-semanticConcept |
| Schema.org mapping: | — |

### telephone

|                     |     |
| ------------------- | --- |
| Definition:         | The telephone number. (cf. [Schema.org: telephone](https://schema.org/telephone)) |
| Label:              | Telephone number |
| Data type/format:   | string |
| Used in:            | [Organization Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#organization-object), [Person Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#person-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#telephone |
| OpenAPI mapping:    | x-telephone |
| Schema.org mapping: | [telephone](https://schema.org/telephone) |

### title

|                     |     |
| ------------------- | --- |
| Definition:         | The title of the software. (cf. [OpenAPI: title](https://swagger.io/specification/))|
| Label:              | Software title |
| Data type/format:   | string |
| Used in:            | [Info Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#info-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#title |
| OpenAPI mapping:    | [title](https://swagger.io/specification/) |
| Schema.org mapping: | [name](https://schema.org/name) |

### type

|                     |     |
| ------------------- | --- |
| Definition:         | The data type of a schema is defined by the type keyword, for example, type: string. (cf. [OpenAPI: type](https://swagger.io/docs/specification/data-models/data-types/)) |
| Label:              | Data type |
| Data type/format:   | string or object |
| Used in:            | [Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#data-schema-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#type |
| OpenAPI mapping:    | [type](https://swagger.io/docs/specification/data-models/data-types/) |
| Schema.org mapping: | [DataType](https://schema.org/DataType) |

### uniqueItems

|                     |     |
| ------------------- | --- |
| Definition:         | Declares whether all items in an array must be unique. (cf. [OpenAPI: uniqueItems](https://swagger.io/docs/specification/data-models/data-types/)) |
| Label:              | Items have to be unique |
| Data type/format:   | boolean |
| Used in:            | [Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#data-schema-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#uniqueItems |
| OpenAPI mapping:    | [uniqueItems](https://swagger.io/docs/specification/data-models/data-types/) |
| Schema.org mapping: | — |

### unit

|                     |     |
| ------------------- | --- |
| Definition:         | A reference or URI to the unit of measure of a quantity (variable or constant) of interest. (cf. [qudt: unit](https://qudt.org/schema/qudt/unit)) |
| Label:              | Unit reference |
| Data type/format:   | string |
| Used in:            | [Data Schema Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#data-schema-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#unit |
| OpenAPI mapping:    | x-unit |
| Schema.org mapping: | [unitText](https://schema.org/unitText) |

### url

|                     |     |
| ------------------- | --- |
| Definition:         | URL of the item. (cf. [Schema.org: url](https://schema.org/url)) |
| Label:              | URL |
| Data type/format:   | string/url |
| Used in:            | [Contact Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#contact-object), [External Documentation Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#external-documentation-object), [License Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#license-object), [Organization Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#organization-object), [Person Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#person-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#url |
| OpenAPI mapping:    | [url](https://swagger.io/specification/) |
| Schema.org mapping: | [url](https://schema.org/url) |

### version

|                     |     |
| ------------------- | --- |
| Definition:         | Version of the software instance. (cf. [Schema.org: softwareVersion](https://schema.org/softwareVersion)) |
| Label:              | Software version |
| Data type/format:   | string |
| Used in:            | [Info Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#info-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#version |
| OpenAPI mapping:    | [version](https://swagger.io/specification/) |
| Schema.org mapping: | [softwareVersion](https://schema.org/softwareVersion) |

### volumeNumber

|                     |     |
| ------------------- | --- |
| Definition:         | Identifies the volume of publication or multi-part work; for example, "iii" or "2". (cf. [Schema.org: volumeNumber](https://schema.org/volumeNumber)) |
| Label:              | Volume Number |
| Data type/format:   | integer |
| Used in:            | [Scholarly Article Object](https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#scholarly-article-object) |
| URI:                | https://github.com/FZJ-IEK3-VSA/DataDesc/blob/main/schema/DataDesc_schema_v1.1.md#volumeNumber |
| OpenAPI mapping:    | x-volumeNumber |
| Schema.org mapping: | [volumeNumber](https://schema.org/volumeNumber) |

## DataDesc Document

A document adhering to the DataDesc standard is structured into `info` on the software in general, `apiFunctions` which groups the software's functions and additional top-level information, such as the version of DataDesc (`dataDescVersion`) and OpenAPI (`openapi`) used.
The DataDesc vocabulary is used in the `info` and `apiFunctions` section. In particular, the `info` section contains general metadata about the software, such as the software title, a description of the software and the version of the software. `apiFunctions` is an array of different JSON-objects describing API function definitions. Each function must have a unqiue `identifier`. A `description` of the function as well as information on `inputVariables` and `outputVariables` is not required but highly recommended for clarity. Variables in both arays have a `dataSchema` property that specifies both the data type (`type`) as well as arbitrary metadata (`properties`), which in and of itself is a list of JSON objects.

## Examples

### Data Types

In general, data can be divided into persistent and transient (volatile) data based on their longevity. Persistent data occurs most frequently in the form of files, which are written to a storage device of some sort. Volatile data, on the other hand, appears in the form of <mark>various data structures, variables, objects,</mark> etc.

#### Volatile Data
Most information in this subsection is inferred directly from the OpenAPI specification on [Data Types](https://swagger.io/docs/specification/data-models/data-types/). For more information, please refer to the frequently updated specification.

##### Numbers
OpenAPI, and by extension the DataDesc schema, provides two numeric types - `number` and `integer`. Whereas `integer` only supports integer numbers without decimal points, `number` also includes floating-point numbers. Adding the optional `format` keyword allows for specifying a certain numeric type:

| type | format | description |
| ---- | ------ | ----------- |
| number | - | any numbers. |
| number | float | floating-point numbers. |
| number | double | floating-point numbers with double precision. |
| integer | - | integer numbers. |
| integer | int32 | signed 32-bit integers (most commonly used integer type). |
| integer | int64 | signed 64-bit integers (`long` type) |

##### Minimum and Maximum
The `minimum` and `maximum` keywords make it possible to set lower and upper bounds for possible values.

```json
{
    'type' : 'integer',
    'minimum' : 1,
    'maximum' : 20
}
```

By default, `minimum` and `maximum` values are inclusive to the value range:
```
minimum <= value >= maximum
```

They may be excluded through the usage of the keywords `'exclusiveMinimum' : true` and `'exclusiveMaximum' : true`, respectively.

##### Strings
A string of text is defined as:
```json
{
    'type' : 'string'
}
```

Its length may be restricted using the `minLength` and `maxLength` keywords:
```json
{
    'type' : 'string',
    'minLength' : 3,
    'maxLength' : 20
}
```

An optional `format` modifier hints at the content and format of the string. While `format` is an open value and thereby supports any format, OpenAPI also provides a few built-in formats, which can be used by tools to validate the input or to map the value to a specific type in the chosen programming language:
    * `date` - full-date notation as defined by [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6), for example, *2017-07-21*
    * `date-time` - date-time notation as defined by [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6), for example, *2017-07-21T17:32:28Z*
    * `password` - a hint to UIs to mask the input
    * `byte` - base64-encoded characters, for example, *U3dhZ2dlciByb2Nrcw==*
    * `binary` - binary data, used to describe files

##### Boolean
`'type' : 'boolean'` represents two values: `true` and `false`. Whereas truthy and falsy values such as 'true', '', 0 or `null` are deemed boolean values in most programming languages, OpenAPI does not consider these as such.

##### Array
Arrays are defined as:
```json
{
    'type' : 'array'
    'items' : 
    {
        'type' : 'string'
    }
}
```

Unlike native JSON, the `items` keyword is required when declaring arrays. The value of `items` is a schema that describes the type and format of array items. Arrays can be nested:
```json
# e.g. [ [1, 2], [3, 4] ]
{
    'type' : 'array',
    'items' : 
    {
        'type' : 'array',
        'items' : 
        {
            'type' : 'integer'
        }
    }
}
```

and contain objects:

```json
{
    'type' : 'array'
    'items' : 
    {
        'type' : 'object',
        'properties' : 
        {
            'id' : 
            {
                'type' : 'integer'
            }
        }
    }
}
```

Mixed-type arrays can be defined using `oneOf` or by omitting everything between the value brackets of `items`:

```json
{
    'type' : 'array'
    'items' : 
    {
        'oneOf' : 
        {
            'type' : 'string',
            'type' : 'integer'
        }
    }
}
```

Array length can be controlled using the `minItems` and `maxItems` keyword.

The `uniqueItems : true` keyword specifies that all items in the array must be unique - as in a set.

##### Object

Objects are collections of property-value pairs. The `properties` keyword is used to define the object properties - you need to list the property names and specify a schema for each property.
```json
{
    'type' : 'object',
    'properties' : 
    {
        'id' : 
        {
            'type' : 'integer'
        },

        'name' : 
        {
            'type' : 'string'
        }
    }
}
```

By default, all properties are optional. Required properties can be specified using the `required` keyword:
```json
{
    'type' : 'object',
    'properties' : 
    {
        'id' : 
        {
            'type' : 'integer'
        },

        'name' : 
        {
            'type' : 'string'
        }
    },
    'required' : [ 'id', 'name' ]
}
```

`readOnly` and `writeOnly` can be used to mark specific properties as read-only or write-only. This is useful, for example, when GET returns more properties than used in POST - you can use the same schema in both GET and POST and mark the extra properties as `readOnly`. `readOnly` properties are included in responses but not in requests. `writeOnly` properties may be sent in requests but not in responses.

##### Tables

Tables may be specified and provided by the user in multiple ways: as `CSV`, `JSON`, the commonly used pandas `DataFrame` or as a `NetCDF` file.
The following section shows how the data types discussed above can be used to describe tables and data formats of varying complexity.


Lists of Lists, Lists of Dictionaries, Dictionaries of Dictionaries as well as pandas DataFrames will contain the following information.
|   | name | date | place |
| - | ---- | ---- | ----- |
|  0 | Joe   | 1990-01-13 | Berlin |
|  1 | Niko  | 2000-05-20 | Munich |
|  2 | Anna  | 1965-10-02 | Aachen |
|  3 | Julia | 1983-08-30 | Berlin |


###### Lists of Lists
The Table may be represented using a list of lists. In this case, the first nested array is used to describe the column headers, whereas the following arrays correspond to the given rows. In Python, it might be represented as such:
```python
table = [
    ["name","date","place"],        # header; may be omitted
    ["Joe", "1990-01-13", "Berlin"],
    ["Niko", "2000-05-20", "Munich"],
    ["Anna", "1965-10-02", "Aachen"],
    ["Julia", "1983-08-30", "Berlin"]
]
```

And it could be described using the DataDesc schema and nested arrays.
```json
'inputVariables' : 
{
    'table' : 
    {
        'description': 'Birthdates and places of some people',
        'type' : 'array',
        'items' : 
        {
            'type' : 'array',
            'items' : 
            {
                'type' : 'string'
            }
        }
    }
}
```

###### Lists of Dictionaries
The table may also be represented as an array of dictionaries, where each dictionary in the array corresponds to a row, including the column headers as dictionary keys.
```python
table = [
    {"name":"Joe", "date":"1990-01-13", "place":"Berlin"},
    {"name":"Niko", "date":"2000-05-20", "place":"Munich"},
    {"name":"Anna", "date":"1965-10-02", "place":"Aachen"},
    {"name":"Julia", "date":"1983-08-30", "place":"Berlin"}
]
```
```json
'inputVariables' : 
{
    'table' : 
    {
        'description': 'Birthdates and places of some people',
        'type' : 'array',
        'items' : 
        {
            'type' : 'array',
            'items' : 
            {
                'type' : 'object',
                'properties' : 
                {
                    'name' : {'type' : 'string'},
                    'date' : {'type' : 'string'},
                    'place' : {'type' : 'string'}
                }
            }
        }
    }
}
```

###### Dictionary of Dictionaries
Note that there are multiple ways to represent the table, e.g. using indices as dictionary keys.
```python
table = {
    0: {"name":"Joe", "date":"1990-01-13", "place":"Berlin"},
    1: {"name":"Niko", "date":"2000-05-20", "place":"Munich"},
    2: {"name":"Anna", "date":"1965-10-02", "place":"Aachen"},
    3: {"name":"Julia", "date":"1983-08-30", "place":"Berlin"}
}
```
```json
{
    'inputVariables' : 
    {
        'table' : 
        {
            'description': 'Birthdates and places of some people',
            'type' : 'object',
            'properties' : 
            {
                    'index' : {'type' : 'integer'},
                    'data' : 
                    {
                        'type' : 'object',
                        'properties' : 
                        {
                            'name' : {'type' : 'string'},
                            'date' : {'type' : 'string'},
                            'place' : {'type' : 'string'}
                        }
                    }
                
            }
        }
    }
}
```

```python
table = { # prone to failure due to possibly duplicate keys 
    "Joe": {"date":"1990-01-13", "place":"Berlin"},
    "Niko": {"date":"2000-05-20", "place":"Munich"},
    "Anna": {"date":"1965-10-02", "place":"Aachen"},
    "Julia": {"date":"1983-08-30", "place":"Berlin"}
}
```
```json
{
'inputVariables' : {
    'table' : {
        'description': 'Birthdates and places of some people',
        'type' : 'object',
        'properties' : {
                'index' : {'type' : 'string'},
                'data' : 
                {
                    'type' : 'object',
                    'properties' : {
                        'date' : {'type' : 'string'},
                        'place' : {'type' : 'string'}
                    }
                }
            
            }
        }
    }
}
```
###### Pandas DataFrame
With DataDesc it is also possible to describe more complex data types, such as pandas DataFrames.
```python
import pandas as pd
table = pd.DataFrame( 
        [
            ["Joe", "1990-01-13", "Berlin"],
            ["Niko", "2000-05-20", "Munich"],
            ["Anna", "1965-10-02", "Aachen"],
            ["Julia", "1983-08-30", "Berlin"]
        ], columns=["name","date","place"]
    )
```
```json
{
    'inputVariables' : {
        'table' : {
            'description': 'Birthdates and places of some people',
            'type' : 'object',
            'mediaType' : 'application/x-pandas+json',
            'columns': {
                'type' : 'object',
                'properties' : {
                    'name' : { 'type' : 'string' },
                    'date' : {
                        'type' : 'string',
                        'format' : 'YYYY-MM-DD'
                        },
                    'place' : {'type' : 'string'}
                }
            }
        }
    }
}
```

###### NetCDF & XArray
For a more sophisticated example, NetCDF and XArray were used to describe a table illustrated on the [*ArcGIS Pro* helpdesk](https://pro.arcgis.com/de/pro-app/latest/help/data/multidimensional/fundamentals-of-netcdf-data-storage.htm) for NetCDF files.
```json
{
    'inputVariables' : {
        'table' : {
            'description': 'Rainfall data',
            'type' : 'object',
            'mediaType' : 'application/x-netcdf',
            'dimensions' : {
                'lat' : {
                    'type' : 'object',
                    'properties' : {
                        'size' : {
                            'type' : 'integer',
                            'description' : 'Number of latitudes',
                            'minimum' : 1,
                            'maximum' : 180,
                            'example' : 3,
                        }
                    }
                },
                'lon' : {
                    'type' : 'object',
                    'properties' : {
                        'size' : {
                            'type' : 'integer',
                            'description' : 'Number of longitudes',
                            'minimum' : 1,
                            'maximum' : 360,
                            'example' : 4,
                        }
                    }
                },
                'time' : {
                    'type' : 'object',
                    'properties' : {
                        'size' : {
                            'type' : 'integer',
                            'description' : 'Number of time steps',
                            'minimum' : 1,
                            'example' : 2,
                        }
                    }
                }
            },
            'variables' : {
                'description' : 'Variables of the dataset',
                'type' : 'object',
                'properties' : {
                    'lat' : {
                        'type' : 'object',
                        'properties' : {
                            'long_name' : {
                                'type' : 'string',
                                'description' : 'Long name of the variable',
                                'example' : 'Latitude',
                            },
                            'units' : {
                                'type' : 'string',
                                'description' : 'Units of the variable',
                                'example' : 'degrees_north',
                            }
                        }
                        'dimensions' : ['lat']
                    },
                    'lon' : {
                        'type' : 'object',
                        'properties' : {
                            'long_name' : {
                                'type' : 'string',
                                'description' : 'Long name of the variable',
                                'example' : 'Longitude',
                            },
                            'units' : {
                                'type' : 'string',
                                'description' : 'Units of the variable',
                                'example' : 'degrees_east',
                            }
                        },
                        'dimensions' : ['lon']
                    },
                    'time' : {
                        'type' : 'object',
                        'properties' : {
                            'long_name' : {
                                'type' : 'string',
                                'description' : 'Long name of the variable',
                                'example' : 'Time',
                            },
                            'units' : {
                                'type' : 'string',
                                'description' : 'Units of the variable',
                                'example' : 'days since 1895-01-01',
                            },
                            'calendar' : {
                                'type' : 'string',
                                'description' : 'Calendar used for the variable',
                                'example' : 'gregorian',
                            }
                        },
                        'dimensions' : ['time']
                    },
                    'rainfall' : {
                        'type' : 'object',
                        'properties' : {
                            'long_name' : {
                                'type' : 'string',
                                'description' : 'Long name of the variable',
                                'example' : 'Precipitation',
                            },
                            'units' : {
                                'type' : 'string',
                                'description' : 'Units of the variable',
                                'example' : 'mm yr-1',
                            },
                            'missing_value' : {
                                'type' : 'number',
                                'description' : 'Missing value of the variable',
                                'example' : -9999.0
                            }
                        },
                        'dimensions' : ['time', 'lat', 'lon']
                    }
                }
            }
        }
    }
}
```
