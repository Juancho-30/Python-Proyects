import cv2

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml") #Cascade clasifier object for the face recognition

img = cv2.imread("news.jpg") #Without parameter is read as color image

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #cONVERT COLOR IMAGE TO GRAYSCALE

faces = face_cascade.detectMultiScale(gray_img, 
scaleFactor=1.05, #Decrease the scale by 5% for next search, downscale the image and search for faces
minNeighbors=5) #

for x,y, w, h in faces:
   img=cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 3)

resized = cv2.resize(img,(int(img.shape[1]/3), int(img.shape[0]/3)))
cv2.imshow("Gray",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()