from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from sightings.models import Squirrel


def detail(request):
    sightings=Squirrel.objects.all()[:100]
    context={
        'sightings':sightings,
    }
    return render(request, 'map/map.html',context)
