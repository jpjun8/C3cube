import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
from sklearn import linear_model

plt.rc('font', family='Malgun Gothic')
plt.style.use('ggplot')

"""
2019-2021 세계 행복지수 보고서
dystopia = 1.83
부정부패: 높을수록 없음
GDP 점수, 사회복지, 삶의 질, 의사결정, 관대함: 높을수록 좋음
"""

df = pd.read_csv("WHR22.csv", encoding="cp949")
min_score = df["Dystopia + Residual"]
gdp = df["GDP"]
social = df["Social Support"]
health = df["Healthy Life Expectancy"]
freedom = df["Freedom"]
generosity = df["Generosity"]
corruption = df["Corruption"]

# print(gdp.head())

################################

# barchart: vertical/horizontal
## vertical
# colors = ['orangered', 'dodgerblue', 'darkorchid', 'forestgreen']
# x = ["대한민국", "일본", "미국", "독일"]
# height = [175.52, 172.06, 176.94, 180.28]
# bars = plt.bar(x, height)
# for i in range(len(bars)):
#     bars[i].set_color(colors[i])
# plt.title("나라별 평균키")
# plt.ylabel("키(cm)")
# plt.ylim(170, 185)
# # plt.legend()
# plt.show()

# stacked barchart
# 용돈 사용처? 음식 종류별 먹은 횟수? (월마다)
# df = pd.DataFrame(
#     {
#         "월": ["9월", "10월", "11월", "12월"],
#         "한식": [20, 10, 15, 5],
#         "일식": [5, 9, 11, 3],
#         "중식": [2, 5, 1, 10],
#         "양식": [3, 7, 3, 13]
#     }
# )

# df.plot(x="월", kind='bar', stacked=True, title="월별 음식 종류별 섭취 횟수", alpha=0.75, rot=0)
# plt.ylabel("섭취 횟수")
# plt.legend(bbox_to_anchor=(1.0, 1.0))
# plt.show()

# pie chart: 2022년 상반기 스마트폰 점유율
x = ["애플", "삼성", '오포', '샤오미', '기타']
data = np.array([57, 19, 4, 4, 16])
plt.title("세계 스마트폰 점유율")
plt.pie(data, labels=x, startangle=90, autopct='%1.1f%%', shadow=True)
plt.show()

# comparison: pie chart vs. barchart

# plot

# comparison: barchart vs. plot

# challenge: 1 dataset for all questions

################################

