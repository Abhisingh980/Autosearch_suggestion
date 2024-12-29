from .elasticserchwraper import create_index, index_document

# Define index settings
index_name = "products"
settings = {
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 0,
    },
    "mappings": {
        "properties": {
            "name": {"type": "text"},
            "description": {"type": "text"},
            "price": {"type": "float"},
            "available": {"type": "boolean"},
        }
    }
}

# Create the index
create_index(index_name, settings)

# Index some data
index_document(index_name, 1, {
    "name": "Product A",
    "description": "A high-quality product.",
    "price": 99.99,
    "available": True,
})
