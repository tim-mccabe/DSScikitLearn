import pandas as pd


data_dict = {
    'investments': [
        '100_000_000', 
        '100_000', 
        '30_000_000', 
        '100_500_000'
    ]
}
df = pd.DataFrame(data=data_dict)

df['investments'] = df['investments'].str.replace('_', '').astype(int)

print(df)