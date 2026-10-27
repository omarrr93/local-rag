import lancedb
import pyarrow as pa

LANCE_DB_URI="./lancedb"
db = lancedb.connect(LANCE_DB_URI)

schema = pa.schema([
    pa.field("id", pa.string()),
    pa.field("vector", pa.list_(pa.float32(), 256)),
    pa.field("text", pa.string()),
    pa.field("source_file", pa.string()),
    pa.field("title", pa.string()),
    pa.field("file_type", pa.string()),
    pa.field("chunk_index", pa.int64()),
])

def get_table():
    if "documents" in db.table_names():
        return db.open_table("documents")

    return db.create_table("documents", schema=schema)

table = get_table()