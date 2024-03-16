import pandas as pd

csv_file_path = 'processed_data/cost.csv'
df = pd.read_csv(csv_file_path)

column = 'tuition'
has_nulls = df[column].isnull()

# Print out num of null values
print(sum(has_nulls))