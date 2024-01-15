<a href="https://www.fz-juelich.de/en/iek/iek-3"><img src="https://raw.githubusercontent.com/OfficialCodexplosive/README_Assets/862a93188b61ab4dd0eebde3ab5daad636e129d5/FJZ_IEK-3_logo.svg" alt="FZJ Logo" width="300px"></a>

# Framework for machine-actionable Software Metadata

Key components of the framework are a metadata schema for software documentation with focus on interfaces, a machine-actionable metadata exchange format and a software toolkit supporting the documentation, extraction and publication of software metadata.

## Features
The framework for machine-actionable Software Metadata combines four distinct python software packages:
- a form to convert general software metadata into a DataDesc compliant JSON file
- a parser for extracting extensive metadata information from python source code to DataDesc compliant JSON
- a tool for combining two DataDesc compliant JSON files into a single one
- a tool for uploading DataDesc compliant files to the ORKG, GitHub, PyPI, and more

## Installation
The ecosystem can be installed directly via git - this will preserve the connection to the GitHub repository:
```console
	git clone https://github.com/FZJ-IEK3-VSA/DataDesc
```

Most parts of this framework are out-of-the-box solutions which do not need to be installed. For others, a proper installation and usage instruction is provided alongside the files themselves.

## License

MIT License

Copyright (c) 2022 Patrick Kuckertz (FZJ/IEK-3), Jan-Maris Göpfert (FZJ/IEK-3), Oliver Karras (TIB), David Neuroth (FZJ/IEK-3), Julian Schönau (FZJ/IEK-3), Rodrigo Pueblas (FZJ/IEK-3), Stephan Ferenz (University of Oldenburg/ Dept. of Computer Science), Felix Engel (TIB), Noah Pflugradt (FZJ/IEK-3), Jann Michael Weinand (FZJ/IEK-3), Leander Kotzur (FZJ/IEK-3), Astrid Nieße (University of Oldenburg/ Dept. of Computer Science), Sören Auer (TIB), Detlef Stolten (FZJ/IEK-3, RWTH)

You should have received a copy of the MIT License along with this program.
If not, see https://opensource.org/licenses/MIT

## About Us

The [Institute of Energy and Climate Research - Techno-economic Systems Analysis (IEK-3)](https://www.fz-juelich.de/en/iek/iek-3) belongs to the [Forschungszentrum Jülich](https://www.fz-juelich.de/en). The department's interdisciplinary research is focusing on energy-related process and systems analyses. Data searches and system simulations are used to determine energy and mass balances, as well as to evaluate performance, emissions and costs of energy systems. The results are used for performing comparative assessment studies between the various systems. The current priorities include the development of energy strategies, in accordance with the German Federal Government’s greenhouse gas reduction targets, by designing new infrastructures for sustainable and secure energy supply chains and by conducting cost analysis studies for integrating new technologies into future energy market frameworks.

The [Data Science & Digtal Libraries research group](https://www.tib.eu/en/research-development/research-groups-and-labs/data-science-digital-libraries) belonging to the [TIB - Leibniz Information Centre for Science and Technology](https://www.tib.eu/en/) was established in July 2017 by the call of Prof. Dr. Sören Auer, which was jointly conducted with [Leibniz Universität Hannover](https://www.uni-hannover.de/de/). The research group serves TIB's strategic goal of improving access to and work with information, data and knowledge. The overall objective of the research group is to transform the current document-based knowledge communication in the sciences (Scholarly Communication) into knowledge-based communication ("from papers to knowledge graphs").

The Digitalized Energy Systems (DES) group is part of the Department of Computer Science of the University of Oldenburg. The group was established by Prof. Astrid Nieße in 2020. The group works in the field of energy informatics and focuses on distributed artificial intelligence, like agent-based systems, strategy learning in energy markets and machine learning approaches for cyber-physical energy systems (CPES).  With the high importance of data and open software in this field, research data management and how to integrate both FAIRness and industry involvement in CPES research, is a rising research area in the DES group.

## Acknowledgements
The authors would like to thank the Federal Ministry for Economic Affairs and Energy of Germany (BMWi) for supporting this work with a grant for the project LOD-GEOSS (03EI1005B).

Furthermore, the authors would like to thank the German Federal Government, the German State Governments, and the Joint Science Conference (GWK) for their funding and support as part of the NFDI4Ing consortium. Funded by the German Research Foundation (DFG) - project number: 442146713.

In addition, the work was supported by the Lower Saxony Ministry of Science and Culture within the Lower Saxony ‘‘Vorab’’ of the Volkswagen Foundation under Grant 11-76251-13-3/19–ZN3488 (ZLE), and by the Center for Digital Innovation (ZDIN).

This work was also supported by the Helmholtz Association under the program "Energy System Design".

<a href="https://www.bmwk.de/Navigation/EN/Home/home.html"><img src="https://www.bmwk.de/SiteGlobals/BMWI/StyleBundles/Bilder/bmwi_logo_en.svg?__blob=normal&v=13" alt="BMWK Logo" width="130px"></a>
