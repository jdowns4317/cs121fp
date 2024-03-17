import pandas as pd

csv_file_path = 'processed_data/population_comma.csv'
df = pd.read_csv(csv_file_path)


df['population'] = df['population'].str.replace(',', '').astype(int)

new_file_path = 'processed_data/population.csv'
df.to_csv(new_file_path, index=False)
print("done")