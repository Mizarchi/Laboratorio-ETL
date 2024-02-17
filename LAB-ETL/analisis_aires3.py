# Ejercicio 3 limpiando datos demograficos

import pandas as pd
from typing import Set

def ej_3_limpiar_datos_demograficos(data_demograficos: pd.DataFrame) -> pd.DataFrame:

    # Elimina filas duplicadas
    data_demograficos = data_demograficos.drop_duplicates()
    print("Datos corregidos con exito")
    return data_demograficos

if __name__ == "__main__":
    df = pd.read_csv("datos_demograficos.csv")
    ej_3_limpiar_datos_demograficos(df)