from elasticsearch import Elasticsearch
#from .add_data_to_databse import add_data_to_database

# Initialize Elasticsearch client
#

es = Elasticsearch("http://localhost:9200")
#add_data_to_database() #uncomment this line to add data to database
print(es,"\nelastic search connected\n data add to database")



def create_index(index_name, settings):


    # Create the index with the specified settings
    es.indices.create(index=index_name, body=settings)
    print(f"Index '{index_name}' created successfully!")

def index_document(index_name, id, document):


    # Index (i.e., add) the document
    es.index(index=index_name, id=id, body=document)
    print(f"Document '{id}' indexed successfully!")

def search(index_name, query):


    # Search the index with the specified query
    response = es.search(index=index_name, body=query)
    return response
