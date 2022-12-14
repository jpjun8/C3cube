import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import linear_model
import scipy.stats as stats

plt.rc('font', family='Malgun Gothic')

# TODO: What is mean(average)?

# bi = np.random.binomial(n=100, p=0.5, size=1000)
# s = np.random.normal(50, 20, size=1000)

# plt.rc('font', family='Malgun Gothic')
# plt.title("씨큐브학교 수학 점수 vs. 인원")
# plt.xlabel("점수")
# plt.ylabel("인원")
# # plt.hist(s, alpha=0.5, bins=25, range=(0, 100))
# plt.scatter(s, np.arange(0, 1000))
# plt.show()

# TODO: What is mode?

# tips = sns.load_dataset("tips")
# sns.scatterplot(data=tips, x="total_bill", y="tip", hue="sex")
# plt.show()

# TODO: 1 small variance, 1 large variance

# views = [1700, 2100, 3500, 2400, 1800, 2500, 3200]
# views2 = np.random.normal(np.mean(views), 100, size=7)
# print(views)
# print(views2)
# print(np.mean(views))
# print(np.mean(views2))

# x = ["12/1", "12/2", "12/3", "12/4", "12/5", "12/6", "12/7"]

# plt.title("게임 동영상 조회수")
# plt.scatter(x, views2, label="조회수", c = 'darkorange')
# plt.axhline(y = np.mean(views2), color="red", label="평균")

# plt.ylim(1500, 3600)
# plt.xlabel("날짜")
# plt.ylabel("조회수")
# plt.legend()

# plt.show()

# TODO: variance plot to explain how variance works

# x = np.arange(0,100, 0.01)
# plt.title("수학 점수 vs. 학생수(%)")
# plt.plot(x, stats.norm.pdf(x, 30, 30) * 100, label="A반") # low variance
# plt.plot(x, stats.norm.pdf(x, 50, 10) * 100, label="B반") # medium variance
# plt.plot(x, stats.norm.pdf(x, 70, 20) * 100, label="C반")   # high variance
# # plt.text(35, 3.5, "A반")
# # plt.text(15, 1.0, "B반")
# plt.axvline(x = 50, linestyle="--", color="black")
# plt.xlabel("수학 점수")
# plt.ylabel("학생수(%)")
# plt.legend(prop={'size': 15})
# plt.show()

# TODO: variance sample for 'check'

# x = np.arange(140, 190, 0.01)
# plt.title("키 vs. 학생 수")
# plt.plot(x, stats.norm.pdf(x, 153, 10) * len(x), label="여학생", c="orangered")
# plt.plot(x, stats.norm.pdf(x, 175, 20) * len(x), label="남학생", c="dodgerblue")
# plt.axvline(x = 153, linestyle="--", color="crimson", label="여학생 평균")
# plt.axvline(x = 175, linestyle="--", color="navy", label="남학생 평균")
# plt.xlabel("키")
# plt.ylabel("학생 수")
# plt.ylim(0.0, 250)
# plt.legend(prop={'size': 15})
# plt.show()

