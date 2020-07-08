import cv2;

image1 = cv2.imread("./images/bill.jpg")
image2 = cv2.imread("./images/flip.jpg")

h, w = image1.shape[:2]
image2 = cv2.resize(image2, (w, h))


dst = cv2.addWeighted(image1, 0.7, image2, 0.3, 0)
cv2.imshow("image 1", image1)
cv2.imshow("image 2", image2)
cv2.imshow("Blended", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()