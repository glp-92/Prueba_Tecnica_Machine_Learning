import pandas as pd

from data.data_clean import delete_duplicated_rows, delete_null_rows, delete_bad_data_rows


def test_dataframe_clean(df, preproc_cfg, log):
    """
    Args:
        df: Pandas dataframe
        preproc_cfg: Datos de test desde configuracion
        log: Registro de informacion
    Returns:
        None
    Raises:
        AssertionError: Test no superado
    About:
        Se prueba las funciones de limpieza del dataset inyectando datos en el dataframe nulos, duplicados o fuera de rango
    """
    log.info("TEST:: Realizando prueba de limpieza de valores nulos...")
    df.loc[len(df)] = preproc_cfg["null_value"]
    delete_null_rows(df = df)
    # Existen valores nulos tras la limpieza
    is_empty = df[df.isna().any(axis=1)] # Se trata de obtener las rows con valor nulo
    assert is_empty.empty, "El conjunto de datos contiene valores nulos"
    log.info("TEST:: Prueba superada")

    log.info("TEST:: Realizando prueba de limpieza de valores duplicados...")
    df.loc[len(df)] = preproc_cfg["duplicate_value"]
    df.loc[len(df)] = preproc_cfg["duplicate_value"]
    delete_duplicated_rows(df = df)
    n_duplicated = df.duplicated().sum()
    assert n_duplicated == 0, "El conjunto de datos contiene valores duplicados"
    log.info("TEST:: Prueba superada")

    log.info("TEST:: Realizando prueba de limpieza de valores fuera de límites fijados...")
    value_limit_dict = preproc_cfg["out_of_bounds_value"]["value_limit_df"]
    df.loc[len(df)] = preproc_cfg["out_of_bounds_value"]["test_value"]
    df = delete_bad_data_rows(df=df, value_limit_dict=value_limit_dict)
    delete_mask = pd.Series([False])
    for column_name, limit_list in value_limit_dict.items():
        delete_mask = (df[column_name] < min(limit_list)) | (df[column_name] > max(limit_list))
        if any(delete_mask): break
    assert not any(delete_mask), f"El conjunto de datos contiene valores fuera de los límites establecidos en la columna {column_name}"
    log.info("TEST:: Prueba superada")