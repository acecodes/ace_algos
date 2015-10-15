from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet, ClassificationDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure import FeedForwardNetwork, LinearLayer, SigmoidLayer, TanhLayer, FullConnection
from pybrain.utilities import percentError
from pybrain.structure.modules import SoftMaxLayer
from scipy import diag, arange, meshgrid, where
from numpy.random import multivariate_normal

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
# print('Clearing data set...')
# data_set.clear()

# print('Inputs (cleared): {}'.format(data_set['input']))
# print('Outputs: {}'.format(data_set['target']))

# Another ANN, this time to illustrate training
ann2 = buildNetwork(2, 3, 1, bias=True, hiddenclass=TanhLayer)
trainer = BackpropTrainer(ann2, data_set)

# Trains one full epoch
trainer.train()

# Trains until convergence
trainer.trainUntilConvergence()

# Create a feedforward (one direction) network
ff_net = FeedForwardNetwork()
input_layer = LinearLayer(2, name='Input Layer')
hidden_layer = SigmoidLayer(3, name='Hidden layer')
output_layer = LinearLayer(1, name='Output layer')

ff_net.addInputModule(input_layer)
ff_net.addModule(hidden_layer)
ff_net.addOutputModule(output_layer)

# Create explicit connections between layers
input_to_hidden = FullConnection(input_layer, hidden_layer)
hidden_to_output = FullConnection(hidden_layer, output_layer)

ff_net.addConnection(input_to_hidden)
ff_net.addConnection(hidden_to_output)

# Sort for proper network operation
ff_net.sortModules()

print(ff_net.activate([1, 2]))
print(ff_net.activate([3, 5]))

# Start over

ff_net.reset()
print('Network reset.')
print(ff_net.activate([5, 8]))
print(ff_net.activate([12, 2]))

print(ff_net)

"""
Feedfordward Neural Network Classification
"""

means = [(-1, 0), (2, 4), (3, 1)]

cov = [diag([1, 1]), diag([0.5, 1.2]), diag([1.5, 0.7])]
all_data = ClassificationDataSet(2, 1, nb_classes=3)
for n in range(400):
    for klass in range(3):
        input_1 = multivariate_normal(means[klass], cov[klass])
        all_data.addSample(input_1, [klass])

tstdata, trndata = all_data.splitWithProportion(0.25)

trndata._convertToOneOfMany()
tstdata._convertToOneOfMany()

print("Number of training patterns: ", len(trndata))
print("Input and output dimensions: ", trndata.indim, trndata.outdim)
print("First sample (input, target, class):")
print(trndata['input'][0], trndata['target'][0], trndata['class'][0])
