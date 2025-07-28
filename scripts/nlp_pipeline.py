import pandas as pd
from nlp_utils import aplicar_tfidf

# 1. Cargar el dataset limpio
df = pd.read_csv("data/processed/noticias_limpias.csv")
print(df.columns)

# 2. Aplicar limpieza y TF-IDF
df_limpio, tfidf_df = aplicar_tfidf(df)

# 3. Guardar resultados
df_limpio.to_csv("data/processed/news_medical_text_clean.csv", index=False)
tfidf_df.to_csv("data/processed/news_medical_tfidf.csv", index=False)

print("Procesamiento NLP finalizado y archivos guardados.")
