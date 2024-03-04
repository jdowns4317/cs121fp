import pandas as pd

csv_file_path = 'raw_college_data.csv'
df = pd.read_csv(csv_file_path)

column = 'CITY'
longest_string_length = df[column].astype(str).map(len).max()
print(f"The length of the longest string in the '{column}' column is: {longest_string_length}")

