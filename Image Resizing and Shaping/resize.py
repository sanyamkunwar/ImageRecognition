import cv2

image = cv2.imread('./images/python-ball.jpg')

if image is None:
    print("Error: Could not load image.")
else:
    print("Image loaded successfully.")
    resized = cv2.resize(image, (300, 300)) #resize the image to 300x300 pixels in tuple format
    cv2.imshow('Original Image', image) #open the original image in a window
    cv2.imshow('Resized Image', resized) #open the resized image in a window

    cv2.imwrite('./images/resized_image.jpg', resized) #save the resized image to a file

    cv2.waitKey(0) #wait for a key press to close the window
    cv2.destroyAllWindows() #close the window