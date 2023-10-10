## Estructura del proyecto
El proyecto se ha estructurado en los siguientes directorios:
- src: contiene los módulos de programa de Python, donde 'main.py' es el fichero principal de ejecución
    - controller
        - `Pipeline` clase que maneja y centraliza la lógica de programa, en este caso la Pipeline de ML, desde ingestion de datos, procesamiento, entrenamiento e inferencia, utilizando el resto de módulos de programa.
    - data
        - `data_clean` limpieza de dataset de valores duplicados, nulos o fuera de rango.
        - `data_export` funciones de plot de los modelos (histograma, correlación, mapa)
        - `data_validation` verificación de tipo de datos correcto en el dataframe de entrada.
        - `get_dataset` descarga del dataset usando sklearn.
        - `prepare_dataset` realiza la división del dataset en train y test y realiza la normalización min-max.
    - metrics
        - `export_scatter_map` función para exportar en imagen el mapa de dispersión, empleada por cada uno de los modelos.
        - `get_metrics` calcula las métricas dado los valores de predicción y los del valor de test.
    - model
        - `lineal_correlation` modelo de correlación lineal empleado para ver las relaciones entre variables.
        - `SKL_Decission_Tree` clase de árbol de decisión de scikit-learn.
        - `SKL_Lasso` clase de algoritmo de Lasso de scikit-learn.
        - `SKL_Linear_Regression` clase de algoritmo de regresión lineal múltiple de scikit-learn.
        - `TF_Custom_Dense_Net` modelo custom en tensorflow que trata de abordar el problema.
    - util
        - `class_log` clase para generar logs del programa
        - `generate_html_report` clase para generar el html en base al experimento realizado.
        - `make_dir` función para creación de directorio y adición de `/` al final de la ruta especificada si no la tiene.

- src_test: contiene scripts de prueba de la aplicación. Dentro del directorio `data` está el script que inyecta datos simulados al dataframe y utiliza las funciones de limpieza para la posterior comprobación de su eficacia.
- doc: contiene la documentación extraída del proyecto
- cfg: contiene los archivos de configuración. Se ha optado por usar un 'cfg.json', podría utilizarse un '.env' u otro tipo de archivo. Se opta por '.json' por facilidad de importar y leer diccionarios. Estos ficheros en producción no deberían estar en directorio público.
- logs: directorio con los registros del programa
- runs: directorio donde se almacenan las salidas del programa (experimentos), gráficas, mapas o tablas.
- weights: directorio de pesos de la Custom_Dense_net empleada.

## Acerca de California Housing Dataset
- 20640 filas de datos, expresa la mediana del valor de la viviendo para los distritos de california
- Es posible que haya ciertos atributos con valor Null
- El valor de vivienda esta expresado sobre 100.000$
- Cada bloque de viviendas típicamente comprende entre 600 - 3000 personas
- Es posible encontrar bloques con casas vacías y elevado número de habitaciones, como resorts.
- Datos:

| Columna | Acerca de | 
| --- | --- |
| MedInc | Mediana de ingresos de los habitantes por bloque |
| HouseAge | Mediana de edad de las viviendas por bloque |
| AveRooms | Numero promedio de habitaciones por hogar en bloque |
| AveBedrms | Numero promedio de dormitorios por hogar en bloque |
| Population | Numero de personas que habitan en el bloque |
| AveOccup | Numero promedio de personas por hogar en bloque |
| Latitude | Latitud del bloque |
| Longitude | Longitud del bloque | 

## Procedimiento
En una primera aproximación, y basándose en el tiempo disponible para la realización de la prueba, se tratará únicamente con el dataset sugerido, ya que el análisis de datos no es una tarea habitual. En caso de obtener buenos resultados y disponer de mas tiempo, se tratará de incorporar datos 'extra' al modelo (distancia al mar, servicios proximos...) así como optimización. Se aprovechará la oportunidad para refrescar conceptos y métodos de matplotlib, numpy, pandas y scikit-learn.

[Procedimiento completo](doc/procedimiento.md)

## Ejecución

[Ejecución de la Pipeline](doc/ejecución.md)

## Métricas
- MSE: el valor medio de la diferencia entre valor real y predicho al cuadrado
    - Sensible a cambios entre valor real y predicho por elevar la diferencia al cuadrado
    - Sensible a valores atípicos, penalizando las desviaciones
    - No es comparable entre modelos con diferente unidad métrica
    - Valores deseados: próximo a 0
- MAE: Promedio de diferencia absoluta entre valor real y predicho. Usado típicamente en finanzas
    - Menor sensibilidad a valores atípicos que mse
    - Simple y facil de interpretar
    - Comparable entre modelos con diferente unidad métrica
    - Valores deseados: próximo a 0
- RMSE: Raiz cuadrada del mse
    - Mayor sensibilidad a valores atípicos que mae, pero la penalización de mse la reduce a la raíz cuadrada
    - Valores deseados: próximo a 0
