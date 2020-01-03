from keras.models import Sequential
from keras.layers import BatchNormalization,SeparableConv2D,MaxPooling2D,Activation,Flatten,Dropout,Dense
from keras import backend as K


class CancerModel:
    
    @staticmethod
    def build(image_shape , classes):
        
        model = Sequential()
        height, width, channels = image_shape
        chanDim = -1
        
        if K.image_data_format() == 'channels_first':
            chanDim = 1
            image_shape = (channels,height,width)
#           depthwise separable convolution:
#               Is more efficient.
#               Requires less memory.
#               Requires less computation.
#               Can perform better than standard convolution in some situations.        
            
#               Create the layers
        model.add(SeparableConv2D(filters=32,kernel_size=(3,3),padding='same',input_shape = image_shape ))
        model.add(Activation('relu'))
        model.add(BatchNormalization(axis = chanDim))
        model.add(MaxPooling2D(pool_size=(2,2)))
        model.add(Dropout(0.25))
        
        model.add(SeparableConv2D(filters=64,kernel_size=(3,3),padding='same',input_shape = image_shape ))
        model.add(Activation('relu'))
        model.add(BatchNormalization(axis = chanDim))
        model.add(SeparableConv2D(filters=64,kernel_size=(3,3),padding='same',input_shape = image_shape ))
        model.add(Activation('relu'))
        model.add(BatchNormalization(axis = chanDim))
        model.add(MaxPooling2D(pool_size=(2,2)))
        model.add(Dropout(0.25))
        
        model.add(SeparableConv2D(filters=128,kernel_size=(3,3),padding='same',input_shape = image_shape ))
        model.add(Activation('relu'))
        model.add(BatchNormalization(axis = chanDim))
        model.add(SeparableConv2D(filters=128,kernel_size=(3,3),padding='same',input_shape = image_shape ))
        model.add(Activation('relu'))
        model.add(BatchNormalization(axis = chanDim))
        model.add(SeparableConv2D(filters=128,kernel_size=(3,3),padding='same',input_shape = image_shape ))
        model.add(Activation('relu'))
        model.add(BatchNormalization(axis = chanDim))
        model.add(MaxPooling2D(pool_size=(2,2)))
        model.add(Dropout(0.25))
            
#       Fully connected layers
        
        model.add(Flatten())
        model.add(Dense(256))
        model.add(Activation('relu'))
        model.add(BatchNormalization())
        model.add(Dropout(0.5))
        
        model.add(Dense(classes))
        model.add(Activation('softmax'))
        
        
        return model
        
            

model = CancerModel.build((24,34,3),2)
model.summary()