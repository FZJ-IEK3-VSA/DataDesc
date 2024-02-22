# Comparison of DataDesc documents

## Overview

This script is designed to compare two DataDesc compliant JSON files - a module description and a data description. It provides functionality to compare their structures and create a compatibility report. The report indicates the differences between the two JSON files in terms of their data schema.

## Installation

Before running the script, make sure you have installed the necessary Python packages. You can install them using the following command:

```bash
pip install deepdiff
```

## Usage

To use the script from the command line, you need to provide the following arguments:

* `-m` or `--module`: Path to module datasheet.
* `-f` or `--function`: Identifier of module function.
* `-v` or `--variable`: Identifier of function parameter.
* `-d` or `--data`: Path to input datasheet.
* `-o` or `--out`: Path to output compatibility report file.

Note that paths are resolved by default from the `files` subfolder.

## Example
```bash
python main -m annotated_complex.json -f PowerOutputCalculator.process_pm -v pm -d data.json -o report.json
```

This command compares the parameter `pm` from the `process_pm` function found in the `PowerOutputCalculator` class described in `./files/annotated_complex.json` with `./files/data.json` and writes the result to `./files/report.json`.