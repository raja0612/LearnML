import cv2
image = cv2.imread("./images/bill.jpg")
(B, G, R) = cv2.split(image)


merged = cv2.merge([B, G, R])
cv2.imshow("merged", merged)

print(B.shape)
print(G.shape)
print(R.shape)

print(merged.shape)
print('first pixel of B {0}'.format(B[0][0]))
print('first pixel of G {0}'.format(G[0][0]))
print('first pixel of R {0}'.format(R[0][0]))

print('first pixel of merged {0}'.format(merged[0][0]))


# HSV Hue Saturated value
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)
(H, S, V) = cv2.split(image)
cv2.imshow("Hue", H)
cv2.imshow("Saturation", S)
cv2.imshow("Value", V)
merged = cv2.merge([H, S, V])


# LAB Lightness Red/Green Value, Blue/Yellow value

# convert image to LAB
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
cv2.imshow("LAB", lab)

(L, A, B) = cv2.split(image)
cv2.imshow("L", L)
cv2.imshow("A", A)
cv2.imshow("B", B)
merged = cv2.merge([L, A, B])
cv2.imshow("LAB Merged", merged)


# Gray Scale Images(GSI)
GSI = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("GSI", GSI)

cv2.waitKey(0)
cv2.destroyAllWindows()


