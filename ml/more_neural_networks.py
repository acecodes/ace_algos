import numpy as np


def nonlin(x, deriv=False):
    """Sigmoid function"""
    if deriv:
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))

if __name__ == '__main__':

    # Input dataset
    X = np.array([
        [0, 0, 1],
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
        ])

    # Output dataset
    y = np.array([[0], [1], [1], [0]])

    # Seed random numbers to make calculation
    # deterministic - generally a good practice
    # because it means you'll get the same random
    # distributions each time
    np.random.seed(1)

    # Randomly initialize weights with mean 0
    # syn0 = synapse zero
    syn0 = 2 * np.random.random((3, 4)) - 1
    syn1 = 2 * np.random.random((4, 1)) - 1

    for j in range(60000):

        # Forward propagation
        l0 = X  # First layer
        l1 = nonlin(np.dot(l0, syn0))  # Second/hidden layer
        l2 = nonlin(np.dot(l1, syn1))  # Third/hidden layer

        l2_error = y - l2

        if j % 10000 == 0:
            print('Error: ' + str(np.mean(np.abs(l2_error))))

        # In what direction is the target value?
        # Were we really sure? If so, don't change too much.
        l2_delta = l2_error * nonlin(l2, deriv=True)

        # How much did each l1 value contribute to the l2 error
        # (according to weights)?
        l1_error = l2_delta.dot(syn1.T)

        # Multiply how much we missed by the slope of the sigmoid
        # at the values of 11
        l1_delta = l1_error * nonlin(l1, deriv=True)

        # Update weights
        syn1 += l1.T.dot(l2_delta)
        syn0 += l0.T.dot(l1_delta)

    print('Output after training:')
    print(l1)
