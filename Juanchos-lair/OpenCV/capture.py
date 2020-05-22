import cv2, time

video = cv2.VideoCapture(0) #Method that captures video , 0, 1, 2, 3 for webcams, " " for a video saved

a=0
while True:
      a=a+1
      check, frame = video.read() #check is for if the video is there, frame is 3 bands image procesing by frames

      gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


      #time.sleep(3)
      cv2.imshow("Capturing", gray)

      key = cv2.waitKey(1)

      if key==ord('q'):
            break

print(a) #number of iterations being created 
video.release()
cv2.destroyAllWindows