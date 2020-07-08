import matplotlib
matplotlib.use("MacOSX")
from matplotlib import pyplot as plt
import cv2

image = cv2.imread('./images/bill.jpg')
cv2.imshow("Original", image)
colors = ("b", "g", "r")
plt.figure()
plt.title("'Flattened' Color plot Histogram1")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
for i, col in enumerate(colors):
    hist = cv2.calcHist([image], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])
plt.show()