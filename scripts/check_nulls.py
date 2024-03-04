import pandas as pd

csv_file_path = 'data/raw_college_data.csv'
df = pd.read_csv(csv_file_path)

column = 'ADM_RATE'
has_nulls = df[column].isnull()

# Print out num of null values
print(sum(has_nulls))