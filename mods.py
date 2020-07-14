import pandas as pd 
df = pd.read_csv('modified.csv')
df['count'] = 1
print(df.groupby(['Type 1', 'Type 2']).count()['count'])


new_df = pd.DataFrame(columns=df.columns)
for df in pd.read_csv('modified.csv',chunksize=5):
    results = df.groupby(['Type 1']).count()
    new_df = pd.concat([new_df,results])
print(new_df.head(4))