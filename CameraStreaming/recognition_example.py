import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
lst = ["a_unevenness", "main_road", "no_drive", "no_entry", "parking", "pedistrain", "road_works", "stop", "way_out"]
while(True):
   ret, frame = cap.read()
   print (ret)
   hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

   hsv = cv.blur(hsv, (5, 5))

   lower = np.array([0, 100, 100])
   upper = np.array([129, 255, 255])
   thresh = cv.inRange(hsv, lower, upper)
   cv.imshow("test", thresh)
   thresh = cv.erode(thresh, None, iterations=2)
   thresh = cv.dilate(thresh, None, iterations=4)

   contours = cv.findContours(thresh.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
   contours=contours[1]
   for cnt in contours:
      c = sorted(contours, key=cv.contourArea, reverse=True)[0]
      rect = cv.minAreaRect(c)
      box = np.int0(cv.boxPoints(rect))
      cv.drawContours(frame, [box], -1, (0, 255, 0), 3)  # draw contours in green color
      cv.imshow("test",frame)
      y1 = int(box[0][1])
      x2 = int(box[1][0])
      y2 = int(box[1][1])
      x3 = int(box[2][0])

      roiImg = frame[y2:y1, x2:x3]

      if roiImg.any():
         cv.imshow('roiImg', roiImg)
         for i in lst:
             noDrive = cv.imread("/home/user/Desktop/raspberry_car/signs/"+i+".png")
             resizedRoi = cv.resize(roiImg, (100, 100))
             noDrive=cv.resize(noDrive,(100, 100))

             xresizedRoi=cv.inRange(resizedRoi, lower, upper)
             xnoDrive=cv.inRange(noDrive, lower, upper)

             identity_percent=0
             for i in range(100):
                for j in range(100):
                   if (xresizedRoi[i][j]==xnoDrive[i][j]):
                      identity_percent=identity_percent+1
             print (identity_percent)

   cv.imshow('frame', frame)

   if cv.waitKey(1) & 0xFF == ord('q'):
       break
cap.release()
cv.destroyAllWindows()
