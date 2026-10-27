# these are in chars, not tokens
# should probably change to tokens later tho (512 token chunking + 5% overlap)
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# simple chunking function - change later to better chunking strategy
def chunk_text(text: str) -> list[str]:
    chunks = []
    if len(text) <= CHUNK_SIZE:
        return [text]
        
    start = 0
    while start < len(text):
        end = start + CHUNK_SIZE
        chunks.append(text[start:end])
        start += (CHUNK_SIZE - CHUNK_OVERLAP)
        
    return chunks