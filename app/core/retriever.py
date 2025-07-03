import faiss
import os
import json
import numpy as np
from app.services.embedder import get_embedder
from app.core.config import EMBEDDING_MODEL

FAQ_PATH = "app/data/faq.json"
INDEX_PATH = "app/embeddings/faiss_index.bin"

def normalize_vectors(vectors: list[list[float]]) -> np.ndarray:
    vectors = np.array(vectors)
    norms = np.linalg.norm(vectors, axis=1, keepdims=True)
    return vectors / norms

def create_embeddings():
    with open(FAQ_PATH) as f:
        faqs = json.load(f)
    questions = [faq["question"] for faq in faqs]

    embedder = get_embedder(EMBEDDING_MODEL)
    embeddings = embedder.encode(questions)
    normalized_embeddings = normalize_vectors(embeddings)

    embedding_dimension = normalized_embeddings.shape[1]
    index = faiss.IndexFlatIP(embedding_dimension)
    index.add(normalized_embeddings.astype("float32"))

    faiss.write_index(index, INDEX_PATH)

def retrieve_answer(query: str) -> str:
    if not os.path.exists(INDEX_PATH):
        return None

    index = faiss.read_index(INDEX_PATH)
    embedder = get_embedder(EMBEDDING_MODEL)

    query_vector = embedder.encode([query])
    query_vector = normalize_vectors(query_vector)

    D, I = index.search(np.array(query_vector).astype("float32"), k=1)

    with open(FAQ_PATH) as f:
        faqs = json.load(f)

    similarity = D[0][0]
    if similarity < 0.7:
        return None

    return faqs[I[0][0]]["answer"]
