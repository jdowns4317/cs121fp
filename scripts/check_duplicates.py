import pandas as pd

csv_file_path = 'processed_data/basic_info.csv'
df = pd.read_csv(csv_file_path)

duplicate_u_ids = df[df.duplicated('u_id', keep=False)]

if not duplicate_u_ids.empty:
    print("Duplicates:")
    print(duplicate_u_ids)
else:
    print("No duplicates")
