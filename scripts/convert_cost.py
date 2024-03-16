import pandas as pd

csv_file_path = '../data/ic2022_ay.csv'
df = pd.read_csv(csv_file_path)

new_rows = []

for i, row in df.iterrows():
    if row['XTUIT3'] == 'A':
        new_rows.append({'u_id': row['UNITID'], 'tuition': row['TUITION5'], 'in_state': 0})
    else:
        new_rows.append({'u_id': row['UNITID'], 'tuition': row['TUITION3'], 'in_state': 0})
        if row['TUITION2'] != row['TUITION3']:
            new_rows.append({'u_id': row['UNITID'], 'tuition': row['TUITION2'], 'in_state': 1})

new_df = pd.DataFrame(new_rows, columns=['u_id', 'tuition', 'in_state'])
new_file_path = 'processed_data/cost.csv'
new_df.to_csv(new_file_path, index=False)
print("done")