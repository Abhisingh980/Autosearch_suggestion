from django.shortcuts import render

# Create your views here.

def search_text(request):
    return render(request,'search.html')
