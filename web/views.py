from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index_cze(request):
    request.META['CSRF_COOKIE_USED'] = True
    template = loader.get_template('web/index_cze.html')
    return HttpResponse(template.render({}, request))


def index_eng(request):
    request.META['CSRF_COOKIE_USED'] = True
    template = loader.get_template('web/index_eng.html')
    return HttpResponse(template.render({}, request))


def searchengine(request):
    print("pred if")
    request.META['CSRF_COOKIE_USED'] = True
    if request.method == 'POST':
        print("test")
