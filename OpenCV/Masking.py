import cv2
import numpy as np
image = cv2.imread("./images/bill.jpg")
blackImage = np.zeros((image.shape[:2]), dtype="uint8")
circle = cv2.circle(blackImage, (200, 180), 150, 255, -1)
cv2.imshow("circle", circle)
cv2.imshow("bill face", image)

maskedImage = cv2.bitwise_and(image, image, mask=circle)
cv2.imshow("Mask Applied to Image", maskedImage)
cv2.waitKey(0)
cv2.destroyAllWindows()