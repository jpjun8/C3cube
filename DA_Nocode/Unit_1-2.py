import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
from sklearn import linear_model

df = pd.read_csv("rain.csv", encoding="cp949")

year_20 = df[df["년도"] == 2020]
rain_20 = year_20["강수량"]

# print(f"2020년도 강수량 분산: {np.var(rain_20)}")
# print(f"2020년도 강수량 표준편차: {np.std(rain_20)}")

year_22 = df[df["년도"] == 2022]
rain_22 = year_22["강수량"]
days_22 = year_22["강수일"]

# print(f"2022년도 강수 일수 평균: {np.average(days_22)}")
# print(f"2022년도 강수 일수 분산: {np.var(days_22)}")
# print(f"2022년도 강수 일수 표준편차: {np.std(days_22)}")

print(f"2022년도 강수량 평균: {np.average(rain_22)}")
print(f"2022년도 강수량 분산: {np.var(rain_22)}")
print(f"2022년도 강수량 표준편차: {np.std(rain_22)}")

print(f"중앙값: {np.median(rain_22)}")

print(rain_22.sort_values())