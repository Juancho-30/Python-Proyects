import cv2, time, pandas
from datetime import datetime

first_frame = None #Variable with nothing to it
status_list = [None, None]
times = []
df = pandas.DataFrame(columns = ["Start", "End"])

video = cv2.VideoCapture(0) #Method that captures video , 0, 1, 2, 3 for webcams, " " for a video saved

a=0
while True:

      check, frame = video.read() #check is for if the video is there, frame is 3 bands image procesing by frames
      status = 0 
      gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      gray = cv2.GaussianBlur(gray, (21,21), 0) #Blur the image, smooth it and removes noise for calculation of difference
                              #Parameters: Image - Tuple of bluriness(widt and height), (standrad deviation)
      if first_frame is None:
            first_frame = gray #First frame store the gray frame
            continue #After first frame is gotten, go to second iteration as continue statement

      delta_frame = cv2.absdiff(first_frame, gray) #absolute diference between 2 frames, diference between intensities of corresponding pixels

      thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1] #Difference, 255 for white, black pixel for less than 30
      thresh_frame = cv2.dilate(thresh_frame, None, iterations = 3) #Smooth the image, bigger iterations, smoother

      (cnts,_) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                                    #Ccopy of the frame, Retrieve external (Draw external contours of the object, Aproximation method)

      for contour in cnts:
            if cv2.contourArea(contour) < 10000: #if are is less than 10000 pixels continue
                  continue
            status = 1
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255,0), 3) #Draw rectangle in actual frame
                              #(x,y) upper left corner, (x+w, y+h) down right corner, (0, 255,0) color, 3 width

      status_list.append(status)

      status_list = status_list[-2:]


      if status_list[-1] == 1 and status_list[-2] == 0: #When status  changed from 1 to 0
            times.append(datetime.now())
      if status_list[-1] == 0 and status_list[-2] == 1: #And 0 to 1
            times.append(datetime.now())

      cv2.imshow("Gray Frame", gray)
      cv2.imshow("Delta Frame",delta_frame)
      cv2.imshow("Threshold Frame",thresh_frame)
      cv2.imshow("Color Frame", frame)


      key = cv2.waitKey(1) #wait 1 ms
      #print(gray)

      if key==ord('q'):
            if status == 1: # if entered an object
                  times.append(datetime.now())
            break

print(status_list)
print(times)


for i in range(0, len(times), 2):
      df = df.append({"Start":times[i], "End":times[i+1]}, ignore_index=True)

df.to_csv("Times.csv")

video.release()
cv2.destroyAllWindows