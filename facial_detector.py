import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("news.jpg")
grey_image = cv2.imread("news.jpg", 0)
#grey_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Converts image to greyscale.

faces = face_cascade.detectMultiScale(grey_image, scaleFactor=1.05, minNeighbors=5)

for x, y, h, w in faces:
    img=cv2.rectangle(img, (x,y),(x+w, y+h), (0,255,0), 3)
    # Params: img-file to draw on
    #         (x,y)- coordinates of the left hand top of rectangle
    #         (x+w, y+h) - Coordinates of lower right edge of rectangle
    #         (0,233,0) - BGR value of rectangle
    #         3 - width of rectangle
    
    
print(type(faces))
print(faces)

cv2.imshow('Gray', img)
cv2.waitKey(0)
cv2.destroyAllWindows()