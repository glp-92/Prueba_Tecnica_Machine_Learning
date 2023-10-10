from datetime import datetime
import os

from data.get_dataset import get_dataset
from data.data_validation import validate_data
from data.data_clean import clean_data
from data.data_export import plot_histogram, plot_correlation_map, plot_price_map
from data.prepare_dataset import prepare_dataset

from metrics.get_metrics import calc_mse, calc_mae, calc_rmse, calc_r2
from metrics.export_scatter_map import export_scatter_map

from util.make_dir import make_dir
from util.generate_html_report import generate_html_report

from model.lineal_correlation import calculate_lineal_correlation
from model.SKL_Decission_Tree import SKL_Decission_Tree
from model.SKL_Linear_Regression import SKL_Linear_Regression
from model.SKL_Lasso import SKL_Lasso
from model.TF_Dense_Net import TF_Dense_Net


class Pipeline():
    
    def __init__(self, cfg, log):
        self.cfg = cfg 
        self.log = log

    def run_experiment(self, **args):
        """
        Args:
            verbose: Si True, imprime por pantalla features del dataset importado
            runs_dir_path: ruta del directorio /runs que se recoge del cfg
            export_data: si True, almacena datos en /runs
        Returns:
            None
        Saves:
            - runs/ : genera un directorio con la huella temporal del experimento que contiene:
                - data_visual: 
                    - histogramas
                    - mapa de correlación
                    - mapa geográfico
                - results:
                    - configuración arbol de decisión (tree_depth...)
                    - gráficas de dispersión de cada modelo
        Raises:
            TypeError: El diccionario de configuracion de limite de valores no tiene los valores requeridos
            ValueError: Columna del cfg de limite no existe en el dataframe
        About:
            Ejecuta los siguientes pasos:
            1. Importa el dataset en un dataframe de Pandas
            2. Valida la entrada del formato del dataframe para evitar vulnerabilidades
            3. Limpia el dataframe de valores nulos, repetidos y fuera de rango marcado por configuracion
            4. Exporta figuras de visualización de datos
                1. Histogramas de cada columna del dataframe con su repetibilidad
                2. Mapa de correlacion, dependencias de variables independientes con la variable dependiente (y)
                3. Mapa con marcadores de parte de los datos, con localización GPS y precio.
            5. Distribuye el dataset entre conjunto de entrenamiento y de test (usado posteriormente para extraer métricas)
            6. Ajusta el dataset a los diversos modelos predictivos y extrae las métricas MSE, MAE, RMSE, y R cuadrado para realizar comparación, así como el gráfico de dispersión entre predicción y valor de test
            7. Genera informe en runs/exp..../report.html para visualización sencilla
        """

        def pre_processing_data(df_housing):
            validate_data(df=df_housing, validation_types=self.cfg["pre_processing_data"]["data_validation_types"])
            self.log.info("DATASET_VAL:: Dataset validado correctamente contra los tipos de datos especificados")
            df_housing = clean_data(df=df_housing, value_limit_dict=self.cfg["pre_processing_data"]["value_limit_df"])
            df_housing = df_housing.reset_index(drop=True)
            self.log.info("DATASET_CLEAN:: Limpieza de dataset sin errores")
            return df_housing
            
        def plot_dataset_features(df_housing):
            for column in list(df_housing):
                plot_histogram(
                    data=df_housing[column], 
                    exp_path=f"{folders['visualization_dir']}hist_{column}.png", 
                    title=column,
                    xlabel=column, 
                    ylabel='Frecuencia'
                )
            self.log.info("PLOT_HIST:: Exportados histogramas del dataframe")
            df_corr = calculate_lineal_correlation(df=df_housing)
            plot_correlation_map(df_corr, exp_path=f"{folders['visualization_dir']}corr_map.png")
            self.log.info("PLOT_CORR:: Exportado mapa de correlacion de dataframe")
            plot_price_map(df=df_housing, exp_path=f"{folders['visualization_dir']}coord_map.html", n_samples=100)
            self.log.info("PLOT_CORR:: Exportado mapa html con coordenadas y precios")
            return 
        
        def calc_metrics(y_val, predictions):
            mse = calc_mse(y_val=y_val, predictions=predictions)
            mae = calc_mae(y_val=y_val, predictions=predictions)
            rmse = calc_rmse(y_val=y_val, predictions=predictions)
            r2 = calc_r2(y_val=y_val, predictions=predictions)
            return mse, mae, rmse, r2


        error_on_pipeline = False

        # Huella temporal para el nuevo experimento
        time_stamp = datetime.now()
        time_stamp_str = time_stamp.strftime("exp%Y%m%d%H%M%S/") 

        # Creando directorios de experimento
        try:
            if args["export_data"]:
                folders = {
                    "visualization_dir": f"{args['runs_dir_path']}{time_stamp_str}data_visual/", 
                    "results_dir": f"{args['runs_dir_path']}{time_stamp_str}results/"
                }
                for folder in folders.values():
                    make_dir(folder)
                self.log.info(f"EXP_DIR:: Creado directorio de experimento {time_stamp_str}") 
        except Exception as e:
            error_on_pipeline = True
            self.log.error(f"EXP_DIR:: Error en creación de directorios de experimento: {type(e).__name__}:{e}")

        # Obtencion de dataset
        if not error_on_pipeline: 
            try:
                df_housing = get_dataset(log=self.log, verbose=args["verbose"])
            except Exception as e:
                error_on_pipeline = True 
                self.log.error(f"DATA_IMPORT:: Error importando dataset: {type(e).__name__}:{e}")

        # Pre procesamiento de datos
        if not error_on_pipeline: 
            try:
                df_housing = pre_processing_data(df_housing=df_housing)
            except Exception as e:
                error_on_pipeline = True
                self.log.error(f"DATASET_PREPROCESS:: {type(e).__name__}:{e}")

        # Exportando datos de visualizacion del dataframe
        if not error_on_pipeline and args["export_data"]: 
            try:
                plot_dataset_features(df_housing=df_housing)
            except Exception as e:
                error_on_pipeline = True 
                self.log.error(f"DATA_FEATURE_EXPORT:: Error exportando features del dataset: {type(e).__name__}:{e}")

        # Dividiendo el set de datos en train y test
        if not error_on_pipeline: 
            try:
                x_train, y_train, x_val, y_val, y_min, y_max = prepare_dataset(df=df_housing)
            except Exception as e:
                error_on_pipeline = True 
                self.log.error(f"DATASET_PREPARING:: Error creando conjuntos train y test de dataset: {type(e).__name__}:{e}")

        # Cargando cada uno de los modelos y extrayendo metricas y predicciones
        if not error_on_pipeline:
            results = {
                "decission_tree": None,
                "linear_regression": None,
                "lasso": None,
                "dense_net": None
            }
            # Decission Tree
            try:
                self.log.info("DECISSION_TREE:: Ejecutando model arbol de decision...")
                max_depth = self.cfg["model"]["decission_tree"]["max_depth"]
                model = SKL_Decission_Tree(log=self.log, max_depth=max_depth)
                export_path = None
                if args["export_data"]:
                    export_path = f"{folders['results_dir']}tree_depth.png"
                model.fit(x_train=x_train, y_train=y_train, export_tree_path=export_path)
                self.log.info(f"DECISSION_TREE:: Realizando prediccion para depth {max_depth}")
                predictions = model.predict(x_val)
                self.log.info(f"DECISSION_TREE:: Extrayendo metricas...")
                mse, mae, rmse, r2 = calc_metrics(y_val=y_val, predictions=predictions)
                results["decission_tree"] = (mse, mae, rmse, r2)
                self.log.info(f"DECISSION_TREE_RES:: max_depth={max_depth}: MSE={mse}; MAE={mae}; RMSE={rmse}; R2={r2}")
                if args["export_data"]:
                    export_scatter_map(
                        title=f"Decission tree depth {max_depth}",
                        predictions=predictions, 
                        y_val=y_val, 
                        points_to_draw=self.cfg["export"]["scatter_map"]["points_to_draw"],
                        path_to_export=f"{folders['results_dir']}tree_depth_scatter.png"
                    )
            except Exception as e:
                error_on_pipeline = True 
                self.log.error(f"DECISSION_TREE:: Error en modelo Decission Tree: {type(e).__name__}:{e}")

            # Linear regression
            try:
                self.log.info(f"LINEAR_REGRESSION:: Ejecutando modelo de regresion lineal...")
                model = SKL_Linear_Regression(log=self.log)
                model.fit(x_train=x_train, y_train=y_train)
                self.log.info(f"LINEAR_REGRESSION:: Realizando prediccion")
                predictions = model.predict(x_val)
                self.log.info(f"LINEAR_REGRESSION:: Extrayendo metricas...")
                mse, mae, rmse, r2 = calc_metrics(y_val=y_val, predictions=predictions)
                results["linear_regression"] = (mse, mae, rmse, r2)
                self.log.info(f"LINEAR_REGRESSION:: max_depth={max_depth}: MSE={mse}; MAE={mae}; RMSE={rmse}; R2={r2}")
                if args["export_data"]:
                    export_scatter_map(
                        title=f"Linear Regression",
                        predictions=predictions, 
                        y_val=y_val, 
                        points_to_draw=self.cfg["export"]["scatter_map"]["points_to_draw"],
                        path_to_export=f"{folders['results_dir']}linear_regression_scatter.png"
                    )
            except Exception as e:
                error_on_pipeline = True 
                self.log.error(f"LINEAR_REGRESSION:: Error en modelo de regresion lineal: {type(e).__name__}:{e}")

            # Lasso
            try:
                self.log.info(f"LASSO:: Ejecutando modelo de Lasso...")
                model = SKL_Lasso(log=self.log)
                model.fit(x_train=x_train, y_train=y_train)
                self.log.info(f"LASSO:: Realizando prediccion")
                predictions = model.predict(x_val)
                self.log.info(f"LASSO:: Extrayendo metricas...")
                mse, mae, rmse, r2 = calc_metrics(y_val=y_val, predictions=predictions)
                results["lasso"] = (mse, mae, rmse, r2)
                self.log.info(f"LASSO:: max_depth={max_depth}: MSE={mse}; MAE={mae}; RMSE={rmse}; R2={r2}")
                if args["export_data"]:
                    export_scatter_map(
                        title=f"Lasso",
                        predictions=predictions, 
                        y_val=y_val, 
                        points_to_draw=self.cfg["export"]["scatter_map"]["points_to_draw"],
                        path_to_export=f"{folders['results_dir']}lasso_scatter.png"
                    )
            except Exception as e:
                error_on_pipeline = True 
                self.log.error(f"LASSO:: Error en modelo de Lasso: {type(e).__name__}:{e}")

            # Dense net
            try:
                self.log.info(f"DENSE_NET:: Ejecutando modelo de Deep Learning con dense layers...")
                model_path = f"{args['weights_path']}{self.cfg['model']['dense_net']['model_name']}"
                from_saved = args["saved_model"]
                if from_saved and not os.path.exists(model_path):
                    from_saved = False
                model = TF_Dense_Net(log=self.log, 
                    x_ncols=len(x_val.columns), 
                    y_ncols=len(y_train.shape), 
                    model_path=model_path,
                    from_saved=from_saved
                )
                if not from_saved:
                    model.fit(
                        x_train=x_train,
                        y_train=y_train, 
                        batch_size=self.cfg["model"]["dense_net"]["batch_size"], 
                        epochs=self.cfg["model"]["dense_net"]["epochs"]
                    )
                self.log.info(f"DENSE_NET:: Realizando prediccion")
                predictions = model.predict(x_val)
                self.log.info(f"DENSE_NET:: Extrayendo metricas...")
                mse, mae, rmse, r2 = calc_metrics(y_val=y_val, predictions=predictions)
                results["dense_net"] = (mse, mae, rmse, r2)
                self.log.info(f"DENSE_NET:: max_depth={max_depth}: MSE={mse}; MAE={mae}; RMSE={rmse}; R2={r2}")
                if args["export_data"]:
                    export_scatter_map(
                        title=f"Dense Net",
                        predictions=predictions, 
                        y_val=y_val, 
                        points_to_draw=self.cfg["export"]["scatter_map"]["points_to_draw"],
                        path_to_export=f"{folders['results_dir']}dense_net_scatter.png"
                    )
            except Exception as e:
                error_on_pipeline = True 
                self.log.error(f"DENSE_NET:: Error en modelo Dense Net: {type(e).__name__}:{e}")
            
        if not error_on_pipeline and args["export_data"]:
            try:
                generate_html_report(
                    time_stamp=time_stamp, 
                    results=results, 
                    path_to_report=f"{args['runs_dir_path']}{time_stamp_str}report.html"
                )
                self.log.info(f"REPORT_GEN:: Reporte generado en: {args['runs_dir_path']}{time_stamp_str}")
            except Exception as e:
                error_on_pipeline = True 
                self.log.error(f"REPORT_GEN:: Error en generacion de reporte: {type(e).__name__}:{e}")

        return error_on_pipeline
            

        
        

