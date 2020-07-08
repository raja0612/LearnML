import cv2
import numpy as np
image = cv2.imread("./images/bill.jpg")
# kernel matrix to find edges
edgeDetection = np.array((
    [-1, -1, -1],
    [-1,  8, -1],
    [-1, -1, -1],

), dtype="int")

edges = cv2.filter2D(image, -1, edgeDetection)
cv2.imshow("Edge Detection", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
