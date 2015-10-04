from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer

# New network with 2 inputs, 3 hidden layers and 1 output
ann = buildNetwork(2, 3, 1)

# Data set with two dimensional inputs and one output
data_set = SupervisedDataSet(2, 1)

# Add 4 samples to network (XOR)
data_set.addSample((0, 0), (0,))
data_set.addSample((0, 1), (1,))
data_set.addSample((1, 0), (1,))
data_set.addSample((1, 1), (0,))

# Print out all inputs and outputs
for inpt, output in data_set:
    print(inpt, output)

# Print individual sets of the data
print('Inputs: {}'.format(data_set['input']))
print('Outputs: {}'.format(data_set['target']))

# Let's clear the data and see what it looks like...
print('Clearing data set...')
data_set.clear()

print('Inputs (cleared): {}'.format(data_set['input']))
print('Outputs: {}'.format(data_set['target']))

# Another ANN, this time to illustrate training
ann2 = buildNetwork(2, 3, 1, bias=True, hiddenclass=TanhLayer)
trainer = BackpropTrainer(ann2, data_set)

# Trains one full epoch
trainer.train()

# Trains until convergence
trainer.trainUntilConvergence()
