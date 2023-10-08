

def validate_data(df, validation_types):
    """
    Args:
        df_housing: Pandas dataframe
    Returns:
        df_housing: Pandas dataframe validado
    Raises:
        ValueError: Tipo de dato no esperado en el dataframe
    About:
        Es posible la inyección de código JS, por ejemplo, si se utiliza en Python la función eval() sin cuidado, o si el dataframe se exporta a csv.
        Para reducir la superficie de ataque, se validará la entrada de cualquier fuente no confiable respecto al tipo de dato.
    """
    columns = df.columns
    assert len(columns) == len(validation_types), "El número de tipos de variable a controlar del dataframe debe coincidir con su número de columnas"
    # Comprueba que los valores de las variables sean del tipo adecuado.
    for col, expected_data in zip(columns, validation_types):
        dtype = df[col].dtype
        if dtype != expected_data:
            raise ValueError(f"El tipo de dato de la variable '{col}' es incorrecto")