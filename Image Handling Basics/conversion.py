import cv2

image = cv2.imread('./images/python-ball.jpg')
imageOfDog = cv2.imread('./images/dog.jpeg')

if image is not None:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #convert the image to grayscale
    cv2.imshow('Grayscale Image', gray) #open the grayscale image in a window
    cv2.waitKey(0) #wait for a key press to close the window
    cv2.destroyAllWindows() #close the window
else:
    print("Error: Could not load image.")

imageOfDog = cv2.imread('./images/dog.jpeg')
if imageOfDog is not None:
    grayDog = cv2.cvtColor(imageOfDog, cv2.COLOR_BGR2GRAY) #convert the dog image to grayscale
    cv2.imshow('Grayscale Dog Image', grayDog) #open the grayscale dog image in a window
    cv2.waitKey(0) #wait for a key press to close the window
    cv2.destroyAllWindows() #close the window

    h,w,c = grayDog.shape
    print("Grayscale Dog Image dimensions: {}x{} pixels, Channels: {}".format(w,h,c)) #ValueError: not enough values to unpack (expected 3, got 2) 
    #The error occurs because the grayscale image has only one channel, so the shape of the grayscale image will return only two values (height and width) instead of three (height, width, channels).

else:
    print("Error: Could not load dog image.")