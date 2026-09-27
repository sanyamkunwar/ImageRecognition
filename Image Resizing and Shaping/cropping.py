import cv2

image = cv2.imread('./images/resized_image.jpg')

if image is not None:
    cropped_image = image[50:200, 100:300] #crop the image to a specific region
    cv2.imshow('Original Image', image) #open the original image in a window
    cv2.imshow('Cropped Image', cropped_image) #open the cropped image in a window
    cv2.waitKey(0) #wait for a key press to close the window
    cv2.destroyAllWindows() #close the window
else:
    print("Error: Could not load image.")