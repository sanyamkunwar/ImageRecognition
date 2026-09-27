import cv2

image = cv2.imread('./images/python-ball.jpg')

if image is None:
    print('could not load image')
else:
    print('Image loaded')
    (h,w) = image.shape[:2]
    # linned_image = cv2.line(image,(w//2-50,h//2),(w//2+50,h//2),(255,255,255),5)
    rectangled_image = cv2.rectangle(image,(w//2-50,h//2 - 50),(w//2+50,h//2 + 50),(255,255,255),5)
    # cv2.imshow('Linned Image', linned_image)
    cv2.imshow('Rectangled Image', rectangled_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()