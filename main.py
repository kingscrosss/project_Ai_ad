import serial
import time
import sys

sys.path.append('/home/jetson/work/project_Ai_ad/LCS')
sys.path.append('/home/jetson/work/project_Ai_ad/YYB')

from face_detection import detection


serial_port = '/dev/ttyACM12'  # 시리얼 포트명, window의 경우 장치관리자에 들어가서 com으로 변경
baud_rate = 115200  # 통신 속도 (bps)

# 시리얼 포트 열기
ser = serial.Serial(serial_port, baud_rate)

emotion, sex, age = detection()
print(emotion)
sex = round(sex)
age = int(age/10)


data = sex*10+age
print(data)

data_to_send = data

try:
    while True:
        data_to_send = input().encode()     # 회전 상태 반전
        # 데이터 전송
        ser.write(data_to_send)
        print(data_to_send)
        time.sleep(1)

except KeyboardInterrupt:
    # Ctrl+C로 종료하면 예외가 발생하고, 시리얼 포트를 닫습니다.
    ser.close()
    print("Serial port closed.")