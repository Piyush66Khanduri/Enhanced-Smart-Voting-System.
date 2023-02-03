import cv2
import face_Recognition
vd=cv2.VideoCapture(0);

img=face_Recognition.load_image_file("Allimg/piyush.jpg")[0]
img2=cv.cvtColor(img,cv.COLOR_BGR2RGB);

cv.imshow(" ",img2);
cv.waitKey(0)