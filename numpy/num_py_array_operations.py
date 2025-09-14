import numpy as np

# arr = np.array([1,2,3,4,5,6])
# reshaped = arr.reshape((2,3))
# print(reshaped)

# expanded = arr[:,np.newaxis]
# print(expanded)

# a = np.array([1,2,3])
# b = np.array([4,5,6])

# print(a+b)
# print(a*b)
# print(a/b)

# print(np.sqrt(a))
# print(np.sum(a))
# print(np.mean(a))
# print(np.median(a))
# print(np.max(a))

#INDEXING

arr = np.array([10,20,30,40,50,60])
print(arr[2])
print(arr[-1])


#SLICING
print(arr[1:3])
print(arr[3:])
print(arr[:-1])

#RESHAPING

reshaped = arr.reshape(3,2)
print(reshaped)