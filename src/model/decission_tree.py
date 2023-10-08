from sklearn import tree
import matplotlib.pyplot as plt
import numpy as np


class DecissionTree():

    def __init__(self, log, max_depth = 2):
        self.log = log
        self.max_depth = max_depth
        self.tree = tree.DecisionTreeRegressor(max_depth=max_depth)

    def fit(self, x_train, y_train, export_tree_path = None):
        self.tree.fit(x_train, y_train)
        if export_tree_path:
            try:
                plt.figure(figsize=(6*self.max_depth,6*self.max_depth))
                tree.plot_tree(self.tree, feature_names=x_train.columns)
                plt.savefig(export_tree_path)
            except Exception as e:
                self.log.error(f"TREE_EXPORT:: Error exportando fichero de arbol de decision: {type(e).__name__}:{e}")
        return
    
    def predict(self, x_data):
        if len(x_data.shape) < 2:
            x_data = np.expand_dims(x_data, axis = 0)
        return self.tree.predict(x_data)