import numpy as np
import pandas as pd

df1 = pd.read_excel('files/111/post.xlsx')
df1['num'] = df1['num'].astype('str')
nun_list = df1['num'].tolist()
list3 = []
for n in nun_list:
    if n != 'nan':
        list3.append(str(n.split('.')[0]))
df2 = pd.read_excel('files/111/ved4.xlsx')
df2['num'] = df2['num'].astype('str')
nun_list1 = df2['num'].tolist()
intersect = list(set(list3) & set(nun_list1))
df = pd.DataFrame(columns=df2.columns)
for n in intersect:
    df = df._append(df2[df2.isin([n]).any(axis=1)])

df.to_excel('files/111/itog.xlsx')



