from sklearn.model_selection import train_test_split


def prepare_dataset(df, cols_to_drop, log):
    drop_this = ['MedHouseVal']
    cols_to_drop = set(cols_to_drop) # Elimina duplicados
    if len(df.columns) - 1 >= len(cols_to_drop):
        for col in cols_to_drop:
            if col in df.columns:
                log.warning(f"DATASET_PREPARE:: Se eliminará la columna {col} del dataset")
                drop_this += [col]
            else:
                log.error(f"DATASET_PREPARE:: Se pretendía eliminar la columna no existente {col}. Se ha ignorado")
    else:
        log.error(f"DATASET_PREPARE:: Borrado ignorado. Debe haber >= 1 variable dependiente. Revisar cfg")
    x_data = df.drop(drop_this, axis = 1) # Se elimina de x_train el precio, ya que es el resultado esperado (y_train)
    y_data = df['MedHouseVal']
    normalized_x_data = (x_data-x_data.min())/(x_data.max()-x_data.min())
    normalized_y_data = (y_data-y_data.min())/(y_data.max()-y_data.min())
    x_train, x_test, y_train, y_test = train_test_split(
        normalized_x_data, 
        normalized_y_data, 
        test_size=0.2
    )
    return x_train, y_train, x_test, y_test, y_data.min(), y_data.max()
