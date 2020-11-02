import numpy as np
import scipy

class nerual_newtork(object):
    def __init__(self, input_layers, hidden_layers, output_layers, learning_rate = 0.1, n_iterations =100 ):
        self.input_nodes = input_layers
        self.hidden_nodes = hidden_layers
        self.output_nodes = output_layers
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.weights_with_input_hidden  = (np.random.rand(self.hidden_nodes, self.input_nodes) - 0.5 )
        self.weights_with_output_hidden = (np.random.rand(self.output_nodes, self.hidden_nodes) - 0.5)

        self.activiation_function = lambda x : scipy.special.expit(x)

    def train(self, inputs_list, targets_list):
        inputs =  np.array(inputs_list, ndmin=2).T
        targets = np.array(targets_list, ndmin=2).T

        hidden_inputs = np.dot(self.weights_with_input_hidden, inputs)
        hidden_outputs = self.activiation_function(hidden_inputs)

        final_inputs = np.dot(self.weights_with_output_hidden, hidden_outputs)
        final_outputs = self.activiation_function(final_inputs)


    def query(self, input_list):
        inputs = np.array(input_list, ndmin=2).T

        hidden_outputs = np.dot(self.weights_with_input_hidden, inputs)

        final_outputs = np.dot(self.weights_with_output_hidden, hidden_outputs)
        return final_outputs

input_layers = 3
hidden_layers = 3
output_layers = 3

nn = nerual_newtork(input_layers, hidden_layers, output_layers)