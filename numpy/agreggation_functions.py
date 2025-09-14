import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

print('Sum: ', np.sum(arr))
print('Mean: ', np.mean(arr))
print('Max: ', np.max(arr))
print('Standart deviation: ', np.std(arr))
print('Sum along rows: ', np.sum(arr, axis=1))
print('Sum along cols: ', np.sum(arr, axis=0))
