import cv2
import matplotlib
matplotlib.use("MacOSX")
from matplotlib import pyplot as plt
import numpy as np

image = cv2.imread("./images/bill.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("GSI", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# construct a gray scale histogram
# calcHist() function returns tuple(x axis contains colors (0 to 256) y axis contains intensity of color)
# (graphical representation of an image) of an image
hist = cv2.calcHist([image], [0], None, [256], [0, 256])

# plot the histogram
plt.figure()
plt.title("Gray scale Plot Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
plt.plot(hist)
plt.xlim([0, 256])

# plot the histogram

plt.figure()
plt.title("Grayscale bar Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
x = np.arange(256, dtype='uint8')
y = [int(y[0]) for y in hist]
plt.bar(x, y)
print("Max pixel count {0}".format(max(y)))
print("Max color pixel is {0}".format(y.index(max(y))))
plt.show()
