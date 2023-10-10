# python main.py --verbose False --export True --saved_model True
import json, sys, os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__), 
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

def str_to_bool(value):
    if isinstance(value, bool):
        return value
    if value.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif value.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

import argparse
parser = argparse.ArgumentParser(description='Programa principal:: Predicción de precio de vivienda')
parser.add_argument('--verbose', type=str, required=True, help='Registra dataset importado en logs')
parser.add_argument('--export', type=str, required=True, help='Si se desea exportar los datos')
parser.add_argument('--saved_model', type=str, required=True, help='Si se desea importar el modelo Dense')
args = parser.parse_args()

verbose = str_to_bool(args.verbose)
export = str_to_bool(args.export)
saved_model = str_to_bool(args.saved_model)

from controller.Pipeline import Pipeline
from util.class_log import Log
from util.make_dir import make_dir


try: # Creacion de directorios y carga de configuracion

    with open('../cfg/cfg.json', 'r') as f: # Recomendable rutas absolutas por seguridad
        cfg = json.load(f)
    log_dir_path = make_dir(cfg["project_routes"]["log_dir_path"]) # Se crea directorio de almacenamiento de logs de no existir
    runs_dir_path = make_dir(cfg["project_routes"]["runs_dir_path"])
    weights_path = make_dir(cfg["project_routes"]["weights_path"])
    log_manager = Log()
    log = log_manager.build(name='log', log_path=log_dir_path, storage_days=7, console_handler=True)
except Exception as e:
    print(f"{type(e).__name__}:{e}")
    sys.exit() # Detiene la ejecucion si no hay logs ni configuracion disponibles


if __name__ == '__main__':
    pipeline = Pipeline(cfg=cfg, log=log)
    err = pipeline.run_experiment(verbose=verbose, runs_dir_path=runs_dir_path, weights_path=weights_path, export_data=export, saved_model=saved_model)
    if not err:
        log.info("PIPELINE_SUCEED:: Pipeline finalizada sin errores\n\n")
    else:
        log.error("PIPELINE_ERROR:: Error en pipeline\n\n")