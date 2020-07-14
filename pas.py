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