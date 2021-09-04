import cv2
from random import randrange
# cv2.__version__
#loading some pre trained data from github opencv (haar cascade algorithm)
# obj=cv2()
# trained_face_data =cv2.cv2.CascadeClassifier('haarcascade_frontalface_extended.xml')
trained_face_data = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#choosing a image to detecting face
# img=cv2.imread('rj.png')
# webcam = cv2.cv2.VideoCapture(video_name)    #use vieoname for detect faces in video '0' use for webcam
webcam = cv2.VideoCapture(0)

#iterate forever over frame
while True:
    # read the current frame
    successful_frame_read, frame=webcam.read() 

    grayscaled_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    for (x,y,w,h) in face_coordinates:
        cv2.rectangle(frame, (x,y), (x+w,y+h),(randrange(128,256),randrange(128,256),randrange(128,256)),2)


    cv2.imshow('Rohit Singh',frame)

    key = cv2.waitKey(1)
    if key==81 or key==113:
        break

webcam.release()
#must convert it to greyscale
# grayscaled_img=cv2.cvtColor(img,cv2.cv2.COLOR_BGR2GRAY)
# grayscaled_img=cv2.cvtColor(frame,cv2.cv2.COLOR_BGR2GRAY)

#detect faces
# face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
# print(face_coordinates)

#draw rectangle around the faces
# (x,y,w,h)=face_coordinates[0]
# for (x,y,w,h) in face_coordinates:
#     cv2.rectangle(img, (x,y), (x+w,y+h),(randrange(128,256),randrange(128,256),randrange(128,256)),2)


#display image with faces
# cv2.cv2.imshow('Rohit Singh',grayscaled_img)
# cv2.waitKey(1)

print("code completed")
