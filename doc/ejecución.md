1. Al codificar el programa, y no saber en que entorno ni en que directorio se colocarán los ficheros de programa, se utiliza rutas relativas de forma excepcional. Utilizar rutas relativas puede dar lugar a vulnerabilidades en el código tales como escalada de privilegios, inyección de código o cross-site-scripting.
2. Debido a las rutas relativas, la ejecución del script `main.py` del programa principal y el script `main.py` de los tests debe realizarse desde dentro del directorio `/src`. Además, el informe html generado contiene rutas relativas a las gráficas por lo que si se desplaza de directorio no se mostrarían.
3. Instalación de dependencias.
    1. Con [Anaconda](https://docs.anaconda.com/free/anaconda/install/index.html) (con la que se ha desarrollado):
        1. Creación y activación de entorno
            ```
            conda create -n env python=3.10
            conda activate env
            ```
        2. Navegar al directorio raíz del proyecto con el entorno activo:
            ```
            pip install -r requirements.txt
            ```
4. Ejecución.
    1. Con el entorno activo, navegar al directorio `src` y ejecutar el main:
        ```
            cd src
            python main.py --verbose False --export True --saved_model False
        ```
        - verbose: imprimirá en el log detalles sobre el dataset descargado
        - export: en el directorio `/runs` creará un subdirectorio con la fecha del experimento, y guardará ahí todas las gráficas y documentos generados.
        - saved_model: si se pone en True, el programa tratará de cargar el fichero `.h5` de la red neuronal, al ser la que más tiempo de ejecución requiere por el entrenamiento. Si no se encuentra la ruta de ese fichero en el programa, realizará igualmente el entrenamiento y posteriormente la inferencia.
    2. Se ha creado tests para comprobar validación y limpieza del dataset. Para ejecutarlos:
        ```
            cd src_test
            python main.py
        ```
5. Ficheros de configuración:
    1. `cfg/cfg.json` Contiene las siguientes entradas:
        - `project_routes`: rutas donde se generarán directorios para almacenar logs, resultados y pesos de entrenamiento.
        - `pre_processing_data`: diccionario de preprocesado del dataset
            - `data_validation_types`: tipos de dato de validacion del dataset, cada columna debe corresponder en orden con el tipo de dato especificado en la lista.
            - `value_limit_df`: límite de valores en el dataframe.
        - `model`: reúne alguna configuración externa para alguno de los modelos
        - `export`: permite especificar el número de puntos que tendrá el mapa de dispersión.
    2. `cfg/cfg_test.json` Contiene las siguientes entradas:
        - `project_routes`: rutas donde se generarán directorios para almacenar logs, resultados y pesos de entrenamiento.
        - `pre_processing_test`: contiene diccionarios con valores que se van a introducir en el dataframe colocando datos nulos, fuera de rango o repetidos, sirve para probar la efectividad de los algoritmos de limpieza.