import pandas as pd
# read csv files:
import glob
import os
from collections import defaultdict
os.chdir('/Users/adambouras/Downloads/')
# Get a list of all CSV files in the directory
csv_files = glob.glob('11_01_2024_edp_seed_file_2024_11_*.csv')
print(csv_files)
# Create an empty list to store the dataframes
dict = {}


# Read each CSV file into a dataframe and append it to the list
# print(csv_files)

try:
    for i, file in enumerate(csv_files):
        # if i <3:
            df = pd.read_csv(file, dtype=str)
            df['cdm_code'] = "'"+df['cdm_code']
            df['cdmx_code']= "'"+df['cdmx_code']
        
            if 'cdm_field' in df.columns.tolist():
                cdm_field = df['cdm_field'].unique()[0]
                cdm_table = df['cdm_table'].unique()[0]
                if cdm_table in dict.keys():
                    dict[f"{cdm_table}"].update({f"{cdm_field}":df})
                else:
                    dict.update({f"{cdm_table}":{f"{cdm_field}":df.astype(str)}})
                     

except Exception as e:
    print(f'Error reading file {file}: {str(e)}')
# print(dict['cancer_related_surgical_procedure'])
     
os.chdir('/Users/adambouras/excel_merge/')
for cdm_table in dict:
    print(dict[cdm_table].keys())
    with pd.ExcelWriter(f'{cdm_table}.xlsx') as writer:
        for cdm_field in dict[cdm_table].keys():
            print(dict[cdm_table][cdm_field])
            dict[cdm_table][cdm_field].to_excel(writer, sheet_name=cdm_field, index=False, na_rep='NULL')
