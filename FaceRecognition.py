import sys 			# for exit
import os			# for file exist check
import cv2			# for image operations, face recognition

# Create a CascadeClassifier object.
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Get image path from user.
# image_path = raw_input("Insert image path: ")

# if not os.file.exists():
# 	print(image_path + " is not a valid image path")
# 	sys.exit()

# Reading the image.
image = cv2.imread(<insert image here>)

# Reading the image as gray scale image.
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Search the coordinate if the image.
faces = face_cascade.detectMultiScale(gray_image, scaleFactor = 1.05, minNeighbors = 5)

print(type(faces))
print(faces)

for x, y, w, h in faces:
	image = cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 3)

resized_image = cv2.resize(image, (int(image.shape[1]/2), int(image.shape[0]/2)))
window_headline = "Face Recognition"
cv2.imshow(window_headline, resized_image)

# User must press any key to close the image window.
cv2.waitKey(0)