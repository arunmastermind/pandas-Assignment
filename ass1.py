import pandas as pd
import numpy as np

# 1.
# df1 = pd.read_csv('rounds2.csv', encoding = 'unicode_escape', sep=',')
# a = df1.company_permalink
# b = a.drop_duplicates().size
# print(b)

# 2.
# df2 = pd.read_csv('companies.txt', sep='\t', lineterminator='\r', encoding = 'unicode_escape')
# print(df2.permalink.drop_duplicates().size)

# 3.
# df3 = pd.read_csv('companies.txt', sep='\t', lineterminator='\r', encoding = 'unicode_escape')
# print(df3.permalink.drop_duplicates().size)
# print(df3.permalink.size)
#thus unique

# 4.
# df1 = pd.read_csv('rounds2.csv', encoding = 'ISO-8859-1', sep=',')
# df2 = pd.read_csv('companies.txt', sep='\t', encoding = 'ISO-8859-1')
# df1=df1.apply(lambda x: x.astype(str).str.lower())
# df2=df2.apply(lambda x: x.astype(str).str.lower())
#
# df1.company_permalink.drop_duplicates(inplace=True)
# df2.permalink.drop_duplicates(inplace=True)
#
# print(df1.company_permalink.size)
# print(df2.permalink.size)

# # 5.
df1 = pd.read_csv('rounds2.csv', encoding = 'ISO-8859-1', sep=',')
df2 = pd.read_csv('companies.txt', sep='\t', encoding = 'ISO-8859-1')

df1.drop_duplicates(inplace=True)
df2.drop_duplicates(inplace=True)

df1=df1.apply(lambda x: x.astype(str).str.lower())
df2=df2.apply(lambda x: x.astype(str).str.lower())

df2 = df2.rename(columns = {"permalink":"company_permalink"})
master_frame = pd.merge(df1, df2)

master_frame.raised_amount_usd=master_frame.raised_amount_usd.astype('float')
# print(master_frame.groupby('funding_round_type')['raised_amount_usd'].mean())
# master_frame.to_csv('master_frame.csv')

#checkpoint4
# 1
df2 = pd.read_csv('companies.txt', sep='\t', encoding = 'ISO-8859-1')
df2['primary_sector'] = (df2.category_list.str.split('|').str[0].tolist())
# # print(df2.columns)
# # print(df2.primary_sector)
#
# # 2
df3 = pd.read_csv('mapping.csv', encoding = 'ISO-8859-1', sep=',')
df3=df3.apply(lambda x: x.astype(str).str.lower())
df2=df2.apply(lambda x: x.astype(str).str.lower())
df3 = df3.rename(columns = {"category_list":"primary_sector"})
mergedDF = pd.merge(df2, df3, on='primary_sector')
mainSectors = list(df3.columns)
del mainSectors[0]
for mainSector in mainSectors:
    mergedDF[mainSector] = mergedDF[mainSector].astype('int')
    mergedDF.loc[mergedDF[mainSector] == 1, 'main_sector'] = mainSector
# print(mergedDF.main_sector)

# checkpoint 5
