from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np


def calc_mse(y_val, predictions):
    """
    Args:
        y_val: val data df or arr
        predictions: pred arr
    Returns:
        mean_squared_error
    About:
        Funcion para calcular mse: el valor medio de la diferencia entre valor real y predicho al cuadrado
        Sensible a cambios entre valor real y predicho por elevar la diferencia al cuadrado
        Sensible a valores atípicos, penalizando las desviaciones
        No es comparable entre modelos con diferente unidad métrica
        Valores deseados: próximo a 0
    """
    return mean_squared_error(y_val, predictions)

def calc_mae(y_val, predictions):
    """
    Args:
        y_val: val data df or arr
        predictions: pred arr
    Returns:
        mean_absolute_error
    About:
        Promedio de diferencia absoluta entre valor real y predicho. Usado típicamente en finanzas
        Menor sensibilidad a valores atípicos que mse
        Simple y facil de interpretar
        Comparable entre modelos con diferente unidad métrica
        Valores deseados: próximo a 0
    """
    return mean_absolute_error(y_val, predictions)

def calc_rmse(y_val, predictions):
    """
    Args:
        y_val: val data df or arr
        predictions: pred arr
    Returns:
        rmse
    About:
        Raiz cuadrada del mse
        Mayor sensibilidad a valores atípicos que mae, pero la penalización de mse la reduce a la raíz cuadrada
        Valores deseados: próximo a 0
    """
    return np.sqrt(mean_squared_error(y_val, predictions))

def calc_r2(y_val, predictions):
    """
    Args:
        y_val: val data df or arr
        predictions: pred arr
    Returns:
        r2_score
    About:
        Coeficiente de determinación. Explica como una variable se ve afectada por la variación de otra
        Sirve para medir la performance de un modelo. 
        Valores próximos a uno dicen que el modelo es capaz de explicar la variación en datos en el porcentaje que dá
        Mejor posible 1, puede ser negativo.
    """
    return r2_score(y_val, predictions)