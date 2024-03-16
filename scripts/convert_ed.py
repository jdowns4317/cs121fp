import pandas as pd

csv_file_path = '../data/raw_college_data.csv'
df = pd.read_csv(csv_file_path)

new_df = df[['UNITID', 'INSTNM', 'UGDS', 'CITY', 'STABBR', 'HBCU', 'MENONLY', 'WOMENONLY', 'HIGHDEG', 'ADM_RATE']]

new_file_path = 'processed_data/basic_info.csv'
new_df.to_csv(new_file_path, index=False)
print("done")