from sentence_transformers import SentenceTransformer
from .database import db, table
from .chunking import chunk_text
from pathlib import Path

# file types we want to support for embedding
SUPPORTED_EXTENSIONS = {".txt"}
# self explanatory
model = SentenceTransformer("google/embeddinggemma-2")

# Create documents directory if it doesn't exist
dir_path = Path("files/")
dir_path.mkdir(parents=True, exist_ok=True)

# list of chunked strings as per chunk_text() func in chunking.py
chunked_text = []

# iterate through directory and extend list of chunked strings to our big string for embedding
# (chunk_text func needs to be changed to a better suited chunking strategy)
for file_path in dir_path.iterdir():
    if (
        file_path.is_file()
        and file_path.suffix.lower() in SUPPORTED_EXTENSIONS
    ):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                chunks = chunk_text(f.read())

            if not chunks:
                continue

            embeddings = model.encode(
                chunks,
                truncate_dim=256,
                normalize_embeddings=True,
                prompt_name="Document",
            )

            rows = []
            for index, (chunk, embedding) in enumerate(
                zip(chunks, embeddings)
            ):
                rows.append({
                    "id": f"{file_path.resolve()}_chunk_{index}",
                    "vector": embedding.tolist(),
                    "text": chunk,
                    "source_file": str(file_path.resolve()),
                    "title": f"{file_path.stem} (Part {index + 1})",
                    "file_type": file_path.suffix.lower(),
                    "chunk_index": index,
                })
                
                (
                    table.merge_insert("id")
                    .when_matched_update_all()
                    .when_not_matched_insert_all()
                    .execute(rows)
                )

            print(f"Added {len(rows)} chunks from {file_path.name}")

        except Exception as e:
            print(f"Skipping {file_path.name} due to error: {e}")

# hard coded query, change so that users can input their own query later
query = "How does binary search improve on linear search?"

# this embeds the query, params were on the HF page for embeddinggemma2 lowk forgot what some of these do
query_emb = model.encode(
    query,
    truncate_dim=256,
    normalize_embeddings=True,
    prompt_name="SearchQuery")

# temporary - shows top 3 results from query
results = (
    table.search(query_emb.tolist())
    .limit(3)
    .select(["id", "title", "chunk_index", "text"])
    .to_list()
)

for result in results:
    print(result["title"], result["chunk_index"])
    print(result["text"])
