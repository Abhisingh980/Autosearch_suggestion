from .elasticserchwraper import create_index, index_document
from .models import BookSummary

# Define index settings
index_name = "categories"
settings = {
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 0,
    },
    "mappings": {
        "properties": {
            "name": {"type": "text"},
            "summeries": {"type": "text"},
            "categories": {"type": "text"},
        }
    }
}

# Create the index
create_index(index_name, settings)

# Index the documents which are already in the database in model.py file


def bookindex():
    book_summaries = BookSummary.objects.all()
    for book in book_summaries:
        document = {
            "name": book.name,
            "summeries": book.summeries,
            "categories": book.categories,
        }
        index_document(index_name, book.id, document)
    print("All documents indexed successfully!")

# Get all book summaries from the database and index them
