import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import os

sns.set(style="whitegrid")

def cargar_datos(ruta: str) -> pd.DataFrame:
    return pd.read_csv(ruta)

def resumen_general(df: pd.DataFrame):
    print("\nResumen General:")
    print(df.info())
    print("\nDescripción:")
    print(df.describe(include='all'))

def revisar_nulos(df: pd.DataFrame):
    print("\nValores Nulos por columna:")
    print(df.isnull().sum())

def revisar_duplicados(df: pd.DataFrame):
    duplicados = df.duplicated().sum()
    print(f"\nDuplicados: {duplicados}")
    return duplicados

def graficar_medios(df: pd.DataFrame):
    plt.figure(figsize=(10, 5))
    df['source.name'].value_counts().head(10).plot(kind='bar')
    plt.title("Top 10 fuentes más frecuentes")
    plt.xlabel("Fuente")
    plt.ylabel("Cantidad de noticias")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("Fuentes.png")
    plt.close()
    #plt.show()



def graficar_tendencia_tiempo(df: pd.DataFrame):
    df['fecha_publicacion'] = pd.to_datetime(df['fecha_publicacion'], errors='coerce')
    df['fecha'] = df['fecha_publicacion'].dt.date
    conteo = df['fecha'].value_counts().sort_index()

    plt.figure(figsize=(10, 6))
    conteo.plot(kind='line', marker='o')
    plt.title('Tendencia de noticias a lo largo del tiempo')
    plt.xlabel('Fecha')
    plt.ylabel('Cantidad de noticias')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("Tendencias.png")
    plt.close()
    #plt.show()


def generar_wordcloud(df: pd.DataFrame, columna: str):
    texto = " ".join(str(x) for x in df[columna].dropna())
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(texto)

    plt.figure(figsize=(12, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(f"Nube de palabras ({columna})")
    plt.savefig("FWorld.png")
    plt.close()
    #plt.show()