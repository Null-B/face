import cv2

THE_Data = cv2.CascadeClassifier('yes2.xml')
webcam = cv2.VideoCapture(0)

while True:
    succesful_webcam_read,  feame =  webcam.read()

    grey_img = cv2.cvtColor(feame, cv2.COLOR_BGR2GRAY)

    face_coerds = THE_Data.detectMultiScale(grey_img)


    for (x,y,w,h) in face_coerds:
        cv2.rectangle(feame, (x,y), (x+w, y+h), (0,255,0),2)
    
    cv2.imshow('dfd', feame)
    cv2.waitKey(1)
