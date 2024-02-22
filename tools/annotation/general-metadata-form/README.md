# Installation and Usage Guide for GeneralMetadataCollector

## Install Required Packages
Before you begin, make sure you have Python and pip installed on your system. To install the necessary packages, open a terminal and run the following commands:

```bash
pip install -r requirements.txt
```

## Launch Jupyter Notebook
To run the `GeneralMetadataCollector` notebook, follow these steps:

1. Open a terminal and navigate to the directory where the notebook is located.

2. Run the following command to start the Jupyter Notebook server:
```bash
jupyter notebook
```

3. This will open a new tab in your web browser displaying the Jupyter Notebook interface.

4. In the Jupyter Notebook interface, navigate to the directory containing the `GeneralMetadataCollector.ipynb` file.

5. Click on the `GeneralMetadataCollector.ipynb` file to open the notebook.

## Using the GeneralMetadataCollector Notebook
Once the notebook is open, you can use it to collect and generate metadata in DataDesc JSON format. Here's a brief explanation of how to use the notebook:

### 1. Software Metadata Input
The notebook provides a set of input fields for software metadata. Fill in the required information such as Identifier, Software Title, Description, Contact Info, License Info, Authors, and more.

### 2. Export to JSON
The notebook includes a function to export the entered information to a JSON file (`meta.json`).
After filling in the required information, click the "`Generate meta.json`" button.

### 3. Download JSON
Once you click the button, a link to download the generated `meta.json` file will be displayed.