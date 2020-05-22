import cv2

img=cv2.imread('galaxy.jpg', 0) #method to read image, parameter: image, how do you want to read the image 0 grayscale, 1 3 band color, -1 color image

print(type(img))
print(img)
print(img.shape) #values of pixels in horizontal and vertical direction as a tuple
print(img.ndim) #display dimensions of the array


resized_image=cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
cv2.imshow("Galaxy", resized_image) #Show the image, Parameters: Title -  image object
cv2.imwrite("Galaxy_resized.jpg", resized_image) #Save resized image
cv2.waitKey(0) #0 for closing window any button, zb. 2000 miliseconds
cv2.destroyAllWindows()