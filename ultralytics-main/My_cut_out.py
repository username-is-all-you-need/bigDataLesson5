import cv2
video = cv2.VideoCapture("../BVN2.mp4")
num = 0   #计数器
save_step = 30 #间隔帧
while True:
 ret, frame = video.read()
 if not ret:break;
 num += 1
 if num % save_step == 0 :
    cv2.imwrite("../images/test" + str(num) + ".jpg",frame)