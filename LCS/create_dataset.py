import random
import pandas as pd
import csv


sex =[]
age = []
drink = []
emotion = []

# 커피, 우유, 이온음료, 과일쥬스. 탄산음료
male = [2.28, 2.41, 2.23, 2.67, 2.20]
female = [2.29, 2.39, 2.09, 2.67, 1.94]

a1 = [2.12, 2.63, 2.60, 2.89, 2.62]
a2 = [2.34, 2.54, 2.31, 2.83, 2.22]
a3 = [2.35, 2.24, 2.08, 2.62, 1.86]
a4 = [2.40, 2.24, 1.80, 2.45, 1.74]
a5 = [2.17, 2.27, 1.75, 2.45, 1.54]


for i in range(10000):
    data1 = random.randint(0, 1)
    data2 = random.randint(1, 5)
    data3 = random.randint(0, 4)
    sex.append(data1)
    age.append(data2)
    drink.append(data3)
    if data1 == 0 and data2 == 1:
        data4 = female[data3] + a1[data3]
    if data1 == 1 and data2 == 1:
        data4 = male[data3] + a1[data3]
    if data1 == 0 and data2 == 2:
        data4 = female[data3] + a2[data3]
    if data1 == 1 and data2 == 2:
        data4 = male[data3] + a2[data3]
    if data1 == 0 and data2 == 3:
        data4 = female[data3] + a3[data3]
    if data1 == 1 and data2 == 3:
        data4 = male[data3] + a3[data3]
    if data1 == 0 and data2 == 4:
        data4 = female[data3] + a4[data3]
    if data1 == 1 and data2 == 4:
        data4 = male[data3] + a4[data3]
    if data1 == 0 and data2 == 5:
        data4 = female[data3] + a5[data3]
    if data1 == 1 and data2 == 5:
        data4 = male[data3] + a5[data3]
    emotion.append(round(data4))

df = pd.DataFrame({'sex': sex, 'age' : age, 'drink' : drink, 'emotion' : emotion})

df.to_csv('recommendation_datasets.csv', index=False)

print(df.head())
