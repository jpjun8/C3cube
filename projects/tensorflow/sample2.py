# 데이터 전처리
import pandas as pd

data = pd.read_csv('gpascore.csv')

# print(data.isnull().sum())
data = data.dropna()

y데이터 = data['admit'].values
x데이터 = []

for i, rows in data.iterrows():
    x데이터.append([rows['gre'], rows['gpa'], rows['rank']])

import tensorflow as tf
import numpy as np

# 딥러닝 모델 디자인하기

## Sequential 쓰면 신경망 레이어들 쉽게 만들어줌
## activation 종류 : sigmoid, tanh, relu, softamx, leakyRelu, ...
model = tf.keras.models.Sequential([
    # 일반적인 레이어
    # 64, 128, 1 : 레이어의 갯수 / 노드 갯수 
    ## 결과 잘 나올때까지 실험으로 파악
    tf.keras.layers.Dense(64, activation='tanh'),
    tf.keras.layers.Dense(128, 'tanh'),
    tf.keras.layers.Dense(1, activation='sigmoid'), # 확률 한개를 예측
])

## optimizer : 알파값을 알맞게 조정해줌
## adam, adagrad, adadelta, rmsprop, sgd, ...

## loss : 손실함수
## binary_crossentropy : 결과가 0과 1사이의 분류/확률 문제에서 사용
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

## x 데이터 : independent variables, 예측에 필요한 input
## y 데이터 : dependent variables, 답
## x, y 모두 numpy array 또는 tf로 넣어주어야함
model.fit(np.array(x데이터), np.array(y데이터), epochs=1000)

# 예측
예측값 = model.predict([[750, 3.70, 3], [400, 2.2, 1]])
print(예측값)