import pandas as pd


def delete_null_rows(df):
    df.dropna(inplace = True)

def delete_duplicated_rows(df):
    df.drop_duplicates(inplace = True)

def delete_bad_data_rows(df, value_limit_dict):
    """
    Args:
        df: DataFrame a limpiar.
        value_limit_dict: Diccionario que establece los límites de valores para cada columna. Lista blanca para filtrar valores confiables.
    Returns:
        DataFrame limpio.
    Raises:
        TypeError: El diccionario de configuracion de limite de valores no tiene los valores requeridos
        ValueError: Columna del cfg de limite no existe en el dataframe
    About:
        Elimina filas del DataFrame que contienen valores fuera de los límites establecidos.
    """
    # Validacion de diccionario de limite de valores
    for column_name, limit_list in value_limit_dict.items():
        if column_name not in df.columns:
            raise ValueError(f"La columna {column_name} no existe en el DataFrame")
        if not isinstance(limit_list, list):
            raise TypeError(f"La columna {column_name} debe marcar los límites con una lista")
        if len(limit_list) != 2:
            raise TypeError(f"La columna {column_name} debe tener una lista límite de 2 valores")
        if not isinstance(limit_list[0], (int, float)) or not isinstance(limit_list[1], (int, float)):
            raise TypeError(f"La columna {column_name} debe tener límites de tipo numérico")
    # Eliminar filas fuera de los límites
    for column_name, limit_list in value_limit_dict.items():
        df = df.loc[(df[column_name] >= min(limit_list)) & (df[column_name] <= max(limit_list))]
    return df 

def clean_data(df, value_limit_dict):
    '''
    Args:
        df: Pandas dataFrame sin limpiar.
    Returns:
        df: Pandas dataframe limpio
    Raises:
        TypeError: Si df no es un DataFrame.
    About:
        Se limpia el dataframe contra valores nulos, duplicados, o fuera de lógica.
    '''
    if not isinstance(df, pd.DataFrame):
        raise TypeError("El argumento `df` debe ser del tipo DataFrame")
    delete_null_rows(df=df)
    delete_duplicated_rows(df=df)
    df = delete_bad_data_rows(df=df, value_limit_dict=value_limit_dict)
    return df