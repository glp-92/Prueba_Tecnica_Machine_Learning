from datetime import datetime 
import json, sys
import sys
sys.path.append('../src')

from util.make_dir import make_dir
from util.class_log import Log
from data.test_data_clean import test_dataframe_clean
from data.get_dataset import get_dataset


try: # Creacion de directorios y carga de configuracion
    with open('../cfg/cfg_test.json', 'r') as f: # Recomendable rutas absolutas por seguridad
        cfg = json.load(f)
    log_dir_path = make_dir(cfg["project_routes"]["log_dir_path"]) # Se crea directorio de almacenamiento de logs de no existir
    runs_dir_path = make_dir(cfg["project_routes"]["runs_dir_path"])
    log_manager = Log()
    log = log_manager.build(name='test_log', log_path=log_dir_path, storage_days=7, console_handler=True)
except Exception as e:
    print(f"{type(e).__name__}:{e}")
    sys.exit() # Detiene la ejecucion si no hay logs ni configuracion disponibles

if __name__ == '__main__':
    time_stamp = datetime.now()
    df_housing = get_dataset(log = log, verbose=True)
    try: 
        test_dataframe_clean(df=df_housing, preproc_cfg=cfg["pre_processing_test"], log=log)
        log.info("TESTS:: Tests superados")
    except Exception as e:
        log.error(f"{type(e).__name__}:{e}")
