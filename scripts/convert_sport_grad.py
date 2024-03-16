import pandas as pd

csv_file_path = '../data/raw_sport_grad.csv'
df = pd.read_csv(csv_file_path)

new_df = df[['SPORT_CODE', 'FED_RATE_2011']]

new_file_path = 'processed_data/sport_grad.csv'
new_df.to_csv(new_file_path, index=False)
print("done")