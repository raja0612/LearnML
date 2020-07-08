import cv2
image = cv2.imread("./images/shapes.png")
cv2.imshow("Original Image", image)

# convert to gray scale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# blur the image
blurred = cv2.GaussianBlur(gray, (3, 3), 0)

# thresholding
(thresholdValue, thresh) = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
cv2.imshow("Threshold", thresh)

# find contours
contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2
                            .CHAIN_APPROX_NONE)
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
for c in contours:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.04 * peri, True)
    shape = ""
    if len(approx) == 3:
       shape = "triangle"
    elif len(approx) == 4:
         (x, y, w, h) = cv2.boundingRect(approx)
         diff = abs(w - h)
    if diff < 10:
        shape = "square"
    else:
        shape = "rectangle"
    else:
        shape = "circle"





cv2.waitKey(0)
cv2.destroyAllWindows()