import pandas as pd 

print(pd)
df = pd.read_csv('pokemon_data.csv')
# print(df.head(4))
print(df['Defense'])
##Read headers
print(df.columns)
##Reacd each column 
# print(df[['Name','Type 1','HP']])
##df slicing
print(df.iloc[0:4])
##Read each row 
# for index,row in df.iterrows():
#     print(index,row['Name'])

##Search for a specific row name
# df.loc(df['Type 1' == "Grass"])
print(df.loc[df['Type 1'] == "Grass"])

##Read a specific location
print(df.iloc[9,1])

#####Making changes to data 
# df['Total'] = df.iloc[:,4:10].sum(axis=1)
# print(df['Total'])

cols = list(df.columns)
print(cols)

# df = df[cols[0:4] + [cols[-1]] + cols[4:11]]
# print(df.head(2))

##saving to desired format 
df.to_csv('modified.txt',index=False,sep='\t')