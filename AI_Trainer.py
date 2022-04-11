import numpy as np
import time
import cv2
import posemodule as pm
import rf_random

cap=cv2.VideoCapture("C://Users//mathu//Downloads//curl.mp4")

detector=pm.poseDetector()
pTime=0
count = 0
dir = 0
while True:
    success, img=cap.read()
    #img = cv2.imread("C://Users//mathu//Downloads//pexels-gustavo-fring-3984372.jpg")
    img=cv2.resize(img,(1280,600))
    img=detector.findPose(img,False) #for draw line
    lmList=detector.findPosition(img,False) #for creating dots
    #print(lmList)
    if len(lmList)!=0:
        #for left arm
        angle=detector.findAngle(img,11,13,15)
        angle = detector.findAngle(img, 12, 14, 16)
        per = np.interp(angle, (210,310), (0, 100))
        bar = np.interp(angle, (220, 310), (650, 100))


        #per = np.interp(angle, (210, 310), (0, 100))
        #bar = np.interp(angle, (220, 310), (650, 100))
        #print(angle,per)
        #for right arm
        #detector.findAngle(img, 12, 14, 16)if per == 100:
        # Check for the dumbbell curls
        color = (255, 0, 255)

        if per == 100:
            color = (0, 255, 0)
            if dir == 0:
                count += 0.5
                dir = 1
        if per == 0:
            color = (0, 0, 255)
            if dir == 1:
                count += 0.5
                dir = 0
        print(count)
        # Draw Bar
        cv2.rectangle(img, (1100, 100), (1175, 650), color, 3)
        cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)
        cv2.putText(img, f'{int(per)} %', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 4,
                    color, 4)
        #DRAW CURLS
        cv2.rectangle(img, (0, 450), (200, 700), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(int(count)), (20, 600), cv2.FONT_HERSHEY_PLAIN, 10,
                    (255.0,0), 10)
    '''cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5,
                (255, 0, 0), 5)'''

    cv2.imshow("image",img)

    key=cv2.waitKey(1)
    if key == ord("q") or key == ord("Q"):
        break
cap.release()
cv2.destroyAllWindows()

import pickle
file=open("AI_Trainer.pkl","wb")
pickle.dump(,file)
