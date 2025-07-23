from scripts.eda import (
    cargar_datos, resumen_general, revisar_nulos,
    revisar_duplicados, graficar_medios,
    graficar_tendencia_tiempo, generar_wordcloud
)

# Ruta a datos procesados
ruta = "data/processed/noticias_limpias.csv"
df = cargar_datos(ruta)

# Análisis
resumen_general(df)
revisar_nulos(df)
revisar_duplicados(df)

# Gráficas
graficar_medios(df)
graficar_tendencia_tiempo(df)
generar_wordcloud(df, columna="titulo")
generar_wordcloud(df, columna="descripcion")
