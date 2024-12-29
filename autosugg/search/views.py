from django.shortcuts import render
from .elasticserchwraper import search
# Create your views here.

def search_text(request):
    query = request.GET.get('q', '')
    results = []
    if query:
        es_query = {
            "query": {
                "multi_match": {
                    "query": query,
                    "fields": ["name", "description"]
                }
            }
        }
        response = search("products", es_query)
        results = [hit["_source"] for hit in response["hits"]["hits"]]
        return render(request,'search.html',{'results':results,'query':query})
