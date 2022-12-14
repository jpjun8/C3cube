import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

# TODO: 문제 정의
# 

# train.csv from bike data (not using test)

df = pd.read_csv("train.csv")
print(df.head())