- R cuadrado: Coeficiente de determinación. Explica como una variable se ve afectada por la variación de otra
    - Sirve para medir la performance de un modelo. 
    - Valores próximos a uno dicen que el modelo es capaz de explicar la variación en datos en el porcentaje que dá
    - Mejor posible 1, puede ser negativo.
- Mapa de dispersión: si el modelo es perfecto, debería visualizarse una línea diagonal. Permite ver la desviación entre valor predicho y esperado.

## Conclusiones y resultados
Se ha observado que la Custom_Dense_net es la que mejor se comporta, tanto por métricas como visualizando los diagramas de dispersion, para un experimento donde se ajusta el batch size a 64, 30 epochs, y Decission Tree con profundidad de 5 

| Id Model | MSE | MAE | RMSE | R2 | 
| --- | --- | --- | --- | --- |
| Linear Regression | 0.022 | 0.1089 | 0.1483 | 0.6206 |
| Decission Tree | 0.0214 | 0.1071 | 0.1463 | 0.6304 |
| Lasso | 0.0357 | 0.1474 | 0.189 | 0.3834 |
| Custom_Dense_net | 0.0198 | 0.1031 | 0.1406 | 0.6586 |

En los diagramas de dispersión, se ha observado que la Custom_Dense_net y el algoritmo de Regresion Lineal se ajustan mejor a los valores del dataset de test; por otro lado, el algoritmo de Lasso tiende a predecir precios aproximándose al punto medio del rango, por lo que para precios reales elevados la desviación es grande. El árbol de decisión tiende a formar escalones en la predicción de precios, tanto en profundidad 2 como a profundidad 5, por lo que no resultaría un modelo deseable en este caso.

Por otro lado, se ha probado a eliminar del dataframe las columnas asociadas a las coordenadas geográficas, ya que no deberían asociarse directamente al precio; quizás la distancia a la línea de mar en California resultaria una variable mejor, ya que por norma general las residencias próximas al mar tienen un precio mayor; pero las coordenadas como tal no deberían tratarse en este dataset si no se asociarán de alguna forma a esta clase de variables (distancia al mar, a hospitales, a zonas históricas...) y en este caso, no hay una asociación a priori lineal con el precio.

Los resultados son los siguientes:

| Id Model | MSE | MAE | RMSE | R2 | 
| --- | --- | --- | --- | --- |
| Linear Regression | 0.026 | 0.1184 | 0.1613 | 0.5434 |
| Decission Tree | 0.0215 | 0.1062 | 0.1467 | 0.6223 |
| Lasso | 0.0355 | 0.1458 | 0.1884 | 0.3765 |
| Custom_Dense_net | 0.0246 | 0.1161 | 0.157 | 0.5672 |

En cuanto a los gráficos de dispersion, se observa cómo el árbol de decisión presenta un mejor comportamiento respecto al resto de modelos al haber eliminado las 2 columnas. Para tratar de verificar que hay una relación fuerte con las coordenadas, el siguiente experimento utilizará éstas solamente para ver la relación con el precio, eliminando el resto de variables independientes:

Los resultados son los siguientes:

| Id Model | MSE | MAE | RMSE | R2 | 
| --- | --- | --- | --- | --- |
| Linear Regression | 0.0428 | 0.1593 | 0.2068 | 0.2418 |
| Decission Tree | 0.0309 | 0.1297 | 0.1757 | 0.4527 |
| Lasso | 0.0564 | 0.1873 | 0.2375 | -0.0 |
| Custom_Dense_net | 0.0415 | 0.157 | 0.2036 | 0.2654 |

El modelo que mejor comportamiento ha tenido ha sido el árbol de decisión, pese a que tanto las métricas como las gráficas muestran un ajuste menor a los datos de test. Se puede concluir que la relación del precio con las coordenadas no es fuerte.

Como conclusión, el modelo que mejor responde a la determinación del precio empleando estas variables ha sido el modelo de DL personalizado en Tensorflow. Después, el modelo de regresión lineal ha demostrado buena performance mientras que el árbol de decisión mayor tolerancia a grandes modificaciones en el dataset.

Los experimentos se adjuntan en la carpeta [/doc/experimentos](/doc/experimentos/)

## Referencias
Se ha utilizado las siguientes referencias para el proyecto:
- [California Housing Dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html)
- [Folium Map Representation](https://python-visualization.github.io/folium/latest/getting_started.html)
- [ML Performance Metrics](https://neptune.ai/blog/performance-metrics-in-machine-learning-complete-guide)
- [Drop null values of Df](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html)
- [Find duplicated values of Df](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.duplicated.html)
- [Filter dataframe by conditions](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html)
- [Plot correlation matrix](https://stackoverflow.com/questions/29432629/plot-correlation-matrix-using-pandas)
- [Pandas df DOC](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- [Decission Tree](https://scikit-learn.org/stable/modules/tree.html)
- [R2 Metric](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html)
- [Keras Regression Model](https://www.tensorflow.org/tutorials/keras/regression?hl=es-419)

Se ha utilizado IA Generativa (ChatGPT, Bard...) para implementación rápida de ciertos métodos, el planteamiento del problema y solución son propios, basado en experiencia y conocimiento en el campo.