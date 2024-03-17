import pandas as pd

csv_file_path = 'processed_data/population.csv'
df = pd.read_csv(csv_file_path)

column = 'population'
has_nulls = df[column].isnull()

# Print out num of null values
print(sum(has_nulls))