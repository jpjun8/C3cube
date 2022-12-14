import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
from sklearn import linear_model

df = pd.read_csv("rain.csv", encoding="cp949")

year_22 = df[df["년도"] == 2022]
# print(year_22)

month_22 = year_22["월"]
# print(month_22)

rain_22 = year_22["강수량"]
# print(rain_22)

rain_22_summer = rain_22.iloc[5:8]
# print(rain_22_summer)

year_22_nonsummer = year_22[(year_22["월"] < 6) | (year_22["월"] > 8)]
# print(year_22_nonsummer)

rain_22_nonsummer = year_22_nonsummer["강수량"]
# print(rain_22_nonsummer)

rain_days_22 = year_22["강수일"]

rain_avg_22 = np.average(rain_22, axis=0)
print(f"전체 평균: {rain_avg_22}")

rain_avg_22summer = np.average(rain_22_summer, axis=0)
print(f"여름 평균: {rain_avg_22summer}")

rain_avg_22nonsummer = np.average(rain_22_nonsummer, axis=0)
print(f"여름 제외 평균: {rain_avg_22nonsummer}")

# variance
print(f"분산: {np.var(rain_22)}")

# std
print(f"표준편차: {np.std(rain_22)}")

# temp = pd.DataFrame({
#     'x': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
#     'y': random.sample(range(1, 15), 12)
# })

# plt.scatter(temp.x, temp.y)
# plt.axhline(y = np.nanmean(temp.y))

# plt.show()

# X = np.c_[.5, 1].T
# y = [.5, 1]
# X_test = np.c_[0, 2].T

# reg = linear_model.LinearRegression()
# reg.fit(X, y)

# np.random.seed(0)
# for _ in range(6):
#     noisy_X = X + np.random.normal(loc=0, scale=.1, size=X.shape)
#     plt.plot(noisy_X, y, 'o')
#     reg.fit(noisy_X, y)
#     plt.plot(X_test, reg.predict(X_test))

# plt.show()

# eng = [95, 55,60, 85, 100, 30, 75]
# print(np.mean(eng))
# print(np.median(eng))
# print(np.var(eng))
# print(np.std(eng))

# print(np.average([1, 121, 16, 36, 361, 961, 576]))