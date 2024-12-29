from elasticsearch import Elasticsearch

# Initialize Elasticsearch client
es = Elasticsearch("http://localhost:9200")

def create_index(index_name, settings=None):
    """Create an Elasticsearch index."""
    if not es.indices.exists(index=index_name):
        es.indices.create(index=index_name, body=settings)
        print(f"Index '{index_name}' created successfully!")

def index_document(index_name, doc_id, document):
    """Index a document."""
    es.index(index=index_name, id=doc_id, document=document)

def search(index_name, query):
    """Search for documents."""
    return es.search(index=index_name, body=query)
