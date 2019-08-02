import numpy as np
from data_prep import features, targets, features_test, targets_test


def sigmoid(x):
    """
    Calculate sigmoid
    """
    return 1 / (1 + np.exp(-x))

# TODO: We haven't provided the sigmoid_prime function like we did in
#       the previous lesson to encourage you to come up with a more
#       efficient solution. If you need a hint, check out the comments
#       in solution.py from the previous lecture.

sigmoid_prime = sigmoid(features) * (1 - sigmoid(features))

# Use to same seed to make debugging easier
np.random.seed(42)

n_records, n_features = features.shape
last_loss = None

# Neural Network hyperparameters
epochs = 1000
learnrate = 0.5
n_hidden = 2

# Initialize weights
weights_input_hidden = np.random.normal(scale=1 / n_features**.5, size=( n_features, n_hidden) )
weights_hidden_output = np.random.normal(scale=1 / n_features**.5, size= n_hidden )


for e in range(epochs):
    del_w_input_hidden = np.zeros(weights_input_hidden.shape)
    del_w_hidden_output = np.zeros(weights_hidden_output.shape)

    for x, y in zip(features.values, targets):
      
        ## Forward Pass
        # TODO: Calculate the output
        hidden_input = np.dot(x , weights_input_hidden )
        hidden_output = sigmoid( hidden_input )
        output = sigmoid(np.dot(hidden_output, weights_hidden_output))

        ## Backward pass ##
        # TODO: Calculate the network's prediction error
        error = y - output

        # TODO: Calculate the error term
        error_term = error * output * (1-output)

        ## propagate errors to hidden layer
        # TODO: Calculate the error term for the hidden layer
        hidden_error_term = np.dot(weights_hidden_output , error_term ) * \
                            hidden_output * ( 1 - hidden_output )

         # TODO: Update the change in weights
        del_w_hidden_output += error_term*hidden_output
        del_w_input_hidden +=  hidden_error_term*x[:,None]
    # TODO: Update weights using the learning rate and the average change in weights
    weights_input_hidden += learnrate * del_w_input_hidden / n_records
    weights_hidden_output += learnrate * del_w_hidden_output / n_records
    # Printing out the mean square error on the training set
    if e % (epochs / 10) == 0:
        hidden_output = sigmoid(np.dot(x, weights_input_hidden))
        out = sigmoid(np.dot(hidden_output,
                             weights_hidden_output))
        loss = np.mean((out - targets) ** 2)

        if last_loss and last_loss < loss:
            print("Train loss: ", loss, "  WARNING - Loss Increasing")
        else:
            print("Train loss: ", loss)
        last_loss = loss

# Calculate accuracy on test data
hidden = sigmoid(np.dot(features_test, weights_input_hidden))
out = sigmoid(np.dot(hidden, weights_hidden_output))
predictions = out > 0.5
accuracy = np.mean(predictions == targets_test)
print("Prediction accuracy: {:.3f}".format(accuracy))


"""
Train loss:  0.22938960279764808
Train loss:  0.22202199088539817
Train loss:  0.22030177987898966
Train loss:  0.2197781809601994
Train loss:  0.21963941580650892
Train loss:  0.21965655830275446   WARNING - Loss Increasing
Train loss:  0.21978971086762186   WARNING - Loss Increasing
Train loss:  0.22006161406657188   WARNING - Loss Increasing
Train loss:  0.22050957432577717   WARNING - Loss Increasing
Train loss:  0.22116278036079903   WARNING - Loss Increasing
Prediction accuracy: 0.725
"""
