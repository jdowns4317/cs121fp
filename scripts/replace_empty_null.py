import pandas as pd
import numpy as np

csv_file_path = 'processed_data/cost.csv'
df = pd.read_csv(csv_file_path)
# cols = ['admission_rate', 'ug_pop', 'hbcu', 'men_only', 'women_only']
cols = ['tuition']
for col in cols:
    df[col] = df[col].replace('.', 'NULL')
new_file_path = 'processed_data/cost.csv'
df.to_csv(new_file_path, index=False)
print("done")
