import numpy as np

# random seeds
# sticks all random values to a specific set until seed number is changed
np.random.seed(1)

# random numbers from 0 to 1 uniformly distributed
random_array = np.random.rand(3, 3)
print(random_array)


random_integers = np.random.randint(0, 10, size=(2, 3))
print(random_integers)
