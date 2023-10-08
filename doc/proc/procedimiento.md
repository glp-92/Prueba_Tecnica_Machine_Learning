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
    3. Se realizará un split entre set de datos de entrenamiento, validación y test, de los cuales se tratará de extraer métricas del modelo.
6. Entrenamiento.
    1. Se probará diversos algoritmos, se reservará un set de testing para realizar inferencias posteriores y tratar de extraer métricas en base a ello.
        1. Arboles de decision: 
            - Divide de forma recursiva, en profundidad los datos en 2 grupos. 
            - El parámetro `max_depth` marca la profundidad del árbol, o el número máximo de divisiones que hace. Un valor elevado puede causar overfitting, aprendiendo detalles más precisos, ruido incluido.
7. Optimización. Entre las posibles optimizaciones que se ha planteado se contempla las siguientes:
    1. El modelo usa un tipo de dato float64, ver si float32 produce alguna optimización. Inclusive la posibilidad de pasar el dataframe a formato int32.
    2. Se tratará de eliminar las columnas del dataset que tengan menor influencia sobre el valor del inmueble usando el mapa de correlación para hallar dichas columnas.
    3. Prunning y quantization de ser posible, de forma dinámica tras el entrenamiento, o estática.
8. Emisión de resultados.
    1. Gráficas de resultados, función que permita utilizar el modelo