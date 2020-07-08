import cv2
import numpy as np


# first create an array 500 * 500 with channel 3 means color image
# and multiply each cell (1, 1, 1) * 255 = white color
image = np.ones((500, 500, 3), dtype="uint8") * 255


# line
cv2.line(image, (0, 0), (500, 500), (0, 0, 255), 5)

# rectangle
cv2.rectangle(image, (200, 200), (300, 300), (255, 0, 0), -1)

# circle
cv2.circle(image, (200, 400), 50, (255, 255, 0), 5)

# text
cv2.putText(image, "Rectangle", (250, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()