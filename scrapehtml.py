
import requests, bs4
import textwrap
import re
import pandas as pd
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

#read the website
url='https://en.m.wikipedia.org/wiki/List_of_territorial_entities_where_English_is_an_official_language'
req=requests.get(url)
soup = BeautifulSoup(req.content,'lxml')
#get the table
table = soup.find_all('table')[1]
df = pd.read_html(str(table))
df1 = pd.DataFrame(df[0])

#data cleaning
pattern1 = r'\[.*?\]'
pattern2 = r'\(.*?\)'
df1 = df1.rename(columns = {"Primary language?":"pri_lang"})

df1.Population1 = df1.Population1.str.replace(pattern1, "")
df1.Population1 = df1.Population1.str.replace('+', "")
df1.Country = df1.Country.str.replace(',', "")

df1.Country = df1.Country.str.strip()
df1.Country = df1.Country.str.replace(pattern1, "")

df1.pri_lang = df1.pri_lang.str.replace(pattern2, "")
df1.pri_lang = df1.pri_lang.str.replace(pattern1, "")
df1.pri_lang = df1.pri_lang.str.strip()

df1.Population1 = df1.Population1.str.strip()
df1.Population1 = df1.Population1.str.replace(',', '').astype('int')

#sorting
df1.sort_values(by=['Population1'], inplace=True, ascending=False)
#filtering
filter = df1.pri_lang == 'Yes'
#top 3 english speaking countries
b = (df1.where(filter).dropna().head(9))
print(b)
# df1.to_csv('a.csv')
# print()
# print( tabulate(df[0], headers='keys', tablefmt='psql') )