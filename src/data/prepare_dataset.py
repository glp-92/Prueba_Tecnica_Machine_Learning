from sklearn.model_selection import train_test_split


def prepare_dataset(df):
    x_data = df.drop(['MedHouseVal'], axis = 1) # Se elimina de x_train el precio, ya que es el resultado esperado (y_train)
    y_data = df['MedHouseVal']
    x_train, x_test, y_train, y_test = train_test_split(
        x_data, 
        y_data, 
        test_size=0.2
    )
    return x_train, y_train, x_test, y_test
