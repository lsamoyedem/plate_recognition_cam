from __future__ import print_function
import cv2
import time
import pickle
import requests
import jsonpickle

addr = 'http://127.0.0.1:5000'
test_url = addr + '/api/test'

content_type = 'image/jpeg'
headers = {'content-type': content_type}

cam = cv2.VideoCapture('C:\\resource\\video720p.mkv')

cam.set(3, 320)
cam.set(4, 240)

img_counter = 0

encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
frame_rate = 10
prev = 0
while cam.isOpened(): 
    ret, frame = cam.read()
    if (ret == False):
          break
    time_elapsed = time.time() - prev
    if time_elapsed > 2./frame_rate:
        prev = time.time()
        startTime = time.time()

        result, frame = cv2.imencode('.jpg', frame, encode_param)
        data = pickle.dumps(frame, 0)
        response = requests.post(test_url, data=frame.tostring(), headers=headers)
        if response.status_code == 200:
            print('Encontrou')
            print(jsonpickle.decode(response.text))

cam.release()