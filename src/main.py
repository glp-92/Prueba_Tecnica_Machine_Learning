import json, sys, os, time
from datetime import datetime 
import numpy as np
from sklearn.metrics import mean_squared_error

from data.get_dataset import get_dataset
from data.data_validation import validate_data
from data.data_clean import clean_data
from data.data_export import plot_histogram, plot_correlation_map, plot_price_map
from data.prepare_dataset import prepare_dataset
from util.class_log import Log
from util.make_dir import make_dir
from model.lineal_correlation import calculate_lineal_correlation
from model.decission_tree import DecissionTree


try: # Creacion de directorios y carga de configuracion
    with open('../cfg/cfg.json', 'r') as f: # Recomendable rutas absolutas por seguridad
        cfg = json.load(f)
    log_dir_path = make_dir(cfg["project_routes"]["log_dir_path"]) # Se crea directorio de almacenamiento de logs de no existir
    runs_dir_path = make_dir(cfg["project_routes"]["runs_dir_path"])
    log_manager = Log()
    log = log_manager.build(name='log', log_path=log_dir_path, storage_days=7, console_handler=True)
except Exception as e:
    print(f"{type(e).__name__}:{e}")
    sys.exit() # Detiene la ejecucion si no hay logs ni configuracion disponibles


if __name__ == '__main__':
    time_stamp = datetime.now()
    time_stamp = time_stamp.strftime("exp%Y%m%d%H%M%S/") # Huella temporal para el directorio de almacenamiento de datos del proyecto

    df_housing = get_dataset(log=log, verbose=False)
    try:
        validate_data(df=df_housing, validation_types=cfg["pre_processing_data"]["data_validation_types"])
        log.info("DATASET_VAL:: Dataset validado correctamente contra los tipos de datos especificados")
        df_housing = clean_data(df=df_housing, value_limit_dict=cfg["pre_processing_data"]["value_limit_df"])
        df_housing = df_housing.reset_index(drop=True)
        log.info("DATASET_CLEAN:: Limpieza de dataset sin errores")
    except Exception as e:
        log.error(f"DATASET_PREPROCESS:: {type(e).__name__}:{e}")

    exp_dir = f"{runs_dir_path}{time_stamp}"
    make_dir(exp_dir)
    log.info(f"EXP_DIR:: Creado directorio de experimento {time_stamp}")

    # Plotting data
    plot_data = False
    if plot_data:
        column_names = list(df_housing)
        for column in list(df_housing):
            plot_histogram(
                data=df_housing[column], 
                exp_path=f"{exp_dir}hist_{column}.png", 
                title=column,
                xlabel=column, 
                ylabel='Frecuencia'
            )
        log.info("PLOT_HIST:: Exportados histogramas del dataframe")
        df_corr = calculate_lineal_correlation(df=df_housing)
        plot_correlation_map(df_corr, exp_path=f"{exp_dir}corr_map.png")
        log.info("PLOT_CORR:: Exportado mapa de correlacion de dataframe")
        plot_price_map(df=df_housing, exp_path=f"{exp_dir}coord_map.html", n_samples=100)
        log.info("PLOT_CORR:: Exportado mapa html con coordenadas y precios")

    # Dataset Preparing
    x_train, y_train, x_val, y_val = prepare_dataset(df=df_housing)
    # print(x_train.describe())
    # print(y_train.describe())

    for max_depth in [2,3,4,5,6,7,8,9,10]:
        decission_tree = DecissionTree(log=log, max_depth=max_depth)
        decission_tree.fit(x_train=x_train, y_train=y_train, export_tree_path=f"{exp_dir}tree_depth{max_depth}.png")
        predictions = decission_tree.predict(x_val)
        mse = mean_squared_error(y_val, predictions)
        print(f"max_depth={max_depth}: MSE={mse}")