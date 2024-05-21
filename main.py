import numpy as np
import pandas as pd


def byt():
    df1 = pd.read_excel('files/Сбыт.xlsx')
    df2 = pd.read_excel('files/ТСО.xlsx')
    # df2['ЛС'].astype('object')
    print(df1.info())
    print(df2.info())
    df3 = pd.merge(df1, df2, on=['ЛС', 'Тариф'], how='right')
    df3.to_excel('files/итог.xlsx')
    df4 = pd.merge(df1, df2, on=['ЛС', 'Тариф'], how='inner')
    df4['dev'] = df4['counter'] - df4['кон.']
    df4.to_excel('files/итог1.xlsx')
    df6 = df4[df4['dev'] > 500]
    df6.to_excel('files/Большие отклонение.xlsx')
    df6 = df4[df4['dev'] < -500]
    df6.to_excel('files/Отрицательные отклонение.xlsx')
    df5 = df3[df3['ФИО'].isnull()]
    df5.to_excel('files/Не принятые.xlsx')
    print(df5.head(10))


def prom():
    df1 = pd.read_excel('files/Сбыт пром.xlsx')
    df2 = pd.read_excel('files/ТСО пром.xlsx')
    print(df1.info())
    print(df2.info())
    df3 = pd.merge(df1, df2, on=['Номер', 'Тариф'], how='right')
    df3.to_excel('files/итог пром.xlsx')
    df4 = pd.merge(df1, df2, on=['Номер', 'Тариф'], how='inner')
    df4.to_excel('files/итог1 пром.xlsx')
    df4['dev'] = (df4['counter'] - df4['Кон']) * df4['Коэфф']
    df6 = df4[df4['dev'] > 500]
    df6.to_excel('files/Большие отклонение пром.xlsx')
    df6 = df4[df4['dev'] < -500]
    df6.to_excel('files/Отрицательные отклонение пром.xlsx')
    df5 = df3[df3['Договор'].isnull()]
    df5.to_excel('files/Не принятые пром.xlsx')
    print(df5.head(10))


if __name__ == "__main__":
    # byt()
    prom()