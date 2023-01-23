# DataDesc
The DataDesc scheme portrays an attempt to describe data models of software interfaces with detailed and machine-actionable metadata, extending traditional research metadata.

# Exchange Format
In addition to the scheme, we introduce an exchange format and support tools for easy collection and automated publishing of software documentation.

The exchange format builds upon the OpenAPI standard. A single OpenAPI-conform YAML file is used to store all relevant software metadata. This makes it both easy to read as well as machine-actionable.

It describes the metadata in a hierarchically-structed way and is comprised of two main areas: `info` and `components`.
`info` stores all general metadata of the software, such as name, version number, authors, etc.
`components` focuses on technical software information, interface descriptions, input and output parameters.

In conjuction, they provide all information needed to more efficiently work with and use the software.