import cv2

image = cv2.imread('./images/python-ball.jpg')

if image is not None:
    success = cv2.imwrite('./images/saved_image.jpg', image) #save the image to a file
    if success:
        print("Image saved successfully as './images/saved_image.jpg'.")
    else:
        print("Error: Could not save image.")
else:
    print("Error: Could not load image.")