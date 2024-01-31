import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
import matplotlib.pyplot as plt


df = pd.read_csv('/home/jetson/project_Ai_ad/recommendation_datasets.csv')

target = df[['drink']]
print(target)
training_data = df.drop(['drink'], axis = 'columns')
print(training_data)

X_train, X_test, Y_train, Y_test = train_test_split(training_data, target, test_size = 0.2)

print(X_test)
print(X_train.shape)
print(X_test.shape)
print(Y_train.shape)
print(Y_test.shape)

model = Sequential()
model.add(Dense(128, input_dim =3, activation = 'relu'))
model.add(Dropout(0.02))
model.add(Dense(256, activation = 'relu'))
model.add(Dropout(0.2))
model.add(Dense(512, activation = 'relu'))
model.add(Dropout(0.2))
model.add(Dense(256, activation = 'relu'))
model.add(Dropout(0.2))
model.add(Dense(128, activation = 'relu'))
model.add(Dropout(0.02))
model.add(Dense(64, activation = 'relu'))
model.add(Dropout(0.02))
model.add(Dense(32, activation = 'relu'))
model.add(Dropout(0.02))
model.add(Dense(5, activation = 'softmax'))
model.summary()

model.compile(loss = 'mse', optimizer = 'adam',metrics = ['binary_accuracy'])
fit_hist = model.fit(X_train, Y_train, batch_size = 50, epochs = 30, validation_split = 0.2, verbose =1)

plt.plot(fit_hist.history['binary_accuracy'])
plt.plot(fit_hist.history['val_binary_accuracy'])
plt.show()

model.save('./models/recommendation_{}.h5'.format(fit_hist.history['binary_accuracy'][-1]))

score = model.evaluate(X_test, Y_test, verbose = 0)
print('loss :', score[0])
print('accuracy :', score[1])