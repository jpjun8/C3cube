import csv
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
from sklearn.linear_model import LinearRegression
# from sklearn.preprocessing import PolynomialFeatures - For polynomial regression

# 1. Frequency of Listening Music vs. Duration of Study

f1 = open("survey.csv", "r", encoding="UTF-8")
d1 = csv.reader(f1)

freq = []
duration = []

# freq: 1-5 (not listening ~ listening enthusiastically)
# duration: duration of study (in minutes)

next(d1) # exclude header from csv

for row in d1:
	# row[0] includes id
	freq.append(int(row[1]))
	duration.append(float(row[2]))

f1.close()

# Linear Regression Analysis

x = np.array(freq).reshape((-1, 1))
y = np.array(duration)

model = LinearRegression().fit(x, y)

r_sq = model.score(x, y)

print(f"R val: {np.sqrt(r_sq)}") # 상관계수, R
print(f"coefficient of determination: {r_sq}") # 결정계수, R^2
print(f"intercept: {model.intercept_}") # y 절편
print(f"slope: {model.coef_}") # 기울기

# Prediction (Optional)

# y_pred = model.predict(x)
# print(f"predicted response :\n{y_pred}")

# Poly (Optional)

# trans = PolynomialFeatures(degree=6, include_bias=False)
# x_ = trans.fit_transform(x)

# mod = LinearRegression().fit(x_, y)

# print('================POLY=================')
# print(f"coefficient of determination: {mod.score(x_, y)}") # 결정계수, R^2
# print(f"intercept: {mod.intercept_}") # B0
# print(f"slope: {mod.coef_}") # B1

# 2. Lyrical vs. Non-lyrical Music
# Do they give us statistically significant difference?

f2 = open("lyrics.csv", "r", encoding="UTF-8")
d2 = csv.reader(f2)

next(d2)

nonlyrical = []
lyrical = []

# genre, difficulty, helpful, will be helpful

for row in d2:
	if row[0] == "Non-lyrical":
		nonlyrical.append(np.array(row[1:]).astype(np.int_))
	elif row[0] == "Lyrical":
		lyrical.append(np.array(row[1:]).astype(np.int_))

nonlyrical = np.array(nonlyrical)
lyrical = np.array(lyrical)

# Equal variance assumed
eq_var = stats.ttest_ind(nonlyrical, lyrical, equal_var=True)
print(eq_var)
# print(eq_var.pvalue)

# Nonequal variance assumed
noneq_var = stats.ttest_ind(nonlyrical, lyrical, equal_var=False)
print(noneq_var)
# print(noneq_var.pvalue)

## T-test < 0.05 (p-value) : Does not matter the type of music being played while studying

# 3. Classification Analysis

f3 = open("classification.csv", "r", encoding="UTF-8")
d3 = csv.reader(f3)

next(d3)

tot = []
names = []

for row in d3:
	names.append(row[0])
	tot.append(int(row[1]))

how = tot[:5] # how does music influence in studying
will = tot[5:] # do you think music is helpful in academic performance

how_names = names[:5]
will_names = names[5:]

# Graph Representation (Scatterplot and Linear Regression)

fig = plt.figure(figsize=(12, 8))
plt.subplots_adjust(wspace = 0.25, hspace = 0.25)

## Regression Plot Prep

coef = np.polyfit(freq, duration, 1)
poly1d_fn = np.poly1d(coef)

## Classification Plot Prep

colors = ['limegreen', 'turquoise', 'darkorange', 'blueviolet', 'firebrick']

sub1 = fig.add_subplot(2, 2, 1)
plt.annotate('sub1', xy = (0.5, -0.5), va = 'center', ha = 'center')
sub1.plot(freq, duration, 'yo', freq, poly1d_fn(freq), '--k')

sub2 = fig.add_subplot(2, 2, (3, 4))
plt.annotate('sub2', xy = (0.5, -0.5), va = 'center', ha = 'center')
barlist1 = sub2.barh(how_names, how)
for i in range(len(barlist1)):
	barlist1[i].set_color(colors[i])

sub3 = fig.add_subplot(2, 2, 2)
plt.annotate('sub3', xy = (0.5, -0.5), va = 'center', ha = 'center')
barlist2 = sub3.bar(will_names, will)
barlist2[0].set_color('limegreen')
barlist2[1].set_color('firebrick')
barlist2[2].set_color('yellow')

plt.show()