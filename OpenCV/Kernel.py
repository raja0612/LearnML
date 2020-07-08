import cv2
import numpy as np


# convolve function
def convolve(image, kernel):
    # parameter value -1  is ddepth the desired depth of destination image
    # -1 means output image has same depth as source image
    return cv2.filter2D(image, -1, kernel)


# step 1 read the input image
image = cv2.imread("./images/bill.jpg")


# step 2 : kernel(small odd matrix to process the image) to blur the image
blurKernal = np.ones((3, 3), np.float32)/9

# step 3 apply filter2D
blurredImage = convolve(image, blurKernal)
cv2.imshow("original", image)
cv2.imshow("Blur Image", blurredImage)

# kernel to detect edge
kernel = np.array((
    [-1, -1, -1],
    [-1, 8, -1],
    [-1, -1, -1],
), dtype="int")

resultImage = cv2.filter2D(image, -1, kernel)

cv2.imshow("Edge detection Image", resultImage)

cv2.waitKey(0)
cv2.destroyAllWindows()