import cv2

image = cv2.imread('./images/python-ball.jpg')

if image is None:
    print('could not load image')
else:
    print('Image loaded')
    (h,w) = image.shape[:2]
    # linned_image = cv2.line(image,(w//2-50,h//2),(w//2+50,h//2),(255,255,255),5)
    # rectangled_image = cv2.rectangle(image,(w//2-50,h//2 - 50),(w//2+50,h//2 + 50),(255,255,255),5)
    # circled_image = cv2.circle(image,(w//2,h//2),50,(0,0,255),-1)
    # circled_image = cv2.circle(image,(w//2,h//2),20,(0,255,255),-1)

    texts_img = cv2.putText(image,'TEXT',(w//2-40,h//2), cv2.FONT_HERSHEY_COMPLEX,1.2,(255,0,255),2)

    # cv2.imshow('Linned Image', linned_image)
    # cv2.imshow('Rectangled Image', rectangled_image)
    # cv2.imshow('Circled Image', circled_image)
    cv2.imshow('Text on Image', texts_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()