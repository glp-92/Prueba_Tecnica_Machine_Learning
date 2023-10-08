## Estructura del proyecto
El proyecto se ha estructurado en los siguientes directorios:
- src: contiene los módulos de programa de Python, donde 'main.py' es el fichero principal de ejecución
    - data: paquete que contiene el dataset, import, export y visualizacion del mismo
    - model: contiene la arquitectura de los modelos que se probarán
- src_test: contiene scripts de prueba de la aplicación
- doc: contiene la documentación extraída del proyecto
- cfg: contiene los archivos de configuración. Se ha optado por usar un 'cfg.json', podría utilizarse un '.env' u otro tipo de archivo. Se opta por '.json' por facilidad de importar y leer diccionarios. Estos ficheros en producción no deberían estar en directorio público.
**Importante** Dada la incertidumbre en cuanto a ejecución de la prueba, se ha optado por rutas relativas de ficheros, por lo que se debe acceder a '/src' o '/src_test' para realizar las ejecuciones de las pruebas o del programa principal. Usar rutas relativas no se considera buena práctica en desarrollo, ya que se incrementa la superficie de ataque pudiendo permitir a un atacante navegar a través del sistema de archivos.

## Acerca de California Housing Dataset
- 20640 filas de datos, expresa la mediana del valor de la viviendo para los distritos de california
- Es posible que haya ciertos atributos con valor Null
- El valor de vivienda esta expresado sobre 100.000$
- Cada bloque de viviendas típicamente comprende entre 600 - 3000 personas
- Es posible encontrar bloques con casas vacías y elevado número de habitaciones, como resorts.
- Datos:
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
En una primera aproximación, y basándose en el tiempo disponible para la realización de la prueba, se tratará únicamente con el dataset sugerido, ya que el análisis de datos no es una tarea habitual. En caso de obtener buenos resultados y disponer de mas tiempo, se tratará de incorporar datos 'extra' al modelo (distancia al mar, servicios proximos...). Se aprovechará la oportunidad para refrescar conceptos y métodos de matplotlib, numpy, pandas y scikit-learn.

[Procedimiento](doc/proc/primera_aproximacion.md)

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