from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index_cze(request):
    template = loader.get_template('web/index_cze.html')
    if request.method == "POST":
        return print("test")
    return HttpResponse(template.render())

def index_eng(request):
    template = loader.get_template('web/index_eng.html')
    return HttpResponse(template.render())

def searchengine(request):
    if request.method == 'POST':
        print("test")
