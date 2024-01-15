# JSON Merge Script Documentation

## Overview

This script is designed to merge two JSON files containing schemas. It provides functionality to merge the schemas and handle version checks, nested updates, and user input for ambiguous fields. The primary use case is merging a technical metadata file (`file_main`) with a general metadata file (`file_general`) to produce a merged JSON file (`output`).

## Prerequisites

Before using the script, make sure you have the following:

- Python installed (version 3.6 or higher).
- `deepdiff` installed. You can install them using:
```bash
pip install deepdiff
```

## Usage

1. **Setup files**
Copy the `json` files that are to be merged into the `files` folder.

2. **Execute the script**
Run the script from the command line with the following parameters:
```bash
python main.py -f1 <file_main> -f2 <file_general> -o <output>
```
- **file_main**: the path to the main metadata file (to merge into).
- **file_general**: the path to the general metadata file.
- **output**: the path to the output file (default is `merged.json`).

3. **Navigating user prompts**
If the script encounters ambiguous or deleted fields during the merge, it will prompt you to choose between existing and new values. All non-ambiguous fields are copied from `file_general` into `file_main`.

## Example
```bash
python main.py -f1 main_schema.json -f2 general_schema.json -o merged_schema.json
```
This command merges `./files/main_schema.json` with `./files/general_schema.json` and writes the result to `./files/merged_schema.json`.