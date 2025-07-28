import re
import string
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Descargar recursos de NLTK si no los tienes
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

stop_words = set(stopwords.words('spanish'))
lemmatizer = WordNetLemmatizer()

def limpiar_texto(texto: str) -> str:
    texto = texto.lower()
    texto = re.sub(r'\d+', '', texto)
    texto = texto.translate(str.maketrans('', '', string.punctuation))
    tokens = nltk.word_tokenize(texto)
    tokens = [t for t in tokens if t not in stop_words]
    tokens = [lemmatizer.lemmatize(t) for t in tokens]
    return ' '.join(tokens)

def aplicar_tfidf(df: pd.DataFrame, columna_texto: str = "descripcion", max_features: int = 1000):
    df["texto_limpio"] = df[columna_texto].apply(limpiar_texto)
    vectorizer = TfidfVectorizer(max_features=max_features)
    tfidf_matrix = vectorizer.fit_transform(df["texto_limpio"])
    tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=vectorizer.get_feature_names_out())
    # Calcular promedio de TF-IDF para cada palabra
    tfidf_means = tfidf_df.mean(axis=0)

    # Ordenar y mostrar top 10
    top_10 = tfidf_means.sort_values(ascending=False).head(10)
    print("\n10 palabras más relevantes por TF-IDF:")
    for palabra, valor in top_10.items():
        print(f"{palabra}: {valor:.4f}")
    
    
    return df, tfidf_df
