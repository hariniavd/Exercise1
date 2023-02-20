import os
import pathlib


REPO_PATH = pathlib.Path(__file__).parent
INPUT_FILE_PATH = os.path.join(REPO_PATH, "Input-Files")
OUTPUT_FOLDER_PATH = os.path.join(REPO_PATH, "Output")
OUTPUT_FILE_PATH = os.path.join(OUTPUT_FOLDER_PATH, "target.xlsx")
PRIMARY_KEYS = ['Field1', 'Field2']
XLSX_FORMAT = '.xlsx'
