from sklearn.model_selection import train_test_split


def prepare_dataset(df):
    x_data = df.drop(['MedHouseVal'], axis = 1) # Se elimina de x_train el precio, ya que es el resultado esperado (y_train)
    y_data = df['MedHouseVal']
    normalized_x_data = (x_data-x_data.min())/(x_data.max()-x_data.min())
    normalized_y_data = (y_data-y_data.min())/(y_data.max()-y_data.min())
    x_train, x_test, y_train, y_test = train_test_split(
        normalized_x_data, 
        normalized_y_data, 
        test_size=0.2
    )
    return x_train, y_train, x_test, y_test, y_data.min(), y_data.max()
