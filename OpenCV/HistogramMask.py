import matplotlib
matplotlib.use("MacOSX")
from matplotlib import pyplot as plt
import cv2
import numpy as np
image = cv2.imread("./images/bill.jpg")
cv2.imshow("Image", image)
# mask is black image with same size of image
mask = np.zeros(image.shape[:2], dtype="uint8")

# rectangle white mask on black sqaure
cv2.rectangle(mask,(280, 310),(340, 360), 255, -1)
cv2.imshow("Mask", mask)


colors = ("b", "g", "r")
plt.figure()
plt.title("Without mask Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")

for i, col in enumerate(colors):
    hist = cv2.calcHist([image],[i], None, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])

plt.show()

plt.title("'With Mask Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")

for i, col in enumerate(colors):
    hist = cv2.calcHist([image], [i], mask, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])

plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()