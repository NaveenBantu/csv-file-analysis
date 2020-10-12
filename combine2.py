import os
import pandas as pd
import glob

os.chdir('D:\\ComCore_Projects\\JacareiPM1\\4_10_2020_Logs\\\RunLogic APP\\')

def extract_problem_logs(df):
   # prob_csv = df.loc[(df['ClassId']>1) & (df['ClassId']<=8)]
    prob_csv = df.loc[(df['ClassId'] == 8)]
    print(prob_csv)
    prob_csv.to_csv("exceptions.csv", index=False, encoding='utf-8-sig')

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

print(all_filenames)

#combine all files in the list
header_names = ['Timestamp', ' CmpId', 'ClassId', 'ErrorId', 'InfoId', 'InfoText']
combined_csv = pd.concat([pd.read_csv(f, header=None, comment=';', names=header_names, skip_blank_lines=True, usecols=[0,1,2,3,4,5]) for f in all_filenames], ignore_index=True)

print(combined_csv['InfoText'].str.contains('Persistence').value_counts()[True])
extract_problem_logs(combined_csv)

#write the combined csv to a file
combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')

