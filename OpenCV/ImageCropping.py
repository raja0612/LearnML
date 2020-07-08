import cv2
import numpy as np
image = cv2.imread("./images/bill.jpg")


# cropping
startX = 30  # height of an cropping image
startY = 90   # width of an cropping image
width = 260
height = 210

face = np.copy(image[startY:(startY+height), startX:(startX+width)])
# face = np.copy(image[90:300, 30:290])

cv2.imshow("bill original image", image)
cv2.imshow("bill cropping image", face)

print('cropping image height width and channel', face.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()
