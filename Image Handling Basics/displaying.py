import cv2

image = cv2.imread('./images/python-ball.jpg')

if image is not None:
    cv2.imshow('Loaded Image', image) #open the image in a window
    cv2.waitKey(0) #wait for a key press to close the window
    cv2.destroyAllWindows() #close the window
else:
    print("Error: Could not load image.")