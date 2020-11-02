import numpy as np


class Perceptron_one(object):
    def __init__(self, no_of_inputs, threshold=100, learning_rate=0.01):
        self.threshold = threshold
        self.learning_rate = learning_rate
        self.weights = np.zeros(no_of_inputs + 1)

    def predict(self, inputs):
        summation = np.dot(inputs, self.weights[1:]) + self.weights[0]
        activation = 0
        if summation > 0:
            activation = 1
        return activation

    def train(self, training_inputs, labels):
        for _ in range(self.threshold):
            for inputs, label in zip(training_inputs, labels):
                prediction = self.predict(inputs)
                self.weights[1:] += self.learning_rate * (label - prediction) * inputs
                self.weights[0] += self.learning_rate * (label - prediction)


y = np.array([1, -1, -1, -1])
X = np.array([
    [1, -1],
    [1, 1],
    [-1, 1],
    [-1, -1]
])


class Perceptron_two(object):

    def __init__(self, learning_rate=0.01, n_iterations=50):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.w_ = None
        self.errors_ = []

    def train(self, X, y):
        self.w_ = np.zeros(1 + X.shape[1])

        for _ in range(self.n_iterations):
            errors = 0
            for x_index, target in zip(X, y):
                update = self.learning_rate * (target - self.predict(x_index))
                self.w_[1:] += update * x_index
                self.w_[0] += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self

    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def predict(self, X):
        return np.where(self.net_input(X) >= 0.0, 1, -1)


print(y)
print(X)

ppn = Perceptron_two()
# ppn = Perceptron_one(2)
ppn.train(X, y)
print(ppn.predict(np.array([1, -1])))
print(ppn.predict(np.array([1, 1])))
print(ppn.predict(np.array([-1, 1])))
print(ppn.predict(np.array([-1, -1])))
print(ppn.w_[1:])
