from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np


class SKL_Linear_Regression():

    def __init__(self, log):
        self.log = log
        self.linear_regression = LinearRegression()

    def fit(self, x_train, y_train, export_path = None):
        self.linear_regression.fit(x_train, y_train)
        if export_path:
            try:
                pass
            except Exception as e:
                self.log.error(f"LINEAR_REG_EXPORT:: Error exportando fichero de regresión lineal: {type(e).__name__}:{e}")
        return
    
    def predict(self, x_data):
        if len(x_data.shape) < 2:
            x_data = np.expand_dims(x_data, axis = 0)
        return self.linear_regression.predict(x_data)