import os
import glob
import pandas as pd
from pathlib import Path

# Open TUI folder
path = Path('D:\\Python_DEV\\RunLogic APP\\')

def combine_files(extension=None):
    all_filenames = glob.glob(os.path.join(path, "*.csv"))
    print(all_filenames)

    #combine all files in the list
    all_csv = (pd.read_csv(f, sep=',') for f in all_filenames)
    #df_merged = pd.concat(all_csv, ignore_index=True)
    print(all_csv)
    #df_merged.to_csv("merged.csv", index=False, encoding='utf-8-sig')

    #export to csv
    #combined_csv.to_csv("combined_csv.csv", index=False, encoding='utf-8-sig')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    combine_files('csv')