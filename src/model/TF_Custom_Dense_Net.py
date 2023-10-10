import tensorflow as tf
from tensorflow import keras
from keras.models import load_model
import numpy as np


class TF_Custom_Dense_Net():

    def __init__(self, log, x_ncols, y_ncols, model_path = None, from_saved = False):
        self.log = log
        self.model_path = model_path
        if from_saved and model_path is not None:
            self.model = load_model(self.model_path)
            return
        self.build(x_ncols=x_ncols, y_ncols=y_ncols)
        return 
    
    def build(self, x_ncols, y_ncols):
        self.model = tf.keras.models.Sequential([
            tf.keras.layers.Dense(x_ncols, activation='relu', input_shape=(x_ncols,)),
            tf.keras.layers.Dense(x_ncols, activation='relu'),
            tf.keras.layers.Dense(y_ncols)
        ])
        self.model.compile(optimizer='adam', loss='mse')
        return
    
    def fit(self, x_train, y_train, batch_size, epochs):
        early_stop = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=10)
        self.model.fit(x_train, y_train, batch_size = batch_size, epochs = epochs, validation_split = 0.2, callbacks = [early_stop])
        if self.model_path is not None:
            self.model.save(self.model_path)
        return
    
    def predict(self, x_data):
        if len(x_data.shape) < 2:
            x_data = np.expand_dims(x_data, axis = 0)
        return self.model.predict(x_data)
    