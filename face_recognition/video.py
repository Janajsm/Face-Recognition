import cv2
trainedDataset = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

video=cv2.VideoCapture('videos/team_video.mp4')
while True:
    success,frame = video.read()
    if success == True:
        gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = trainedDataset.detectMultiScale(gray_img)
        for x, y, w, h in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.imshow('video', frame)
        cv2.waitKey(1) #One mile second delay
    else:
        print("Video Completed or Frame Nil")
        break
