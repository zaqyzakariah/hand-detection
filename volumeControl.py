from handDetection import HandDetection
import cv2
import math
import numpy as np


handDetection = HandDetection(min_detection_confidence=0.5,min_tracking_confidence=0.5)

webcam = cv2.VideoCapture()
webcam.open(0,cv2.CAP_DSHOW)

min_dest,max_dest = 25,190
while True:
    status , frame = webcam.read()
    frame = cv2.flip(frame,1)
    handLandMarks = handDetection.findHandLandMarks(image=frame,draw=True)
    if len(handLandMarks) !=0:
        x4,y4 = handLandMarks[4][1],handLandMarks[4][2]
        x8,y8 = handLandMarks[8][1],handLandMarks[8][2]

        #circle
        cv2.circle(frame,(x4,y4),10,(255,255,0),cv2.FILLED)
        cv2.circle(frame,(x8,y8),10,(255,255,0),cv2.FILLED)
        xTengah,yTengah = int((x4+x8)/2),int((y4+y8)/2)
        cv2.circle(frame,(xTengah,yTengah),10,(255,255,0),cv2.FILLED)
        cv2.line(frame,(x4,y4),(x8,y8),(255,255,0),5)

        length = math.hypot(x4-x8,y4-y8)
        vol_bar = np.interp(length,[min_dest,max_dest],[340,143])
        vol_perc = np.interp(length,[min_dest,max_dest],[0,100])
        
        #kotak
        cv2.rectangle(frame,(55,140),(85,340),(0,0,0),3)
        cv2.rectangle(frame,(58,int(vol_bar)),(82,337),(0,255,0),cv2.FILLED)


        cv2.putText(frame, f'Vol = {int(vol_perc)} % ',(18,110),cv2.FONT_HERSHEY_COMPLEX, 0.6 ,(0,0,255),2)

    cv2.imshow("Volume Control",frame)
    if cv2.waitKey(1) == ord('a'):
        break
cv2.destroyAllWindows()
webcam.release()