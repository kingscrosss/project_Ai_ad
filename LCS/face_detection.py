import subprocess



def detection():
    file_path = '/home/jetson/intel/open_model_zoo/demos/build/aarch64/Release/interactive_face_detection_demo'

    run_argument= ['-i', '0', '-m', '/home/jetson/intel/open_model_zoo/demos/interactive_face_detection_demo/cpp/intel/face-detection-adas-0001/FP16/face-detection-adas-0001.xml', 
                '--mag', '/home/jetson/intel/open_model_zoo/demos/interactive_face_detection_demo/cpp/intel/age-gender-recognition-retail-0013/FP16/age-gender-recognition-retail-0013.xml',
                '--mhp', '/home/jetson/intel/open_model_zoo/demos/interactive_face_detection_demo/cpp/intel/head-pose-estimation-adas-0001/FP16/head-pose-estimation-adas-0001.xml', 
                '--mem', '/home/jetson/intel/open_model_zoo/demos/interactive_face_detection_demo/cpp/intel/emotions-recognition-retail-0003/FP16/emotions-recognition-retail-0003.xml', 
                    '-d', 'CPU', '-r', '--noshow']

    process = subprocess.Popen([file_path] + run_argument, stdout=subprocess.PIPE, universal_newlines=True)

    emotion = ['neutral', 'happy', 'sad', 'surprise', 'anger']
    flag = 0
    try:
        # 실시간으로 표준 출력을 읽어와서 확인
        for line in iter(process.stdout.readline, ''):
            if "neutral" in line:
                split_by_comma = line.split(',')
                result = [item.split('=') for item in split_by_comma]
                max = result[0][1]
                max_value = 0
                for i in range(5):
                    if result[i][1]>max:
                        max = result[i][1]
                        max_value = i
                print(max, emotion[max_value])
                flag = flag+1
            elif "male" in line:
                split_by_comma1 = line.split(',')
                result1 = [item.split('=') for item in split_by_comma1]
                sex = float(result1[1][1])
                age = float(result1[2][1])
                print('male : ', sex)
                print('age : ', age)
                flag = flag+1
            if flag==2:
                process.terminate()
                break
            
    finally:
        # subprocess가 종료되면 반환 코드 확인
        return_code = process.wait()
        print(f"Subprocess exited with return code: {return_code}")
    
    return max_value, sex, age

# a, b, c = detection()
# print(a, b, c)