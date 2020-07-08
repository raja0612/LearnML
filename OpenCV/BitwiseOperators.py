import cv2
import numpy as np
rectangleImage = np.zeros((500, 500), dtype="uint8")
cv2.rectangle(rectangleImage, (50, 50), (450, 450), 255, -1)
cv2.imshow("Rectangle", rectangleImage)

circleImage = np.zeros((500, 500), dtype="uint8")
cv2.circle(circleImage, (250, 250), 250, 225, -1)
cv2.imshow("Circle", circleImage)

bitwiseAND = cv2.bitwise_and(rectangleImage, circleImage)
cv2.imshow("bitwiseAnd", bitwiseAND)

bitwiseOR = cv2.bitwise_or(rectangleImage, circleImage)
cv2.imshow("bitwiseOR", bitwiseOR)

bitwiseXOR = cv2.bitwise_xor(rectangleImage, circleImage)
cv2.imshow("bitwiseXOR", bitwiseXOR)

bitwiseNOT = cv2.bitwise_not(rectangleImage)
cv2.imshow("bitwiseNOT", bitwiseNOT)

cv2.waitKey(0)
cv2.destroyAllWindows()