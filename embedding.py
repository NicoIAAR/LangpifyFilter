from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Ejemplos típicos de inyección SQL
sql_injections = [
    "' OR '1'='1' --",
    '" OR "1"="1" --',
    "' OR 1=1 --",
    '" OR 1=1 --',
    "admin' --",
    'admin" --',
    "' OR 'a'='a",
    '" OR "a"="a',
    "' OR 1=1#",
    '" OR 1=1#',
    "' OR 1=1/*",
    '" OR 1=1/*',
    "' UNION SELECT * FROM users --",
    '" UNION SELECT * FROM users --',
    "' DROP TABLE users; --",
    '" DROP TABLE users; --',
]

# Inicializa el modelo de embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')

# Calcula los embeddings de los ejemplos de inyección
injection_embeddings = model.encode(sql_injections)

def is_sql_injection(prompt, threshold=0.7):
    """
    Retorna True si el prompt es similar a un patrón de inyección SQL.
    threshold: entre 0 y 1, mayor es más estricto.
    """
    prompt_emb = model.encode([prompt])
    sims = cosine_similarity(prompt_emb, injection_embeddings)[0]
    max_sim = np.max(sims)
    return max_sim > threshold, max_sim

if __name__ == "__main__":
    prompt = input("Introduce el prompt a analizar: ")
    es_inyeccion, similitud = is_sql_injection(prompt)
    if es_inyeccion:
        print(f"⚠️  Posible inyección SQL detectada (similitud: {similitud:.2f})")
    else:
        print(f"✅ Prompt seguro (similitud: {similitud:.2f})")
