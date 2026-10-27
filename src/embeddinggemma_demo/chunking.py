from langchain_text_splitters import RecursiveCharacterTextSplitter
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("google/embeddinggemma-2")
# in tokens
CHUNK_SIZE = 512
CHUNK_OVERLAP = 51

text_splitter = RecursiveCharacterTextSplitter.from_huggingface_tokenizer(
    tokenizer=tokenizer,
    chunk_size=CHUNK_SIZE,
    chunk_overlap=CHUNK_OVERLAP,
)

# simple chunking function - change later to better chunking strategy
def chunk_text(text: str) -> list[str]:
    return text_splitter.split_text(text)