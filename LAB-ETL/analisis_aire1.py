import pandas as pd
from typing import Set

#Ejercicio 1 carga de datos

def ej_1_cargar_datos_demograficos() -> pd.DataFrame:
    url = "https://public.opendatasoft.com/explore/dataset/us-cities-demographics/download/?format=csv&timezone=Europe/Berlin&lang=en&use_labels_for_header=true&csv_separator=%3B"
    data = pd.read_csv(url, sep=';')
    data.drop(columns=['Race', 'Count', 'Number of Veterans'], inplace=True)
    data.drop_duplicates(inplace=True)

    # Guardar los datos demográficos en un archivo CSV
    data.to_csv("datos_demograficos.csv", index=False)

    return data



