from keras.models import Sequential
from keras.layers.core import Dense, Activation ,Dropout

from keras.layers import Conv2D,Input,ZeroPadding2D,BatchNormalization ,MaxPooling2D ,Flatten
from sklearn.metrics import f1_score

def build_model( input_shape ):
    
    model = Sequential()
    
#     X_input = Input(input_shape)
    
    model.add(ZeroPadding2D(2, input_shape = input_shape))
    model.add(Conv2D(32 ,(7,7) ))
    model.add(BatchNormalization(axis = 3))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size = (4,4)) )
    model.add(Dropout(0.25))
    model.add(MaxPooling2D(pool_size = (4,4)) )
           
    model.add(Conv2D(32 ,(7,7) ))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size = (2,2)) )
    model.add(Dropout(0.25))
    model.add(MaxPooling2D(pool_size = (2,2)) ) 
    
    model.add(Flatten())
    model.add(Dense(256))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))

    model.add(Dense(1))
    model.add(Activation('sigmoid'))
    
    # Let's train the model using RMSprop
    model.compile(loss='binary_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy']) 
    
    return model
