from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse



def index(request):
    Fourth = '<h1> fourth project</h1>'
    return HttpResponse( Fourth)