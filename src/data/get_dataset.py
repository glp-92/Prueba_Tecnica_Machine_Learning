import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing


def get_dataset(log, verbose = False):
    """
    Obtiene el dataset 'California Housing' de sklearn

    Args:
        log: Log para almacenar registros
        verbose: registrar detalles del dataframe importado

    Returns:
        df_housin: dataset full.
    """
    housing = fetch_california_housing(as_frame=True)
    if verbose: 
        log.info(housing.DESCR)
    df_housing = housing.frame
    if verbose: 
        log.info(df_housing.info())
        log.info(df_housing.describe())
    return df_housing

'''
# Entrenar el modelo
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

model = LinearRegression()
model.fit(X_train, y_train)

# Predecir los precios de las viviendas en el conjunto de validación
y_pred = model.predict(X_test)

# Evaluar el rendimiento del modelo
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"RMSE: {rmse:.2f}")

# Evaluar el rendimiento del modelo
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"RMSE: {rmse:.2f}")

# Imprimir un informe de rendimiento del modelo
print(f"Rendimiento del modelo:")
print(f"RMSE: {rmse:.2f}")
print(f"R2: {model.score(X_test, y_test):.2f}")
'''