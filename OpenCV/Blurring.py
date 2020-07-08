import cv2
import numpy as np
image = cv2.imread("./images/bill.jpg")

# 1. Average Blur
# filter2D() function
blurKernal = np.ones((3, 3), np.float32) / (3*3)
blurred = cv2.filter2D(image, -1, blurKernal)
cv2.imshow("AverageBlur filter2D()" .format(3, 3), blurred)

# blur() function
blurred1 = cv2.blur(image, (3, 3))
cv2.imshow("AverageBlur blur()" .format(3, 3), blurred)


# 2. Gaussian Blur
gaussianBlur = cv2.GaussianBlur(image, (3, 3), 0)
cv2.imshow("GaussianBlur()", gaussianBlur)


# 3. Median Blur
medianBlur = cv2.medianBlur(image, 3)
cv2.imshow("medianBlur", medianBlur)


# 4 . Bilateral Blur

bilateralBlur = cv2.bilateralFilter(image, 11, 61, 39)
cv2.imshow("bilateralBlur", bilateralBlur)

cv2.waitKey(0)
cv2.destroyAllWindows()

