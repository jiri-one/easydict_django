from django.shortcuts import render
from django.http import HttpResponse


def index_cze(request):
    return render(request, 'web/index_cze.html')


def index_eng(request):
    return render(request, 'web/index_eng.html')


def search(request):
    if request.method == 'POST':
        searched_text = request.POST.get('searched_text')
        language = request.POST.get('language')
        fulltext = request.POST.get('optionsRadios')
        print(request.POST)
        return HttpResponse("Here's the text of the web page.")
    else:
        return render(request, None)


def csrf_failure(request, reason=""):
    print(request, reason)
