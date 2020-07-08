import cv2
import numpy as np
image = cv2.imread("./images/sudoku.png", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Original", image)


# Sobel X filter
sobelXKernel = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]], dtype="int8")

sobelXImage = cv2.filter2D(image, cv2.CV_64F, sobelXKernel)
cv2.imshow("Sobel X Image", sobelXImage)

gX = cv2.Sobel(image, ddepth=cv2.CV_64F, dx=1, dy=0)
cv2.imshow("Sobel X2 Image", gX)


# Sobel Y filter

sobelYKernel = np.array([
    [-1, -2, -1],
    [0, 0, 0],
    [1, 2, 1]], dtype="int8")

sobelYImage = cv2.filter2D(image, cv2.CV_64F, sobelYKernel)

# or
gY = cv2.Sobel(image, ddepth=cv2.CV_64F, dx=0, dy=1)

cv2.imshow("Sobel Y Image", sobelYImage)


laplacianKernel = np.array([
    [0, 1, 0],
    [1, -4, 1],
    [0, 1, 0]], dtype="int8")

laplacianImage = cv2.filter2D(image, cv2.CV_64F, laplacianKernel)

#or
LaplacianImage = cv2.Laplacian(image, ddepth=cv2.CV_64F)
cv2.imshow("Laplacian Image", laplacianImage)





cv2.waitKey(0)
cv2.destroyAllWindows()