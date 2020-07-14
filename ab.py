import pandas as pd 

df = pd.read_csv('pokemon_data.csv')
print(df.head(3))

# for index,row in df.iterrows():
    # print(index,row['Attack'])
print('Fire')
# print(df.loc[df['Type 1'] == 'Fire'])
# print(df.describe())
# print(df.sort_values(['Type 1','HP'],ascending=[1,0]))
# df['Total'] = df['HP'] + df['Attack'] + df['Defense'] 
# df.drop(columns=['Total '])
df['Total'] = df.iloc[:,4:10].sum(axis=1)
# print(df['Total'])
cols = list(df.columns.values)
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]
# print(df.head)


## filtering 
print(df.loc[df['Type 1'] == 'Grass'])

new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['Total'] > 500)]
new_df.to_csv('filtered.csv')
new_df.reset_index(drop=True,inplace=True)
print(new_df.head(4))
import re 
# print(df.loc[df['Name'].str.contains('Fire|Grass',regex=True)])
# print(df.loc[df['Name'].str.contains('^pi[a-z]*',regex=True,flags=re.I)])
# print(df.loc[~df['Name'].str.contains('Mega')])

# df.loc[df['Type 1'] == 'Fire','Type 1'] = 'Flamer'
# print(df.loc[df['Type 1'] == 'Flamer'])
# df.loc[df['Total'] > 500, ['Generation']] = 'TEST_VALUE'
# print(df.head(2))

df = pd.read_csv('modified.csv')
print(df.head(4))
df.groupby(['Type 1']).mean().sort_values('Defense',ascending=False)


for df in pd.read_csv('modified.csv',chunksize=5):
    print()
    print(df.head(3))
    print()
