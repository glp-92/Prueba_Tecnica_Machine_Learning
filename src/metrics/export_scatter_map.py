import matplotlib.pyplot as plt


def export_scatter_map(predictions, y_val, points_to_draw, path_to_export):
    y_val = y_val.to_numpy()
    y_val = y_val[:points_to_draw]
    predictions = predictions[:points_to_draw]
    plt.clf()
    plt.figure(figsize=(5,5))
    plt.scatter(y_val, predictions)
    plt.xlabel('True Values')
    plt.ylabel('Predictions')
    plt.axis('equal')
    plt.axis('square')
    plt.xlim([0,1])
    plt.ylim([0,1])
    _ = plt.plot([-100, 100], [-100, 100])
    # Mostrar el gráfico
    plt.savefig(path_to_export)
    return