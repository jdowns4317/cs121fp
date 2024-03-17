import pandas as pd

import pandas as pd

csv_file_path1 = 'processed_data/sport_programs_extra.csv'
df1 = pd.read_csv(csv_file_path1)

csv_file_path2 = 'processed_data/basic_info.csv'
df2 = pd.read_csv(csv_file_path2)

set1 = set(df1['u_id'])
set2 = set(df2['u_id'])
difference = set1 - set2

new_rows = []

for i, row in df1.iterrows():
    if row['u_id'] not in difference:
        new_rows.append(row)

new_df = pd.DataFrame(new_rows, columns=['u_id', 'assoc', 'sport'])
new_file_path = 'processed_data/sport_programs.csv'
new_df.to_csv(new_file_path, index=False)
print("done")