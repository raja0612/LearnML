import cv2
image = cv2.imread('./images/bill.jpg')

print("(height, width, channel)", image.shape)
print("height: {0} pixels".format(image.shape[0]))
print("width: {0} pixels".format(image.shape[1]))
print("first pixel value {0}".format(image[0][0]))

print("Gray Scale Image")

img2 = cv2.imread("./images/bill.jpg", cv2.IMREAD_GRAYSCALE)
print("GSI first pixel value {0}".format(img2[0][0]))

cv2.imshow('Bill Gates', image)
cv2.imshow("Black & White Bill", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
