import serial
import time
import cv2
import sys
import glob
import dlib
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
import threading

sys.path.append('/home/jetson/project_Ai_ad/LCS')
sys.path.append('/home/jetson/project_Ai_ad')

from face_detection import detection
# from serial_eyetracking import eye_tracking

## 얼굴 검출기 초기화
detector = dlib.get_frontal_face_detector()
# 얼굴 및 눈 검출을 위한 dlib의 face landmark predictor 로딩
predictor_path = './eye_tracking/shape_predictor_68_face_landmarks.dat'
predictor = dlib.shape_predictor(predictor_path)

serial_port = '/dev/ttyACM0'  # 시리얼 포트명, window의 경우 장치관리자에 들어가서 com으로 변경
baud_rate = 115200  # 통신 속도 (bps)

# 시리얼 포트 열기
ser = serial.Serial(serial_port, baud_rate)

emotion, sex, age = detection()
sex = round(sex)
age = age

model = load_model('/home/jetson/project_Ai_ad/models/recommendation_0.20546874403953552.h5')

new_data = pd.DataFrame({'sex': [sex], 'age': [age], 'emotion': [emotion]}, index=[0])

input_data = new_data.values
predictions = model.predict(input_data)

print(predictions)
predicted_class = int(np.argmax(predictions, axis=1))

print("Predicted Class:", predicted_class)

data_path = sorted(glob.glob('sample/*.mp4'))

video = cv2.VideoCapture(data_path[predicted_class])

new_size = (800, 600)

cap = cv2.VideoCapture(0)

# 눈동자 중심 좌표 이동 평균을 위한 큐 초기화
left_eye_center_queue = []
right_eye_center_queue = []
queue_size = 5  # 큐 크기
eye_check = 0
flag = 0
count = 0
eye_count = 0


def eye_tracking():    
    global eye_check
    global eye_count
    global count
    # 프레임 읽기
    while cap.isOpened():
        if flag ==1:
            break
        ret1, frame1 = cap.read()
        # 그레이스케일 변환
        gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
        img_gray_gaussian = cv2.GaussianBlur(gray, (5, 5), 0)  # 가우시안 필터 적용
        # 얼굴 검출
        faces = detector(img_gray_gaussian)

        for face in faces:
            # 얼굴에서 눈 영역 찾기
            landmarks = predictor(gray, face)

            left_eye_pts = []
            right_eye_pts = []

            for n in range(36, 42):  # 왼쪽 눈 랜드마크 인덱스: 36 ~ 41
                x, y = landmarks.part(n).x, landmarks.part(n).y
                left_eye_pts.append((x, y))

            for n in range(42, 48):  # 오른쪽 눈 랜드마크 인덱스: 42 ~ 47
                x, y = landmarks.part(n).x, landmarks.part(n).y
                right_eye_pts.append((x, y))

            # 눈 영역 추출
            left_eye_region = np.array(left_eye_pts, np.int32)
            right_eye_region = np.array(right_eye_pts, np.int32)

            # 눈동자 추정을 위해 ROI 설정
            left_eye_roi = gray[min(left_eye_region[:, 1]):max(left_eye_region[:, 1]),
                        min(left_eye_region[:, 0]):max(left_eye_region[:, 0])]
            right_eye_roi = gray[min(right_eye_region[:, 1]):max(right_eye_region[:, 1]),
                            min(right_eye_region[:, 0]):max(right_eye_region[:, 0])]

            # 눈동자 검출
            _, left_eye_thresh = cv2.threshold(left_eye_roi, 40, 255, cv2.THRESH_BINARY)
            _, right_eye_thresh = cv2.threshold(right_eye_roi, 40, 255, cv2.THRESH_BINARY)

            # 가장 어두운 부분 찾기
            left_eye_dark_region = np.unravel_index(np.argmin(left_eye_roi), left_eye_roi.shape)
            right_eye_dark_region = np.unravel_index(np.argmin(right_eye_roi), right_eye_roi.shape)

            # 눈동자 영역 그리기
            cv2.circle(frame1, (min(left_eye_region[:, 0]) + left_eye_dark_region[1],
                            min(left_eye_region[:, 1]) + left_eye_dark_region[0]), 2, (0, 255, 0), -1)

            cv2.circle(frame1, (min(right_eye_region[:, 0]) + right_eye_dark_region[1],
                            min(right_eye_region[:, 1]) + right_eye_dark_region[0]), 2, (0, 255, 0), -1)

            # 눈동자 중심 좌표 계산
            left_eye_center = (min(left_eye_region[:, 0]) + left_eye_dark_region[1],
                            min(left_eye_region[:, 1]) + left_eye_dark_region[0])
            right_eye_center = (min(right_eye_region[:, 0]) + right_eye_dark_region[1],
                                min(right_eye_region[:, 1]) + right_eye_dark_region[0])

            # 이동 평균을 적용하여 흔들림 보정
            left_eye_center_queue.append(left_eye_center)
            right_eye_center_queue.append(right_eye_center)

            if len(left_eye_center_queue) > queue_size:
                left_eye_center_queue.pop(0)
            if len(right_eye_center_queue) > queue_size:
                right_eye_center_queue.pop(0)

            left_eye_center_smoothed = np.mean(left_eye_center_queue, axis=0)
            right_eye_center_smoothed = np.mean(right_eye_center_queue, axis=0)

            # 보정된 눈동자 중심 좌표 출력
            print(f'Left Eye Center: {left_eye_center_smoothed},  Right Eye Center: {right_eye_center_smoothed}')
            if 330 <= left_eye_center_smoothed[0] <= 400:   # 모니터 양끝을 보고 값 측정해서 조절 필요
                eye_check = 1
                eye_count += 1
            else:
                eye_check = 0
            count += 1

    # return eye_check

eye_thread = threading.Thread(target=eye_tracking)
eye_thread.start()


while video.isOpened(): 

    ret, frame = video.read()
    # data_to_send = [0, 0]       # 아이트래킹 결과값, 제공음료 번호

    # for i in range(5):
    print(count, eye_count)

    if not ret:
        break 
    cv2.namedWindow('frame', cv2.WINDOW_NORMAL) 
    cv2.setWindowProperty('frame', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    # frame =cv2.resize(frame, new_size)
    if not ret:
        print("프레임을 수신할 수 없습니다(스트림 끝?). 종료 중 ...")
        break
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', frame)
    if cv2.waitKey(42) == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
flag =1
eye_thread.join()
print(eye_count)
print(count)

if eye_count/count >= 0.3:
    data = str(10 + predicted_class)
else:
    data = '00'
data_to_send = data.encode()

ser.write(data_to_send)
print(data_to_send)
time.sleep(1)
ser.close()
print("Serial port closed.")