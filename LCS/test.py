import cv2
import glob
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model


model = load_model('/home/jetson/project_Ai_ad/models/recommendation_0.20546874403953552.h5')

new_data = pd.DataFrame({'sex': [1], 'age': [5], 'emotion': [5]}, index=[0])

input_data = new_data.values
predictions = model.predict(input_data)

print(predictions)
predicted_class = int(np.argmax(predictions, axis=1))

print("Predicted Class:", predicted_class)

data_path = sorted(glob.glob('sample/*.mp4'))

print(data_path)

video = cv2.VideoCapture(data_path[predicted_class])

new_size = (800, 600)

while video.isOpened(): 
    ret, frame = video.read()
    frame =cv2.resize(frame, new_size)
    if not ret:
        print("프레임을 수신할 수 없습니다(스트림 끝?). 종료 중 ...")
        break
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Otter', frame)
    if cv2.waitKey(42) == ord('q'):
        break
video.release()
cv2.destroyAllWindows()