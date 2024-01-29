##### 생성했던 데이터셋을 통해
### 모델을 생성 및 학습한 후, 예상되는 음료수 값을 출력하고, 
### 출력된 값과 실제 값 사이의 오차 지표를 생성하는 코드.



import pandas as pd
import numpy as np

# Make numpy values easier to read.
np.set_printoptions(precision=3, suppress=True)

import tensorflow as tf
from tensorflow.keras import layers


abalone_Full = pd.read_csv("/home/jetson/work/project_Ai_ad/YYB/Proj_ADR_01/Datasets_02.csv", 
                            names=["Sex", "Age", "Bvrg"])

abalone_Full["Sex"] = abalone_Full["Sex"].map({"남": 1, "여": 2},
                                                na_action=None,)
# abalone_train["Age"] = abalone_train["Age"].map({"10": 10, "20": 20,
#                                                  "30": 30, "40": 40, "50": 50},
#                                                 na_action=None,)

print(abalone_Full.dtypes)

print(abalone_Full.head())


abalone_features_T = abalone_Full.copy()
abalone_labels_T = abalone_features_T.pop('Bvrg')



abalone_features_T = np.array(abalone_features_T)
print(abalone_features_T)


######################

from tensorflow.keras.layers import Dense, Input, Flatten
from tensorflow.keras.models import Sequential, Model



#출력 데이터 크기 : 15개의 카테고리
num_classes = 1

#[1]
model = Sequential()
#[2]
model.add(Input(shape=(2,)))

model.add(Dense(10, activation='relu'))

model.add(Dense(15, activation='relu'))

model.add(Dense(10, activation='relu'))
#[3]
model.add(Dense(num_classes, activation='softmax'))


######################


# model = tf.keras.Sequential([
#   layers.Dense(64),
#   layers.Dense(1)
# ])



model.compile(loss = tf.keras.losses.MeanSquaredError(),
                      optimizer = tf.keras.optimizers.Adam())



model.fit(abalone_features_T, abalone_labels_T, 
                  batch_size = 100, epochs=100)



####################

abalone_Full = pd.read_csv("/home/jetson/work/project_Ai_ad/YYB/Proj_ADR_01/Datasets_01.csv", 
                            names=["Sex", "Age", "Bvrg"])

abalone_Full["Sex"] = abalone_Full["Sex"].map({"남": 1, "여": 2},
                                                na_action=None,)
# abalone_train["Age"] = abalone_train["Age"].map({"10": 10, "20": 20,
#                                                  "30": 30, "40": 40, "50": 50},
#                                                 na_action=None,)

print(abalone_Full.dtypes)

print(abalone_Full.head())


abalone_features_E = abalone_Full.copy()
abalone_labels_E = abalone_features_E.pop('Bvrg')



abalone_features_E = np.array(abalone_features_E)
print(abalone_features_E)



####################

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
import numpy as np
from sklearn.metrics import mean_squared_error

import random


X_Exam = abalone_features_E
Y_Exam = abalone_labels_E
# Y_Pred = model.predict(X_Exam)
Y_Pred = []

for i in range(1000):
    Y_Pred.append(random.choices(range(1, 16)))

print(Y_Pred)



### 예측했던 값과 실제 값과의 오차 지표 : rmse 값

mse = mean_squared_error(Y_Exam, Y_Pred)
rmse = np.sqrt(mse)
print(rmse)