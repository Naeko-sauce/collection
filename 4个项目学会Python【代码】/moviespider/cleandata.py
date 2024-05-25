import pandas as pd
df = pd.read_excel('movieinfo_nona.xlsx')

def clearName(x):
    return x[:x.find(' ')]

df['电影名字'] = df['电影名字'].apply(clearName)
df['时长'] = df['时长'].apply(clearName)
df['上映时间'] = df['上映时间'].apply(clearName)
print(df[['电影名字', '时长', '上映时间']])
df.to_excel('movieinfo_cleaned.xlsx', index=False)