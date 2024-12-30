from django.shortcuts import render


# Create your views here.

from .elasticserchwraper import search
from .elasticsearch import create_index,bookindex


def search_text(request):
    # query = request.GET.get('q', '')
    # results = []
    # if query:
    #     es_query = {
    #         "query": {
    #             "multi_match": {
    #                 "query": query,
    #                 "fields": ["name", "description"]
    #             }
    #         }
    #     }
    #     response = search("products", es_query)
    #     results = [hit["_source"] for hit in response["hits"]["hits"]]
    return render(request,'search.html')
