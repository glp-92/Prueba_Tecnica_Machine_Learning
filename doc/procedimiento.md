1. Obtención del dataset a través de librería scikit-learn
2. Conversion en dataframe. El dataset integra funciones para leerlo como Df con Pandas.
3. Limpieza de datos
    1. Validación de datos: la entrada de una fuente no confiable que será utilizada por el programa debe validarse en cuanto a tipo de dato y rango, se cotejará haciendo whitelisting de tipos de datos.
    2. En la descripción del dataset se hace entrever que puede haber valores nulos. Esas filas serán eliminadas para evitar su influencia en la creación del modelo. Se realizara un test conforme tras esta operación no existan valores nulos en el dataset.
    3. Se tratará de eliminar duplicados. Se realizará un test comprobando que los métodos son fiables.
    4. Se tratará de eliminar valores negativos y demasiado elevados de la misma manera, a través de whitelisting. Se realizará un test comprobando la correcta eliminación.
4. Visualización: para tener una idea de las correlaciones entre datos y como se comporta el precio de la vivienda según diversos parámetros, así como su distribución y repetitividad, se permitirá exportar tanto histogramas, como mapas de correlacion, como un mapa con las coordenadas GPS y algunas de las localizaciones con su precio.
5. Preparacion de dataset:
    1. x_train será el dataframe sin los precios
    2. y_train será el precio de cada fila del dataframe
    3. Se aplicará una normalización min-max value para que el dataframe tome valores entre 0 y 1, lo cual ayudará al cómputo y manejar rangos comunes de datos.
    4. Se realizará un split entre set de datos de entrenamiento, y test, de los cuales se tratará de extraer métricas del modelo.
6. Entrenamiento.
    1. Se probará diversos algoritmos, se reservará un set de testing para realizar inferencias posteriores y tratar de extraer métricas en base a ello.
        1. Arboles de decision: 
            - Divide de forma recursiva, en profundidad los datos en 2 grupos. 
            - El parámetro `max_depth` marca la profundidad del árbol, o el número máximo de divisiones que hace. Un valor elevado puede causar overfitting, aprendiendo detalles más precisos, ruido incluido.
        2. Regresión lineal:
            - Utilizada para predecir el valor de una variable dependiente de otras independientes. Se analiza la variabilidad de la variable dependiente mediante combinaciones lineales de las variables independientes.
        3. Lasso:
            - Modelo de regresión lineal regularizada, con mayor tolerancia al ruido de datos, mejor interpretabilidad que el modelo de regresión y ayuda a prevenir overfitting por la regularización.
        4. Modelo de Deep Learning custom:
            - Empleando tensorflow, se ha creado un modelo secuencial con 3 capas dense para enfrentar sus valores a los modelos lineales de regresión. Debido a que según las epochs de entrenamiento la ejecución puede requerir tiempo, se puede cargar el modelo desde el directorio weights/ si ya se ha entrenado en alguna ocasión. 
7. Optimización.
    1. Se pretende eliminar aquellas variables independientes (columnas) que menos relación tuviesen con la dependiente, examinado a través del mapa de correlación. Así, se ha realizado pruebas eliminando las coordenadas geográficas, cuya relación no se ha considerado lineal con el precio.
    2. (No se ha llegado finalmente) Se pretendía reducir el formato del dataset a float32 de ser posible
    3. (No se ha llegado finalmente) Se pretendía convertir el modelo de tensorflow .h5 a sqlite y quantizarlo a float16, mejorando su performance (ha dado buenos resultados con modelos de clasificación tipo Vggnet)
8. Emisión de resultados.
    1. Gráficas de resultados, informe Html con resumen de todas las métricas y gráficas útiles.