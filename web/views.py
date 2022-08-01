from django.shortcuts import render
from django.http import HttpResponse
from .helpers import db_search


def index_cze(request):
    return render(request, 'web/index_cze.html')


def index_eng(request):
    return render(request, 'web/index_eng.html')


def search(request):
    if request.method == 'POST':
        searched_text = request.POST.get('searched_text')
        language = request.POST.get('language')
        fulltext = request.POST.get('optionsRadios')
        results = db_search(language, searched_text, fulltext)
        return HttpResponse(results)
