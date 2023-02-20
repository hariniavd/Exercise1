""" This tool takes the input folder as an argument, and list out all the files existing in the folder
and opens each and every xl file and as per the given logic performs Insert(I), Update(U) and Delete(D)
operations and updates the same to the target xl file.
"""
import os
import openpyxl
import pandas as pd
import defaults


def generate_output(xl_file_list):
    """ This function takes xl files as an input and target_path which is output file, location where
    target xl file is saved. This function generates the logical path and updates the xl file.

    Args:
        xl_file_list(List): List containing xl files in input path.
    """
    target_df = open_target_dataset()
    # Iterating through all the xl files
    for xl_file in xl_file_list:
        xl_file = os.path.join(defaults.INPUT_FILE_PATH, xl_file)
        # Reads the excel file from pandas library.
        df = pd.read_excel(io=xl_file, sheet_name="Sheet1")
        
        # Removes the duplicated rows present in input file, and keeps the track of latest once only.
        df_new = df[df[defaults.PRIMARY_KEYS].duplicated(keep='last')==False]
        if target_df.empty:
            # When the target_df i.e output file is empty, then simply read the input file
            # and upload the same values in the output file
            target_df = pd.concat([target_df, df_new], ignore_index=True)
            # Upating the UID for the first set of values as Insert(I)
            target_df['UID'] = 'I'
        else:
            # Comparing the input and output datasets which gives results of Updates and Inserted rows data
            # Removing the rows which is exisiting in output but not in input that has to be considered as Delete(D)  
            target_df1 = pd.concat([df_new,target_df]).drop_duplicates(defaults.PRIMARY_KEYS,keep='first', ignore_index=True)
            # Comparing the input and output datasets which gives results of Deleted and Inserted rows data
            # Removing the rows which has updated data
            target_df2 = pd.concat([df_new,target_df]).drop_duplicates(defaults.PRIMARY_KEYS,keep=False, ignore_index=True)
            # Target_df2 has only data of inserted and deleted once. 
            # Here if the UID is not empty, then considering it as Delete(D)
            target_df2['UID'].loc[~target_df2['UID'].isnull()] = 'D'
            # Now we have Delete rows, rest of the rows would be Inserted rows.So updating sae
            target_df2['UID'].loc[target_df2['UID'].isnull()] = 'I'
            # Concatinating the target dataset with Deleted ad Inserted values.
            test = pd.concat([target_df1,target_df2]).drop_duplicates(defaults.PRIMARY_KEYS,keep='last', ignore_index=True)
            # Rest other rows has been updated UID values as Update(U)
            target_df2.fillna('U')
            # Now we have to get the common values from target data and input data to update it as Insert(I)
            common = target_df.merge(df_new, how = 'inner', indicator=False)
            # concatinate the common dataset with data having insert and delete values
            final = pd.concat([test, common]).drop_duplicates(defaults.PRIMARY_KEYS,keep='last', ignore_index=True)
            # From here we are getting Updated data rows, so updating UID With Update(U)
            final['UID'].loc[final['UID'].isnull()] = 'U'
            # Renaming final dataset as target_df for return
            target_df = final

        # Saving the calculated dataset and updating it to target.
        target_df.to_excel(defaults.OUTPUT_FILE_PATH)


def open_target_dataset():
    """ This function creates a target.xlsx file, if it does not exists and adds columns that 
    are needed and returns the empty dataset. If a dataset is already created, then it reads the
    data and returns it.
    """
    # Checks if the output target file exists or not.
    if not os.path.exists(defaults.OUTPUT_FILE_PATH):
        # Used openpyxl library to create a Workbook.
        wb = openpyxl.Workbook()
        sheet = wb.active
        # Creating columns in the xl file.
        sheet['A1'] = "Field1"
        sheet['B1'] = "Field2"
        sheet['C1'] = "Field3"
        sheet['D1'] = "Field4"
        sheet['E1'] = "Field5"
        sheet['F1'] = "UID"
        # After adding columns save the updated contents in the file
        wb.save(defaults.OUTPUT_FILE_PATH)
    
    # Reads the Excel file
    try:
        # When the file is created for the first time, name of the sheet is by default Sheet.
        # Once we save the file, it gets saves as Sheet1
        df = pd.read_excel(io=defaults.OUTPUT_FILE_PATH, sheet_name="Sheet")
    except:
        # Existing file has sheet name as Sheet1 by default.
        df = pd.read_excel(io=defaults.OUTPUT_FILE_PATH, sheet_name="Sheet1")

    return df
