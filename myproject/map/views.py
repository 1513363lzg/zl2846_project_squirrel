from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def detail(request):

    return render(request, 'map/map.html')


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
# Create your views here.
