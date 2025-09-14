import numpy as np

maxtrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
vector = np.array([1, 0, -1])

result_add = maxtrix + vector
print(result_add)


result_mult = maxtrix * 2
print(result_mult)


# generate random dataset
dataset = np.random.randint(1, 51, size=(5, 5))
print(dataset)

# filter values greater than 25 and replace by 0
dataset[dataset > 25] = 0
print('Modified dataset: \n', dataset)

# calculate stats
print('Mean: ', np.mean(dataset))
print('STD: ', np.std(dataset))
