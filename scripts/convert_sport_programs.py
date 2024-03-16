import pandas as pd

csv_file_path = '../data/ic2022.csv'
df = pd.read_csv(csv_file_path)

new_rows = []
sport_dict = {'SPORT1': ['MFB'], 'SPORT2' : ['MBB', 'WBB'], 'SPORT3':['MBA'], 'SPORT4': ['MTR', 'WTR']}

def find_assoc(row):
    if row['ASSOC1'] == 1:
        return "NCAA"
    elif row['ASSOC2'] == 1:
        return "NAIA"
    elif row['ASSOC3'] == 1:
        return "NJCAA"
    elif row['ASSOC4'] == 1:
        return 'NSCAA'
    elif row['ASSOC5'] == 1:
        return 'NCCAA'
    else:
        return 'Other'

for i, row in df.iterrows():
    for sport in sport_dict.keys():
        if row[sport] == 1:
            for s in sport_dict[sport]:
                new_rows.append({'u_id': row['UNITID'], 'assoc': find_assoc(row), 'sport': s})

new_df = pd.DataFrame(new_rows, columns=['u_id', 'assoc', 'sport'])
new_file_path = 'processed_data/sport_programs.csv'
new_df.to_csv(new_file_path, index=False)
print("done")