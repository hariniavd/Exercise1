""" Main.py calls the core functionality.
"""
import os
import defaults
from generate_xl import generate_output


def main():
    """ Main function.
    """
    # Checks if the input folder path exists or not
    if not os.path.exists(defaults.INPUT_FILE_PATH):
        # Returning with an error message, when the path does not exists.
        return "Input File Error: Please make sure if the input folder path exists"
    
    # Getting all the file list that exists in the input folder path
    input_files = os.listdir(defaults.INPUT_FILE_PATH)
    # Validation to get only xlsx files.
    input_files = [input_file for input_file in input_files if input_file.endswith(defaults.XLSX_FORMAT)]
    # If input folder is empty, return with a message
    if not input_files:
        return "Input folder does not have xlsx files, please add and try running the code."
    # Function that generates the target output xl file
    generate_output(input_files)


main()

