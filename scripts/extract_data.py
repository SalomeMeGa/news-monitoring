import requests  
import pandas as pd  
import os  # Para acceder a variables de entorno
from dotenv import load_dotenv  # Para cargar las variables del archivo .env

load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

if not NEWS_API_KEY:
    raise Exception("La API Key no está configurada. Verifica tu archivo .env.")

def extraer_noticias(query="medicine", language="es", page_size=50):
    """
    Consulta la API de NewsAPI para extraer noticias relacionadas con un término específico.

    :param query: término a buscar (por ejemplo, 'economía')
    :param language: idioma ('es' para español)
    :param page_size: cantidad máxima de noticias a obtener (máx 100 por petición)
    :return: DataFrame con las noticias
    """

    url = "https://newsapi.org/v2/everything"

    params = {
        "q": query,
        "language": language,
        "pageSize": page_size,
        "apiKey": NEWS_API_KEY
    }

    print(f"Consultando API para: '{query}'...")

    response = requests.get(url, params=params)

    if response.status_code != 200:
        raise Exception(f"Error en la API: {response.status_code} - {response.text}")

    data = response.json()  # Convertimos la respuesta en formato JSON a un diccionario

    #Extraemos solo la lista de noticias
    noticias = data.get("articles", [])

    if not noticias:
        print("No se encontraron noticias.")
        return pd.DataFrame()

    #Creamos un DataFrame limpio
    df_noticias = pd.json_normalize(noticias)[['source.name', 'author', 'title', 'description', 'url', 'publishedAt']]

    print(f"Se obtuvieron {len(df_noticias)} noticias.")
    return df_noticias


# Uso básico del script, para ejecutar el archivo directamente
#query es obligatorio, no tiene valor por defecto
#languaje y max_results tienen valores por defecto: "en" y 50
if __name__ == "__main__":
    df = extraer_noticias(query="Medicina")
    print(df.head())
