import cv2
import numpy as np
image = cv2.imread("./images/sudoku.png", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Original", image)

# erosion
for i in (1, 2, 5):
    eroded = cv2.erode(image.copy(), None, iterations=i)
    cv2.imshow("Erosion {}".format(i), eroded)
    cv2.waitKey(0)


# dilation
for i in (1, 2, 5):
    dilate = cv2.dilate(image.copy(), None, iterations=i)
    cv2.imshow("Dilate {}".format(i), dilate)
    cv2.waitKey(0)


# opening
image2 = cv2.imread("./images/MLCRUNCH.png", cv2.IMREAD_GRAYSCALE)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
# or kernel = np.ones((5,5), dtype="uint8")
opened = cv2.morphologyEx(image2.copy(), cv2.MORPH_OPEN, kernel)
cv2.imshow("opened", opened)
cv2.waitKey(0)

# closing
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
# or kernel = np.ones((3,3), dtype="uint8")
closed = cv2.morphologyEx(image2.copy(), cv2.MORPH_CLOSE, kernel)
cv2.imshow("closed", closed)
cv2.waitKey(0)

# Gradient
kernel = np.ones((3,3), dtype="uint8")
# or kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
gradient = cv2.morphologyEx(image2.copy(), cv2.MORPH_GRADIENT, kernel)
cv2.imshow("Gradient", gradient)
cv2.waitKey(0)





cv2.destroyAllWindows()
