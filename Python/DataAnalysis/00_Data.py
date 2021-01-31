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

dates = pd.date_range('20210131', periods=6)  # 6일 동안의 날짜 범위를 만들어줌
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['A', 'B', 'C', 'D'])
print(df.head(6))
print(df.index)
print(df.columns)
print(df.info())
print(df.describe())
