import numpy as np
# x is an array contains 4 rows and 4 columns
x = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print(x)
print('selecting 2 and 3 rows')

print(x[1:2])  # start index : end index(not included). index starts from 0


print('selecting 2 and 3 rows and column index 1 and 2 elements')

print(x[1:3, 1:3])
