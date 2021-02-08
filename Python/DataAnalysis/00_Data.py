import pandas as pd
import numpy as np

# ------------------------------------- 데이터 분석

CCTV_Seoul = pd.read_csv('./CCTV_in_seoul.csv', encoding='cp949')
print(CCTV_Seoul.head())
print(CCTV_Seoul.columns)
CCTV_Seoul.rename(columns={CCTV_Seoul.columns[0]: '구분'}, inplace=True)
print(CCTV_Seoul.columns)

# -------------------------------------- 시리즈

s = pd.Series([1, 3, 5, 7, 9])
print(s)

# --------------------------------------- 데이터 프레임

dates = pd.date_range('20210131', periods=5)  # 6일 동안의 날짜 범위를 만들어줌
df = pd.DataFrame(np.random.randn(5, 3), index=dates, columns=['A', 'B', 'C'])
print(df.head(6))
print(df.index)
print(df.columns)
print(df.info())
print(df.describe())

# ---------------------------------------

print(df.sort_values(by='B', ascending=True), end="\n\n")  # 정렬
print(df[['A']])
print(df[0:3])
print(df.iloc[1:4, [1, 2]])
print(df.iloc[:, :])
print(df[df > 0])

df2 = df
print(df2)
print(df2.sort_values(by='A', ascending=False))

df2["순위"] = [1, 2, 3, 4, 5]
print(df2)
print(df2["순위"].isin([1, 3, 5]))
print(df2.apply(np.cumsum))
print(df2.apply(lambda x: x.max() - x.min()))
