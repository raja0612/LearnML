import cv2


# step 1 . read an image with gray scale mode
image = cv2.imread("./images/bill.jpg", cv2.IMREAD_GRAYSCALE)

# step 2 apply gaussian blur filter with kernel size 5X5
blurred = cv2.GaussianBlur(image, (5, 5), 0)

# use Canny function with lower and upper thresh hold
edges = cv2.Canny(blurred, 70, 210)
cv2.imshow("Edge Detection", edges);
cv2.waitKey(0)
cv2.destroyAllWindows()