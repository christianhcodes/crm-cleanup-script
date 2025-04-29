import pandas as pd

df = pd.read_csv('raw_clients.csv')

# Clean formatting
df['Customer Name'] = df['Customer Name'].str.title()
df['Email'] = df['Email'].str.lower()
df['Phone'] = df['Phone'].str.replace(r'[^0-9]', '', regex=True)

# Drop duplicates
df = df.drop_duplicates(subset='Email')

df.to_csv('cleaned_clients.csv', index=False)
