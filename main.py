import pandas as pd
from scripts.extract_data import extraer_noticias
from scripts.transform_data import transformar_noticias
import os

def guardar_df(df: pd.DataFrame, ruta: str, descripcion: str):
    """
    Guarda un DataFrame como CSV.
    """
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    df.to_csv(ruta, index=False, encoding='utf-8')
    print(f"{descripcion} guardado en: {ruta}")

if __name__ == "__main__":
    print("Iniciando proceso ETL de Noticias")
    print("Extrayendo datos...")
    df_raw = extraer_noticias(query="medicine")
    print(f"Noticias extraídas: {len(df_raw)}")

    ruta_raw = os.path.join("data", "raw", "noticias_crudas.csv")
    guardar_df(df_raw, ruta_raw, "Datos crudos")

    print("Transformando datos...")
    df_limpio = transformar_noticias(df_raw)
    print(f"Noticias tras limpieza: {len(df_limpio)}")

    ruta_processed = os.path.join("data", "processed", "noticias_limpias.csv")
    guardar_df(df_limpio, ruta_processed, "Datos limpios")

    print("ETL completado exitosamente ")
