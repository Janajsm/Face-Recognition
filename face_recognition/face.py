import cv2
# print(cv2.__version__)

#Trained DataSet
trainedDataset = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#Read a Image
img = cv2.imread('images/grp_img.jpg')

#convert into grayscale
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = trainedDataset.detectMultiScale(gray)
# print(faces)
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow('Jana',img)
# cv2.imshow('Group Img',gray)
cv2.waitKey()
