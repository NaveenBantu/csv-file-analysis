import os
import pandas as pd
import glob

os.chdir('D:\\Python_DEV\\RunLogic APP\\')

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

print(all_filenames)

#combine all files in the list
header_names = ['Timestamp', ' CmpId', 'ClassId', 'ErrorId', 'InfoId', 'InfoText']
combined_csv = pd.concat([pd.read_csv(f, header=None, comment=';', names=header_names) for f in all_filenames], ignore_index=True)

print(combined_csv.info())
combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')