import numpy as np

# 1 Dimensional Array
x = np.array([1, 2, 3])

for i in x:
    print(i)

# accessing by index
print(x[0])


# 2 Dimensional Array
# 2 rows and 3 columns

y = np.array([[2, 5, 3], [7, 9, 0]])


for i in y:
    print(i)
print('\n 1st row \n')
print(y[0])
print('\nelement at [0][0] \n')
print(y[0][0])


# 3 dimensional array
z = [[[4, 23, 5, 6], [14, 3, 55, 16]], [[14, 13, 57, 68], [24, 23, 85, 96]]]

print("\n", z[0])

# create an array with 4 dimensions.

a = np.array([1, 3, 5], ndmin=4)
print(a)
print(a[0][0][0][2])

# create an array with float type
b = np.array([1.8, 2.9], dtype="float64")
print(b.dtype)
print(b)

