import tensorflow as tf
import numpy as np


class TF_Dense_Net():

    def __init__(self, log):
        self.log = log
        return 
    
    def build(self, x_ncols, y_ncols):
        self.model = tf.keras.models.Sequential([
            tf.keras.layers.Dense(x_ncols, activation='relu', input_shape=(x_ncols,)),
            tf.keras.layers.Dense(x_ncols, activation='relu'),
            tf.keras.layers.Dense(y_ncols)
        ])
        self.model.compile(optimizer='adam', loss='mse')
        return
    
    def fit(self, x_train, y_train, epochs):
        early_stop = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=10)
        self.model.fit(x_train, y_train, epochs = epochs, validation_split = 0.2, callbacks = [early_stop])
        return
    
    def predict(self, x_data):
        if len(x_data.shape) < 2:
            x_data = np.expand_dims(x_data, axis = 0)
        return self.model.predict(x_data)
    