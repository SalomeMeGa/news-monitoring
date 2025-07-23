import pandas as pd

def transformar_noticias(df: pd.DataFrame) -> pd.DataFrame:
    """
    Es na funciòn que recibe un argumento Dataframe de pandas(df) y devuelve otro Dataframe de pandas
    -> pd.DataFrame: Indica que la fnciòn devuelve n DataFrame de Pandas. Tambièn es una anotaciòn de tipo
    """
    columnas_a_eliminar = ['source', 'author', 'urlToImage', 'content', 'url']
    df = df.drop(columns=[col for col in columnas_a_eliminar if col in df.columns], errors='ignore')
    df = df.rename(columns={
        'publishedAt': 'fecha_publicacion',
        'description': 'descripcion',
        'title': 'titulo'
    })
    df['fecha_publicacion'] = pd.to_datetime(df['fecha_publicacion'], errors='coerce')
    df = df.dropna(subset=['titulo', 'descripcion', 'fecha_publicacion'])
    df = df.reset_index(drop=True)
    return df
