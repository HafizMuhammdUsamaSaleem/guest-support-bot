from sentence_transformers import SentenceTransformer

def get_embedder(model_name: str):
    return SentenceTransformer(model_name)
