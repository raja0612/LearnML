import cv2
image = cv2.imread("./images/cards.png")
cv2.imshow("Original Image", image)

# convert to gray scale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# blur the image
blurred = cv2.GaussianBlur(gray, (3, 3), 0)

# thresholding
(thresholdValue, thresh) = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
cv2.imshow("Threshold", thresh)

# find contours and draw them

contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

contours = contours[0] if len(contours) == 2 else contours[1]
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
cv2.imshow("All External Contours", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

