import cv2

image = cv2.imread('./images/python-ball.jpg')

if image is None:
    print("Error: Could not load image.")
else:
    print("Image loaded successfully.")