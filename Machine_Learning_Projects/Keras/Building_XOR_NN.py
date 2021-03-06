from keras.layers.core import Dense, Activation
from keras.models import Sequential
import numpy as np
from keras.utils import np_utils
import tensorflow as tf
# Using TensorFlow 1.0.0; use tf.python_io in later versions
tf.python_io.control_flow_ops = tf

# Set random seed
np.random.seed(42)

# Our data
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]]).astype('float32')
y = np.array([[0], [1], [1], [0]]).astype('float32')

# Initial Setup for Keras
# One-hot encoding the output
y = np_utils.to_categorical(y)

# Building the model
xor = Sequential()

# Add required layers
xor.add(Dense(8, input_dim=X.shape[1] ))
xor.add(Activation('tanh'))
xor.add(Dense(2))
xor.add(Activation('sigmoid'))

# Specify loss as "binary_crossentropy", optimizer as "adam",
# and add the accuracy metric
xor.compile(optimizer = 'adam', loss='binary_crossentropy'  ,metrics=['accuracy'])

# Uncomment this line to print the model architecture
xor.summary()

# Fitting the model
history = xor.fit(X, y, epochs=800, verbose=0)

# # Scoring the model
score = xor.evaluate(X, y)
print("\nAccuracy: ", score[-1])

# # Checking the predictions
print("\nPredictions:")
print(xor.predict_proba(X))

"""
Accuracy:  1.0

Predictions:
[[0.8599172  0.16491759]
 [0.30646425 0.5681351 ]
 [0.18805876 0.75621223]
 [0.7179891  0.40460438]]
"""
