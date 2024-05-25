import pandas as pd

df = pd.read_excel('movieinfo_cleaned.xlsx')
print(df['分数'].mean())
print(df[df['分数'] > df['分数'].mean()][['电影名字', '分数']])

def hasChina(x):
    return '中国' in x

def hasJapan(x):
    return '日本' in x

print(df[(~df['国家'].apply(hasChina)) & (df['分数'] > df['分数'].mean())][['电影名字', '国家', '分数']])


