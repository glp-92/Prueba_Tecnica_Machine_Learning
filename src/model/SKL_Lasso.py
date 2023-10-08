import numpy as np
from sklearn.linear_model import Lasso


class SKL_Lasso():

    def __init__(self, log):
        self.log = log
        self.lasso = Lasso(alpha=0.01) # valor para evitar overfitting

    def fit(self, x_train, y_train, export_path = None):
        self.lasso.fit(x_train, y_train)
        if export_path:
            try:
                pass
            except Exception as e:
                self.log.error(f"LASSO_EXPORT:: Error exportando fichero de Lasso: {type(e).__name__}:{e}")
        return
    
    def predict(self, x_data):
        if len(x_data.shape) < 2:
            x_data = np.expand_dims(x_data, axis = 0)
        return self.lasso.predict(x_data)