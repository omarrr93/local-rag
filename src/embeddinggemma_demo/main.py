from sentence_transformers import SentenceTransformer
import lancedb

model = SentenceTransformer("google/embeddinggemma-2")

query = "What causes the northern lights?"
document = "The northern lights are caused by charged particles from the sun."

query_emb = model.encode(
    query,
    truncate_dim=256,
    normalize_embeddings=True,
    prompt_name="SearchQuery")
doc_emb = model.encode(
    document,
    truncate_dim=256,
    normalize_embeddings=True,
    prompt_name="Document")
score = model.similarity(query_emb, doc_emb)

print(f"Similarity: {score.item():.4f}")
#print(model.prompts)
