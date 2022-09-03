import pandas as pd


data_dict = {
    'hashtags': [
        '#good#vibes', 
        '#hot#summer#holiday', 
        '#street#food', 
        '#workout'
    ]
}
df = pd.DataFrame(data=data_dict)
df = df['hashtags'].str.split('#', expand=True)
df = df.drop(columns=[0])
df.columns = ['hashtag1', 'hashtag2', 'hashtag3']
print(df)