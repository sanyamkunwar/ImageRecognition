import cv2

image = cv2.imread('./images/python-ball.jpg')

if image is None:
    print('Could not load image')
else:
    flipped_horizontal = cv2.flip(image,1)
    flipped_vertical = cv2.flip(image, 0)
    flipped_both = cv2.flip(image, -1)

    cv2.imshow('ORG', image)
    cv2.imshow('HORIZONTAL',flipped_horizontal)
    cv2.imshow('VER',flipped_vertical)
    cv2.imshow('both', flipped_both)

    cv2.waitKey(0)
    cv2.destroyAllWindows()