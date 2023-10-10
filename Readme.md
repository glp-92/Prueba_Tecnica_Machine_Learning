## Estructura del proyecto
El proyecto se ha estructurado en los siguientes directorios:
- src: contiene los módulos de programa de Python, donde 'main.py' es el fichero principal de ejecución
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
        - `TF_Dense_Net` modelo custom en tensorflow que trata de abordar el problema.
    - util
        - `class_log` clase para generar logs del programa
        - `generate_html_report` clase para generar el html en base al experimento realizado.
        - `make_dir` función para creación de directorio y adición de `/` al final de la ruta especificada si no la tiene.

- src_test: contiene scripts de prueba de la aplicación. Dentro del directorio `data` está el script que inyecta datos simulados al dataframe y utiliza las funciones de limpieza para la posterior comprobación de su eficacia.
- doc: contiene la documentación extraída del proyecto
- cfg: contiene los archivos de configuración. Se ha optado por usar un 'cfg.json', podría utilizarse un '.env' u otro tipo de archivo. Se opta por '.json' por facilidad de importar y leer diccionarios. Estos ficheros en producción no deberían estar en directorio público.
- logs: directorio con los registros del programa
- runs: directorio donde se almacenan las salidas del programa (experimentos), gráficas, mapas o tablas.
- weights: directorio de pesos de la Dense_net empleada.

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