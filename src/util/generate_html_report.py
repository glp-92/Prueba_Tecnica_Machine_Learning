def generate_html_report(time_stamp, results, path_to_report):
    
    time_stamp = time_stamp.strftime("%Y/%m/%d %H:%M:%S")
    title = f"Reporte Generado Automaticamente {time_stamp}"
    result_table = f"<tr><td>Model ID</td><td>MSE</td><td>MAE</td><td>RMSE</td><td>R2</td></tr>"
    for id_net, results in results.items():
        result_table += f"<tr><td>{id_net}</td>"
        for res in results:
            result_table += f"<td>{round(res,4)}</td>"
        result_table += "</tr>"

    html_string = f"""
    <!DOCTYPE html>
    <html>
    <head>
    </head>
    <body>
        <h1>{title}</h1>
        <h2>Resultados</h2>
        <h3>Métricas generadas</h3>
        <table>{result_table}</table>
        <h3>Gráficos de dispersión</h3>
        <div className = "dispersion">
            <h4>Arboles de decision</h4>
            <img width="300" src = results/tree_depth_scatter.png>
        </div>
        <div className = "dispersion">
            <h4>Regresión lineal</h4>
            <img width="300" src = results/linear_regression_scatter.png>
        </div>
        <div className = "dispersion">
            <h4>Lasso</h4>
            <img width="300" src = results/lasso_scatter.png>
        </div>
        <div className = "dispersion">
            <h4>Dense Net</h4>
            <img width="300" src = results/dense_net_scatter.png>
        </div>

        <h2>Dataset</h2>
        <h3>Mapa de correlacion</h3>
        <div className = "corr">
            <h4>Correlación entre variables</h4>
            <img width="500" src = data_visual/corr_map.png>
        </div>
        <h3>Histogramas</h3>
        <div className = "hist">
            <h4>Valor inmueble</h4>
            <img width="300" src = data_visual/hist_MedHouseVal.png>
        </div>
        <div className = "hist">
            <h4>Población</h4>
            <img width="300" src = data_visual/hist_Population.png>
        </div>
        <div className = "hist">
            <h4>Mediana Ingresos</h4>
            <img width="300" src = data_visual/hist_MedInc.png>
        </div>
        <div className = "hist">
            <h4>Edad viviendas</h4>
            <img width="300" src = data_visual/hist_HouseAge.png>
        </div>
        <div className = "hist">
            <h4>Promedio de habitaciones</h4>
            <img width="300" src = data_visual/hist_AveRooms.png>
        </div>
        <div className = "hist">
            <h4>Promedio de dormitorios</h4>
            <img width="300" src = data_visual/hist_AveBedrms.png>
        </div>
        <div className = "hist">
            <h4>Promedio de ocupación</h4>
            <img width="300" src = data_visual/hist_AveOccup.png>
        </div>
        <div className = "map">
            <a href="data_visual/coord_map.html">Click para acceder al mapa</a>
        </div>
            
    </body>
    </html>
    """
    with open(path_to_report, "w") as f:
        f.write(html_string)
    pass


if __name__ == '__main__':
    from datetime import datetime 
    results = {
        "decission_tree": (0,0,0,0),
        "linear_regression": (1,1,1,1),
        "lasso": (2,2,2,2),
        "dense_net": (3,3,3,3)
    }
    time_stamp = datetime.now()
    path_to_exp = "../../runs/exp20231010111726/"
    generate_html_report(time_stamp=time_stamp, results=results, path_to_exp = path_to_exp, path_to_report="./report.html")