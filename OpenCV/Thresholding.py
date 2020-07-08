import cv2
# Thresholding is converting gray scale images to binary images
image = cv2.imread("./images/receipt.png", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Original", image)


# 1.Simple thresholding
(thresholdValue, imageRes) = cv2.threshold(image, 170, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold", image)

(thresholdInvValue, imageInvRes) = cv2.threshold(image, 170, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold Inv", imageInvRes)



# 2.OTSU Thresholding
otsuImage = cv2.GaussianBlur(image, (3, 3), 0)
(otsuThresholdValue, otsuImageRes) = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print('OTSU Threshold value ={0}'.format(otsuThresholdValue))
cv2.imshow("OTSU THRESHOLD IMAGE", otsuImageRes)

#Adaptive Thresholding:


thresh = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 3)
cv2.imshow("OpenCV Gaussian Thresh", thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()

