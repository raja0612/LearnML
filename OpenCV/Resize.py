import cv2
image = cv2.imread("./images/bill.jpg")
height, width, channel = image.shape

print('Image height {0} width:{1}'.format(height, width))
cv2.imshow("Original Image", image)

resizedImage = cv2.resize(image, (height-200, width-200))

cv2.imshow("Re sized Image", resizedImage)
rh, rw = resizedImage.shape[:2]
print('After resizing Image height {0} width:{1}'.format(rh, rw))



# increase size by 40%

newHeight = int(height * 140/100)
newWidth = int(width * 140/100)

resizedImage3 = cv2.resize(image, (newWidth, newHeight))
cv2.imshow("Re sized Image by 40%", resizedImage3)
rh1, rw2 = resizedImage3.shape[:2]
print('After resizing Image height {0} width:{1} by 40%'.format(rh1, rw2))

cv2.waitKey(0)
cv2.destroyAllWindows()
