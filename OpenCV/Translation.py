import cv2
import numpy as np

image = cv2.imread("./images/bill.jpg")
rows, cols, c = image.shape

for i in range(10):
    M = np.float32([[1, 0, -10*i], [0, 1, 10*i]])
    print(M)
    image = cv2.warpAffine(image, M, (rows, cols))

    cv2.imshow("image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


