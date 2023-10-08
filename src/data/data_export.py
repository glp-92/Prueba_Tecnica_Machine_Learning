import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import folium


def plot_histogram(data, exp_path, title, xlabel, ylabel, n_bins = 20, ):
    """
    Args:
        data: data to export
        exp_path: path to experiments dir
    Returns:
        None
    About:
        Funcion para almacenar en experimentos los plots de histogramas de dataframe
    """
    plt.hist(data, bins=20)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(exp_path)
    plt.clf()
    return

def plot_correlation_map(corr, exp_path):
    """
    Args:
        corr: correlation map
        exp_path: path to experiments dir
    Returns:
        None
    About:
        Funcion para almacenar en experimentos los plots de mapas de correlacion
    """
    fig = plt.figure(figsize=(10, 10))
    plt.subplots_adjust(left=0.25, right=0.75, top=0.75, bottom=0.25)
    sns.heatmap(corr, 
            annot = True,
            ax=fig.gca())
    plt.savefig(exp_path)
    plt.clf()

def plot_price_map(df, exp_path, n_samples = 200):
    """
    Args:
        df: dataFrame de datos.
        n_samples: El número de puntos aleatorios a mostrar en el mapa.
    Returns:
        None
    About:
        Crea un mapa de precios con los puntos aleatorios de un DataFrame.
    """
    df_sample = df.sample(n_samples)
    m = folium.Map(location=[37.422743, -122.085456], zoom_start=6)
    for _, row in df_sample.iterrows():
        folium.Marker(
            location=[row["Latitude"], row["Longitude"]],
            tooltip="Click para ver precio",
            popup=f"Precio: {round(row['MedHouseVal'] * 100000)}",
            icon=folium.Icon(color="green"),
        ).add_to(m)
    m.save(exp_path)
