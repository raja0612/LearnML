import cv2
import numpy as np

imageAddition = cv2.add(np.uint8([200, 150]), np.uint8([200, 200]))
# [200 + 200 , 150 + 200] = [255, 255] // max value is 255 on color code so it prints 255 255
print(imageAddition)

image = cv2.imread("./images/bill.jpg")

# create an array with ones with shape(rows,columns, channel) of an image
M = np.ones(image.shape, dtype='uint8') * 100

resultImage = cv2.add(image, M)
cv2.imshow("Original Image", image)
cv2.imshow("Brighter Image", resultImage)

resultImage2 = cv2.subtract(image, M)
cv2.imshow("Contrast Image", resultImage2)
cv2.waitKey(0)
cv2.destroyAllWindows()