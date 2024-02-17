# Ejercio 4 cargar base de datos

import sqlite3
import pandas as pd

def ej_4_crear_cargar_base_de_datos():
    # Conexión a la base de datos (se crea si no existe)
    db = sqlite3.connect('calidad_aire.db')

    try:
        # Cargar y guardar datos demográficos en la base de datos
        df_demograficos = pd.read_csv("datos_demograficos.csv")
        print("Datos demográficos cargados correctamente.")
        print(df_demograficos.head())  # Imprime los primeros registros para verificar

        df_demograficos.to_sql('demografia', db, if_exists='replace', index=False)
        print("Datos demográficos guardados en la base de datos.")

        # Cargar y guardar datos de calidad del aire en la base de datos
        df_calidad_aire = pd.read_csv("calidad_aire.csv")
        print("Datos de calidad del aire cargados correctamente.")
        

        df_calidad_aire.to_sql('calidad_aire', db, if_exists='replace', index=False)
        print("Datos de calidad del aire guardados en la base de datos.")

    except Exception as e:
        print("Ocurrió un error durante la carga de datos: ", e)
    finally:
        # Cerrar la conexión a la base de datos
        db.close()
        print("Conexión a la base de datos cerrada.")

if __name__ == "__main__":
    ej_4_crear_cargar_base_de_datos()

# Ejercicio 5 analizar calidad de aire

def ej_5_analizar_calidad_aire_ciudades_mas_pobladas() -> pd.DataFrame:
    # Conectar a la base de datos SQLite
    db = sqlite3.connect('calidad_aire.db')

    # Consulta SQL para JOIN entre las tablas y ordenar por población y calidad del aire
    consulta_sql = """
    SELECT d.City, d.State, d.`Total Population`, a.overall_aqi
    FROM demografia d
    INNER JOIN calidad_aire a ON d.City = a.city
    ORDER BY d.`Total Population` DESC, a.overall_aqi DESC
    LIMIT 10
    """

    # Ejecutar la consulta y obtener los resultados
    resultados = pd.read_sql_query(consulta_sql, db)
    print(resultados)

    # Cerrar la conexión a la base de datos
    db.close()


if __name__ == "__main__":
    ej_5_analizar_calidad_aire_ciudades_mas_pobladas()