import pandas as pd
import glob
import os
from collections import defaultdict
os.chdir('/Users/adambouras/Downloads/')
# Get a list of all CSV files in the directory
csv_files = glob.glob('*.csv')
print(csv_files)
# Create an empty list to store the dataframes
dict = {}


# Read each CSV file into a dataframe and append it to the list
# print(csv_files)

try:
    for i, file in enumerate(csv_files):
        # if i <3:
            df = pd.read_csv(file, dtype=str)
            childkey = df['childkey'].unique()[0]
            parentkey = df['parentkey'].unique()[0]
            if childkey in dict.keys():
                dict[f"{parentkey}"].update({f"{childkey}":df})
            else:
                dict.update({f"{parentkey}":{f"{childkey}":df.astype(str)}})
                     

except Exception as e:
    print(f'Error reading file {file}: {str(e)}')
# print(dict['cancer_related_surgical_procedure'])
os.chdir('/Users/adambouras/excel_merge/')
for parentkey in dict:
    print(dict[parentkey].keys())
    with pd.ExcelWriter(f'{parentkey}.xlsx') as writer:
        for childkey in dict[parentkey].keys():
            print(dict[parentkey][childkey])
            dict[parentkey][childkey].to_excel(writer, sheet_name=childkey, index=False, na_rep='NULL')
