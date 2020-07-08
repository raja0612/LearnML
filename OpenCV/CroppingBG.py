import cv2
import numpy as np
image = cv2.imread("./images/bill.jpg")


# cropping
face = np.copy(image[90:300, 30:290])

# convert complete bill image to green back ground
image[:, :] = [0, 255, 0]

# adding cropping bill image to above green back ground image
image[90:300, 30:290] = face

cv2.imshow("bill with back ground", image)
cv2.imshow("cropping bill", face)

cv2.waitKey(0)
cv2.destroyAllWindows()
