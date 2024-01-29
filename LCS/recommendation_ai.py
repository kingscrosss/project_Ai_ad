import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("/home/jetson/work/project_Ai_ad/YYB/Proj_ADR_01/Datasets_02.csv", names=["Sex", "Age", "Bvrg"])

print(df.head())

df["Sex"] = df["Sex"].map({"남": 1, "여": 0},
                                                na_action=None,)

print(df.head())

scaler = StandardScaler()
scaled_data = scaler.fit_transform(value_data)
value_data = pd.DataFrame(scaled_data, columns = value_data.columns)
