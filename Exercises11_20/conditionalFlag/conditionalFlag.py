import pandas as pd

data_dict = {
    'currency': [['PLN', 'USD'], ['EUR', 'USD', 'PLN', 'CAD'], ['GBP'], ['JPY', 'CZK', 'HUF'], []]
}
df = pd.DataFrame(data=data_dict)

df['PLN_flag'] = df['currency'].apply(lambda x: 1 if 'PLN' in x else 0)

print(df)