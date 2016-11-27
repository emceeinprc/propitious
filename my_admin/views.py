from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.views import generic
from django.template import loader

def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'index.html', {})
