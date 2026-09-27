import cv2

image = cv2.imread('./images/python-ball.jpg')
imageOfDog = cv2.imread('./images/dog.jpeg')

if image is not None:
    height, width, channels = image.shape
    print(f"Image dimensions: {width}x{height} pixels, Channels: {channels}")
else:
    print("Error: Could not load image.")

if imageOfDog is not None:
    height, width, channels = imageOfDog.shape
    print(f"Dog Image dimensions: {width}x{height} pixels, Channels: {channels}")
else:
    print("Error: Could not load dog image.")