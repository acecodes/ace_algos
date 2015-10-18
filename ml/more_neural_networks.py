import numpy as np


def nonlin(x, deriv=False):
    """Sigmoid function"""
    if deriv:
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))

# Input dataset
X = np.array([
    [0, 0, 1],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
    ])

# Output dataset
y = np.array([[0, 0, 1, 1]]).T

# Seed random numbers to make calculation
# deterministic - generally a good practice
# because it means you'll get the same random
# distributions each time
np.random.seed(1)

# Randomly initialize weights with mean 0
# syn0 = synapse zero
syn0 = 2 * np.random.random((3, 1)) - 1

for iter in range(10000):

    # Forward propagation
    l0 = X  # First layer
    l1 = nonlin(np.dot(l0, syn0))  # Second/hidden layer

    # How much did we miss?
    l1_error = y - l1

    # Multiply how much we missed by the slope of the sigmoid
    # at the values of 11
    l1_delta = l1_error * nonlin(l1, deriv=True)

    # Update weights
    syn0 += np.dot(l0.T, l1_delta)

print('Output after training:')
print(l1)
