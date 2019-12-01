from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from sightings.models import Squirrel

def detail(request):
    squirrels=Squirrel.objects.all()
    context={
            'squirrels':squirrels,
            }
    return render(request, 'map/map.html',context)



        
        # Create your views here.
