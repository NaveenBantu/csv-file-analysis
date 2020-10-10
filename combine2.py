import os
import pandas as pd
import glob

os.chdir("F:\\python_test\\")

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

print(all_filenames)

read_csv = []

#combine all files in the list
for f in all_filenames:
    read_csv.append(pd.read_csv(f, sep=',', encoding='utf-8'))
print(read_csv)
#combined_csv = pd.concat([pd.read_csv(f, sep=',', encoding='utf-8') for f in all_filenames])

combined_csv = pd.concat(read_csv)
print(combined_csv)